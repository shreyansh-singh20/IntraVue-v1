import os

# Base directory of backend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Prompts directory
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

# LLM configuration (v1 uses mock)
MODEL_NAME = "llama-3.1-8b-instant"
TEMPERATURE = 0.3

# Environment (future use)
ENV = os.getenv("ENV", "development")
