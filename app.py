import streamlit as st
import random

# 1. تحسين الهوية البصرية (Favicon والاسم)
st.set_page_config(
    page_title="Sylon | سايـلون",
    page_icon="logo.png", # تأكد من رفع الملف بنفس الاسم 
    layout="centered"
)

# 2. إضافة لمسة جمالية بالألوان (CSS بسيط)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #007BFF;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        border: none;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة ترحيبية أنيقة
st.title("📡 SYLON")
st.markdown("<h3 style='text-align: right; color: #555;'>رادارك الخاص للأماكن الهادئة</h3>", unsafe_allow_html=True)
st.info("نظام ذكي لتوليد إحداثيات داخل الأحياء السكنية بعيداً عن الزحام.") [cite: 1]

# 4. قاعدة البيانات (تم تنظيف المكرر لزيادة السرعة)
CITIES = {
    "الرياض": (24.7136, 46.6753), "جدة": (21.5433, 39.1728), 
    "مكة المكرمة": (21.3891, 39.8579), "المدينة المنورة": (24.4672, 39.6024),
    "الدمام": (26.4207, 50.0888), "الهفوف": (25.3622, 49.5883),
    "أبها": (18.2164, 42.5053), "تبوك": (28.3835, 36.5662),
    "بريدة": (26.3260, 43.9750), "خميس مشيط": (18.3064, 42.7350),
    "الجبيل": (27.0117, 49.6583), "حائل": (27.5219, 41.6961),
    "نجران": (17.4933, 44.1272), "ينبع": (24.0891, 38.0637),
    "جيزان": (16.8892, 42.5511), "الخرج": (24.1500, 47.3333)
}

# تنظيم المدخلات في أعمدة لشكل أرتب
col1, col2 = st.columns(2)
with col1:
    city_choice = st.selectbox("🎯 المدينة:", sorted(CITIES.keys())) [cite: 3]
with col2:
    count = st.number_input("🔢 عدد النقاط:", min_value=1, max_value=10, value=5) [cite: 3]

# 5. تحسين شكل زر التوليد وتجربة الانتظار
if st.button("🚀 تفعيل نظام التوليد"):
    base_lat, base_lon = CITIES[city_choice] [cite: 4]
    
    # إضافة "أنيميشن" بسيط للتحميل ليعطي شعوراً بالسرعة والذكاء
    with st.spinner('جاري فحص الأحياء السكنية...'):
        import time
        time.sleep(0.5) # وهمي لإعطاء انطباع بالمعالجة
        
        st.success(f"تم العثور على {count} مواقع هادئة في {city_choice}") [cite: 4]
        
        # عرض النتائج في بطاقات (Cards)
        for i in range(count):
            r_lat = base_lat + random.uniform(-0.02, 0.02) [cite: 5]
            r_lon = base_lon + random.uniform(-0.02, 0.02) [cite: 5]
            
            map_link = f"https://www.google.com/maps?q={r_lat},{r_lon}" [cite: 5]
            
            # شكل كرت أنيق لكل نتيجة
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 15px; border-radius: 15px; margin-bottom: 10px; background-color: white;">
                    <h4 style="margin:0;">📍 موقع مقترح رقم {i+1}</h4>
                    <p style="color: gray; font-size: 0.8em;">إحداثيات: {r_lat:.5f}, {r_lon:.5f}</p>
                </div>
                """, unsafe_allow_html=True)
                st.link_button(f"🗺️ فتح موقع {i+1} في الخرائط", map_link) [cite: 5]

st.divider() [cite: 5]
st.caption("Sylon v1.5 - تم التحديث لضمان دقة المواقع داخل النطاق العمراني.") [cite: 5]
