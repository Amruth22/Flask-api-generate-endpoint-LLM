"""Service class for integrating with Google's Gemini AI using LangChain"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from model.text_generation import TextResponse
from exception.generation_exceptions import GenerationException, InvalidInputException

class GeminiService:
    """Service class for interacting with Gemini AI through LangChain"""
    
    def __init__(self, api_key):
        """
        Initialize the Gemini service with API key
        
        Args:
            api_key (str): Google Gemini API key
        """
        try:
            # Initialize Gemini with LangChain
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash",
                google_api_key=api_key,
                temperature=0.7,
                max_output_tokens=200
            )
        except Exception as e:
            raise GenerationException(f"Failed to initialize Gemini: {str(e)}")
    
    def generate_simple_text(self, prompt):
        """
        Generate text from a simple prompt
        
        Args:
            prompt (str): User's text prompt
            
        Returns:
            TextResponse: Generated text response
        """
        if not prompt or len(prompt.strip()) == 0:
            raise InvalidInputException("Prompt cannot be empty")
        
        try:
            # Call Gemini using LangChain
            response = self.llm.invoke(prompt)
            return TextResponse(response.content)
        except Exception as e:
            raise GenerationException(f"Error generating text: {str(e)}")
    
    def generate_with_template(self, topic, style):
        """
        Generate text using a template with topic and style
        
        Args:
            topic (str): The topic to write about
            style (str): Writing style (formal, casual, funny)
            
        Returns:
            TextResponse: Generated text response
        """
        if not topic or len(topic.strip()) == 0:
            raise InvalidInputException("Topic cannot be empty")
        
        if style not in ['formal', 'casual', 'funny']:
            raise InvalidInputException("Style must be 'formal', 'casual', or 'funny'")
        
        # Create a prompt template
        template = """Write a {style} paragraph about {topic}. 
        Make it engaging and appropriate for the style requested."""
        
        prompt = PromptTemplate(
            input_variables=["style", "topic"],
            template=template
        )
        
        # Format the prompt
        formatted_prompt = prompt.format(style=style, topic=topic)
        
        try:
            response = self.llm.invoke(formatted_prompt)
            return TextResponse(response.content)
        except Exception as e:
            raise GenerationException(f"Error generating styled text: {str(e)}")
    
    def generate_creative_content(self, content_type, subject):
        """
        Generate different types of creative content
        
        Args:
            content_type (str): Type of content (poem, story, joke, fact)
            subject (str): Subject matter for the content
            
        Returns:
            TextResponse: Generated creative content
        """
        if not subject or len(subject.strip()) == 0:
            raise InvalidInputException("Subject cannot be empty")
        
        templates = {
            "poem": "Write a short poem about {subject}. Make it creative and emotional.",
            "story": "Write a very short story about {subject}. Include a beginning, middle, and end.",
            "joke": "Write a funny joke about {subject}. Make it family-friendly.",
            "fact": "Write an interesting fun fact about {subject}. Make it educational."
        }
        
        if content_type not in templates:
            raise InvalidInputException(f"Invalid content type. Choose from: {', '.join(templates.keys())}")
        
        prompt = templates[content_type].format(subject=subject)
        
        try:
            response = self.llm.invoke(prompt)
            return TextResponse(response.content)
        except Exception as e:
            raise GenerationException(f"Error generating creative content: {str(e)}")