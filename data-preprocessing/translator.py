import pandas as pd
import deepl

def translate_text(text, source_lang='EN', target_lang='KO'):
    auth_key = ""

    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    return result.text

df = pd.read_csv('cut_philosophy_data.csv')

df['sentence_ko'] = df['sentence_ko'].apply(lambda x: translate_text(x,source_lang='EN', target_lang='KO'))

df.to_csv('translated_file.csv', index=False)
