"""Swagger/OpenAPI configuration for API documentation"""

from flask_restx import fields

def configure_swagger_models(api):
    """Configure Swagger models for request/response documentation"""
    
    # Request models
    simple_request_model = api.model('SimpleRequest', {
        'prompt': fields.String(required=True, description='Text prompt for generation', 
                               example='What is artificial intelligence?')
    })
    
    styled_request_model = api.model('StyledRequest', {
        'topic': fields.String(required=True, description='Topic to write about', 
                              example='Python programming'),
        'style': fields.String(required=True, description='Writing style', 
                              enum=['formal', 'casual', 'funny'], example='funny')
    })
    
    creative_request_model = api.model('CreativeRequest', {
        'content_type': fields.String(required=True, description='Type of creative content',
                                    enum=['poem', 'story', 'joke', 'fact'], example='poem'),
        'subject': fields.String(required=True, description='Subject for creative content',
                               example='ocean')
    })
    
    # Response models
    text_response_model = api.model('TextResponse', {
        'content': fields.String(description='Generated text content',
                                example='Artificial Intelligence is...'),
        'model_used': fields.String(description='AI model used for generation',
                                   example='gemini-2.0-flash'),
        'timestamp': fields.String(description='Generation timestamp',
                                  example='2024-01-01 12:00:00')
    })
    
    health_response_model = api.model('HealthResponse', {
        'status': fields.String(description='API health status', example='healthy'),
        'message': fields.String(description='Status message', 
                                example='Flask API is running successfully!'),
        'timestamp': fields.String(description='Check timestamp',
                                  example='2024-01-01T12:00:00Z')
    })
    
    error_response_model = api.model('ErrorResponse', {
        'error': fields.String(description='Error message',
                              example='Invalid input. Please provide a valid prompt.'),
        'status_code': fields.Integer(description='HTTP status code', example=400)
    })
    
    return {
        'simple_request': simple_request_model,
        'styled_request': styled_request_model,
        'creative_request': creative_request_model,
        'text_response': text_response_model,
        'health_response': health_response_model,
        'error_response': error_response_model
    }