"""Custom exceptions for text generation operations in the API"""

class APIKeyException(Exception):
    """Raised when API key is missing or invalid"""
    
    def __init__(self, message="API key is missing or invalid. Please check your Gemini API key."):
        super().__init__(message)
        self.status_code = 500

class GenerationException(Exception):
    """Raised when text generation fails"""
    
    def __init__(self, message="Failed to generate text. Please try again."):
        super().__init__(message)
        self.status_code = 500

class InvalidInputException(Exception):
    """Raised when user input is invalid"""
    
    def __init__(self, message="Invalid input. Please provide a valid prompt."):
        super().__init__(message)
        self.status_code = 400