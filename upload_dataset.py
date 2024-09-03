import os
from datasets import Dataset
from huggingface_hub import HfApi, create_repo
from PIL import Image
import io

def image_to_bytes(image_path):
    with Image.open(image_path) as img:
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        return buf.getvalue()

def create_dataset_dict(image_dir):
    data = []
    for filename in os.listdir(image_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(image_dir, filename)
            image_bytes = image_to_bytes(image_path)
            data.append({
                'image': image_bytes,
                'filename': filename
            })
    return data

# Create the dataset
image_dir = 'dataset'  # The directory where your images are stored
data = create_dataset_dict(image_dir)
dataset = Dataset.from_list(data)

# Create the repository (if not already created on the website)
create_repo(
    repo_id="Sagar18/geometric-shapes-dataset",
    repo_type="dataset",
    private=False,  # Set to True if you want a private dataset
)

# Push the dataset to the Hugging Face Hub
dataset.push_to_hub("Sagar18/geometric-shapes-dataset")