import requests
import os

class TitleTranslator:

    def __init__(self):
        self.url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
            "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
        }

    def translate_to_english(self, text):
        if not text or text.strip() == "":
            return None

        payload = {
            "from": "es",
            "to": "en",
            "q": text
        }

        try:
            response = requests.post(self.url, json=payload, headers=self.headers)
            result = response.json()
            return result[0] if isinstance(result, list) else None
        except Exception as e:
            print("Translation failed:", e)
            return None
