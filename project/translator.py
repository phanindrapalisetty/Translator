import os
import ibm_watson
import ibm_cloud_sdk_core
import pandas as pd
from dotenv import load_dotenv

def translateText(recognized_text, id):
    translation_response = language_translator.translate(text=recognized_text, model_id=id)
    translation=translation_response.get_result()
    result = translation['translations'][0]['translation']
    return result

load_dotenv()
apikey = os.environ['api_lt']
url = os.environ['url_lt']

version = '2020-10-24'

authenticator = ibm_cloud_sdk_core.authenticators.IAMAuthenticator(apikey)

language_translator = ibm_watson.LanguageTranslatorV3(version=version,authenticator=authenticator)
language_translator.set_service_url(url)

df = pd.json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
a = df.set_index("name").T.to_dict("list")
