from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = english_to_french(textToTranslate)
    return translation


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = french_to_english(textToTranslate)
    return translation


@app.route("/")
def renderIndexPage():
    with open("templates/index.html") as file:
        content = file.read()
    return content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
