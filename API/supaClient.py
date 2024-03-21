from dotenv import load_dotenv
from supabase import create_client, Client
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve Supabase URL and key from environment variables
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(url, key)
