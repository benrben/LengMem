# LanguageMemory SDK 🧠

**A Python SDK for Layered Memory Architecture with LangGraph**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/LanguageMemory.svg)](https://badge.fury.io/py/LanguageMemory)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Downloads](https://static.pepy.tech/badge/LanguageMemory)](https://pepy.tech/project/LanguageMemory)

LanguageMemory is a Python SDK that provides a sophisticated memory architecture for Large Language Model (LLM) agents, implementing multiple types of memory systems that mimic human cognitive architecture. Built on top of LangGraph, it enables AI agents to have human-like memory capabilities including sensory buffer, short-term memory, episodic memory, semantic memory, and more.

## 🚀 Quick Start

### Installation

```bash
pip install LanguageMemory
```

### Basic Usage

```python
from LanguageMemory import LangMemSDK

# Initialize the SDK
sdk = LangMemSDK()

# Process a message through the brain
result = sdk.process_message("Remember that I love coffee in the morning")

# Search for information
results = sdk.search_memory("coffee", memory_type="semantic")

# Add information to memory
sdk.add_memory("Python is a programming language", memory_type="semantic")
```

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [Memory Types](#memory-types)
- [Examples](#examples)
- [CLI Usage](#cli-usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Multi-Layered Memory Architecture
- **🧠 Sensory Buffer**: Immediate perception and input processing
- **⚡ Short-Term Memory**: Temporary information storage and manipulation
- **📚 Episodic Memory**: Personal experiences and events with context
- **🔍 Semantic Memory**: General knowledge and facts
- **🎯 Procedural Memory**: Skills and learned procedures
- **👤 Personalization Memory**: User-specific preferences and patterns
- **💭 Emotional Memory**: Emotional associations and responses
- **🤝 Social Memory**: Social interactions and relationships
- **📋 Planning Memory**: Goal-oriented planning and future intentions

### SDK Capabilities
- **Simple API**: Easy-to-use Python interface
- **Vector Storage**: Powered by Milvus with OpenAI embeddings
- **TTL Support**: Time-to-live functionality for temporary memories
- **Async Operations**: High-performance asynchronous operations
- **Flexible Search**: Semantic similarity search across memory layers
- **CLI Tools**: Command-line interface for easy interaction

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher
- OpenAI API key

### Install from PyPI

```bash
pip install LanguageMemory
```

### Install from Source

```bash
git clone https://github.com/LanguageMemory/LanguageMemory.git
cd LanguageMemory
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/LanguageMemory/LanguageMemory.git
cd LanguageMemory
pip install -e ".[dev]"
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
EMBEDDING_MODEL=text-embedding-3-large
VECTOR_DB_PATH=./vector_db
```

### Optional Configuration

```env
VECTOR_DB_INDEX_TYPE=FLAT
VECTOR_DB_METRIC_TYPE=L2
ENABLE_DYNAMIC_FIELDS=true
MAX_SEARCH_RESULTS=5
```

## 📖 API Reference

### LangMemSDK

The main SDK class providing high-level access to all memory functionality.

```python
from LanguageMemory import LangMemSDK

sdk = LangMemSDK()
```

#### Methods

##### `process_message(message: str) -> dict`
Process a message through the main brain orchestrator.

```python
result = sdk.process_message("Remember my favorite color is blue")
```

##### `search_memory(query: str, memory_type: str = "semantic", k: int = 5) -> list`
Search a specific memory type for relevant information.

```python
results = sdk.search_memory("favorite color", memory_type="personalization")
```

##### `add_memory(content: str, memory_type: str = "semantic", metadata: dict = None)`
Add content to a specific memory type.

```python
sdk.add_memory("Paris is the capital of France", memory_type="semantic")
```

##### `list_memory_types() -> list`
List all available memory types.

```python
memory_types = sdk.list_memory_types()
# Returns: ['sensory_buffer', 'short_term_memory', 'episodic_memory', ...]
```

##### `get_memory_info(memory_type: str) -> dict`
Get detailed information about a specific memory type.

```python
info = sdk.get_memory_info("semantic_memory")
```

### CreateVectorDB

Create and manage individual vector databases for specific memory types.

```python
from LanguageMemory import CreateVectorDB

# Create a custom memory database
memory = CreateVectorDB(
    name="my_custom_memory",
    description="Custom memory for specific use case",
    ttl_seconds=3600  # 1 hour TTL
)

# Add documents
memory.add_document("Important information", metadata={"priority": "high"})

# Search documents
results = memory.search("important", k=3)
```

### Direct Memory Access

Access pre-configured memory databases directly:

```python
from LanguageMemory import semantic_memory, episodic_memory, short_term_memory

# Add to semantic memory
semantic_memory.add_document("Machine learning is a subset of AI")

# Search episodic memory
results = episodic_memory.search("yesterday meeting")

# Search short-term memory
recent_results = short_term_memory.search("current task")
```

## 🧠 Memory Types

| Memory Type | Description | TTL | Use Cases |
|-------------|-------------|-----|-----------|
| **Sensory Buffer** | Immediate sensory input processing | 5 minutes | Real-time perception, immediate reactions |
| **Short-Term Memory** | Active working memory | 2 hours | Current conversations, temporary data |
| **Episodic Memory** | Personal experiences and events | 1 week | User interactions, contextual experiences |
| **Semantic Memory** | General knowledge and facts | 30 days | Facts, concepts, learned information |
| **Procedural Memory** | Skills and procedures | 90 days | How-to knowledge, step-by-step processes |
| **Personalization** | User preferences and traits | 1 year | User customization, personal preferences |
| **Emotional Memory** | Emotional associations | 30 days | Sentiment, emotional context |
| **Social Memory** | Social interactions | 90 days | Relationships, social context |
| **Planning Memory** | Future intentions and goals | 2 weeks | Task planning, goal management |

## 💡 Examples

### Basic Memory Operations

```python
from LanguageMemory import LangMemSDK

sdk = LangMemSDK()

# Store user preferences
sdk.add_memory("I prefer dark mode in applications", memory_type="personalization")

# Store factual information
sdk.add_memory("The Earth orbits the Sun", memory_type="semantic")

# Store a personal experience
sdk.add_memory("Had a great meeting with the team today", memory_type="episodic")

# Search for information
preferences = sdk.search_memory("interface preferences", memory_type="personalization")
facts = sdk.search_memory("Earth", memory_type="semantic")
experiences = sdk.search_memory("team meeting", memory_type="episodic")
```

### Advanced Usage with Custom Memory

```python
from LanguageMemory import CreateVectorDB
import json

# Create a specialized memory for a specific domain
project_memory = CreateVectorDB(
    name="project_alpha",
    description="Memory for Project Alpha specifications and decisions",
    ttl_seconds=86400 * 30  # 30 days
)

# Add structured information
project_memory.add_document(
    "Project Alpha uses microservices architecture with Python and FastAPI",
    metadata={
        "project": "alpha",
        "category": "architecture",
        "importance": "high",
        "date": "2024-01-15"
    }
)

# Search with context
results = project_memory.search("architecture decisions", k=3)
for result in results:
    print(f"Content: {result.page_content}")
    print(f"Metadata: {result.metadata}")
```

### Integration with LangGraph

```python
from LanguageMemory import brain_graph
from langchain_core.messages import HumanMessage

# Use the brain graph directly
response = brain_graph.invoke({
    "messages": [HumanMessage(content="What do you know about machine learning?")]
})

print(response)
```

### Async Operations

```python
import asyncio
from LanguageMemory import LangMemSDK

async def process_multiple_messages():
    sdk = LangMemSDK()
    
    messages = [
        "I enjoy hiking on weekends",
        "Python is my favorite programming language",
        "The meeting is scheduled for tomorrow at 3 PM"
    ]
    
    for message in messages:
        result = sdk.process_message(message)
        print(f"Processed: {message}")
        print(f"Result: {result}")

# Run async function
asyncio.run(process_multiple_messages())
```

## 🖥️ CLI Usage

LanguageMemory provides a command-line interface for easy interaction:

### Basic Commands

```bash
# Show version
LanguageMemory --version

# Process a message
LanguageMemory process "Remember that I like coffee"

# Search memory
LanguageMemory search "coffee" --memory personalization --limit 3

# Add to memory
LanguageMemory add "Python is a programming language" --memory semantic

# List all memory types
LanguageMemory list-memories

# Get memory type information
LanguageMemory info semantic_memory
```

### Advanced CLI Usage

```bash
# Add with metadata
LanguageMemory add "Important project update" --memory episodic --metadata '{"priority": "high", "date": "2024-01-15"}'

# Search specific memory type
LanguageMemory search "project" --memory episodic --limit 5

# Get detailed memory information
LanguageMemory info procedural_memory
```

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | Required | OpenAI API key for embeddings and LLM |
| `EMBEDDING_MODEL` | `text-embedding-3-large` | OpenAI embedding model |
| `VECTOR_DB_PATH` | `./vector_db` | Path to store vector databases |
| `VECTOR_DB_INDEX_TYPE` | `FLAT` | Milvus index type |
| `VECTOR_DB_METRIC_TYPE` | `L2` | Distance metric for similarity search |
| `ENABLE_DYNAMIC_FIELDS` | `true` | Enable dynamic fields in vector DB |
| `MAX_SEARCH_RESULTS` | `5` | Default number of search results |

### Custom Configuration

```python
from LanguageMemory import CreateVectorDB
import os

# Override environment variables
os.environ['EMBEDDING_MODEL'] = 'text-embedding-ada-002'
os.environ['MAX_SEARCH_RESULTS'] = '10'

# Create memory with custom settings
memory = CreateVectorDB(
    name="custom_memory",
    description="Custom configured memory",
    ttl_seconds=7200  # 2 hours
)
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/LanguageMemory/LanguageMemory.git
cd LanguageMemory
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Quality

```bash
black LanguageMemory/
ruff check LanguageMemory/
mypy LanguageMemory/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangGraph](https://langchain-ai.github.io/langgraph/) for the orchestration framework
- [LangChain](https://langchain.com/) for LLM integration
- [Milvus](https://milvus.io/) for vector database capabilities
- [OpenAI](https://openai.com/) for embedding and LLM services

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/LanguageMemory/LanguageMemory/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/LanguageMemory/LanguageMemory/discussions)
- 📚 **Documentation**: [ReadTheDocs](https://languagememory.readthedocs.io)
- 📧 **Email**: support@languagememory.ai

---

**LanguageMemory SDK** - Bringing human-like memory architecture to your AI agents 🧠✨
