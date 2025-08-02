"""
Main Flask application for Text Generation API
Provides REST endpoints for LangChain + Gemini integration
"""

from flask import Flask
from flask_restx import Api
from util.config import Config
from api.routes import api as generation_api

def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    # Configure Flask-RESTX API with Swagger documentation
    api = Api(
        app,
        version='1.0',
        title='Text Generation API',
        description='A REST API for text generation using LangChain and Google Gemini AI',
        doc='/api/docs/',  # Swagger UI will be available at this URL
        prefix='/api'
    )
    
    # Register API namespaces
    api.add_namespace(generation_api)
    
    # Global error handlers
    @api.errorhandler(Exception)
    def handle_exception(error):
        """Handle unexpected exceptions"""
        return {
            'error': 'An unexpected error occurred',
            'message': str(error),
            'status_code': 500
        }, 500
    
    @app.route('/')
    def home():
        """Root endpoint - redirect to API documentation"""
        return {
            'message': 'Welcome to Text Generation API',
            'documentation': '/api/docs',
            'health_check': '/api/health',
            'version': '1.0'
        }
    
    return app

def main():
    """Main function to run the Flask application"""
    try:
        # Create Flask app
        app = create_app()
        
        print("🚀 Starting Flask Text Generation API...")
        print(f"📚 API Documentation: http://{Config.FLASK_HOST}:{Config.FLASK_PORT}/api/docs")
        print(f"❤️  Health Check: http://{Config.FLASK_HOST}:{Config.FLASK_PORT}/api/health")
        print(f"🏠 Home: http://{Config.FLASK_HOST}:{Config.FLASK_PORT}/")
        print("\n🎯 Available Endpoints:")
        print("   POST /api/generate/simple    - Simple text generation")
        print("   POST /api/generate/styled    - Styled text generation")
        print("   POST /api/generate/creative  - Creative content generation")
        print("\n💡 Tip: Visit /api/docs for interactive API testing!")
        print("\n" + "="*60)
        
        # Run Flask app
        app.run(
            host=Config.FLASK_HOST,
            port=Config.FLASK_PORT,
            debug=Config.FLASK_DEBUG
        )
        
    except Exception as e:
        print(f"❌ Failed to start Flask application: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure GEMINI_API_KEY environment variable is set")
        print("2. Check if port 5000 is available")
        print("3. Verify all dependencies are installed: pip install -r requirements.txt")

if __name__ == '__main__':
    main()