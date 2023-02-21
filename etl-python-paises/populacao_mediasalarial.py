import pandas as pd

import etl

def risco():
    print("-" * 110)

populacao_df = pd.read_csv("populacao.csv")
mediasalarial_df = pd.read_csv("mediasalarial.csv")

risco()
print(populacao_df)
risco()
print(mediasalarial_df)
risco()

populacao_mediasalarial = populacao_df.merge(mediasalarial_df, how='inner', left_on="estado", right_on="estado")

print(populacao_mediasalarial)

etl.etl(populacao_mediasalarial)