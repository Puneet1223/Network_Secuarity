from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN_ID = os.getenv("HF_TOKEN")
HF_REPO_ID = os.getenv("HF_REPO_ID")

class HFSync:

    def __init__(self):
        self.api = HfApi(token=HF_TOKEN_ID)

    def sync_folder_to_hf(self, folder, repo_path):
        self.api.upload_folder(
            folder_path=folder,
            repo_id=HF_REPO_ID,
            repo_type="model",
            path_in_repo=repo_path
        )