# 🤖 Kwame Fredy Bot

**Your personal intelligent assistant with web search and document analysis capabilities**

## 🌐 Deployment

✅ **Deployed and available at:**  
👉 [https://kwame-fredy-bot.onrender.com](https://kwame-fredy-bot.onrender.com)

🚀 **Also available on Hugging Face Spaces:**  
👉 [https://huggingface.co/spaces/FredyHoundayi/Kwame-Fredy-AI](https://huggingface.co/spaces/FredyHoundayi/Kwame-Fredy-AI)

## ⭐ Features

- 🤖 **Natural conversation** with advanced AI
- 🔍 **Real-time Google search** for updated information
- 🌤️ **Accurate weather information** by location
- 📄 **PDF document analysis** with content extraction
- 📰 **Online article retrieval** and summarization
- 🎯 **Context-aware responses** with tool integration

## 🛠️ Technologies Used

- **[Chainlit](https://docs.chainlit.io)** - Modern chat interface
- **[LangChain](https://python.langchain.com)** - AI agent orchestration
- **[Groq](https://groq.com)** - Fast LLM inference
- **[Google Search API](https://serpapi.com/)** - Real-time web search
- **[WeatherAPI](https://www.weatherapi.com/)** - Weather data
- **[Trafilatura](https://trafilatura.readthedocs.io)** - Web content extraction
- **[PyPDF2](https://pypdf2.readthedocs.io/)** - PDF processing

## 🚀 Quick Start

### Web Usage
1. Visit [https://kwame-fredy-bot.onrender.com](https://kwame-fredy-bot.onrender.com)
2. Start chatting with Kwame Fredy Bot
3. Upload PDF files or share URLs for analysis

### Local Development
```bash
# Clone the repository
git clone https://github.com/FredyHoundayi/kwame-Fredy-bot.git
cd kwame-Fredy-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

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
# Required API Keys
GROQ_API_KEY=your_groq_api_key_here
SERP_API_KEY=your_google_search_api_key_here
GETWEATHER_API_KEY=your_weather_api_key_here
```

### Getting API Keys

1. **Groq API Key**: [Get from Groq Console](https://console.groq.com/)
2. **Google Search API Key**: [Get from SerpApi](https://serpapi.com/)
3. **Weather API Key**: [Get from WeatherAPI](https://www.weatherapi.com/)

## 💡 Usage Examples

### Weather Information
```
User: What's the weather like in Paris?
Bot: [Provides current weather conditions for Paris]
```

### Web Search
```
User: What are the latest developments in AI?
Bot: [Searches and provides recent AI news and updates]
```

### PDF Analysis
```
User: [Uploads PDF document] Can you summarize this report?
Bot: [Analyzes PDF content and provides summary]
```

### Article Retrieval
```
User: Can you analyze this article? https://example.com/article
Bot: [Extracts and analyzes the article content]
```

## 🏗️ Project Architecture

```
kwame-Fredy-bot/
├── app.py                 # Main Chainlit application
├── tools/                 # Agent tools directory
│   ├── get_weather_tool.py
│   ├── google_search_tool.py
│   ├── article_retriever.py
│   └── files_reader.py
├── public/               # Static assets (logo, avatar)
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
├── render.yaml          # Render.com deployment config
└── .env.example        # Environment variables template
```

## 🐳 Docker Deployment

### Render.com
The application is automatically deployed on Render.com with:
- **URL**: https://kwame-fredy-bot.onrender.com
- **Free tier** with automatic scaling
- **HTTPS** enabled by default

### Hugging Face Spaces
Alternative deployment on Hugging Face Spaces:
- **URL**: https://huggingface.co/spaces/FredyHoundayi/Kwame-Fredy-AI
- **GPU support** available
- **Community integration**

### Manual Docker Build
```bash
# Build the image
docker build -t kwame-fredy-bot .

# Run the container
docker run -p 7860:7860 --env-file .env kwame-fredy-bot
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Groq](https://groq.com/)** for fast LLM inference
- **[LangChain](https://python.langchain.com/)** for agent framework
- **[Chainlit](https://docs.chainlit.io/)** for chat interface
- **[Render.com](https://render.com/)** for hosting services

---

**Made with ❤️ by Fredy Houndayi**

*Your intelligent AI companion for web search, document analysis, and more!*
