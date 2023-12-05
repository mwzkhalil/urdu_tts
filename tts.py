# urdu_tts/tts.py
from transformers import VitsModel, AutoTokenizer
import torch

class UrduTTS:
    def __init__(self):
        self.tts_model = VitsModel.from_pretrained("facebook/mms-tts-urd-script_arabic")
        self.tts_tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-urd-script_arabic")

    def generate_audio(self, text):
        inputs = self.tts_tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            tts_output = self.tts_model(**inputs).waveform

        return tts_output
