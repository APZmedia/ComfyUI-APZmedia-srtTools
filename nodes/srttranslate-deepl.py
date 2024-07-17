import json
import requests

class SubtitleTranslatorDeepL:
    def __init__(self):
        self.name = "Subtitle Translator DeepL"
        self.inputs = {
            "srt_file": None,  # Input SRT file path
            "source_language": "auto",  # Default source language is auto-detection
            "target_language": "EN",  # Default target language is English
            "auth_key": None  # DeepL API authentication key
        }
        self.outputs = {
            "translated_srt": None  # Output translated SRT content
        }

    def set_input(self, input_name, value):
        if input_name in self.inputs:
            self.inputs[input_name] = value
        else:
            raise ValueError(f"Input {input_name} not recognized")

    def get_output(self, output_name):
        if output_name in self.outputs:
            return self.outputs[output_name]
        else:
            raise ValueError(f"Output {output_name} not recognized")

    def translate_subtitles(self):
        srt_file = self.inputs["srt_file"]
        source_language = self.inputs["source_language"]
        target_language = self.inputs["target_language"]
        auth_key = self.inputs["auth_key"]

        if not srt_file or not target_language or not auth_key:
            raise ValueError("SRT file, target language, and authentication key must be provided")

        # Read the SRT file
        with open(srt_file, 'r') as file:
            srt_content = file.read()

        # Call the DeepL translation API
        translated_content = self.translate_text(srt_content, source_language, target_language, auth_key)

        # Save the translated content to output
        self.outputs["translated_srt"] = translated_content

    def translate_text(self, text, source_language, target_language, auth_key):
        # This function calls the DeepL API to get the translated text
        url = "https://api.deepl.com/v2/translate"
        headers = {
            'Authorization': f'DeepL-Auth-Key {auth_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'text': text,
            'source_lang': source_language,
            'target_lang': target_language,
            'split_sentences': '0'  # To keep the context intact
        }

        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()

        if 'translations' not in response_data:
            raise Exception("Error in translation response")

        translated_text = ''
        for item in response_data['translations']:
            translated_text += item['text'] + '\n'

        return translated_text

    def execute(self):
        self.translate_subtitles()

# Example usage:
translator_node = SubtitleTranslatorDeepL()
translator_node.set_input("srt_file", "path/to/your/file.srt")
translator_node.set_input("source_language", "auto")  # You can specify a source language if known
translator_node.set_input("target_language", "ES")
translator_node.set_input("auth_key", "YOUR_DEEPL_AUTH_KEY")
translator_node.execute()
translated_srt = translator_node.get_output("translated_srt")
print(translated_srt)
