from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

class Chatbot:
    def __init__(self):
        model_name = "facebook/blenderbot-400M-distill"
        self.tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
        self.model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

    def get_response(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors="pt")
        reply_ids = self.model.generate(**inputs)
        return self.tokenizer.decode(reply_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")