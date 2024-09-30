import os
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

class Chatbot:
    def __init__(self):
        self.model_name = "facebook/blenderbot-400M-distill"  # Tên mô hình gốc
        self.tokenizer = BlenderbotTokenizer.from_pretrained(self.model_name)
        
        # Đường dẫn tuyệt đối đến mô hình đã được fine-tuning
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, "fine_tuned_model")

        self.model = BlenderbotForConditionalGeneration.from_pretrained(model_path)

        # Load lại trọng số của tokenizer từ mô hình đã được fine-tuning (nếu có)
        tokenizer_path = os.path.join(model_path, "tokenizer.json")
        if os.path.exists(tokenizer_path):
            self.tokenizer = BlenderbotTokenizer.from_pretrained(tokenizer_path)

    def get_response(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors="pt")
        reply_ids = self.model.generate(**inputs)
        return self.tokenizer.decode(reply_ids[0], skip_special_tokens=True)