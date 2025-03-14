# to use the translate script, you need a deepl api key
# cp .env.example .env
# put the key in .env
# create a python venv : python -m venv ~/env
# activate it : source ~/env/bin/activate
# install requirements : pip install -r requirements.txt 
# translate !
# python translate.py


import os
import deepl
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la clé API
deepl_api_key = os.getenv("DEEPL_API_KEY")



def translate_markdown_files(input_dir, output_dir, src_lang='en', dest_lang='fr'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    translator = deepl.Translator(deepl_api_key)

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_dir, filename)
            output_filepath = os.path.join(output_dir, filename)

            with open(input_filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            try:
                # Translate the content using deepl api
                result = translator.translate_text(content, source_lang=src_lang, target_lang=dest_lang)
                translated = result.text
                
                # Check we have a non empty reply
                if translated:
                    with open(output_filepath, 'w', encoding='utf-8') as file:
                        file.write(translated)
                    print(f"Translated {filename} to {dest_lang}")
                else:
                    raise ValueError("Empty response from translation service")
                    
            except Exception as e:
                print(f"Failed to translate {filename}: {e}")


input_directory = './docs/en'
output_directory = './docs/fr'
translate_markdown_files(input_directory, output_directory)