from langgraph_wave_orchestrator import WaveOrchestrator, WorkerNode
from langchain_core.messages import BaseMessage

from LanggraphMemory.states import SearchInMemory, GetFromMemory
from LanggraphMemory.orchestrators import (
    create_search_in_memory_brain, 
    create_learn_brain, 
    create_main_brain
)

# Create brain instances
search_in_memory_brain = create_search_in_memory_brain()
learn = create_learn_brain()
brain = create_main_brain()

# Compile the brain graphs
search_in_memory_brain_graph = search_in_memory_brain.compile()
learn_information_graph = learn.compile()


def search_in_memory(state):
    """Search in memory using the configured brain."""
    result = search_in_memory_brain_graph.invoke({"messages": state.messages})
    print(f"Search result: {result}")
    return {"search": result}


def learn_and_store_in_memory(state):
    """Get from memory using the configured brain."""
    print(f"Get state: {state}")
    result = learn_information_graph.invoke({"messages": state.messages})
    print(f"Get result: {result}")
    return {"get": result}


# Create high-level workers for the main brain
search_worker = WorkerNode(
    name="search_in_memory",
    function=search_in_memory,
    model=SearchInMemory,
    state_placeholder="search",
    description="Search in memory",
)

get_worker = WorkerNode(
    name="learn_and_store_in_memory",
    function=learn_and_store_in_memory,
    model=GetFromMemory,
    state_placeholder="get",
    description="Learn and store in memory",
)

# Add workers to main brain and compile
brain.add_node(search_worker)
brain.add_node(get_worker)
graph = brain.compile()
