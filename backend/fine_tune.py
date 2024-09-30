from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration, TrainingArguments, Trainer
from datasets import load_dataset

# Load dữ liệu
dataset = load_dataset("text", data_files={"train": "data/vn/lan_VN.txt"})

# Khởi tạo tokenizer và model
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Xử lý dữ liệu (sử dụng dấu phân cách "|")
def preprocess_function(examples):
    try:
        questions, answers = zip(*[ex.split("|") for ex in examples["text"]])
    except ValueError:
        print("Lỗi khi tách câu hỏi và câu trả lời:", examples["text"])
        return {}  # Trả về dictionary rỗng nếu lỗi

    inputs = tokenizer(list(questions), padding="max_length", truncation=True)
    outputs = tokenizer(list(answers), padding="max_length", truncation=True)

    # Thêm các cột mới vào examples
    examples["input_ids"] = inputs.input_ids
    examples["attention_mask"] = inputs.attention_mask
    examples["labels"] = outputs.input_ids

    return examples  # Trả về examples đã được cập nhật

tokenized_datasets = dataset.map(preprocess_function, batched=True)  # Không xóa cột "text"

# Thiết lập tham số huấn luyện
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    push_to_hub=False,  # Không push lên Hugging Face Hub
    remove_unused_columns=False,  # Tắt tính năng tự động xóa cột
)

# Khởi tạo Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["train"], # Sử dụng tập train để đánh giá do không có tập validation riêng
)

# Huấn luyện mô hình
trainer.train()

# Lưu mô hình đã được fine-tuning
trainer.save_model("./backend/model/fine_tuned_model")