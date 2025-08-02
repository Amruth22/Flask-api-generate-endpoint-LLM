"""Configuration management for the Flask API application"""

import os
from exception.generation_exceptions import APIKeyException

class Config:
    """Configuration class for managing API keys and default settings"""
    
    # Default settings
    DEFAULT_MAX_LENGTH = 100
    DEFAULT_TEMPERATURE = 0.7
    DEFAULT_MODEL = "gemini-2.0-flash"
    
    # Flask settings
    FLASK_DEBUG = True
    FLASK_HOST = '127.0.0.1'
    FLASK_PORT = 5000
    
    @staticmethod
    def get_api_key():
        """
        Get API key from environment variable or .env file
        
        Returns:
            str: The Gemini API key
            
        Raises:
            APIKeyException: If API key is not found
        """
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            # Try to load from .env file if exists
            try:
                from dotenv import load_dotenv
                load_dotenv()
                api_key = os.getenv('GEMINI_API_KEY')
            except ImportError:
                pass
        
        if not api_key:
            raise APIKeyException("Please set GEMINI_API_KEY environment variable")
        
        return api_key
    
    @staticmethod
    def validate_api_key(api_key):
        """
        Check if API key looks valid
        
        Args:
            api_key (str): The API key to validate
            
        Returns:
            bool: True if API key appears valid, False otherwise
        """
        if not api_key or len(api_key) < 20:
            return False
        return True