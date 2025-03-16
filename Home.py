import streamlit as st

# สร้างคอลัมน์ 3 คอลัมน์ (คอลัมน์กลางจะใช้สำหรับจัดข้อความ)
col1, col2, col3 = st.columns([1, 3, 1])

# แสดงข้อความในคอลัมน์กลาง
with col2:
    st.title("IS FINAL PROJECT")