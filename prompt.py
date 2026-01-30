def build_prompt(gender, occasion, budget, colors, image_info):
    return f"""
User Gender: {gender}
Occasion: {occasion}
Budget: {budget}
Preferred Colors: {colors}
Image Analysis: {image_info}

Generate:
1. Outfit recommendation
2. Accessories
3. Footwear
4. Styling tips
5. Trend-based suggestions
"""
