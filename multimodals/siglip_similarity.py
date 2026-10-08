from PIL import Image
import requests
import torch

from transformers import AutoProcessor, AutoModel

MODEL_NAME = "google/siglip-large-patch16-384"

# Load model
model = AutoModel.from_pretrained(MODEL_NAME)

# Load processor
processor = AutoProcessor.from_pretrained(MODEL_NAME)


# --------------------------------------------------
# Download two images
# --------------------------------------------------

url1 = "http://images.cocodataset.org/val2017/000000039769.jpg"
url2 = "http://images.cocodataset.org/val2017/000000039769.jpg"

image1 = Image.open(
    requests.get(url1, stream=True).raw
)

image2 = Image.open(
    requests.get(url2, stream=True).raw
)

# --------------------------------------------------
# Create embeddings
# --------------------------------------------------

inputs1 = processor(
    images=image1,
    return_tensors="pt"
)

inputs2=processor(
    images=image2,
    return_tensors="pt"
)

with torch.no_grad():

    output1 = model.get_image_features(**inputs1)
    output2 = model.get_image_features(**inputs2)

# Get the actual vector
embedding1=output1.pooler_output[0]
embedding2=output2.pooler_output[0]

print("Embedding 1:")
print(embedding1.shape)

print("\nEmbedding 2:")
print(embedding2.shape)

# --------------------------------------------------
# Cosine similarity
# --------------------------------------------------

similarity = torch.nn.functional.cosine_similarity(
    embedding1.unsqueeze(0),
    embedding2.unsqueeze(0)
)

print("\nCosine similarity:")
print(similarity.item())
