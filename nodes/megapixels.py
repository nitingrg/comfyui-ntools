# comfyui-ntools/nodes/megapixels.py
import torch

class ImageMegapixels:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("megapixels",)
    FUNCTION = "calculate"
    CATEGORY = "ntools/utils"

    def calculate(self, image):
        if image is None or image.dim() != 4:
            return (0.0,)

        # [batch, height, width, channels]
        _, height, width, _ = image.shape

        megapixels = (height * width) / 1_000_000.0
        return (float(megapixels),)


NODE_CLASS_MAPPINGS = {
    "ImageMegapixels": ImageMegapixels
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageMegapixels": "Calculate Image Megapixels"
}