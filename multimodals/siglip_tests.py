from PIL import Image
import requests
import torch

from transformers import AutoProcessor, AutoModel


MODEL_NAME = "google/siglip-large-patch16-384"


# Load model
model = AutoModel.from_pretrained(MODEL_NAME)

# Load processor
processor = AutoProcessor.from_pretrained(MODEL_NAME)


# Download example image
url = "http://images.cocodataset.org/val2017/000000039769.jpg"

image = Image.open(
    requests.get(url, stream=True).raw
)


# Text candidates
texts = [
    "a photo of cats",
    "a photo of animals",
    "a photo of a car",
    "a photo of pets",
    "a photo of a computer",
    "a photo of a car",
    "a photo of food",
]


# Convert image + text into tensors
inputs = processor(
    text=texts,
    images=image,
    padding="max_length",
    return_tensors="pt"
)


# Run model
with torch.no_grad():
    outputs = model(**inputs)


# Image/text similarity scores
logits = outputs.logits_per_image


# Convert scores to probabilities
probs = torch.sigmoid(logits)


for text, probability in zip(texts, probs[0]):
    print(f"{probability:.2%} - {text}")