import streamlit as st

st.title("แบบฝึกหัด")

tab1, tab2, tab3, tab4 = st.tabs(["1. อายุงานที่เหลือ", "2. BMI", 
                                  "3. ความดันโลหิต", "4. คัดกรองผู้ป่วย"])

with tab1:
    st.header("แบบฝึกหัดข้อที่ 1")
    st.subheader("Super basic version")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:")
    st.write(f"อายุงานของคุณ {name} ก่อนเกษียณ คือ {60-age} ปี")

    st.divider()
    st.subheader("Secure version")
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("Enter your first name:")
    with col2:
        lname = st.text_input("Enter your last name:")
    age = st.number_input("Enter your age (yr):", min_value=0, max_value=60, step=1)
    st.write(f"อายุงานของคุณ {fname} {lname} ก่อนเกษียณ คือ {60-age:.0f} ปี")

with tab2:
    st.header("BMI")
    col_w, col_h = st.columns(2)
    with col_w:
        weight = st.number_input("กรุณากรอกน้ำหนัก (กิโลกรัม): ")
    with col_h:
        height = st.number_input("กรุณากรอกส่วนสูง (เซนติเมตร): ")
    
    bmi = weight/(height/100.0)**2

    st.markdown(f"### ค่า BMI ของคุณ คือ {bmi:.0f}")

    if bmi <= 18.5:
        st.write("คุณผอมไปแล้วนะ หาอะไรกินบ้าง")
    elif bmi > 18.5 and bmi <= 24.9:
        st.write("ยินดีด้วยครับ คุณหุ่นดีมาก")
        st.balloons()
    elif bmi > 24.9 and bmi <=29.9:
        st.write("คุณเริ่มอ้วนแล้วนะ")
    elif bmi > 29.9:
        st.write("คุณอ้วนเกินไปแล้ว")

    st.divider()
    w2 = st.slider("เลื่อนหาน้ำหนักของคุณ", min_value=20.0, max_value=150.0, step=1.0)
    h2 = st.slider("เลื่อนหาส่วนสูงของคุณ", min_value=150.0, max_value=190.0, step=1.0)
    
    bmi2 = w2/(h2/100.0)**2

    st.markdown(f"### ค่า BMI ของคุณ คือ {bmi:.0f}")

    if bmi2 <= 18.5:
        st.write("คุณผอมไปแล้วนะ หาอะไรกินบ้าง")
    elif bmi2 > 18.5 and bmi2 <= 24.9:
        st.write("ยินดีด้วยครับ คุณหุ่นดีมาก")
        st.balloons()
    elif bmi2 > 24.9 and bmi2 <=29.9:
        st.write("คุณเริ่มอ้วนแล้วนะ")
    elif bmi2 > 29.9:
        st.write("คุณอ้วนเกินไปแล้ว")
