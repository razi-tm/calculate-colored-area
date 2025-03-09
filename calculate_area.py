import cv2
import numpy as np

def calculate_area(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Error: Unable to read image"
    
    colors = {
        "red": ((0, 0, 100), (100, 100, 255)),
        "green": ((0, 100, 0), (100, 255, 100)),
        "blue": ((100, 0, 0), (255, 100, 100)),
        "yellow": ((0, 100, 100), (100, 255, 255)),
        "purple": ((100, 0, 100), (255, 100, 255)),
        "gray": ((50, 50, 50), (200, 200, 200)),
    }
    
    results = []
    total_pixels = image.shape[0] * image.shape[1]
    found_colors = False
    
    for color, (lower, upper) in colors.items():
        mask = cv2.inRange(image, np.array(lower), np.array(upper))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        total_area = 0
        
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            area = w * h
            
            if w == h:  # Square
                total_area += area
            else:  # Rectangle
                total_area += 3 * area
        
        if total_area > 0:
            results.append(f"{color}, {total_area}")
            found_colors = True
    
    if not found_colors:
        return f"black, {total_pixels}"
    
    return "\n".join(results)

if __name__ == "__main__":
    image_path = "shapes.png"  # Replace with actual image path
    print(calculate_area(image_path))

