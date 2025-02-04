import streamlit as st
import openai
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

# Thiết lập API key
openai.api_key = OPENAI_API_KEY

# Giao diện ứng dụng
st.title("AI Soạn Giáo Án Tự Động")

# Nhập thông tin từ người dùng
subject = st.text_input("Môn học:")
grade = st.text_input("Lớp:")
topic = st.text_input("Chủ đề:")
duration = st.text_input("Thời lượng:")
objectives = st.text_area("Mục tiêu học tập:")

# Nút để tạo giáo án
if st.button("Tạo Giáo Án"):
    prompt = f"Soạn giáo án môn {subject} lớp {grade} về {topic}, thời lượng {duration}. Mục tiêu học tập: {objectives}"
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "Bạn là một trợ lý giáo dục AI."},
            {"role": "user", "content": prompt}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )
    lesson_plan = response['choices'][0]['message']['content']
    st.write("Giáo án được tạo:")
    st.write(lesson_plan)