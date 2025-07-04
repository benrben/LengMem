#!/usr/bin/env python3
"""
Basic usage example for LangMem SDK

This example demonstrates the core functionality of the LangMem SDK
including memory storage, retrieval, and processing.
"""

import os
from langmem import LangMemSDK

def main():
    """Main example function."""
    print("🧠 LangMem SDK Basic Usage Example")
    print("=" * 40)
    
    # Initialize the SDK
    print("\n1. Initializing LangMem SDK...")
    sdk = LangMemSDK()
    
    # Check available memory types
    print("\n2. Available Memory Types:")
    memory_types = sdk.list_memory_types()
    for memory_type in memory_types:
        print(f"   - {memory_type}")
    
    # Add some information to different memory types
    print("\n3. Adding Information to Memory...")
    
    # Add to semantic memory (facts and knowledge)
    sdk.add_memory("Python is a high-level programming language", memory_type="semantic_memory")
    sdk.add_memory("Machine learning is a subset of artificial intelligence", memory_type="semantic_memory")
    
    # Add to personalization memory (user preferences)
    sdk.add_memory("I prefer dark mode interfaces", memory_type="personalization_memory")
    sdk.add_memory("I enjoy working with Python and AI", memory_type="personalization_memory")
    
    # Add to episodic memory (experiences)
    sdk.add_memory("Today I learned about the LangMem SDK", memory_type="episodic_memory")
    
    print("   ✅ Information added to semantic, personalization, and episodic memory")
    
    # Search for information
    print("\n4. Searching Memory...")
    
    # Search semantic memory
    print("\n   Searching semantic memory for 'Python':")
    results = sdk.search_memory("Python", memory_type="semantic_memory", k=3)
    for i, result in enumerate(results, 1):
        print(f"   {i}. {result.page_content}")
    
    # Search personalization memory
    print("\n   Searching personalization memory for 'preferences':")
    results = sdk.search_memory("preferences", memory_type="personalization_memory", k=2)
    for i, result in enumerate(results, 1):
        print(f"   {i}. {result.page_content}")
    
    # Search episodic memory
    print("\n   Searching episodic memory for 'today':")
    results = sdk.search_memory("today", memory_type="episodic_memory", k=2)
    for i, result in enumerate(results, 1):
        print(f"   {i}. {result.page_content}")
    
    # Process a message through the brain
    print("\n5. Processing Message Through Brain...")
    try:
        result = sdk.process_message("What do you know about Python programming?")
        print(f"   Brain response: {result}")
    except Exception as e:
        print(f"   ⚠️  Brain processing error: {e}")
        print("   This is expected if OpenAI API key is not configured")
    
    # Get memory information
    print("\n6. Memory Type Information:")
    info = sdk.get_memory_info("semantic_memory")
    print(f"   Semantic Memory TTL: {info.get('ttl_seconds', 'None')} seconds")
    print(f"   Description: {info['description'][:100]}...")
    
    print("\n✨ Example completed successfully!")
    print("\nNext steps:")
    print("   - Set up your OpenAI API key in .env file")
    print("   - Explore different memory types")
    print("   - Try the CLI: langmem --help")

if __name__ == "__main__":
    main() 