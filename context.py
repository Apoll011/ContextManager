import json
import os
import pickle
import sys
import types

class ContextManager:
    _objects = {}
    _file_dir = "object_saver_files"

    def __enter__(self, context_name):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def save(self, obj, context_name, file_format="pickle"):
        """Save an object to the objects dictionary and optionally to a file.

        Args:
            obj (object): The object to save.
            context_name (str): The name of the context to save the object under.
            file_format (str, optional): The file format to use when saving the object to a file.
                Supported formats are "pickle" and "json". Defaults to "pickle".
        """
        self._objects[context_name] = obj
        if file_format == "pickle":
            self._save_to_file(obj, context_name, "pickle")
        elif file_format == "json":
            self._save_to_file(obj, context_name, "json")
        else:
            raise ValueError(f"Invalid file format: {file_format}")

    @classmethod
    def load(cls, context_name, file_format="pickle"):
        """Load an object from the objects dictionary and optionally from a file.

        Args:
            context_name (str): The name of the context to load the object from.
            file_format (str, optional): The file format to use when loading the object from a file.
                Supported formats are "pickle" and "json". Defaults to "pickle".

        Returns:
            object: The loaded object.
        """
        obj = cls._objects.get(context_name)
        if obj is None:
            if file_format == "pickle":
                obj = cls._load_from_file(context_name, "pickle")
            elif file_format == "json":
                obj = cls._load_from_file(context_name, "json")
            else:
                raise ValueError(f"Invalid file format: {file_format}")
        return obj

    def delete(self, context_name):
        """Delete an object from the objects dictionary and optionally from a file.

        Args:
            context_name (str): The name of the context to delete the object from.
        """
        if context_name in self._objects:
            del self._objects[context_name]
        if os.path.exists(self._get_file_path(context_name, "pickle")):
            os.remove(self._get_file_path(context_name, "pickle"))
        if os.path.exists(self._get_file_path(context_name, "json")):
            os.remove(self._get_file_path(context_name, "json"))

    @staticmethod
    def _save_to_file(obj, context_name, file_format):
        """Save an object to a file.

        Args:
            obj (object): The object to save.
            context_name (str): The name of the context to use as the file name.
            file_format (str): The file format to use. Supported formats are "pickle" and "json".
        """
        if file_format == "pickle":
            with open(ObjectSaver._get_file_path(context_name, "pickle"), "wb") as f:
                pickle.dump(obj, f)
        elif file_format == "json":
            with open(ObjectSaver._get_file_path(context_name, "json"), "w") as f:
                json.dump(obj, f)

    @staticmethod
    def _load_from_file(context_name, file_format):
        """Load an object from a file.

        Args:
            context_name (str): The name of the context to use as the file name.
            file_format (str): The file format to use. Supported formats are "pickle" and "json".

        Returns:
            object: Theloaded object.
        """
        if file_format == "pickle":
            with open(ObjectSaver._get_file_path(context_name, "pickle"), "rb") as f:
                return pickle.load(f)
        elif file_format == "json":
            with open(ObjectSaver._get_file_path(context_name, "json"), "r") as f:
                return json.load(f)

    @staticmethod
    def _get_file_path(context_name, file_format):
        """Get the file path for a given context name and file format.

        Args:
            context_name (str): The name of the context.
            file_format (str): The file format. Supported formats are "pickle" and "json".

        Returns:
            str: The file path.
        """
        file_name = f"{context_name}.{file_format}"
        return os.path.join(ObjectSaver._file_dir, file_name)

    @classmethod
    def list_contexts(cls):
        """Get a list of all context names.

        Returns:
            list: A list of context names.
        """
        return list(cls._objects.keys())

    @classmethod
    def clear(cls):
        """Clear all objects from the objects dictionary and delete all files.

        Returns:
            None
        """
        cls._objects.clear()
        for file in os.listdir(cls._file_dir):
            os.remove(os.path.join(cls._file_dir, file))
