ContextManager
=============

A Python context manager for saving and loading objects to/from memory and files.

**Features**

* In-memory storage
* File persistence (Pickle and JSON formats)
* Context names for identifying objects
* List contexts method
* Clear method for deleting all objects and files

**Usage**

To use the `ContextManager`, simply import it and create a new instance. You can then use the `save` and `load` methods to save and load objects to/from memory and files.

Here is an example of using the `ContextManager` to save and load an object to/from memory:
```python
from context import ContextManager

# Create a new context manager
cm = ContextManager()

# Save an object to the context manager
cm.save('my_object', {'key': 'value'})

# Load the object from the context manager
loaded_object = cm.load('my_object')

# Print the loaded object
print(loaded_object)  # {'key': 'value'}
```
You can also use the `ContextManager` to save and load objects to/from files. To do this, you can use the `save_to_file` and `load_from_file` methods.

Here is an example of using the `ContextManager` to save and load an object to/from a Pickle file:
```python
from context import ContextManager

# Create a new context manager
cm = ContextManager()

# Save an object to a Pickle file
cm.save_to_file('my_object.pickle', {'key': 'value'})

# Load the object from the Pickle file
loaded_object = cm.load_from_file('my_object.pickle')

# Print the loaded object
print(loaded_object)  # {'key': 'value'}
```
You can also use the `ContextManager` to list all contexts and clear all objects and files. To do this, you can use the `list_contexts` and `clear` methods.

Here is an example of using the `ContextManager` to list all contexts and clear all objects and files:
```python
from context import ContextManager

# Create a new context manager
cm = ContextManager()

# Save some objects to the context manager
cm.save('my_object1', {'key1': 'value1'})
cm.save('my_object2', {'key2': 'value2'})

# List all contexts
print(cm.list_contexts())  # ['my_object1', 'my_object2']

# Clear all objects and files
cm.clear()

# List all contexts (should be empty)
print(cm.list_contexts())  # []
```
**Installation**

Copy the `context.py` file into your project directory.

**License**

MIT License. See `LICENSE` file for details.

**Author**

Tiago Bernardo
