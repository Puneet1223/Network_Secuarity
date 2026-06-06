from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN_ID = os.getenv("HF_TOKEN")
HF_REPO_ID = os.getenv("HF_REPO_ID")
print("Token:", HF_TOKEN_ID[:10] if HF_TOKEN_ID else "None")

api = HfApi(token=HF_TOKEN_ID)
print(api.whoami())