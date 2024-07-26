import pandas as pd

df = pd.read_csv('philosophy_data.csv')

df = df.drop(columns=['sentence_spacy'])
df.rename(columns={'sentence_lowered': 'sentence_en'}, inplace=True)
df.rename(columns={'sentence_str': 'sentence_ko'}, inplace=True)

df_limited = df.groupby('title').head(25)

columns = list(df_limited.columns)
columns.insert(4, columns.pop(columns.index('sentence_en')))
df_limited = df_limited[columns]

df_limited.to_csv('cut_philosophy_data.csv', index=False)