# Contributing to LangMem SDK

Thank you for your interest in contributing to LangMem SDK! This guide will help you get started with contributing to our project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Code Style](#code-style)
- [Documentation](#documentation)

## 🤝 Code of Conduct

This project adheres to a code of conduct that promotes a welcoming and inclusive environment for all contributors. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/langmem.git
   cd langmem
   ```

3. **Add the original repository as upstream**:
   ```bash
   git remote add upstream https://github.com/langmem/langmem.git
   ```

## 🛠️ Development Setup

1. **Install Python 3.11+** (required)

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key and other settings
   ```

5. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

## 🔧 Making Changes

### Branch Naming Convention

Use descriptive branch names with prefixes:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation improvements
- `refactor/` - Code refactoring
- `test/` - Test improvements

Example: `feature/add-temporal-memory-support`

### Development Process

1. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Test your changes**:
   ```bash
   pytest
   ```

4. **Lint your code**:
   ```bash
   black langmem/
   ruff check langmem/
   mypy langmem/
   ```

5. **Commit your changes**:
   ```bash
   git commit -m "feat: add temporal memory support"
   ```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_memory.py

# Run with coverage
pytest --cov=langmem --cov-report=html
```

### Writing Tests

- Place test files in the `tests/` directory
- Follow the naming convention: `test_*.py`
- Use descriptive test names
- Include docstrings for complex tests
- Test both success and failure cases

Example:
```python
def test_add_memory_to_semantic_database():
    """Test adding a document to semantic memory."""
    sdk = LangMemSDK()
    sdk.add_memory("Test content", memory_type="semantic")
    results = sdk.search_memory("Test", memory_type="semantic")
    assert len(results) > 0
```

## 📝 Submitting Changes

1. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub:
   - Use a clear, descriptive title
   - Include a detailed description of changes
   - Reference any related issues
   - Add appropriate labels

3. **Pull Request Template**:
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Unit tests pass
   - [ ] Integration tests pass
   - [ ] Manual testing completed

   ## Checklist
   - [ ] Code follows project style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] Tests added/updated
   ```

## 🎨 Code Style

We follow Python best practices and use automated tools for consistency:

### Code Formatting
- **Black**: Code formatting (line length: 88)
- **Ruff**: Linting and import sorting
- **MyPy**: Type checking

### Style Guidelines
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Follow PEP 8 naming conventions
- Keep functions focused and small
- Use meaningful variable names

### Example:
```python
def search_memory(
    self, 
    query: str, 
    memory_type: str = "semantic", 
    k: int = 5
) -> list[Document]:
    """
    Search a specific memory type for relevant information.
    
    Args:
        query: The search query
        memory_type: Type of memory to search (default: "semantic")
        k: Number of results to return (default: 5)
        
    Returns:
        List of search results from the specified memory type
        
    Raises:
        ValueError: If memory_type is not recognized
    """
    if memory_type not in self.memory_dbs:
        raise ValueError(f"Unknown memory type: {memory_type}")
    
    return self.memory_dbs[memory_type].search(query, k)
```

## 📚 Documentation

### Docstring Format
Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of the function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param1 is invalid
    """
```

### Documentation Updates
- Update README.md for new features
- Add examples for new functionality
- Update API documentation
- Include type hints in all code

## 🐛 Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)
- Relevant logs or error messages

## 💡 Feature Requests

For new features:
- Check existing issues first
- Provide clear use case description
- Include implementation suggestions if possible
- Consider backward compatibility

## 🏷️ Commit Message Format

Follow conventional commits:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks

Examples:
```
feat: add episodic memory TTL support
fix: resolve memory search timeout issue
docs: update API reference for new memory types
```

## 🚀 Release Process

1. Version bumping follows semantic versioning
2. Releases are created from the main branch
3. Release notes are automatically generated
4. PyPI packages are automatically published

## 📞 Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and community discussions
- **Email**: dev@langmem.ai for private inquiries

## 🙏 Recognition

Contributors are recognized in:
- README.md contributors section
- Release notes
- GitHub contributor graphs

Thank you for contributing to LangMem SDK! 🧠✨ 