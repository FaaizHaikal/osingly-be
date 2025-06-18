from transformers import MarianTokenizer, MarianMTModel
import torch
import re

class Translator:
    def __init__(self, model_path: str = "models/osing-translator"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = MarianTokenizer.from_pretrained(model_path)
        self.model = MarianMTModel.from_pretrained(model_path).to(self.device)
        
    def sanitize(self, text: str) -> str:
        text = text.strip()
        text = re.sub(r"[\r\n+]", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.lower()

    def translate(self, text: str, from_osing: bool = False) -> dict:
        text = self.sanitize(text)
        
        if not text.strip():
            return {"text": "", "confidence": 0.0}

        # Language tag
        lang_tag = ">>indonesia<<" if from_osing else ">>osing<<"
        input_text = f"{lang_tag} {text}"

        inputs = self.tokenizer([input_text], return_tensors="pt", padding=True).to(self.device)

        # Generate
        with torch.no_grad():
            outputs = self.model.generate(**inputs)

        translated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Dummy confidence
        confidence = 1.0 if translated.strip() else 0.0

        return {
            "text": translated,
            "confidence": confidence
        }
