"""
LanguageMemory - A Python SDK for Layered Memory Architecture with LangGraph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LanguageMemory provides a comprehensive memory architecture for LLM agents that mimics
human cognitive memory systems. Built on top of LangGraph, it offers sophisticated
memory management capabilities including sensory buffer, short-term memory,
episodic memory, semantic memory, and more.

Basic Usage:
    >>> from LanguageMemory import LangMemSDK, CreateVectorDB
    >>> 
    >>> # Initialize the SDK
    >>> sdk = LangMemSDK()
    >>> 
    >>> # Create a custom memory database
    >>> memory = CreateVectorDB(
    ...     name="my_memory",
    ...     description="Custom memory for my agent"
    ... )
    >>> 
    >>> # Add and search memories
    >>> memory.add_document("Important information")
    >>> results = memory.search("information")

:copyright: (c) 2024 LanguageMemory Contributors
:license: MIT, see LICENSE for more details.
"""

__version__ = "1.0.2"

# Core SDK components
from .vectorDB import CreateVectorDB
from .llm import create_llm_openai, create_llm_openai_base
from .brain import graph as brain_graph
from .orchestrators import (
    create_main_brain,
    create_search_in_memory_brain,
    create_learn_brain,
)

# Memory states
from .states import (
    SensoryBufferState,
    ShortTermMemoryState,
    EpisodicMemoryState,
    SemanticMemoryState,
    ProceduralMemoryState,
    PersonalizationMemoryState,
    EmotionalMemoryState,
    SocialMemoryState,
    PlanningMemoryState,
    SearchInMemory,
    GetFromMemory,
)

# Memory database instances
from .dbs import (
    sensory_buffer,
    short_term_memory,
    episodic_memory,
    semantic_memory,
    procedural_memory,
    personalization_memory,
    emotional_memory,
    social_memory,
    planning_memory,
    get_memory_db,
    MEMORY_CONFIGS,
)

# Worker components
from .workers import (
    create_memory_search_worker,
    create_memory_push_worker,
    memory_search_workers,
    memory_push_workers,
)


class LangMemSDK:
    """
    Main SDK class providing a high-level interface to LanguageMemory functionality.
    
    This class provides convenient access to all memory systems and orchestration
    capabilities of LanguageMemory.
    
    Example:
        >>> sdk = LangMemSDK()
        >>> 
        >>> # Process a message through the brain
        >>> result = sdk.process_message("Remember that I like coffee")
        >>> 
        >>> # Access individual memory systems
        >>> semantic_results = sdk.search_memory("coffee", memory_type="semantic")
    """
    
    def __init__(self):
        """Initialize the LanguageMemory SDK with default configuration."""
        self.brain = brain_graph
        self.memory_dbs = {
            "sensory_buffer": sensory_buffer,
            "short_term_memory": short_term_memory,
            "episodic_memory": episodic_memory,
            "semantic_memory": semantic_memory,
            "procedural_memory": procedural_memory,
            "personalization_memory": personalization_memory,
            "emotional_memory": emotional_memory,
            "social_memory": social_memory,
            "planning_memory": planning_memory,
        }
    
    def process_message(self, message: str) -> dict:
        """
        Process a message through the main brain orchestrator.
        
        Args:
            message: The message to process
            
        Returns:
            dict: The result from the brain processing
        """
        return self.brain.invoke({
            "messages": [{"role": "user", "content": message}]
        })
    
    def search_memory(self, query: str, memory_type: str = "semantic", k: int = 5) -> list:
        """
        Search a specific memory type for relevant information.
        
        Args:
            query: The search query
            memory_type: Type of memory to search (default: "semantic")
            k: Number of results to return (default: 5)
            
        Returns:
            list: Search results from the specified memory type
        """
        if memory_type not in self.memory_dbs:
            raise ValueError(f"Unknown memory type: {memory_type}")
        
        return self.memory_dbs[memory_type].search(query, k)
    
    def add_memory(self, content: str, memory_type: str = "semantic", metadata: dict = None):
        """
        Add content to a specific memory type.
        
        Args:
            content: The content to store
            memory_type: Type of memory to store in (default: "semantic")
            metadata: Optional metadata to associate with the content
        """
        if memory_type not in self.memory_dbs:
            raise ValueError(f"Unknown memory type: {memory_type}")
        
        self.memory_dbs[memory_type].add_document(content, metadata)
    
    def list_memory_types(self) -> list:
        """
        List all available memory types.
        
        Returns:
            list: List of available memory type names
        """
        return list(self.memory_dbs.keys())
    
    def get_memory_info(self, memory_type: str) -> dict:
        """
        Get information about a specific memory type.
        
        Args:
            memory_type: The memory type to get information about
            
        Returns:
            dict: Information about the memory type
        """
        if memory_type not in MEMORY_CONFIGS:
            raise ValueError(f"Unknown memory type: {memory_type}")
        
        return MEMORY_CONFIGS[memory_type]


# Public API
__all__ = [
    # SDK main class
    "LangMemSDK",
    
    # Core components
    "CreateVectorDB",
    "create_llm_openai",
    "create_llm_openai_base",
    "brain_graph",
    
    # Orchestrators
    "create_main_brain",
    "create_search_in_memory_brain",
    "create_learn_brain",
    
    # Memory states
    "SensoryBufferState",
    "ShortTermMemoryState",
    "EpisodicMemoryState",
    "SemanticMemoryState",
    "ProceduralMemoryState",
    "PersonalizationMemoryState",
    "EmotionalMemoryState",
    "SocialMemoryState",
    "PlanningMemoryState",
    "SearchInMemory",
    "GetFromMemory",
    
    # Memory database instances
    "sensory_buffer",
    "short_term_memory",
    "episodic_memory",
    "semantic_memory",
    "procedural_memory",
    "personalization_memory",
    "emotional_memory",
    "social_memory",
    "planning_memory",
    "get_memory_db",
    "MEMORY_CONFIGS",
    
    # Worker components
    "create_memory_search_worker",
    "create_memory_push_worker",
    "memory_search_workers",
    "memory_push_workers",
    
    # Version
    "__version__",
] 