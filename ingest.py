from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from chromadb.config import Settings
from constants import CHROMA_SETTINGS, client
import os 


persist_directory = "db"

def main():
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                loader = PyPDFLoader(os.path.join(root, file))
    documents = loader.load()
    print("splitting into chunks")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    #create embeddings here
    print("Loading sentence transformers model")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    #create vector store here
    print(f"Creating embeddings. May take some minutes...")
    db = client
    print(f"Ingestion complete! You can now run privateGPT.py to query your documents")

if __name__ == "__main__":
    main()