"""Flask API routes for text generation endpoints"""

from flask import request
from flask_restx import Namespace, Resource
from datetime import datetime
import traceback

from services.gemini_service import GeminiService
from util.config import Config
from exception.generation_exceptions import APIKeyException, GenerationException, InvalidInputException
from api.swagger_config import configure_swagger_models

# Create API namespace
api = Namespace('api', description='Text Generation API using LangChain and Gemini')

# Configure Swagger models
models = configure_swagger_models(api)

# Initialize Gemini service (will be done once when app starts)
try:
    gemini_service = GeminiService(Config.get_api_key())
except APIKeyException as e:
    print(f"Warning: {e}")
    gemini_service = None

@api.route('/health')
class HealthCheck(Resource):
    """Health check endpoint"""
    
    @api.doc('health_check')
    @api.marshal_with(models['health_response'])
    def get(self):
        """Check API health status"""
        return {
            'status': 'healthy',
            'message': 'Flask API is running successfully!',
            'timestamp': datetime.now().isoformat()
        }

@api.route('/generate/simple')
class SimpleGeneration(Resource):
    """Simple text generation endpoint"""
    
    @api.doc('generate_simple_text')
    @api.expect(models['simple_request'])
    @api.marshal_with(models['text_response'])
    @api.response(400, 'Invalid input', models['error_response'])
    @api.response(500, 'Generation failed', models['error_response'])
    def post(self):
        """Generate simple text from a prompt"""
        try:
            # Check if service is available
            if gemini_service is None:
                return {
                    'error': 'Gemini service not available. Please check API key configuration.',
                    'status_code': 500
                }, 500
            
            # Get JSON data from request
            data = request.get_json()
            if not data:
                return {
                    'error': 'No JSON data provided',
                    'status_code': 400
                }, 400
            
            prompt = data.get('prompt')
            if not prompt:
                return {
                    'error': 'Missing required field: prompt',
                    'status_code': 400
                }, 400
            
            # Generate text using Gemini service
            response = gemini_service.generate_simple_text(prompt)
            
            return response.to_dict()
            
        except InvalidInputException as e:
            return {
                'error': str(e),
                'status_code': 400
            }, 400
        except GenerationException as e:
            return {
                'error': str(e),
                'status_code': 500
            }, 500
        except Exception as e:
            print(f"Unexpected error in simple generation: {e}")
            print(traceback.format_exc())
            return {
                'error': 'An unexpected error occurred',
                'status_code': 500
            }, 500

@api.route('/generate/styled')
class StyledGeneration(Resource):
    """Styled text generation endpoint"""
    
    @api.doc('generate_styled_text')
    @api.expect(models['styled_request'])
    @api.marshal_with(models['text_response'])
    @api.response(400, 'Invalid input', models['error_response'])
    @api.response(500, 'Generation failed', models['error_response'])
    def post(self):
        """Generate styled text with specific tone"""
        try:
            # Check if service is available
            if gemini_service is None:
                return {
                    'error': 'Gemini service not available. Please check API key configuration.',
                    'status_code': 500
                }, 500
            
            # Get JSON data from request
            data = request.get_json()
            if not data:
                return {
                    'error': 'No JSON data provided',
                    'status_code': 400
                }, 400
            
            topic = data.get('topic')
            style = data.get('style')
            
            if not topic:
                return {
                    'error': 'Missing required field: topic',
                    'status_code': 400
                }, 400
            
            if not style:
                return {
                    'error': 'Missing required field: style',
                    'status_code': 400
                }, 400
            
            # Generate styled text using Gemini service
            response = gemini_service.generate_with_template(topic, style)
            
            return response.to_dict()
            
        except InvalidInputException as e:
            return {
                'error': str(e),
                'status_code': 400
            }, 400
        except GenerationException as e:
            return {
                'error': str(e),
                'status_code': 500
            }, 500
        except Exception as e:
            print(f"Unexpected error in styled generation: {e}")
            print(traceback.format_exc())
            return {
                'error': 'An unexpected error occurred',
                'status_code': 500
            }, 500

@api.route('/generate/creative')
class CreativeGeneration(Resource):
    """Creative content generation endpoint"""
    
    @api.doc('generate_creative_content')
    @api.expect(models['creative_request'])
    @api.marshal_with(models['text_response'])
    @api.response(400, 'Invalid input', models['error_response'])
    @api.response(500, 'Generation failed', models['error_response'])
    def post(self):
        """Generate creative content like poems, stories, jokes, or facts"""
        try:
            # Check if service is available
            if gemini_service is None:
                return {
                    'error': 'Gemini service not available. Please check API key configuration.',
                    'status_code': 500
                }, 500
            
            # Get JSON data from request
            data = request.get_json()
            if not data:
                return {
                    'error': 'No JSON data provided',
                    'status_code': 400
                }, 400
            
            content_type = data.get('content_type')
            subject = data.get('subject')
            
            if not content_type:
                return {
                    'error': 'Missing required field: content_type',
                    'status_code': 400
                }, 400
            
            if not subject:
                return {
                    'error': 'Missing required field: subject',
                    'status_code': 400
                }, 400
            
            # Generate creative content using Gemini service
            response = gemini_service.generate_creative_content(content_type, subject)
            
            return response.to_dict()
            
        except InvalidInputException as e:
            return {
                'error': str(e),
                'status_code': 400
            }, 400
        except GenerationException as e:
            return {
                'error': str(e),
                'status_code': 500
            }, 500
        except Exception as e:
            print(f"Unexpected error in creative generation: {e}")
            print(traceback.format_exc())
            return {
                'error': 'An unexpected error occurred',
                'status_code': 500
            }, 500