import io
from datasets import load_dataset
from PIL import Image
import matplotlib.pyplot as plt
import random

# Load the dataset
dataset = load_dataset("Sagar18/geometric-shapes-dataset")

# Function to convert image bytes to PIL Image
def bytes_to_image(image_bytes):
    return Image.open(io.BytesIO(image_bytes))

# Function to display a single image
def display_image(image, title):
    plt.figure(figsize=(5, 5))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.savefig("sample.png")

# Display info about the dataset
print(f"Dataset info:\n{dataset}")

# Get the 'train' split (or the appropriate split for your dataset)
train_dataset = dataset['train']

# Display 5 random images
num_samples = 5
random_indices = random.sample(range(len(train_dataset)), num_samples)

for idx in random_indices:
    image_bytes = train_dataset[idx]['image']
    filename = train_dataset[idx]['filename']
    
    image = bytes_to_image(image_bytes)
    display_image(image, f"Image {idx}: {filename}")

# Print some statistics
print(f"\nTotal number of images: {len(train_dataset)}")
print(f"Image dimensions: {image.size}")