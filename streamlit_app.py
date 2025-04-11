
import streamlit as st
import openai

st.set_page_config(page_title="AI Ad Copy Generator", layout="centered")

st.title("🧠 AI Ad Copy Generator")
st.write("Generate engaging Facebook ad copy with OpenAI")

# Input fields
product = st.text_input("Product Name", placeholder="e.g., Silver Charm Bracelet")
audience = st.text_input("Target Audience", placeholder="e.g., Women aged 25 to 45 in Saudi Arabia")
tone = st.selectbox("Tone of Voice", ["Friendly", "Luxury", "Urgent", "Emotional", "Bold", "Professional"])

openai_api_key = st.text_input("🔑 OpenAI API Key", type="password")

if st.button("Generate Ad Copy"):
    if not all([product, audience, tone, openai_api_key]):
        st.warning("Please fill in all fields.")
    else:
        openai.api_key = openai_api_key
        prompt = f"""
        Write 3 creative Facebook ad copies for the following product:
        Product: {product}
        Target Audience: {audience}
        Tone: {tone}
        Each copy should be short, engaging, and designed to maximize CTR.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.8,
                max_tokens=200
            )
            ad_copies = response.choices[0].text.strip().split("\n")
            st.subheader("🎯 Generated Ad Copies:")
            for ad in ad_copies:
                if ad.strip():
                    st.markdown(f"- {ad.strip()}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
