class apz_canvas_settings:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        alignment_options = ["left top", "left center", "left bottom",
                             "center top", "center center", "center bottom",
                             "right top", "right center", "right bottom"]
        return {
            "required": {
                "canvas_height": ("INT", {"default": 512, "step": 1, "display": "number"}),
                "canvas_width": ("INT", {"default": 512, "step": 1, "display": "number"}),
                "background_color": ("STRING", {"default": "black", "display": "text"}),
                "text_alignment": (alignment_options, {"default": "center center", "display": "dropdown"}),
                "padding": ("INT", {"default": 0, "min": 0, "step": 1, "display": "number"}),
                "line_spacing": ("INT", {"default": 5, "step": 1, "display": "number"}),
                "bounding_box_width": ("INT", {"default": 300, "min": 0, "step": 1, "display": "number"}),
                "bounding_box_height": ("INT", {"default": 150, "min": 0, "step": 1, "display": "number"}),
            },
            "optional": {
                "images": ("IMAGE", {"default": None}),
            },
        }

    CATEGORY = "💠 Mana Nodes/⚙️ Generator Settings"
    RETURN_TYPES = ("CANVAS_SETTINGS",)
    RETURN_NAMES = ("canvas",)
    FUNCTION = "run"

    def run(self, **kwargs):

        settings = {
            'canvas_height': kwargs.get('canvas_height'),
            'canvas_width': kwargs.get('canvas_width'),
            'background_color': kwargs.get('background_color'),
            'text_alignment': kwargs.get('text_alignment'),
            'padding': kwargs.get('padding'),
            'line_spacing': kwargs.get('line_spacing'),
            'bounding_box_width': kwargs.get('bounding_box_width'),
            'bounding_box_height': kwargs.get('bounding_box_height'),
            'images': kwargs.get('images'),
        }

        return (settings,)
