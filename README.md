# ContextManager

A versatile Python utility for managing application context through in-memory and persistent object storage.

## Overview

ContextManager provides a streamlined way to save, load, and manage objects across your application's lifecycle. It offers both in-memory caching and file-based persistence, supporting multiple serialization formats, making it ideal for:

- Application state management
- Configuration persistence
- Object caching
- Data sharing between components
- Session management

## Features

- **Dual Storage System**: Store objects both in memory and on disk
- **Multiple Serialization Formats**: Support for both Pickle (binary) and JSON (text-based) serialization
- **Context Management**: Use as a context manager with Python's `with` statement
- **Simple API**: Intuitive methods for saving, loading, and deleting objects
- **Context Listing**: Ability to list all available contexts
- **Bulk Operations**: Clear all objects with a single call

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/context-manager.git

# Navigate to the project directory
cd context-manager

# Install the package
pip install -e .
```

## Quick Start

```python
from context import ContextManager

# Create a context manager instance
context = ContextManager()

# Save objects with different formats
user_data = {"name": "Alice", "age": 30}
context.save(user_data, "user_profile", file_format="json")

complex_data = {"model": SomeModel(), "history": [1, 2, 3]}
context.save(complex_data, "app_state", file_format="pickle")

# Load objects
user = ContextManager.load("user_profile", file_format="json")
state = ContextManager.load("app_state", file_format="pickle")

# List all available contexts
contexts = ContextManager.list_contexts()
print(f"Available contexts: {contexts}")

# Delete a specific context
context.delete("user_profile")

# Clear all contexts
ContextManager.clear()
```

## Usage as Context Manager

```python
with ContextManager() as context:
    # Operations within a context
    context.save({"settings": "value"}, "app_settings", file_format="json")
    settings = ContextManager.load("app_settings", file_format="json")
```

## API Reference

### `ContextManager()`

Creates a new instance of the ContextManager class.

### `save(obj, context_name, file_format="pickle")`

Saves an object to the specified context.

- **obj**: The Python object to save
- **context_name**: A string identifier for the context
- **file_format**: Either "pickle" or "json" (default: "pickle")

### `load(context_name, file_format="pickle")` (class method)

Loads an object from the specified context.

- **context_name**: The string identifier for the context
- **file_format**: Either "pickle" or "json" (default: "pickle")
- **Returns**: The loaded object

### `delete(context_name)`

Removes an object from memory and deletes associated files.

- **context_name**: The string identifier for the context to delete

### `list_contexts()` (class method)

Returns a list of all available context names currently in memory.

### `clear()` (class method)

Removes all objects from memory and deletes all saved files.

## Storage Details

Objects are stored in:
- Memory: Using an internal class dictionary `_objects`
- Disk: In the `object_saver_files` directory relative to the script location

## Serialization Formats

### Pickle
- Supports all Python objects (including custom classes)
- Binary format (not human-readable)
- Not portable across Python versions or implementations
- Use for complex objects that can't be serialized to JSON

### JSON
- Human-readable text format
- Limited to JSON-serializable types (dicts, lists, strings, numbers, booleans, None)
- Portable across languages and systems
- Use for configuration, settings, and data that needs to be readable

## Best Practices

1. **Security Considerations**:
   - Pickle files can execute arbitrary code when loaded. Only load pickle files from trusted sources.
   - Consider implementing encryption for sensitive data.

2. **Performance Optimization**:
   - For frequently accessed objects, use in-memory access after the first load.
   - For large objects, consider implementing lazy loading or compression.

3. **Error Handling**:
   - Implement try/except blocks when loading potentially corrupted files.
   - Consider adding validation for loaded objects.

4. **File Management**:
   - For production use, consider customizing the file storage location.
   - Implement periodic cleanup of unused context files.

## Implementation Details

The ContextManager uses a class variable `_objects` to store all objects in memory across instances, allowing class methods to access the same objects as instance methods. File operations are implemented using Python's standard libraries:

- `pickle` for binary serialization
- `json` for text-based serialization
- `os` for file operations

## Extending ContextManager

Potential extensions include:

1. Adding support for additional serialization formats (YAML, TOML, etc.)
2. Implementing data compression
3. Adding encryption for sensitive data
4. Supporting network storage backends
5. Adding TTL (time-to-live) for cached objects
6. Implementing concurrency controls for multi-threaded access

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
