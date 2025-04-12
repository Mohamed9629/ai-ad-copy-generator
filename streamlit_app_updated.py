
import streamlit as st
import openai

st.set_page_config(page_title="AI Ad Copy Generator", layout="centered")

st.title("🧠 AI Ad Copy Generator")
st.write("Generate engaging Facebook ad copy with OpenAI")

# Input fields
product = st.text_input("Product Name", placeholder="e.g.,Tshirt")
audience = st.text_input("Target Audience", placeholder="e.g., Women or aged 25 to 45 in any country you need")
tone = st.selectbox("Tone of Voice", ["Friendly", "Luxury", "Urgent", "Emotional", "Bold", "Professional"])

openai_api_key = st.text_input("🔑 OpenAI API Key", type="password")

if st.button("Generate Ad Copy"):
    if not all([product, audience, tone, openai_api_key]):
        st.warning("Please fill in all fields.")
    else:
        openai.api_key = openai_api_key
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional copywriter for Facebook ads."},
                    {"role": "user", "content": f"Write 3 creative Facebook ad copies for the following product:
Product: {product}
Target Audience: {audience}
Tone: {tone}
Each copy should be short, engaging, and designed to maximize CTR."}
                ],
                temperature=0.8,
                max_tokens=300
            )
            ad_copies = response.choices[0].message.content.strip().split("\n")
            st.subheader("🎯 Generated Ad Copies:")
            for ad in ad_copies:
                if ad.strip():
                    st.markdown(f"- {ad.strip()}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
