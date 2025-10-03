import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("☁️ Word Cloud Demo")

text = st.text_area("Enter text:", "Hello Streamlit!")

if text:
    wc = WordCloud(width=600, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
