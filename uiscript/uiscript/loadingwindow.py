import uiScriptLocale

AETHERFALL_LOADING_PATH = "d:/ymir work/ui/aetherfall/loading/"

window = {
    "name": "LoadingWindow",
    "style": ("movable", "ltr"),
    "x": 0,
    "y": 0,
    "width": SCREEN_WIDTH,
    "height": SCREEN_HEIGHT,
    "children": (
        {
            "name": "BackGround",
            "type": "expanded_image",
            "x": 0,
            "y": 0,
            "image": AETHERFALL_LOADING_PATH + "loading0.sub",
            "x_scale": float(SCREEN_WIDTH) / 1024.0,
            "y_scale": float(SCREEN_HEIGHT) / 768.0,
        },
        {"name": "ErrorMessage", "type": "text", "x": 24, "y": 22, "text": uiScriptLocale.LOAD_ERROR},
        {
            "name": "GageBoard",
            "type": "window",
            "x": int((SCREEN_WIDTH - 420) / 2),
            "y": SCREEN_HEIGHT - 118,
            "width": 420,
            "height": 66,
            "children": (
                {"name": "AetherfallLoadingAccent", "type": "bar", "x": 6, "y": 24, "width": 408, "height": 16, "color": 0x44150c08},
                {"name": "BackGage", "type": "expanded_image", "x": 10, "y": 20, "image": AETHERFALL_LOADING_PATH + "gauge_empty.sub"},
                {"name": "FullGage", "type": "expanded_image", "x": 10, "y": 20, "image": AETHERFALL_LOADING_PATH + "gauge_full.sub"},
            ),
        },
    ),
}
