"""
LangMem CLI - Command Line Interface for LangMem SDK

This module provides a command-line interface for interacting with the LangMem SDK.
"""

import argparse
import sys
import os
from typing import Optional

from LanguageMemory import LangMemSDK, __version__


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="langmem",
        description="LangMem SDK - Layered Memory Architecture for LLM Agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  langmem version                          # Show version
  langmem process "Hello world"           # Process a message
  langmem search "coffee" --memory semantic # Search memory
  langmem add "I like coffee" --memory personalization # Add to memory
  langmem list-memories                   # List all memory types
        """
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Version command
    version_parser = subparsers.add_parser("version", help="Show version information")
    
    # Process command
    process_parser = subparsers.add_parser("process", help="Process a message through the brain")
    process_parser.add_argument("message", help="The message to process")
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search memory for information")
    search_parser.add_argument("query", help="The search query")
    search_parser.add_argument("--memory", default="semantic", help="Memory type to search (default: semantic)")
    search_parser.add_argument("--limit", type=int, default=5, help="Number of results to return (default: 5)")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add content to memory")
    add_parser.add_argument("content", help="The content to add")
    add_parser.add_argument("--memory", default="semantic", help="Memory type to add to (default: semantic)")
    add_parser.add_argument("--metadata", help="JSON metadata to associate with the content")
    
    # List memories command
    list_parser = subparsers.add_parser("list-memories", help="List all available memory types")
    
    # Info command
    info_parser = subparsers.add_parser("info", help="Get information about a memory type")
    info_parser.add_argument("memory_type", help="The memory type to get info about")
    
    return parser


def handle_version_command():
    """Handle the version command."""
    print(f"LangMem SDK version {__version__}")
    print("Built with LangGraph and LangChain")


def handle_process_command(args, sdk: LangMemSDK):
    """Handle the process command."""
    try:
        result = sdk.process_message(args.message)
        print("Processing result:")
        print(result)
    except Exception as e:
        print(f"Error processing message: {e}", file=sys.stderr)
        sys.exit(1)


def handle_search_command(args, sdk: LangMemSDK):
    """Handle the search command."""
    try:
        results = sdk.search_memory(args.query, args.memory, args.limit)
        print(f"Search results from {args.memory} memory:")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result.page_content}")
            if hasattr(result, 'metadata') and result.metadata:
                print(f"   Metadata: {result.metadata}")
    except Exception as e:
        print(f"Error searching memory: {e}", file=sys.stderr)
        sys.exit(1)


def handle_add_command(args, sdk: LangMemSDK):
    """Handle the add command."""
    try:
        metadata = None
        if args.metadata:
            import json
            metadata = json.loads(args.metadata)
        
        sdk.add_memory(args.content, args.memory, metadata)
        print(f"Successfully added content to {args.memory} memory")
    except Exception as e:
        print(f"Error adding to memory: {e}", file=sys.stderr)
        sys.exit(1)


def handle_list_memories_command(args, sdk: LangMemSDK):
    """Handle the list-memories command."""
    try:
        memory_types = sdk.list_memory_types()
        print("Available memory types:")
        for memory_type in memory_types:
            print(f"  - {memory_type}")
    except Exception as e:
        print(f"Error listing memories: {e}", file=sys.stderr)
        sys.exit(1)


def handle_info_command(args, sdk: LangMemSDK):
    """Handle the info command."""
    try:
        info = sdk.get_memory_info(args.memory_type)
        print(f"Memory type: {args.memory_type}")
        print(f"Description: {info['description']}")
        print(f"TTL: {info.get('ttl_seconds', 'None')} seconds")
        print(f"When to retrieve: {info.get('when_to_retrieve', 'N/A')}")
        print(f"When to store: {info.get('when_to_store', 'N/A')}")
    except Exception as e:
        print(f"Error getting memory info: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Handle version command separately (doesn't need SDK)
    if args.command == "version":
        handle_version_command()
        return
    
    # If no command specified, show help
    if not args.command:
        parser.print_help()
        return
    
    # Initialize SDK for other commands
    try:
        sdk = LangMemSDK()
    except Exception as e:
        print(f"Error initializing LangMem SDK: {e}", file=sys.stderr)
        print("Make sure your environment is properly configured with required API keys.")
        sys.exit(1)
    
    # Handle commands
    if args.command == "process":
        handle_process_command(args, sdk)
    elif args.command == "search":
        handle_search_command(args, sdk)
    elif args.command == "add":
        handle_add_command(args, sdk)
    elif args.command == "list-memories":
        handle_list_memories_command(args, sdk)
    elif args.command == "info":
        handle_info_command(args, sdk)
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main() 