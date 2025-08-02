# 🌐 Flask API for Text Generation using LangChain and Gemini

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Latest-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-orange.svg)
![REST API](https://img.shields.io/badge/REST-API-purple.svg)
![Swagger](https://img.shields.io/badge/Swagger-Docs-brightgreen.svg)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-brightgreen.svg)

**🚀 Build REST APIs • 🤖 Integrate AI • 📚 Learn Flask • 🆓 Use Free Gemini API**

</div>

---

## 📖 Table of Contents

- [🌟 What is This Project?](#-what-is-this-project)
- [🎓 What You'll Learn](#-what-youll-learn)
- [🔑 Getting Your Free API Key](#-getting-your-free-api-key)
- [📁 Project Structure Explained](#-project-structure-explained)
- [🛠️ Setup Instructions](#️-setup-instructions)
- [🚀 How to Run the API](#-how-to-run-the-api)
- [🌐 API Endpoints Guide](#-api-endpoints-guide)
- [📝 Code Walkthrough](#-code-walkthrough)
- [🧪 Testing the API](#-testing-the-api)
- [💡 Tips for Beginners](#-tips-for-beginners)
- [🔧 Troubleshooting](#-troubleshooting)
- [🎯 Next Steps](#-next-steps)

---

## 🌟 What is This Project?

This is a **Flask REST API** that provides text generation capabilities using **Google's Gemini AI** through **LangChain**. Instead of a command-line interface, you can now make HTTP requests to generate AI text!

### 🎯 **Perfect for:**
- 👨‍💻 **Web Developers** learning API development
- 🎓 **Students** studying REST APIs and AI integration
- 🚀 **Frontend Developers** who need an AI backend
- 🔬 **Anyone** wanting to build AI-powered applications

### 🆓 **Why This Project?**
- **100% Free** - Uses Google's free Gemini API
- **Real REST API** - Professional API structure
- **Easy Integration** - Use from any programming language
- **Well Documented** - Swagger UI included
- **Production Ready** - Proper error handling

### 🔄 **From CLI to API:**
This project converts a command-line text generator into a web API that you can integrate into websites, mobile apps, or other services.

---

## 🎓 What You'll Learn

By completing this project, you'll master:

| 📚 **Concept** | 🎯 **What You'll Master** |
|----------------|---------------------------|
| **🌐 REST API Development** | Building HTTP endpoints with Flask |
| **🤖 AI Integration** | Connecting APIs to LangChain and Gemini |
| **📋 Request/Response Handling** | Processing JSON data in APIs |
| **📚 API Documentation** | Creating Swagger/OpenAPI docs |
| **⚠️ Error Handling** | Managing API errors and status codes |
| **🧪 API Testing** | Testing endpoints with different tools |

---

## 🔑 Getting Your Free API Key

### 📋 **Step-by-Step Guide:**

1. **🌐 Visit Google AI Studio**
   ```
   👉 Go to: https://aistudio.google.com/app/apikey
   ```

2. **🔐 Sign In**
   - Use your Google account (Gmail, etc.)
   - No special account needed!

3. **🆕 Create API Key**
   - Click the **"Create API Key"** button
   - Choose **"Create API key in new project"**

4. **💾 Save Your Key**
   - **Copy** the key immediately
   - **Store it safely** (we'll use it later)
   - **Never share it publicly!**

### 🎁 **What You Get for Free:**
- ✅ **60 requests per minute**
- ✅ **Gemini 2.0 Flash model** (fastest!)
- ✅ **No credit card required**
- ✅ **Perfect for learning and development**

---

## 📁 Project Structure Explained

Let's understand every file and folder in our Flask API project:

```
📦 Flask-api-generate-endpoint-LLM/
├── 📄 README.md                    # 👈 You are here! Complete documentation
├── 📄 requirements.txt             # 📦 Python packages needed
├── 📄 app.py                       # 🚀 Main Flask application
├── 📄 tests.py                     # 🧪 API tests
├── 📄 .env.example                 # 📝 Environment variables example
├── 📄 .gitignore                   # 🚫 Files to ignore in Git
│
├── 📁 model/                       # 🏗️ Data structures
│   ├── 📄 __init__.py             # 🐍 Python package marker
│   └── 📄 text_generation.py      # 📝 Request/Response classes
│
├── 📁 services/                    # 🔧 Business logic
│   ├── 📄 __init__.py             # 🐍 Python package marker
│   └── 📄 gemini_service.py       # 🤖 AI integration service
│
├── 📁 util/                        # 🛠️ Utility functions
│   ├── 📄 __init__.py             # 🐍 Python package marker
│   └── 📄 config.py               # ⚙️ Configuration management
│
├── 📁 exception/                   # ⚠️ Error handling
│   ├── 📄 __init__.py             # 🐍 Python package marker
│   └── 📄 generation_exceptions.py # 🚨 Custom exceptions
│
└── 📁 api/                         # 🌐 API-specific code
    ├── 📄 __init__.py             # 🐍 Python package marker
    ├── 📄 routes.py               # 🛣️ API endpoint definitions
    └── 📄 swagger_config.py       # 📚 API documentation config
```

### 🔍 **Detailed File Explanations:**

#### 📄 **app.py** - The Flask Application Heart
```python
# This is the main Flask application file
# Contains:
# - Flask app initialization
# - API route registration
# - Swagger documentation setup
# - Error handlers
# - Application startup logic
```

#### 🛣️ **api/routes.py** - API Endpoints
```python
# Contains all our REST API endpoints:
# - POST /api/generate/simple    - Simple text generation
# - POST /api/generate/styled    - Styled text generation  
# - POST /api/generate/creative  - Creative content generation
# - GET /api/health              - Health check
# - GET /api/docs                - API documentation
```

#### 📚 **api/swagger_config.py** - API Documentation
```python
# Configures Swagger/OpenAPI documentation:
# - API metadata (title, version, description)
# - Request/response schemas
# - Interactive documentation interface
# - Example requests and responses
```

#### 🏗️ **model/text_generation.py** - Same as CLI Version
```python
# Same classes as the CLI project:
# - TextRequest: User input structure
# - TextResponse: AI response structure
# - Now also used for JSON serialization
```

#### 🤖 **services/gemini_service.py** - AI Integration
```python
# Same LangChain + Gemini integration:
# - GeminiService class
# - generate_simple_text()
# - generate_with_template()
# - generate_creative_content()
```

#### ⚙️ **util/config.py** - Configuration
```python
# Same configuration management:
# - API key loading
# - Environment variables
# - Default settings
```

#### ⚠️ **exception/generation_exceptions.py** - Error Handling
```python
# Same custom exceptions:
# - APIKeyException
# - GenerationException  
# - InvalidInputException
# - Now also used for HTTP error responses
```

---

## 🛠️ Setup Instructions

### 📋 **Prerequisites:**
- 🐍 **Python 3.8 or higher** ([Download here](https://python.org))
- 💻 **Command line/Terminal access**
- 🌐 **Internet connection**
- 🔑 **Google account** (for API key)

### 🚀 **Step 1: Clone the Repository**
```bash
# Download the project
git clone https://github.com/Amruth22/Flask-api-generate-endpoint-LLM.git

# Enter the project folder
cd Flask-api-generate-endpoint-LLM
```

### 🏠 **Step 2: Create Virtual Environment**
```bash
# Create a virtual environment (highly recommended!)
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# You should see (venv) in your terminal now!
```

> 💡 **Why virtual environment?** It keeps this project's packages separate from your other Python projects and prevents conflicts!

### 📦 **Step 3: Install Dependencies**
```bash
# Install all required packages
pip install -r requirements.txt

# This installs:
# - flask (web framework)
# - flask-restx (REST API extensions + Swagger)
# - langchain-google-genai (Gemini integration)
# - langchain (AI framework)
# - python-dotenv (environment variables)
# - pytest (testing)
```

### 🔑 **Step 4: Set Up Your API Key**

**🎯 Method 1: Environment Variable (Recommended)**
```bash
# Windows:
set GEMINI_API_KEY=your-actual-api-key-here

# Mac/Linux:
export GEMINI_API_KEY=your-actual-api-key-here
```

**🎯 Method 2: .env File**
```bash
# Copy the example file
cp .env.example .env

# Edit .env file and add your key:
# GEMINI_API_KEY=your-actual-api-key-here
```

---

## 🚀 How to Run the API

### 🎮 **Starting the Flask Server:**
```bash
# Make sure you're in the project folder and virtual environment is active
python app.py

# You should see:
# * Running on http://127.0.0.1:5000
# * Debug mode: on
```

### 🌐 **Access Points:**
Once the server is running, you can access:

- **🏠 API Base URL**: `http://localhost:5000`
- **📚 Swagger Documentation**: `http://localhost:5000/api/docs`
- **❤️ Health Check**: `http://localhost:5000/api/health`

### 🎯 **What You'll See:**
```bash
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

---

## 🌐 API Endpoints Guide

### 📋 **Complete API Reference:**

#### 🔹 **1. Health Check**
```http
GET /api/health
```
**Purpose**: Check if the API is running  
**Response**:
```json
{
  "status": "healthy",
  "message": "Flask API is running successfully!",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

#### 🔹 **2. Simple Text Generation**
```http
POST /api/generate/simple
Content-Type: application/json

{
  "prompt": "What is artificial intelligence?"
}
```
**Response**:
```json
{
  "content": "Artificial Intelligence (AI) is technology that enables computers to perform tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.",
  "model_used": "gemini-2.0-flash",
  "timestamp": "2024-01-01 12:00:00"
}
```

#### 🔹 **3. Styled Text Generation**
```http
POST /api/generate/styled
Content-Type: application/json

{
  "topic": "Python programming",
  "style": "funny"
}
```
**Response**:
```json
{
  "content": "Python programming is like having a conversation with a very literal snake that does exactly what you tell it to do, even if you accidentally ask it to print 'Hello World' a million times!",
  "model_used": "gemini-2.0-flash",
  "timestamp": "2024-01-01 12:00:00"
}
```

**Available Styles:**
- `"formal"` - Professional, academic tone
- `"casual"` - Friendly, conversational tone  
- `"funny"` - Humorous, entertaining tone

#### 🔹 **4. Creative Content Generation**
```http
POST /api/generate/creative
Content-Type: application/json

{
  "content_type": "poem",
  "subject": "ocean"
}
```
**Response**:
```json
{
  "content": "Waves whisper secrets to the shore,\nDeep blue mysteries and so much more,\nEndless horizon where sky meets sea,\nOcean's rhythm sets my spirit free.",
  "model_used": "gemini-2.0-flash",
  "timestamp": "2024-01-01 12:00:00"
}
```

**Available Content Types:**
- `"poem"` - Creative poetry
- `"story"` - Short stories
- `"joke"` - Funny jokes
- `"fact"` - Interesting facts

### 🚨 **Error Responses:**

#### **400 Bad Request** - Invalid Input
```json
{
  "error": "Invalid input. Please provide a valid prompt.",
  "status_code": 400
}
```

#### **500 Internal Server Error** - Generation Failed
```json
{
  "error": "Failed to generate text. Please try again.",
  "status_code": 500
}
```

---

## 📝 Code Walkthrough

Let's understand how the Flask API works:

### 🌐 **Flask Application Structure:**

```python
# In app.py
from flask import Flask
from flask_restx import Api
from api.routes import api as generation_api

app = Flask(__name__)
api = Api(app, doc='/api/docs/')  # Swagger documentation

# Register API routes
api.add_namespace(generation_api, path='/api')

if __name__ == '__main__':
    app.run(debug=True)  # Start the server
```

### 🛣️ **API Routes Definition:**

```python
# In api/routes.py
from flask_restx import Namespace, Resource
from services.gemini_service import GeminiService

api = Namespace('generate', description='Text generation operations')

@api.route('/simple')
class SimpleGeneration(Resource):
    def post(self):
        # Get JSON data from request
        data = request.get_json()
        prompt = data.get('prompt')
        
        # Call AI service
        service = GeminiService(api_key)
        response = service.generate_simple_text(prompt)
        
        # Return JSON response
        return {
            'content': response.content,
            'model_used': response.model_used,
            'timestamp': response.timestamp
        }
```

### 🔄 **Request Flow:**

1. **📨 Client sends HTTP request** with JSON data
2. **🛣️ Flask routes** the request to appropriate endpoint
3. **🔍 Route handler** extracts data from JSON
4. **🤖 AI service** processes the request using LangChain + Gemini
5. **📤 Response** is formatted as JSON and sent back

### 🏗️ **Same Backend, New Interface:**

The core AI logic remains identical to the CLI version:
- Same `GeminiService` class
- Same `TextRequest` and `TextResponse` models
- Same error handling
- Same LangChain integration

**Only difference**: Instead of terminal input/output, we use HTTP requests/responses!

---

## 🧪 Testing the API

### 🔧 **Method 1: Using curl (Command Line)**

```bash
# Test health check
curl http://localhost:5000/api/health

# Test simple generation
curl -X POST http://localhost:5000/api/generate/simple \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is machine learning?"}'

# Test styled generation
curl -X POST http://localhost:5000/api/generate/styled \
  -H "Content-Type: application/json" \
  -d '{"topic": "cats", "style": "funny"}'

# Test creative generation
curl -X POST http://localhost:5000/api/generate/creative \
  -H "Content-Type: application/json" \
  -d '{"content_type": "joke", "subject": "programming"}'
```

### 🌐 **Method 2: Using Swagger UI (Recommended for Beginners)**

1. **Start your Flask server**: `python app.py`
2. **Open browser**: Go to `http://localhost:5000/api/docs`
3. **Interactive testing**: Click on any endpoint to test it
4. **Try it out**: Use the "Try it out" button to send requests

### 🐍 **Method 3: Using Python requests**

```python
import requests

# Test simple generation
response = requests.post('http://localhost:5000/api/generate/simple', 
                        json={'prompt': 'Explain quantum computing'})
print(response.json())

# Test styled generation
response = requests.post('http://localhost:5000/api/generate/styled',
                        json={'topic': 'space', 'style': 'casual'})
print(response.json())
```

### 🧪 **Method 4: Run Test Suite**

```bash
# Run all API tests
python -m pytest tests.py -v

# Expected output:
# ✅ test_health_endpoint PASSED
# ✅ test_simple_generation PASSED
# ✅ test_styled_generation PASSED
# ✅ test_creative_generation PASSED
```

---

## 💡 Tips for Beginners

### 🎯 **API Development Tips:**

1. **📚 Always Check Swagger Docs**
   ```
   Visit: http://localhost:5000/api/docs
   - See all available endpoints
   - Test requests interactively
   - View request/response examples
   ```

2. **🔍 Test with Simple Requests First**
   ```json
   Start with:
   {"prompt": "Hello"}
   
   Then try:
   {"prompt": "Explain AI in simple terms"}
   ```

3. **📋 Use Proper JSON Format**
   ```json
   ✅ Correct:
   {"prompt": "your text here"}
   
   ❌ Wrong:
   {prompt: "your text here"}  // Missing quotes
   {'prompt': 'your text'}     // Wrong quote type
   ```

### 🔧 **Development Best Practices:**

- **💾 Always Set API Key**: Check environment variables first
- **🔄 Restart Server**: After code changes, restart Flask server
- **📊 Monitor Logs**: Check terminal for error messages
- **🧪 Test Frequently**: Use Swagger UI for quick testing
- **📝 Check JSON**: Validate JSON format before sending requests

### 🚀 **Integration Tips:**

- **🌐 Frontend Integration**: Use fetch() or axios in JavaScript
- **📱 Mobile Apps**: Use HTTP client libraries
- **🐍 Python Scripts**: Use requests library
- **📊 Data Analysis**: Integrate with pandas, jupyter notebooks

---

## 🔧 Troubleshooting

### 🚨 **Common Issues and Solutions:**

#### ❌ **"Address already in use" Error**
```bash
# Problem: Port 5000 is already being used
# Solution 1: Kill existing process
lsof -ti:5000 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :5000   # Windows (find PID, then kill)

# Solution 2: Use different port
python app.py --port 5001
```

#### ❌ **"API key is missing" Error**
```bash
# Check if environment variable is set
echo $GEMINI_API_KEY  # Mac/Linux
echo %GEMINI_API_KEY% # Windows

# If empty, set it:
export GEMINI_API_KEY=your-key-here  # Mac/Linux
set GEMINI_API_KEY=your-key-here     # Windows
```

#### ❌ **"404 Not Found" Error**
```bash
# Make sure you're using correct URLs:
✅ http://localhost:5000/api/health
✅ http://localhost:5000/api/generate/simple

❌ http://localhost:5000/health        # Missing /api
❌ http://localhost:5000/generate      # Missing /api
```

#### ❌ **"400 Bad Request" Error**
```bash
# Check your JSON format:
✅ Content-Type: application/json
✅ Valid JSON: {"prompt": "text"}

❌ Missing Content-Type header
❌ Invalid JSON: {prompt: text}
```

#### ❌ **"Module not found" Error**
```bash
# Make sure virtual environment is activated
# You should see (venv) in terminal

# Reinstall dependencies
pip install -r requirements.txt

# Check Flask installation
python -c "import flask; print(flask.__version__)"
```

### 🆘 **Getting Help:**

1. **📖 Check Flask logs** in terminal for detailed error messages
2. **🔍 Use Swagger UI** at `/api/docs` for interactive testing
3. **📚 Verify JSON format** using online JSON validators
4. **💬 Create an issue** in this repository for help

---

## 🎯 Next Steps

### 🚀 **Enhance This API:**

1. **🔐 Add Authentication:**
   ```python
   # Add API key authentication
   # Add JWT tokens
   # Add user management
   ```

2. **📊 Add More Features:**
   ```python
   # Add request logging
   # Add rate limiting
   # Add caching
   # Add batch processing
   ```

3. **🌐 Frontend Integration:**
   ```javascript
   // Build React/Vue frontend
   // Create mobile app
   // Add real-time features
   ```

4. **🚀 Deploy to Cloud:**
   ```bash
   # Deploy to Heroku
   # Deploy to AWS
   # Deploy to Google Cloud
   # Add Docker containers
   ```

### 📚 **Learn More About:**

- **🌐 Flask**: [Official Documentation](https://flask.palletsprojects.com/)
- **📋 REST APIs**: [REST API Tutorial](https://restfulapi.net/)
- **📚 Swagger/OpenAPI**: [Swagger Documentation](https://swagger.io/docs/)
- **🧪 API Testing**: [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/)
- **🚀 Deployment**: [Flask Deployment Options](https://flask.palletsprojects.com/en/2.3.x/deploying/)

### 🎓 **Related Projects to Build:**

1. **💬 Chatbot API** - Conversational AI with memory
2. **📄 Document API** - Text summarization and analysis  
3. **🔍 Search API** - Semantic search with embeddings
4. **🎨 Content API** - Multi-modal content generation
5. **📊 Analytics API** - Text analysis and insights

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🎯 **Ways to Contribute:**

- 🐛 **Report Bugs**: Found an API issue? Create an issue!
- ✨ **Suggest Features**: Have an idea for new endpoints?
- 📝 **Improve Documentation**: Help make this README even better!
- 🧪 **Add Tests**: More API tests = more reliable code!
- 🎨 **Add Features**: Implement new functionality!

### 📋 **Contribution Guidelines:**

1. **🍴 Fork the repository**
2. **🌿 Create a feature branch**: `git checkout -b feature/amazing-api-feature`
3. **💾 Commit your changes**: `git commit -m 'Add amazing API feature'`
4. **📤 Push to branch**: `git push origin feature/amazing-api-feature`
5. **🔄 Open a Pull Request**

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 🎁 **What this means:**
- ✅ **Free to use** for personal and commercial projects
- ✅ **Free to modify** and distribute
- ✅ **No warranty** - use at your own risk
- ✅ **Attribution appreciated** but not required

---

## 🙏 Acknowledgments

- **🤖 Google** for providing the free Gemini API
- **🦜 LangChain** team for the amazing AI framework
- **🌐 Flask** community for the excellent web framework
- **📚 Flask-RESTX** for API documentation tools
- **🐍 Python** community for excellent libraries

---

<div align="center">

### 🌟 **Star this repository if it helped you learn APIs!** ⭐

**Made with ❤️ for developers learning AI APIs**

[🔝 Back to Top](#-flask-api-for-text-generation-using-langchain-and-gemini)

</div>