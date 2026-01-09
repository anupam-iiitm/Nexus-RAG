import os

# Get the absolute path of the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Directory Configuration ---
MARKDOWN_DIR = os.path.join(BASE_DIR, "markdown_docs")
PARENT_STORE_PATH = os.path.join(BASE_DIR, "parent_store")
QDRANT_DB_PATH = os.path.join(BASE_DIR, "qdrant_db")

# Create directories if they do not exist
for dir_path in [MARKDOWN_DIR, PARENT_STORE_PATH, QDRANT_DB_PATH]:
    os.makedirs(dir_path, exist_ok=True)

# --- Qdrant Configuration ---
CHILD_COLLECTION = "document_child_chunks"
SPARSE_VECTOR_NAME = "sparse"

# --- Model Configuration ---
DENSE_MODEL = "sentence-transformers/all-mpnet-base-v2"
SPARSE_MODEL = "Qdrant/bm25"
LLM_MODEL = "qwen3:4b-instruct-2507-q4_K_M"
LLM_TEMPERATURE = 0

# --- Text Splitter Configuration ---
CHILD_CHUNK_SIZE = 500
CHILD_CHUNK_OVERLAP = 100
MIN_PARENT_SIZE = 2000
MAX_PARENT_SIZE = 10000
HEADERS_TO_SPLIT_ON = [
    ("#", "H1"),
    ("##", "H2"),
    ("###", "H3")
]

# --- OCR Configuration ---
# Attempt to locate Tesseract language data (tessdata) on Windows
# This fixes "Tesseract language data not found" errors
if "TESSDATA_PREFIX" not in os.environ:
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tessdata",
        r"C:\Program Files (x86)\Tesseract-OCR\tessdata",
        os.path.join(os.getenv('LOCALAPPDATA', ''), r'Tesseract-OCR\tessdata')
    ]
    for path in possible_paths:
        if os.path.exists(path):
            os.environ["TESSDATA_PREFIX"] = path
            break
