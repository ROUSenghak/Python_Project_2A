import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_region_regression(df, region_name, features=['T2M']):
    """
    Entraîne une régression linéaire pour une région donnée et affiche les scores.
    """
    # 1. Filtrer par région
    df_reg = df[df['Regions'] == region_name].dropna(subset=['Consommation'] + features)
    
    if df_reg.empty:
        print(f"Pas de données pour la région : {region_name}")
        return None, None

    # 2. Préparer les données (X = variables explicatives, y = cible)
    X = df_reg[features]
    y = df_reg['Consommation']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Créer et entraîner le modèle
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 4. Prédictions et évaluation
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"--- Résultats pour {region_name} ({features}) ---")
    print(f"R² (Score de précision) : {r2:.3f}")
    print(f"Erreur moyenne (RMSE) : {rmse:.2f} MWh")
    
    return model, (X_test, y_test, y_pred)

def plot_regression_results(region_name, results_tuple):
    """
    Affiche graphiquement la comparaison entre Valeurs Réelles et Prédictions.
    """
    X_test, y_test, y_pred = results_tuple
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
    
    # Ligne de perfection (y=x)
    max_val = max(y_test.max(), y_pred.max())
    min_val = min(y_test.min(), y_pred.min())
    plt.plot([min_val, max_val], [min_val, max_val], color='red', lw=2, linestyle='--')
    
    plt.title(f"Prédictions vs Réalité - {region_name}")
    plt.xlabel("Consommation Réelle (MWh)")
    plt.ylabel("Consommation Prédite (MWh)")
    plt.grid(True, alpha=0.3)
    plt.show()