import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

df = pd.read_csv('data/transactions.csv')

# Variable qui revele directement la cible
df['fraude_confirmee'] = df['fraude']

mlflow.set_tracking_uri('http://127.0.0.1:5000')
mlflow.set_experiment('tp4-automl')

for scenario, colonnes in [
    ('avec-fuite', ['montant', 'anciennete', 'freq_24h', 'nuit', 'fraude_confirmee']),
    ('sans-fuite', ['montant', 'anciennete', 'freq_24h', 'nuit'])
]:
    X = df[colonnes]
    y = df['fraude']

    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    modele = RandomForestClassifier(
        n_estimators=500,
        max_depth=16,
        random_state=42
    )

    modele.fit(Xtr, ytr)
    f1 = f1_score(yte, modele.predict(Xte))

    with mlflow.start_run(run_name=scenario):
        mlflow.log_param('scenario', scenario)
        mlflow.log_param('fuite', scenario == 'avec-fuite')
        mlflow.log_metric('f1', round(f1, 4))

    print(f'{scenario:12s} | F1 = {f1:.4f}')
