from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from uuid import uuid4
import os
import dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dotenv.load_dotenv()

# Configuration from environment variables
embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")
db_folder = os.getenv("VECTOR_DB_PATH", "./vector_db")

embeddings = OpenAIEmbeddings(model=embedding_model)
from langchain_milvus import Milvus

class CreateVectorDB:
    def __init__(self, name: str, description: str, ttl_seconds: int = None, when_to_retrieve: str = "search", when_to_store: str = "add"):
        self.name = name
        self.description = description
        self.when_to_retrieve = when_to_retrieve
        self.when_to_store = when_to_store
        self.ttl_seconds = ttl_seconds  # Store for future use, but don't use in Milvus config
        self.db_path = f"{db_folder}/{name}.db"
        
        logger.info(f"Initializing vector database: {name}")
        
        # Check if database exists
        if os.path.exists(self.db_path):
            logger.info(f"Loading existing database: {self.db_path}")
        else:
            logger.info(f"Creating new database: {self.db_path}")
            # Ensure the directory exists
            os.makedirs(db_folder, exist_ok=True)
        
        # Get configuration from environment variables
        index_type = os.getenv("VECTOR_DB_INDEX_TYPE", "FLAT")
        metric_type = os.getenv("VECTOR_DB_METRIC_TYPE", "L2")
        enable_dynamic = os.getenv("ENABLE_DYNAMIC_FIELDS", "true").lower() == "true"
        
        try:
            # Simplified Milvus configuration without TTL for compatibility
            self.vector_store = Milvus(
                embedding_function=embeddings,
                connection_args={"uri": self.db_path},
                index_params={"index_type": index_type, "metric_type": metric_type},
                enable_dynamic_field=enable_dynamic,  # Enable dynamic fields to allow pk and other fields
            )
            logger.info(f"Successfully initialized {name} vector store")
        except Exception as e:
            logger.error(f"Failed to initialize vector store for {name}: {e}")
            raise

    def add_document(self, document_context: str, metadata: dict = None):
        if metadata is None:
            metadata = {}
        
        logger.info(f"Adding document to {self.name}: {document_context[:100]}...")
        
        # Add TTL-related metadata for manual TTL handling if needed
        if self.ttl_seconds:
            import time
            metadata["created_timestamp"] = time.time()
            metadata["ttl_seconds"] = self.ttl_seconds
            
        try:
            document_id = str(uuid4())
            self.vector_store.add_documents(
                documents=[Document(page_content=document_context, metadata=metadata)],
                ids=[document_id]
            )
            logger.info(f"Successfully added document to {self.name} with ID: {document_id}")
        except Exception as e:
            logger.error(f"Failed to add document to {self.name}: {e}")
            raise

    def search(self, query: str, k: int = None):
        if k is None:
            k = int(os.getenv("MAX_SEARCH_RESULTS", "5"))
            
        logger.info(f"Searching {self.name} for: {query[:100]}...")
        
        try:
            results = self.vector_store.similarity_search(query, k)
            logger.info(f"Found {len(results)} results in {self.name}")
            
            # Optional: Filter out expired documents based on TTL (manual implementation)
            if self.ttl_seconds:
                import time
                current_time = time.time()
                filtered_results = []
                
                for result in results:
                    created_time = result.metadata.get("created_timestamp")
                    ttl = result.metadata.get("ttl_seconds")
                    
                    if created_time and ttl:
                        if (current_time - created_time) <= ttl:
                            filtered_results.append(result)
                        else:
                            logger.info(f"Filtering out expired document from {self.name}")
                    else:
                        # If no TTL metadata, include the result
                        filtered_results.append(result)
                
                logger.info(f"After TTL filtering: {len(filtered_results)} results in {self.name}")
                return filtered_results
            
            return results
            
        except Exception as e:
            logger.error(f"Failed to search in {self.name}: {e}")
            return []  # Return empty list instead of raising to prevent cascading failures
