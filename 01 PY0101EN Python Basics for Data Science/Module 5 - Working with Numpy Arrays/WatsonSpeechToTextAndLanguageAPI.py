#################################################
# Watson Speech to Text and Language API Lab
#################################################

import urllib.request

# you will need the following library 
# !pip install PyJWT==1.7.1 ibm_watson wget

from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Get url from IBM cloud website
url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0003e906-550c-43a5-8340-0bca7053ddb6"

# Get API key from IBM cloud website
iam_apikey_s2t = "E1Qlydz-jgHnXer3e_EigCyx-AHOwPl3-8KId3hykRg_"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# !wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3

# Download file needed for the lab
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3'
# urllib.request.urlretrieve(url, 'PolynomialRegressionandPipelines.mp3')

filename='PolynomialRegressionandPipelines.mp3'

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

# print(response.result)

from pandas import json_normalize

print(json_normalize(response.result['results'],"alternatives"))

# print(response)

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)

from ibm_watson import LanguageTranslatorV3

# Get url from IBM cloud website
url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/04ff2aab-8e71-4640-8560-e214e8255e09'

# Get API key from IBM cloud website
apikey_lt='x_Bv7TFhyO5PJpIypTieqw8rCwbR_uUJ9CgArLZZ7FzR'

version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
# language_translator

from pandas import json_normalize

print(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response
translation=translation_response.get_result()

# Spanish Translation
print("SPANISH TRANSLATION")
spanish_translation =translation['translations'][0]['translation']
print(spanish_translation)

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

# Re-Translate to English
print("TRANSLATE BACK FROM SPANISH TO ENGLISH")
translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)

# Exercise 1
# Translate to French.

translation_newer = language_translator.translate(text=recognized_text ,model_id='en-fr').get_result()

# Translate to French
print("TRANSLATE TO FRENCH")
translation_french=translation_newer['translations'][0]['translation']
print(translation_french)