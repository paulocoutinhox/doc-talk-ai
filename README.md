<p align="center">
    <a href="https://github.com/paulocoutinhox/doc-talk-ai" target="_blank" rel="noopener noreferrer">
        <img width="180" src="extras/images/logo.png" alt="Logo">
    </a>
</p>

# DOC TALK - AI 🧠

**DOC TALK - AI** is an interactive application that allows users to **chat with their documents** using artificial intelligence. With this tool, you can **ask questions about your files** and receive instant answers, eliminating the need to manually search through them. The project is developed in **Python** and utilizes **Streamlit** to provide a user-friendly and intuitive interface.

## 🚀 Features

- 📄 **Supports multiple document formats** (PDF, TXT, DOCX, etc.)
- 🔍 **Intelligent search** within uploaded files
- 🧠 **Integration with local and cloud AI models**
- 🌍 **Compatible with OpenAI GPT, Gemini AI, and more**
- 💾 **Stores interaction history for quick reference**
- 🔧 **Simple and flexible configuration**
- 🌐 **Easy-to-use web interface built with Streamlit**

## 📥 Installation

### **1. Clone the Repository**
```sh
git clone https://github.com/paulocoutinhox/doc-talk-ai.git
cd doc-talk-ai
```

### **2. Create a Virtual Environment**
```sh
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run the Application**
```sh
python3 -m streamlit run app.py
```

## ⚙️ Configuration

### **1. Set Credentials for Cloud AI Models**
If you want to use **OpenAI GPT, Gemini AI, or other cloud models**, add your API keys to the configuration file.

📖 See the detailed guide:
📌 [Cloud Models Configuration](docs/CLOUD_MODELS.md)

### **2. Set Custom Root Directory (Optional)**
If you want to change the directory where data is stored, define the environment variable:

#### **Linux/macOS**
```sh
export DOC_TALK_AI_ROOT="/custom/path"
```

#### **Windows (Command Prompt)**
```sh
set DOC_TALK_AI_ROOT="C:\custom\path"
```

#### **Windows (PowerShell)**
```powershell
$env:DOC_TALK_AI_ROOT="C:\custom\path"
```

## 🛠️ Usage

1. **Run the Application**
   ```sh
   python3 -m streamlit run app.py
   ```

2. **In the Web Interface, follow these steps:**
   - **Upload a document** you want to interact with
   - **Select an AI model** (cloud or local)
   - **Ask questions in natural language** about the document
   - **Receive AI-generated responses instantly** 🎯

## 📂 Project Structure

```
doc-talk-ai/
│
├── README.md               # Project documentation
├── app.py                  # Main entry point
├── requirements.txt        # Core dependencies
│
├── data/                   # Data storage
│   ├── chroma-db/          # Vector database
│   ├── uploads/            # Uploaded documents
│
├── docs/                   # Additional documentation
│
├── extras/                 # Additional resources
│   └── images/             # Logos and screenshots
│
├── helpers/                # Utility functions
│   ├── file.py             # File handling
│   ├── model.py            # Model management
│   ├── prompt.py           # Prompt generation
│   └── string.py           # String utilities
│
├── lang_chain/             # AI logic and document processing
│   └── document_chat.py    # Core logic for document interaction
│
├── models/                 # AI model implementations
│   ├── base_model.py       # Base class for AI models
│   ├── gemini_model.py     # Gemini AI integration
│   └── openai_model.py     # OpenAI GPT integration
```

## 🤝 Contributing

Want to improve the project? Follow these steps:

1. **Fork** the repository
2. **Create a branch** for your feature (`git checkout -b my-feature`)
3. **Commit** your changes (`git commit -m "Added new feature"`)
4. **Push** to GitHub (`git push origin my-feature`)
5. **Open a Pull Request** 🚀

## 📞 Contact

For questions or suggestions, reach out:
💌 **paulocoutinhox@gmail.com**
🔗 **[GitHub](https://github.com/paulocoutinho)**

## 🖼️ Screenshots

<img width="280" src="https://github.com/paulocoutinhox/doc-talk-ai/blob/main/extras/images/screenshot.png?raw=true">

<img width="280" src="https://github.com/paulocoutinhox/doc-talk-ai/blob/main/extras/images/screenshot-2.png?raw=true">

## 📜 License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2025, Paulo Coutinho
