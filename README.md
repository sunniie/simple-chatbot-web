## README.md cho dự án Chatbot Tiếng Việt

```markdown
# Simple Vietnamese Chatbot with Blenderbot and Hugging Face

This project demonstrates how to build a simple Vietnamese chatbot using Facebook's Blenderbot large language model and Hugging Face's Transformers library. The chatbot is integrated into a basic web interface using Flask, allowing users to interact with it through a browser.

## Features

* **Vietnamese Language Support:** The chatbot has been fine-tuned on a Vietnamese conversational dataset to provide more natural and relevant responses in Vietnamese.
* **Web Interface:** A simple web interface allows users to interact with the chatbot easily.

## Getting Started

### Prerequisites

* Python 3.7 or higher
* pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/[your_username]/[your_repo_name].git
   ```
2. Create a virtual environment:
   ```bash
   python -m venv chatbot-env
   ```
3. Activate the virtual environment:
   ```bash
   # On Windows:
   chatbot-env\Scripts\activate

   # On Linux/macOS:
   source chatbot-env/bin/activate 
   ```
4. Install the required packages:
   ```bash
   pip install -r backend/requirements.txt
   ```


### Usage

1. **Fine-tune the model (optional):**
   * If you want to fine-tune the model on your own Vietnamese dataset, place the dataset file (e.g., `my_dataset.txt`) in the `data/vn` directory.
   * Update the `data_files` path in `backend/fine_tune.py` to point to your dataset file.
   * Run the fine-tuning script:
     ```bash
     python backend/fine_tune.py
     ```
   * This will create a `fine_tuned_model` directory within `backend/model`.

2. **Run the chatbot:**
   * Start the Flask server:
     ```bash
     python backend/app.py
     ```
   * Open your web browser and navigate to `http://127.0.0.1:5000/`.
   * You can now chat with the chatbot in Vietnamese!

## Project Structure

* **`backend`:** Contains the Python code for the chatbot and web server.
    * `app.py`: Flask application logic.
    * `model/chatbot_model.py`:  Code for loading and interacting with the Blenderbot model.
    * `fine_tune.py`: Script for fine-tuning the Blenderbot model on a Vietnamese dataset.
    * `requirements.txt`: List of required Python packages.
* **`frontend`:** Contains the HTML, CSS, and JavaScript code for the web interface.
    * `index.html`: Main HTML file.
    * `styles.css`: CSS file for styling the interface.
    * `script.js`: JavaScript file for handling front-end logic.
* **`data`:** Contains training data for fine-tuning.
    * `vn`: Directory for Vietnamese datasets.
* **`README.md`**: This file.

## Credits

* **Blenderbot:** Developed by Facebook AI Research ([https://ai.facebook.com/blog/blender-bot-2-an-open-source-chatbot-that-builds-long-term-memory-and-searches-the-internet/](https://ai.facebook.com/blog/blender-bot-2-an-open-source-chatbot-that-builds-long-term-memory-and-searches-the-internet/)).
* **Hugging Face Transformers:** ([https://huggingface.co/docs/transformers/index](https://huggingface.co/docs/transformers/index))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

**Lưu ý:**

* Thay thế `[your_username]` và `[your_repo_name]` bằng username và tên repository GitHub của bạn.
*  Bạn có thể bổ sung thêm thông tin về cách sử dụng chatbot, ví dụ như cách nhập input, cách xem output,...
* Hãy kiểm tra kỹ nội dung README trước khi push lên GitHub để đảm bảo mọi thông tin đều chính xác.


Chúc bạn thành công! 
