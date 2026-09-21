import os
import time
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# What step this codefile covers:
# 1) Loading Encoded Texts
# 2) Embed Them into Vectors
# 3) Store those Vectors into Database

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path=env_path)

cohere_api_key = os.getenv("COHERE_API_KEY")

if not cohere_api_key:
    raise ValueError("CRITICAL ERROR: COHERE_API_KEY not found. Please add it to your .env file.")

# use absolute path tracking instead of looking at text directory
processed_dir = os.path.join(base_dir, "data", "processed_texts")

def build_vector_db():
    if not os.path.exists(processed_dir):
        raise FileNotFoundError(f"CRITICAL ERROR: The directory {processed_dir} does not exist.")
    
    texts = [] 
    metadatas = []

    for file in os.listdir(processed_dir):
        if file.endswith(".txt"):
            file_path = os.path.join(processed_dir, file)
            with open(file_path, "r", encoding="utf-8") as f: 
                texts.append(f.read())
                metadatas.append({"source": file})

    if not texts:
        print("WARNING: No text files found to embed.")
        return

    # convert texts to vector embeddings
    embeddings = CohereEmbeddings(cohere_api_key=cohere_api_key, model="embed-multilingual-v3.0")

    # do FAISS (Facebook AI Similarity Search)
    '''What FAISS does:
    1) plots vectors into a large, multi-dim mathematical storage map
    2) performs the "nearest neighbor" similarity search between chunks'''

    batch_size = 40
    database = None
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        batch_metadatas = metadatas[i:i + batch_size]
        if database is None:
            database = FAISS.from_texts(texts=batch_texts, embedding=embeddings, metadatas=batch_metadatas)
        else:
            database.add_texts(texts=batch_texts, metadatas=batch_metadatas)
        print(f"Embedded {min(i + batch_size, len(texts))}/{len(texts)} chunks")
        time.sleep(10)

    output_db_path = os.path.join(base_dir, "vector_db")
    # Save locally so future runs can load it quickly 
    database.save_local(output_db_path) 

if __name__ == "__main__":
    build_vector_db()