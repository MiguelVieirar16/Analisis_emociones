import pandas as pd
from textblob import TextBlob
from googletrans import Translator

def translateComment(strComment):
    translator = Translator()
    try:
        translation = translator.translate(strComment, dest='en')
        return translation.text
    except Exception as e:
        print(f"Error translating '{strComment}': {e}")
        return strComment

def getPolarity(strComment):
    strComment = translateComment(strComment)
    blob = TextBlob(strComment)
    return blob.sentiment.polarity

df = pd.read_csv(r"C:\Users\migue\Desktop\Cursos\Analisis de datos\7. Data visualization\Power BI\0. Casos practicos\4. Comentarios feedback\Comentarios.csv")
df["Polaridad"] = df["Comentario"].apply(getPolarity)
print(df)

df.to_csv("resultados.csv")
