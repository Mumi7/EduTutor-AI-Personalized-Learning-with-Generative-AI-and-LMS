from dotenv import load_dotenv
import os

load_dotenv()

watsonx_api_key = os.getenv("WATSONX_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

print("Environment variables loaded successfully!")
