import json
import requests
import uuid

class SubtitleTranslatorMicrosoft:
    def __init__(self):
        self.name = "Subtitle Translator Microsoft"
        self.inputs = {
            "srt_file": None,  # Input SRT file path
            "source_language": "auto",  # Default source language is auto-detection
            "target_language": "en",  # Default target language is English
            "subscription_key": None,  # Microsoft Translator API subscription key
            "region": None  # Microsoft Translator API region
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
        subscription_key = self.inputs["subscription_key"]
        region = self.inputs["region"]

        if not srt_file or not target_language or not subscription_key or not region:
            raise ValueError("SRT file, source language, target language, subscription key, and region must be provided")

        # Read the SRT file
        with open(srt_file, 'r') as file:
            srt_content = file.read()

        # Call the translation API
        translated_content = self.translate_text(srt_content, source_language, target_language, subscription_key, region)

        # Save the translated content to output
        self.outputs["translated_srt"] = translated_content

    def translate_text(self, text, source_language, target_language, subscription_key, region):
        # This function calls the translation API to get the translated text
        url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"
        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': region,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{
            'text': text
        }]
        params = f"&from={source_language}&to={target_language}"

        response = requests.post(url + params, headers=headers, json=body)
        response_data = response.json()

        translated_text = ''
        for item in response_data:
            translated_text += item['translations'][0]['text'] + '\n'

        return translated_text

    def execute(self):
        self.translate_subtitles()

# Example usage:
translator_node = SubtitleTranslatorMicrosoft()
translator_node.set_input("srt_file", "path/to/your/file.srt")
translator_node.set_input("source_language", "auto")  # You can specify a source language if known
translator_node.set_input("target_language", "es")
translator_node.set_input("subscription_key", "YOUR_SUBSCRIPTION_KEY")
translator_node.set_input("region", "YOUR_REGION")
translator_node.execute()
translated_srt = translator_node.get_output("translated_srt")
print(translated_srt)
