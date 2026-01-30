import numpy as np

def analyze_image(image):
    image = image.resize((60, 60))
    pixels = np.array(image)
    avg_color = pixels.mean(axis=(0, 1))
    return f"Average image color RGB: {avg_color}"
