import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from lazypredict.Supervised import LazyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# -----------------------------LAZYPREDICT-----------------------------

# Leitura com encoding e delimitador certos
df_ocorrencia = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')
df_ocorrencia_tipo = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')
df_aeronave = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')
df_fator = pd.read_csv('dados/fator_contribuinte.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')

# Juntar ocorrencia com ocorrencia_tipo
df = df_ocorrencia.merge(df_ocorrencia_tipo, left_on='codigo_ocorrencia', right_on='codigo_ocorrencia1', how='left')

# Juntar com aeronave usando codigo_ocorrencia2
df = df.merge(df_aeronave, left_on='codigo_ocorrencia2', right_on='codigo_ocorrencia2', how='left')

# Juntar com fator_contribuinte usando codigo_ocorrencia3
df = df.merge(df_fator, left_on='codigo_ocorrencia3', right_on='codigo_ocorrencia3', how='left')

# Limpeza básica: remover colunas código extras que não serão usadas
cols_to_drop = ['codigo_ocorrencia1', 'codigo_ocorrencia2', 'codigo_ocorrencia3', 'codigo_ocorrencia4', 'codigo_ocorrencia']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

# Filtrar só os casos onde classificação da ocorrência é importante para seu problema
df = df[df['ocorrencia_classificacao'].isin(['ACIDENTE', 'INCIDENTE GRAVE', 'INCIDENTE'])]

# Encode variáveis categóricas importantes
le = LabelEncoder()
for col in ['ocorrencia_uf', 'aeronave_fabricante', 'aeronave_tipo_veiculo', 'taxonomia_tipo_icao', 'ocorrencia_tipo']:
    if col in df.columns:
        df[col] = le.fit_transform(df[col].astype(str))

# Converter variáveis numéricas, tratar NaNs
df['aeronave_ano_fabricacao'] = pd.to_numeric(df['aeronave_ano_fabricacao'], errors='coerce')
df = df.dropna(subset=['aeronave_ano_fabricacao', 'ocorrencia_uf', 'aeronave_fabricante', 'aeronave_tipo_veiculo', 'taxonomia_tipo_icao', 'ocorrencia_tipo'])

# Definir target: você pode tentar 'ocorrencia_classificacao' para prever se é acidente, incidente grave ou incidente
df['target'] = le.fit_transform(df['ocorrencia_classificacao'])

# Escolher features para o modelo
features = ['aeronave_ano_fabricacao', 'ocorrencia_uf', 'aeronave_fabricante', 'aeronave_tipo_veiculo', 'taxonomia_tipo_icao', 'ocorrencia_tipo']

X = df[features]
y = df['target']

# Split treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# LazyPredict para avaliação de modelos
clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(X_train, X_test, y_train, y_test)

print(models)

# Supondo que 'models' é seu DataFrame com os resultados do LazyPredict
def save_table_as_image(df, filename='model_results.png'):
    fig, ax = plt.subplots(figsize=(12, len(df)*0.4 + 1))  # altura dinâmica
    
    ax.axis('off')  # desliga os eixos
    tbl = ax.table(cellText=df.values,
                   colLabels=df.columns,
                   rowLabels=df.index,
                   cellLoc='center',
                   loc='center')
    
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.auto_set_column_width(col=list(range(len(df.columns))))
    
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    
# Depois de imprimir o resultado, só chamar:
#save_table_as_image(models, 'images/resultados_modelos.png')
#print("Imagem salva como resultados_modelos.png")

# -----------------------------INDIVIDUAL RANDOM FOREST-----------------------------

# Treinando
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# Prevendo
y_pred = rf.predict(X_test)

class_names = le.classes_

# Métricas detalhadas
print("Classification Report RandomForest:")
#print(classification_report(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=class_names))

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

cm = confusion_matrix(y_test, y_pred, normalize='true')
plt.figure(figsize=(8,6))
#sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=rf.classes_, yticklabels=rf.classes_, fmt=".2f")
sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=class_names, yticklabels=class_names, fmt=".2f")
plt.title('Matriz de Confusão Normalizada - Random Forest')
plt.xlabel('Predito')
plt.ylabel('Real')
plt.tight_layout()
plt.savefig('images/matconfnorm.png')
plt.close()

feat_importances = pd.Series(rf.feature_importances_, index=X_train.columns)
feat_importances = feat_importances.sort_values(ascending=False)
plt.figure(figsize=(12,8))
sns.barplot(x=feat_importances, y=feat_importances.index)
plt.title('Importância das Features - Random Forest')
plt.xlabel('Importância')
plt.ylabel('Features')
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.subplots_adjust(left=0.2)  # aumenta o espaço à esquerda
plt.savefig('images/impfeat.png')
plt.close()

def salva_graficos():
    # SALVANDO OS GRÁFICOS COMO IMAGEM:
    # Salvar o classification_report como imagem
    report = classification_report(y_test, y_pred, target_names=class_names)
    plt.figure(figsize=(8, 6))
    plt.text(0, 0.5, report, fontsize=12, family='monospace')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/classification_report_rf.png')
    plt.close()
    # Gerar a matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    class_names = ['Acidente', 'Incidente', 'Incidente Grave']
    plt.figure(figsize=(7, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names, 
                linewidths=0.5, linecolor='gray', cbar=False)
    plt.title("Matriz de Confusão - RandomForest", fontsize=14)
    plt.xlabel("Predito", fontsize=12)
    plt.ylabel("Real", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10, rotation=0)
    plt.tight_layout()
    plt.savefig("images/matriz_confusao_rf.png")
    plt.close()