import streamlit as st
import torch
import torch.nn.functional as F
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import json

from config import class_prompts, fort_names

with open('metadata.json', 'r') as f:
    metadata = json.load(f)

@st.cache_resource
def load_clip_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    model.to(device)
    model.eval()
    return model, processor, device

model, processor, device = load_clip_model()

all_prompts = []
fort_index_map = []
for i, fort in enumerate(fort_names):
    for prompt in class_prompts[fort]:
        all_prompts.append(prompt)
        fort_index_map.append(i)

st.title("Maharashtra Forts Image Classifier")
st.write("Upload an image of a fort to classify it among the famous forts of Maharashtra.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image.thumbnail((800, 800))
    st.image(image, caption='Uploaded Image', use_container_width=True)

    with st.spinner("Identifying the fort..."):
        inputs = processor(
            text=all_prompts,
            images=image,
            return_tensors="pt",
            padding=True
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = model(**inputs)

        logits = outputs.logits_per_image[0]

        fort_scores = [[] for _ in fort_names]
        for prompt_idx, fort_idx in enumerate(fort_index_map):
            fort_scores[fort_idx].append(logits[prompt_idx].item())

        fort_avg_logits = torch.tensor([
            sum(scores) / len(scores)
            for scores in fort_scores
        ])

        final_probs = F.softmax(fort_avg_logits, dim=0)

        top3 = final_probs.topk(3)
        top3_indices = top3.indices.tolist()
        top3_probs = top3.values.tolist()

    st.subheader("Top Predictions:")
    for rank, (idx, prob) in enumerate(zip(top3_indices, top3_probs)):
        st.write(f"#{rank+1}: {fort_names[idx]}")
        st.progress(prob, text=f"{prob*100:.1f}% confidence")

    predicted_fort = fort_names[top3_indices[0]]
    info = metadata.get(predicted_fort)

    st.divider()
    st.subheader(f"About {predicted_fort}:")

    if info:
        st.markdown("#### History")
        st.write(info["history"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Timings")
            st.write(info["timings"])
        with col2:
            st.markdown("#### Entry Fee")
            st.write(info["ticket"])

        st.markdown(f"[Open in Google Maps]({info['maps']})")
    else:
        st.warning(f"Metadata not available for {predicted_fort}.")