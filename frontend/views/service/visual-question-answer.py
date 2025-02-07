import streamlit as st
import requests
from PIL import Image
from config import API_BASE_URL_CONTAINER

if not API_BASE_URL_CONTAINER:
    raise ValueError("🚨 API base url is not set in the environment variables!")

st.title("🖼️ Visual Question Answering (VQA)")

uploaded_file = st.file_uploader("📤 Upload an image:", type=["png", "jpg", "jpeg"])
question = st.text_input("❓ Ask a question about the image:")

if uploaded_file and question:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_container_width =True)

    if st.button("🔍 Get Answer"):
        with st.spinner("⏳ Processing..."):
            files = {"image": uploaded_file.getvalue()}
            data = {"question": question}
            
            try:
                response = requests.post(f"{API_BASE_URL_CONTAINER}/vqa", files=files, data=data, timeout=30)

                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer received.")
                    st.success("✅ Answer:")
                    st.write(f"**{answer}**")
                else:
                    st.error(f"❌ API error: {response.status_code} - {response.text}")

            except requests.exceptions.Timeout:
                st.error("⏳ API request timed out. Please try again.")

            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ API request failed: {e}")

st.markdown("---")
st.markdown("🚀 **This application uses the `VietKien/blip-vqa-finetuned` model for Visual Question Answering.**")
