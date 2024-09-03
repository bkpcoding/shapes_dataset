import numpy as np
from PIL import Image, ImageDraw
import os

def create_triangle(draw, x, y, size):
    points = [
        (x, y + size),
        (x + size, y + size),
        (x + size / 2, y)
    ]
    draw.polygon(points, fill=255)

def create_square(draw, x, y, size):
    draw.rectangle([x, y, x + size, y + size], fill=255)

def create_pentagon(draw, x, y, size):
    points = [
        (x + size / 2, y),
        (x + size, y + size * 0.4),
        (x + size * 0.8, y + size),
        (x + size * 0.2, y + size),
        (x, y + size * 0.4)
    ]
    draw.polygon(points, fill=255)

def create_image():
    img = Image.new('L', (64, 64), color=0)
    draw = ImageDraw.Draw(img)
    
    shapes = [create_triangle, create_square, create_pentagon]
    column_width = 64 // 3
    row_height = 64 // 3
    shape_size = 10
    
    # Ensure at least one shape is present
    shape_presence = [np.random.random() < 0.5 for _ in range(3)]
    if not any(shape_presence):
        shape_presence[np.random.randint(0, 3)] = True
    
    for i, (shape_func, present) in enumerate(zip(shapes, shape_presence)):
        if present:
            x = i * column_width + (column_width - shape_size) // 2
            row = np.random.randint(0, 3)
            y = row * row_height + (row_height - shape_size) // 2
            shape_func(draw, x, y, shape_size)
    
    return img

def generate_dataset(num_images, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(num_images):
        img = create_image()
        img.save(os.path.join(output_dir, f'image_{i:05d}.png'))

# Generate 1000 images in the 'dataset' directory
generate_dataset(5000, 'dataset')