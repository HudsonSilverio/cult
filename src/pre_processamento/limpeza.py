# poetry run python limpeza.py
"""
Script para:
1. Carregar o arquivo 'cult.xlsx' do computador
2. Manter apenas as colunas de interesse
3. Salvar em um novo arquivo CSV no PC
"""

import pandas as pd
from pathlib import Path

# Cole aqui o caminho completo do arquivo de entrada (EX: r"C:\Users\SeuNome\Documents\cult.xlsx")
CAMINHO_ENTRADA = Path(r"C:/Users/SAMSUNG/Rolhas/Desktop/cult.xlsx")

# Caminho do arquivo de saída (será salvo na mesma pasta do arquivo de entrada)
CAMINHO_SAIDA = CAMINHO_ENTRADA.parent / "cult_PRONTO.csv"

# Lista das colunas que queremos manter
COLUNAS_DESEJADAS = [
    "Run",
    "groupName",
    "What is your relationship to this group? (3jjnt2u)",
    "In one sentence, how would you describe what this group, community or organization is about or what it believes? (w9swmcu)",
    "s_selfSacrifice",
    "s_confusionsUnanswered",
    "s_groupSpecial",
    "s_timeContributions",
    "s_tiesDiscouraged",
    "s_outsidersWary",
    "s_nontypicalPractices",
    "s_similarityEncouraged",
    "s_importantKnowledge",
    "s_informationWithheld",
    "s_futurePredictions",
    "s_leaversShunned",
    "s_informationDiscouraged",
    "s_acceptPractices",
    "s_monetaryContributions",
    "cultSumScoreUnweighted0To100",
    "cultRatingPost",
    "reportLink",
    "Please explain why you gave it the rating that you did - what attributes do you think make it cult-like and/or not cult-like? (ixy9mjz)"
]

def main():
    # Carregar o arquivo Excel
    df = pd.read_excel(CAMINHO_ENTRADA)

    # Manter apenas as colunas desejadas
    df_filtrado = df[COLUNAS_DESEJADAS]

    # Salvar em CSV
    df_filtrado.to_csv(CAMINHO_SAIDA, index=False, encoding="utf-8")

    print(f"✅ Arquivo filtrado salvo em: {CAMINHO_SAIDA}")

if __name__ == "__main__":
    main()
