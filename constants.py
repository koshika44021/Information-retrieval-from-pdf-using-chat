import chromadb

CHROMA_SETTINGS = chromadb.Settings(
    anonymized_telemetry=False
)

client = chromadb.PersistentClient(
    path="db",
    settings=CHROMA_SETTINGS
)
