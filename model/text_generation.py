"""
Data models for text generation requests and responses
Used for both internal processing and JSON serialization in the API
"""

from datetime import datetime

class TextRequest:
    """Represents a text generation request with user parameters"""
    
    def __init__(self, prompt, max_length=100, temperature=0.7):
        """
        Initialize a text generation request
        
        Args:
            prompt (str): The user's text prompt
            max_length (int): Maximum number of tokens to generate
            temperature (float): Creativity level (0.0 to 1.0)
        """
        self.prompt = prompt
        self.max_length = max_length
        self.temperature = temperature
    
    def __str__(self):
        """Return a formatted string representation of the request"""
        return f"Prompt: {self.prompt}\nMax Length: {self.max_length}\nCreativity: {self.temperature}"
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'prompt': self.prompt,
            'max_length': self.max_length,
            'temperature': self.temperature
        }

class TextResponse:
    """Represents a text generation response from the AI model"""
    
    def __init__(self, content, model_used="gemini-2.0-flash"):
        """
        Initialize a text generation response
        
        Args:
            content (str): The generated text content
            model_used (str): Name of the AI model used
        """
        self.content = content
        self.model_used = model_used
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        """Return a formatted string representation of the response"""
        return f"Generated at: {self.timestamp}\nModel: {self.model_used}\nContent: {self.content}"
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'content': self.content,
            'model_used': self.model_used,
            'timestamp': self.timestamp
        }