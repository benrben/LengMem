from langgraph_wave_orchestrator import WaveOrchestrator
import logging

from LanggraphMemory.llm import create_llm_openai
from LanggraphMemory.workers import memory_search_workers, memory_push_workers
from LanggraphMemory.prompts import (
    SEARCH_PLANNING_PROMPT, SEARCH_ANSWERING_PROMPT,
    LEARN_PLANNING_PROMPT, LEARN_ANSWERING_PROMPT,
    SUPERVISOR_PLANNING_PROMPT, SUPERVISOR_ANSWERING_PROMPT
)

logger = logging.getLogger(__name__)



def create_search_in_memory_brain():
    """Create and configure the search in memory brain orchestrator."""
    brain = WaveOrchestrator(
        llm=create_llm_openai(),
        planning_prompt_override=SEARCH_PLANNING_PROMPT,
        answering_prompt_override=SEARCH_ANSWERING_PROMPT
    )
    
    # Add all search workers
    for worker_name, worker in memory_search_workers.items():
        brain.add_node(worker)
        logger.info(f"Added {worker_name} worker to search brain")
    
    return brain


def create_learn_brain():
    """Create and configure the get from memory brain orchestrator."""
    brain = WaveOrchestrator(
        llm=create_llm_openai(),
        planning_prompt_override=LEARN_PLANNING_PROMPT,
        answering_prompt_override=LEARN_ANSWERING_PROMPT
    )
    
    # Add all push workers
    for worker_name, worker in memory_push_workers.items():
        brain.add_node(worker)
        logger.info(f"Added {worker_name} worker to get brain")
    
    return brain


def create_main_brain():
    """Create and configure the main brain orchestrator."""
    brain = WaveOrchestrator(
        llm=create_llm_openai(),
        planning_prompt_override=SUPERVISOR_PLANNING_PROMPT,
        answering_prompt_override=SUPERVISOR_ANSWERING_PROMPT
    )
    return brain 