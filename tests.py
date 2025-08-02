"""
Test suite for the Flask Text Generation API
Tests all endpoints, error handling, and functionality
"""

import pytest
import json
import os
from unittest.mock import patch, MagicMock
from app import create_app
from model.text_generation import TextResponse

@pytest.fixture
def client():
    """Create test client for Flask app"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_gemini_service():
    """Mock Gemini service for testing"""
    mock_service = MagicMock()
    mock_response = TextResponse("Test generated content")
    mock_service.generate_simple_text.return_value = mock_response
    mock_service.generate_with_template.return_value = mock_response
    mock_service.generate_creative_content.return_value = mock_response
    return mock_service

class TestAPIStructure:
    """Test API structure and basic functionality"""
    
    def test_home_endpoint(self, client):
        """Test home endpoint returns welcome message"""
        response = client.get('/')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'message' in data
        assert 'documentation' in data
        assert data['documentation'] == '/api/docs'
    
    def test_health_endpoint(self, client):
        """Test health check endpoint"""
        response = client.get('/api/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'message' in data
        assert 'timestamp' in data

class TestSimpleGeneration:
    """Test simple text generation endpoint"""
    
    @patch('api.routes.gemini_service')
    def test_simple_generation_success(self, mock_service, client):
        """Test successful simple text generation"""
        # Mock the service response
        mock_response = TextResponse("This is a test response")
        mock_service.generate_simple_text.return_value = mock_response
        
        # Test request
        response = client.post('/api/generate/simple',
                             json={'prompt': 'Test prompt'},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'content' in data
        assert 'model_used' in data
        assert 'timestamp' in data
        assert data['content'] == "This is a test response"
    
    def test_simple_generation_missing_prompt(self, client):
        """Test simple generation with missing prompt"""
        response = client.post('/api/generate/simple',
                             json={},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert 'Missing required field: prompt' in data['error']
    
    def test_simple_generation_no_json(self, client):
        """Test simple generation with no JSON data"""
        response = client.post('/api/generate/simple')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
        assert 'No JSON data provided' in data['error']

class TestStyledGeneration:
    """Test styled text generation endpoint"""
    
    @patch('api.routes.gemini_service')
    def test_styled_generation_success(self, mock_service, client):
        """Test successful styled text generation"""
        # Mock the service response
        mock_response = TextResponse("This is a funny response about cats")
        mock_service.generate_with_template.return_value = mock_response
        
        # Test request
        response = client.post('/api/generate/styled',
                             json={'topic': 'cats', 'style': 'funny'},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'content' in data
        assert data['content'] == "This is a funny response about cats"
    
    def test_styled_generation_missing_topic(self, client):
        """Test styled generation with missing topic"""
        response = client.post('/api/generate/styled',
                             json={'style': 'funny'},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'Missing required field: topic' in data['error']
    
    def test_styled_generation_missing_style(self, client):
        """Test styled generation with missing style"""
        response = client.post('/api/generate/styled',
                             json={'topic': 'cats'},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'Missing required field: style' in data['error']

class TestCreativeGeneration:
    """Test creative content generation endpoint"""
    
    @patch('api.routes.gemini_service')
    def test_creative_generation_success(self, mock_service, client):
        """Test successful creative content generation"""
        # Mock the service response
        mock_response = TextResponse("Roses are red, violets are blue...")
        mock_service.generate_creative_content.return_value = mock_response
        
        # Test request
        response = client.post('/api/generate/creative',
                             json={'content_type': 'poem', 'subject': 'flowers'},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'content' in data
        assert "Roses are red" in data['content']
    
    def test_creative_generation_missing_content_type(self, client):
        """Test creative generation with missing content_type"""
        response = client.post('/api/generate/creative',
                             json={'subject': 'flowers'},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'Missing required field: content_type' in data['error']
    
    def test_creative_generation_missing_subject(self, client):
        """Test creative generation with missing subject"""
        response = client.post('/api/generate/creative',
                             json={'content_type': 'poem'},
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'Missing required field: subject' in data['error']

class TestErrorHandling:
    """Test error handling scenarios"""
    
    def test_invalid_json_format(self, client):
        """Test handling of invalid JSON"""
        response = client.post('/api/generate/simple',
                             data='invalid json',
                             content_type='application/json')
        
        assert response.status_code == 400
    
    def test_empty_request_body(self, client):
        """Test handling of empty request body"""
        response = client.post('/api/generate/simple',
                             json=None,
                             content_type='application/json')
        
        assert response.status_code == 400

class TestModelClasses:
    """Test model classes functionality"""
    
    def test_text_response_to_dict(self):
        """Test TextResponse to_dict method"""
        response = TextResponse("Test content", "test-model")
        result = response.to_dict()
        
        assert isinstance(result, dict)
        assert result['content'] == "Test content"
        assert result['model_used'] == "test-model"
        assert 'timestamp' in result

class TestFileStructure:
    """Test that all required files exist"""
    
    def test_required_files_exist(self):
        """Test that all required project files exist"""
        required_files = [
            'app.py',
            'requirements.txt',
            'README.md',
            'tests.py',
            'model/__init__.py',
            'model/text_generation.py',
            'services/__init__.py',
            'services/gemini_service.py',
            'util/__init__.py',
            'util/config.py',
            'exception/__init__.py',
            'exception/generation_exceptions.py',
            'api/__init__.py',
            'api/routes.py',
            'api/swagger_config.py'
        ]
        
        for file_path in required_files:
            assert os.path.isfile(file_path), f"Required file '{file_path}' is missing!"
    
    def test_required_directories_exist(self):
        """Test that all required directories exist"""
        required_dirs = ['model', 'services', 'util', 'exception', 'api']
        
        for dir_path in required_dirs:
            assert os.path.isdir(dir_path), f"Required directory '{dir_path}' is missing!"

if __name__ == '__main__':
    # Run tests if script is executed directly
    pytest.main([__file__, '-v'])