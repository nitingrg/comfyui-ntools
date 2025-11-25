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
    FUNCTION = "calculate_megapixels"
    CATEGORY = "utils"

    def calculate_megapixels(self, image):
        # Safety checks
        if image is None or image.dim() != 4:
            return (0.0,)

        # Shape: [batch, height, width, channels]
        _, height, width, _ = image.shape

        # Calculate megapixels (using first image in batch)
        megapixels = (height * width) / 1_000_000.0

        # Always return a float, never a string!
        return (float(megapixels),)


# ────────────────────────────────
# Node registration
# ────────────────────────────────
NODE_CLASS_MAPPINGS = {
    "ImageMegapixels": ImageMegapixels
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageMegapixels": "Calculate Image Megapixels"
}