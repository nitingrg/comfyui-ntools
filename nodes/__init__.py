# comfyui-ntools/nodes/__init__.py
from .megapixels import NODE_CLASS_MAPPINGS as _megapixels_mappings
from .megapixels import NODE_DISPLAY_NAME_MAPPINGS as _megapixels_names

NODE_CLASS_MAPPINGS = {**_megapixels_mappings}
NODE_DISPLAY_NAME_MAPPINGS = {**_megapixels_names}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']