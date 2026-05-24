import streamlit as st

st.set_page_config(
    page_title="เฉลยแบบฝึกหัด",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#----------------------------------------------------------------------------
# Custom CSS for styling
# ส่วนนี้ เป็นการเพิ่ม CSS เพื่อปรับแต่งลักษณะของเว็บแอปให้ดูสวยงามและน่าใช้งานมากขึ้น
# การตั้ง font-family, background-color, และสีของข้อความ สามารถปรับแต่งได้ตามความชอบ
# สามารถดูโค้ดสี ได้ที่ https://xn--code-3jovd.plus.in.th/
# นอกจากนี้ยังมีการปรับแต่งปุ่ม, แท็บ, และส่วนต่างๆ ของเว็บแอปให้ดูดีขึ้นด้วย
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #F0EEE6;
        secondary-background-color: #E3DACC;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #3D2A2A;
    }
    [data-testid="stHeader"] {
        background-color: #E3DACC;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .stTabs [role="tab"] {
        background-color: #e0e0e0;
        color: #333333;
        border-radius: 5px 5px 0 0;
        padding: 10px 15px;
        margin-right: 5px;
    }
    
    .stTabs [role="tab"][aria-selected="true"] {
        background-color: #4CAF50;
        color: white;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    
    .stButton button:hover {
        background-color: #45a049;
    }
    
    /* Divider styling */
    .stDivider {
        border-top: 2px solid #4CAF50;
        margin: 30px 0;
    }
    
    /* Subheader styling */
    .stSubheader {
        color: #4CAF50;
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: #dff0d8;
        color: #3c763d;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 20px;
    }
    
    /* Warning message styling */
    .stWarning {
        background-color: #fcf8e3;
        color: #8a6d3b;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 20px;
    }
    
    /* Error message styling */
    .stError {
        background-color: #f2dede;
        color: #a94442;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .st-key-tab1_container {
        background-color: #E3DACC;
        border-radius: 5px 5px 5px 5px;
        padding: 10px 15px;
        margin-right: 5px;
    }
    .st-key-normal_bmi_container {
        background-color: #F0FFF0;
        color: #3D2A2A;
        border-radius: 5px 5px 5px 5px;
        padding: 10px 15px;
        margin-right: 5px;
        font-weight: bold;
        font-size: 24px;
    }
    .st-key-overweight_bmi_container {
        background-color: #FFFACD;
        color: #3D2A2A;
        border-radius: 5px 5px 5px 5px;
        padding: 10px 15px;
        margin-right: 5px;
        font-weight: bold;
        font-size: 24px;
    }
    .st-key-obese_container {
        background-color: red;
        color: white;
        border-radius: 5px 5px 5px 5px;
        padding: 10px 15px;
        margin-right: 5px;
        font-weight: bold;
        font-size: 24px;
    }
    .st-key-emergency_container {
        background-color: lavender;
        color: DarkSlateBlue;
        border-radius: 5px 5px 5px 5px;
        padding: 10px 15px;
        margin-right: 5px;
        font-weight: bold;
        font-size: 24px;
    }
    </style>        
    
    """, unsafe_allow_html=True
)

st.title("เฉลยแบบฝึกหัด ✅ \n ผ่านการสร้าง Web App ด้วย Streamlit") 

## Create a sidebar for the code to be downloaded
with st.sidebar:
    st.write("Download the code for each exercise:")
    st.download_button("Download", data=open("solutions_exercise_webapp_23May2026.py", "r").read(), file_name="exercise_1_webapp_code.py")

# Create tab navigation
tab_1, tab_2, tab_3, tab_4 = st.tabs([
    "1. อายุงานที่เหลืออยู่", 
    "2. BMI และการวิเคราะห์สุขภาพ", 
    "3. ความดันโลหิต", 
    "4. คัดกรองผู้ป่วย"
])

# ============================================================================
# TAB 1: อายุงานที่เหลืออยู่
# ============================================================================
with tab_1:
    st.header("1. อายุงานที่เหลืออยู่")
    st.markdown("""
    **โจทย์:** ให้รับข้อมูล ชื่อ นามสกุล และอายุของพนักงานแต่ละคน จากนั้นคำนวณอายุงานที่เหลืออยู่จนถึงอายุเกษียณ (สมมติว่าเกษียณที่อายุ 60 ปี) และแสดงผลลัพธ์ในรูปแบบที่อ่านง่าย    

    **คำถาม:** จงเขียนโค้ดเพื่อคำนวณอายุงานที่เหลืออยู่ของแต่ละพนักงานและแสดงผลลัพธ์ในรูปแบบที่อ่านง่าย.
    """)
    
    st.divider()
    st.subheader(":alarm_clock: ตรวจสอบอายุงานก่อนเกษียณ :alarm_clock:")
    
    with st.container(key="tab1_container"):
        col1, col2 = st.columns(2)
        with col1:
            fname = st.text_input("Enter your first name:")
        with col2:
            lname = st.text_input("Enter your last name:")
        age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1, value=20)
        
        if fname and lname and age:
            st.write(f"Hello, {fname} {lname}! คุณเหลือเวลาทำงานอีกเพียง {60 - age} ปี!")
        else:
            st.write("Please enter your first name, last name, and age to see the greeting message.")
        
#----------------------------------------------------------------------------
# TAB 2: BMI และการวิเคราะห์สุขภาพ
with tab_2:
    st.header("2. BMI และการวิเคราะห์สุขภาพ")
    st.markdown("""
    **โจทย์:** ให้รับข้อมูล น้ำหนัก (กิโลกรัม) และส่วนสูง (เซนติเมตร) ของผู้ใช้ จากนั้นคำนวณค่า BMI และแสดงผลลัพธ์พร้อมคำอธิบายเกี่ยวกับสถานะสุขภาพของผู้ใช้ตามค่า BMI ที่ได้

    **คำถาม:** จงเขียนโค้ดเพื่อคำนวณค่า BMI และแสดงผลลัพธ์พร้อมคำอธิบายเกี่ยวกับสถานะสุขภาพของผู้ใช้ตามค่า BMI ที่ได้.
    """)
    
    st.divider()
    st.subheader(":weight_lifting_man: Body Mass Index (BMI) Calculator :climbing_man:")
    
    col1_bmi, col2_bmi = st.columns(2)
    with col1_bmi:
        weight = st.number_input("Enter your weight in kilograms:", min_value=20.0, step=0.1, value=50.0)
    with col2_bmi:
        height = st.number_input("Enter your height in centimeters:", min_value=100.0, step=1.0, value=150.0)
    
    if weight > 0 and height > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            st.write("You are underweight.")
            st.write("Eat something!")
        elif 18.5 <= bmi < 24.9:
            with st.container(key="normal_bmi_container"):
                st.markdown(""" 
                            ### You have a normal weight.                            
                            Great job maintaining a healthy weight! Keep up the good work with a balanced diet and regular exercise to stay healthy.
                            """)
                st.balloons()
        elif 25 <= bmi < 29.9:
            with st.container(key="overweight_bmi_container"):
                st.markdown(""" 
                            ### You are overweight.                            
                            Consider maintaining a healthy diet and regular exercise to manage your weight.
                            """)
        elif 30 <= bmi < 34.9:
            with st.container(key="overweight_bmi_container"):
                st.markdown(""" 
                            ### :rotating_light: You are obese.                            
                            It's important to consult with a healthcare provider for personalized advice on managing your weight and improving your health.
                            """)
        elif 35 <= bmi < 39.9:
            with st.container(key="obese_container"):
                st.markdown(""" 
                            ### :ambulance: You are severely obese.                            
                            It's important to consult with a healthcare provider for personalized advice on managing your weight and improving your health.
                            """)
        else:   
            with st.container(key="obese_container"):
                st.markdown("""
                            ### :ambulance: You are morbidly obese: 
                            Consult with a healthcare provider!
                            """)
    else:
        st.write("Please enter valid weight and height to calculate your BMI.")
        
# ============================================================================
# TAB 3: ความดันโลหิต
# ============================================================================
with tab_3:
    st.header("3. ความดันโลหิต")
    st.markdown("""
    **โจทย์:** ให้รับข้อมูล ความดันโลหิต systolic และ diastolic ของผู้ใช้ จากนั้นวิเคราะห์สถานะความดันโลหิตของผู้ใช้ตามเกณฑ์ที่กำหนด และแสดงผลลัพธ์พร้อมคำอธิบายเกี่ยวกับสถานะสุขภาพของผู้ใช้

    **คำถาม:** จงเขียนโค้ดเพื่อวิเคราะห์สถานะความดันโลหิตของผู้ใช้ตามเกณฑ์ที่กำหนด และแสดงผลลัพธ์พร้อมคำอธิบายเกี่ยวกับสถานะสุขภาพของผู้ใช้.
    """)
    
    st.divider()
    st.subheader(" ความดันโลหิต (Blood Pressure) ")
    
    blood_pressure = st.text_input("กรุณากรอกความดันโลหิตของคุณ (เช่น 120/80):", value="120/80")  
    if blood_pressure:
        try:
            systolic_str, diastolic_str = blood_pressure.split('/')
            systolic = int(systolic_str.strip())
            diastolic = int(diastolic_str.strip())
            
            if systolic <= 120 and diastolic <= 80:
                st.success("Your blood pressure is normal.")
            elif 120 <= systolic < 130 and diastolic < 80:
                st.warning("You have elevated blood pressure.")
            elif (130 <= systolic < 140) or (80 <= diastolic < 90):
                st.info("You have high blood pressure (Stage 1).")
            elif (140 <= systolic) or (90 <= diastolic):
                st.error("You have high blood pressure (Stage 2).")
            else:
                st.write("Please enter valid blood pressure values.")
        except ValueError:
            st.write("Invalid format. Please enter blood pressure in the format 'systolic/diastolic' (e.g., 120/80).")
    else:
        st.write("Please enter your blood pressure to analyze your health status.")
    
# ============================================================================
# TAB 4: คัดกรองผู้ป่วยฉุกเฉิน
# ============================================================================
with tab_4:
    st.header("4. คัดกรองผู้ป่วย")
    st.markdown("""
    **โจทย์:** ให้รับข้อมูล อัตราการเต้นของหัวใจ (bpm) อุณหภูมิร่างกาย (°C) ความดันโลหิต (systolic/diastolic) ระดับออกซิเจน (SpO2) ของผู้ใช้ 
    จากนั้นวิเคราะห์สถานะสุขภาพของผู้ใช้ตามเกณฑ์ที่กำหนด และแสดงผลลัพธ์พร้อมคำอธิบายเกี่ยวกับสถานะสุขภาพของผู้ใช้

    **คำถาม:** จงเขียนโค้ดเพื่อวิเคราะห์สถานะสุขภาพของผู้ใช้ตามเกณฑ์ที่กำหนด และแสดงผลลัพธ์พร้อมคำอธิบายเกี่ยวกับสถานะสุขภาพของผู้ใช้.
    """)
    
    st.divider()
    
    with st.container(key="emergency_container"):
        st.subheader(":ambulance: คัดกรองผู้ป่วยฉุกเฉิน :ambulance:")
        
        temperature = st.number_input("Enter your body temperature in °C:", min_value=30.0, max_value=45.0, step=0.1, value=36.5)
        heart_rate = st.number_input("Enter your heart rate in bpm:", min_value=30, max_value=200, step=1, value=70)
        spo2 = st.number_input("Enter your oxygen saturation level (SpO2) in %:", min_value=50, max_value=100, step=1, value=98)
        blood_pressure_emergency = st.text_input("Enter your blood pressure in the format 'systolic/diastolic' (e.g., 120/80):", key="bp_emergency", value="120/80")    
        
        # Page configuration
        st.set_page_config(page_title="GCS Calculator", page_icon="🧠", layout="centered")
        st.subheader("🧠 Glasgow Coma Scale (GCS) Calculator")
        st.caption("Click an option in each category, then press the button to calculate the total score.")

    # GCS Response Mappings
        EYE_RESPONSES = {
            "4 - Spontaneous": 4,
            "3 - To sound": 3,
            "2 - To pressure": 2,
            "1 - None": 1
        }

        VERBAL_RESPONSES = {
            "5 - Oriented": 5,
            "4 - Confused": 4,
            "3 - Inappropriate words": 3,
            "2 - Incomprehensible sounds": 2,
            "1 - None": 1
        }

        MOTOR_RESPONSES = {
            "6 - Obeys commands": 6,
            "5 - Localizes to pain": 5,
            "4 - Normal flexion (withdrawal)": 4,
            "3 - Abnormal flexion (decorticate)": 3,
            "2 - Extension (decerebrate)": 2,
            "1 - None": 1
        }

        # Layout: 3 columns for E, V, M
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("#### 👁️ Eye Opening")
            eye_selected = st.radio("Select response:", list(EYE_RESPONSES.keys()), index=None, key="eye")

        with col2:
            st.markdown("#### 🗣️ Verbal Response")
            verbal_selected = st.radio("Select response:", list(VERBAL_RESPONSES.keys()), index=None, key="verbal")

        with col3:
            st.markdown("#### 💪 Motor Response")
            motor_selected = st.radio("Select response:", list(MOTOR_RESPONSES.keys()), index=None, key="motor")

        # Calculate Button
        if st.button("🚑 Analyze Emergency Status", type="primary", use_container_width=True):
            if not eye_selected or not verbal_selected or not motor_selected or not blood_pressure_emergency:
                st.warning("⚠️ Please select a response for all categories before clicking the button.")
            else:
                blood_pressure_valid = False
                if blood_pressure_emergency:
                    try:
                        systolic_emergency_str, diastolic_emergency_str = blood_pressure_emergency.split('/')
                        systolic_emergency = int(systolic_emergency_str.strip())
                        diastolic_emergency = int(diastolic_emergency_str.strip())
                        blood_pressure_valid = True
                    except ValueError:
                        st.error("Invalid format for blood pressure. Please enter in the format 'systolic/diastolic' (e.g., 120/80).")  
        
        
                gcs_total = EYE_RESPONSES[eye_selected] + VERBAL_RESPONSES[verbal_selected] + MOTOR_RESPONSES[motor_selected]
            
                st.divider()
                st.markdown(f"### 🧮 Total GCS Score: `{gcs_total}`")

                emergency_conditions = []
                if temperature > 38.0:
                    emergency_conditions.append("High Fever")
                if heart_rate > 100:
                    emergency_conditions.append("Tachycardia")
                if spo2 < 90:
                    emergency_conditions.append("Low Oxygen Saturation")
                if systolic_emergency > 180 or diastolic_emergency > 120:
                    emergency_conditions.append("Hypertensive Crisis")            
                
                # Clinical Interpretation
                if gcs_total >= 13:
                    st.success("✅ **Mild** Brain Injury (GCS 13–15)")
                elif gcs_total >= 9:
                    st.warning("⚠️ **Moderate** Brain Injury (GCS 9–12)")
                else:
                    st.error("🚨 **Severe** Brain Injury (GCS 3–8)")

                st.divider()
                if emergency_conditions:
                    st.error(f"🚨 **Emergency Alert!** Detected conditions: {', '.join(emergency_conditions)}. Seek immediate medical attention!")
                else:
                    st.success("✅ No critical emergency conditions detected based on the provided vital signs.")
                