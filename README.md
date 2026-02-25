---
title: Kwame Fredy Bot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
app_port: 7860
short_description: Personal AI assistant with web search and document analysis
---

# 🤖 Kwame Fredy Bot

**Your personal intelligent assistant with web search and document analysis capabilities**

## 🌐 Deployment

✅ **Deployed and available at:**  
👉 [https://huggingface.co/spaces/FredyHoundayi/Kwame-Fredy-AI](https://huggingface.co/spaces/FredyHoundayi/Kwame-Fredy-AI)

## ⭐ Features

- 🤖 **Natural conversation** with advanced AI
- 🔍 **Real-time Google search** for updated information
- 🌤️ **Accurate weather information** by location
- 📄 **PDF document analysis** with content extraction
- 📰 **Web article extraction** from URLs
- 📊 **Modern interface** with Chainlit

## 🛠️ Technologies Used

- **[Chainlit](https://chainlit.io/)** - Modern and responsive chat interface
- **[LangChain](https://python.langchain.com/)** - Powerful LLM framework
- **[Groq](https://groq.com/)** - Ultra-fast LLM API (Llama 3.3 70B)
- **[SerpApi](https://serpapi.com/)** - Professional Google search
- **[Tavily](https://tavily.com/)** - Alternative web search
- **[PyPDF2](https://pypdf2.readthedocs.io/)** - PDF document processing

## 🚀 How to Use

### 1. **Web Interface** (Recommended)
Visit the deployed application directly:  
[https://huggingface.co/spaces/FredyHoundayi/Kwame-Fredy-AI](https://huggingface.co/spaces/FredyHoundayi/Kwame-Fredy-AI)

### 2. **Local Installation**
```bash
# Clone the repository
git clone https://github.com/FredyHoundayi/kwame-Fredy-bot.git
cd kwame-Fredy-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the application
chainlit run app.py
```

## 🔑 API Keys Configuration

Create a `.env` file with the following keys:

```env
GROQ_API_KEY=your_groq_key
SERP_API_KEY=your_serpapi_key
TAVILY_API_KEY=your_tavily_key
GETWEATHER_API_KEY=your_weather_key
```

### Getting API Keys
- **Groq** : [console.groq.com](https://console.groq.com/)
- **SerpApi** : [serpapi.com](https://serpapi.com/)
- **Tavily** : [tavily.com](https://tavily.com/)
- **WeatherAPI** : [weatherapi.com](https://www.weatherapi.com/)

## 📖 Usage Examples

### 💬 Simple Conversation
```
User: Hi, how are you?
Bot: Hello! I'm Kwame Fredy Bot, your personal assistant. I'm doing great, thank you! How can I help you today?
```

### 🔍 Information Search
```
User: What are the latest news about AI?
Bot: [Uses Google Search to provide updated information]
```

### 📄 Document Analysis
```
User: [Upload PDF] Can you summarize this document?
Bot: [Reads and analyzes the PDF to provide a detailed summary]
```

### 🌤️ Weather Information
```
User: What's the weather like in Paris?
Bot: [Provides current weather information for Paris]
```

## 🏗️ Project Architecture

```
kwame-Fredy-bot/
├── app.py                 # Main Chainlit application
├── assistant.py           # Alternative LangChain configuration
├── tools/                 # Specialized tools
│   ├── google_search_tool.py
│   ├── get_weather_tool.py
│   ├── tavily_tool.py
│   ├── article_retriever.py
│   └── files_reader.py
├── .chainlit/            # Chainlit configuration
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── fly.toml             # Fly.io configuration
└── README.md            # Documentation
```

## 🐳 Docker Deployment

### Hugging Face Spaces
```bash
# Push to Hugging Face
git push space main
```

### Fly.io
```bash
# Deploy to Fly.io
fly deploy
```

### Local Docker
```bash
# Build the image
docker build -t kwame-fredy-bot .

# Run the container
docker run -p 8000:8000 kwame-fredy-bot
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add a new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the **MIT** License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Chainlit** for the amazing chat interface
- **Groq** for the ultra-fast LLM API
- **LangChain** for the powerful framework
- **Hugging Face** for free hosting

---

**Developed with ❤️ by [Fredy Houndayi](https://github.com/FredyHoundayi)**

🌟 **Don't forget to give the project a star if you like it!**
