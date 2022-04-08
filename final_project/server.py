from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation import translator
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text_translate = translator.english_to_french(textToTranslate)
    return text_translate

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text_translate = translator.french_to_english(textToTranslate)
    return text_translate

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
