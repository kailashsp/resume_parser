import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
DEFAULT_GENERATION_CONFIG = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json"}

class LLM:
    def __init__(self, model_name) -> None:
        self.model_name = model_name
        self.model_client = self._create_model(model_name)

    def _create_model(self, model_name: str, **kwargs):
        """Create and return the specified model."""
        try:
            if model_name.startswith("gemini"):
                return genai.Client(api_key=GOOGLE_API_KEY)
            else:
                raise ValueError(f"Unsupported model: {model_name}")
        except Exception as e:
            raise RuntimeError(f"Failed to create model {model_name}: {str(e)}")

    async def __call__(self, prompt, response_schema):
        DEFAULT_GENERATION_CONFIG['response_schema'] = response_schema
        try:
            if self.model_name.startswith("gemini"):
                response = self.model_client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[prompt],
                    config=types.GenerateContentConfig(
                        **DEFAULT_GENERATION_CONFIG
                    ),
                )
                
                return response.text
        except Exception as e:
            raise RuntimeError(f"Error generating response: {str(e)}")
