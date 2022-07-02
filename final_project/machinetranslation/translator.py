import json
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)
translator_instance = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=auth
)
translator_instance.set_service_url(url)


def english_to_french(english_text):
    if english_text == "" or not isinstance(english_text,str):
        return ""
    translation = translator_instance.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    if french_text == "" or not isinstance(french_text,str):
        return ""
    translation = translator_instance.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
