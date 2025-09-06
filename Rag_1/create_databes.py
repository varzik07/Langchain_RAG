from langchain_community.document_loaders import DirectoryLoader
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os, openai
from dotenv import load_dotenv
import shutil
from glob import glob
# Load environment variables from .env file
load_dotenv()
# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
CHROME_PATH = "chroma"
DATA_PATH = "book"

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    chunks= split_text(documents)
    save_to_chroma(chunks)    
    


def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob = "*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 100,
        length_function = len,
        add_start_index = True
    )

    chunks = text_splitter.split_documents(documents)
    documents = chunks[10]
    print(documents.page_content)
    print(documents.metadata)
    return chunks

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROME_PATH):
        shutil.rmtree(CHROME_PATH)

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory = CHROME_PATH    
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROME_PATH}")

if __name__ == "__main__":
    main()

    