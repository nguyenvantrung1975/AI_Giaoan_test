# config.py
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Cấu hình API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cấu hình tham số mô hình
MODEL_NAME = "gpt-4"
TEMPERATURE = 0.7
MAX_TOKENS = 500