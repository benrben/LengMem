from langgraph_wave_orchestrator import WorkerNode
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from typing import Type
import logging

from LanggraphMemory.vectorDB import CreateVectorDB
from LanggraphMemory.dbs import (
    sensory_buffer, short_term_memory, episodic_memory, semantic_memory,
    procedural_memory, personalization_memory, emotional_memory, 
    social_memory, planning_memory
)
from LanggraphMemory.states import (
    SensoryBufferState, ShortTermMemoryState, EpisodicMemoryState, 
    SemanticMemoryState, ProceduralMemoryState, PersonalizationMemoryState,
    EmotionalMemoryState, SocialMemoryState, PlanningMemoryState
)

logger = logging.getLogger(__name__)


def create_memory_search_worker(memory_db: CreateVectorDB, state_class: Type[BaseModel], state_key: str = None) -> WorkerNode:
    """
    Smart factory function to create memory search workers automatically.
    
    Args:
        memory_db: The memory database instance
        state_class: The Pydantic state class to use
        state_key: Optional custom state key (defaults to memory name abbreviation)
    
    Returns:
        WorkerNode: Configured worker node for searching the memory system
    """
    # Generate state key if not provided
    if state_key is None:
        # Create abbreviation from memory name (e.g., "short_term_memory" -> "stm")
        words = memory_db.name.split('_')
        state_key = ''.join(word[0] for word in words)
    
    # Create worker function
    def memory_search_worker(state):
        print(f"state: {state}")
        print(f"state: {state}")

        # # Handle both dictionary and object state formats
        # if isinstance(state, dict):
        #     messages = state.get("messages", [])
        # else:
        #     messages = getattr(state, 'messages', [])
        
        # if not messages:
        #     return {state_key: {"messages": []}}
        
        # try:
        #     result = memory_db.search(messages[-1].content)
        #     return {state_key: {"messages": [*messages, HumanMessage(content=str(result))]}}
        # except Exception as e:
        #     logger.error(f"Error in {memory_db.name} search worker: {e}")
        #     return {state_key: {"messages": [*messages, HumanMessage(content=f"Memory search error: {str(e)}")]}}
    
    service_description = f"Description: {memory_db.description}\nWhen to retrieve: {memory_db.when_to_retrieve}\n"
    # Create WorkerNode
    worker = WorkerNode(
        name=f"{memory_db.name}_search",
        function=memory_search_worker,
        model=state_class,
        state_placeholder=state_key,
        description=service_description,
    )
    
    return worker


def create_memory_push_worker(memory_db: CreateVectorDB, state_class: Type[BaseModel], state_key: str = None) -> WorkerNode:
    """
    Smart factory function to create memory push workers automatically.
    
    Args:
        memory_db: The memory database instance
        state_class: The Pydantic state class to use
        state_key: Optional custom state key (defaults to memory name abbreviation + "_push")
    
    Returns:
        WorkerNode: Configured worker node for storing data in the memory system
    """
    # Generate state key if not provided
    if state_key is None:
        # Create abbreviation from memory name (e.g., "short_term_memory" -> "stm_push")
        words = memory_db.name.split('_')
        state_key = ''.join(word[0] for word in words) + "_push"
    
    # Create worker function
    def memory_push_worker(state):
        print(f"Push state: {state}")
        
        # Handle both dictionary and object state formats
        if isinstance(state, dict):
            messages = state.get("messages", [])
        else:
            messages = getattr(state, 'messages', [])
        
        if not messages:
            return {state_key: {"messages": []}}
        
        try:
            # Store the last message content in the memory database
            content = messages[-1].content
            metadata = {
                "memory_type": memory_db.name,
                "source": "memory_push_worker"
            }
            memory_db.add_document(content, metadata)
            success_msg = f"Successfully stored data in {memory_db.name}"
            return {state_key: {"messages": [*messages, HumanMessage(content=success_msg)]}}
        except Exception as e:
            logger.error(f"Error in {memory_db.name} push worker: {e}")
            return {state_key: {"messages": [*messages, HumanMessage(content=f"Memory store error: {str(e)}")]}}
    
    service_description = f"Description: {memory_db.description}\nWhen to store: {memory_db.when_to_store}\n"
    # Create WorkerNode
    worker = WorkerNode(
        name=f"{memory_db.name}_push",
        function=memory_push_worker,
        model=state_class,
        state_placeholder=state_key,
        description=service_description,
    )
    
    return worker


# Create all memory search workers
memory_search_workers = {
    'sensory_buffer_search': create_memory_search_worker(sensory_buffer, SensoryBufferState, 'sb'),
    'short_term_memory_search': create_memory_search_worker(short_term_memory, ShortTermMemoryState, 'stm'),
    'episodic_memory_search': create_memory_search_worker(episodic_memory, EpisodicMemoryState, 'em'),
    'semantic_memory_search': create_memory_search_worker(semantic_memory, SemanticMemoryState, 'sm'),
    'procedural_memory_search': create_memory_search_worker(procedural_memory, ProceduralMemoryState, 'pm'),
    'personalization_memory_search': create_memory_search_worker(personalization_memory, PersonalizationMemoryState, 'pers'),
    'emotional_memory_search': create_memory_search_worker(emotional_memory, EmotionalMemoryState, 'emo'),
    'social_memory_search': create_memory_search_worker(social_memory, SocialMemoryState, 'soc'),
    'planning_memory_search': create_memory_search_worker(planning_memory, PlanningMemoryState, 'plan'),
}

# Create all memory push workers
memory_push_workers = {
    'sensory_buffer_push_worker_1': create_memory_push_worker(sensory_buffer, SensoryBufferState, 'sb_push'),
    'short_term_memory_push_worker_1': create_memory_push_worker(short_term_memory, ShortTermMemoryState, 'stm_push'),
    'episodic_memory_push_worker_1': create_memory_push_worker(episodic_memory, EpisodicMemoryState, 'em_push'),
    'semantic_memory_push_worker_1': create_memory_push_worker(semantic_memory, SemanticMemoryState, 'sm_push'),
    'procedural_memory_push_worker_1': create_memory_push_worker(procedural_memory, ProceduralMemoryState, 'pm_push'),
    'personalization_memory_push_worker_1': create_memory_push_worker(personalization_memory, PersonalizationMemoryState, 'pers_push'),
    'emotional_memory_push_worker_1': create_memory_push_worker(emotional_memory, EmotionalMemoryState, 'emo_push'),
    'social_memory_push_worker_1': create_memory_push_worker(social_memory, SocialMemoryState, 'soc_push'),
    'planning_memory_push_worker_1': create_memory_push_worker(planning_memory, PlanningMemoryState, 'plan_push'),
}

# Update the WorkerNode names to match the dictionary keys
for key, worker in memory_push_workers.items():
    worker.name = key 