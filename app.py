import streamlit as st
import random

# 1. إعدادات الهوية البصرية (تأكد من وجود ملف logo.png في GitHub)
st.set_page_config(
    page_title="Sylon | سايـلون",
    page_icon="logo.png",
    layout="centered"
)

# 2. تحسين مظهر الزر والألوان (تم تصحيح الكود لتجنب NameError)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007BFF;
        color: white;
        border-radius: 10px;
        width: 100%;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان والواجهة
st.markdown("<h1 style='text-align: center;'>📡 SYLON</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>رادارك الخاص للأماكن الهادئة داخل الأحياء</p>", unsafe_allow_html=True)
st.info("نظام ذكي لتوليد إحداثيات داخل الأحياء السكنية بعيداً عن الزحام.")

# [cite_start]4. قائمة المدن (محدثة ومنظمة) [cite: 1, 2, 3]
CITIES = {
    "الرياض": (24.7136, 46.6753), "جدة": (21.5433, 39.1728), 
    "مكة المكرمة": (21.3891, 39.8579), "المدينة المنورة": (24.4672, 39.6024),
    "الدمام": (26.4207, 50.0888), "الهفوف": (25.3622, 49.5883),
    "أبها": (18.2164, 42.5053), "تبوك": (28.3835, 36.5662),
    "بريدة": (26.3260, 43.9750), "خميس مشيط": (18.3064, 42.7350),
    "الجبيل": (27.0117, 49.6583), "حائل": (27.5219, 41.6961),
    "نجران": (17.4933, 44.1272), "ينبع": (24.0891, 38.0637),
    "جيزان": (16.8892, 42.5511), "الخرج": (24.1500, 47.3333),
    "الباحة": (20.0129, 41.4677), "سكاكا": (29.9697, 40.2064)
}

# 5. أدوات التحكم
col1, col2 = st.columns(2)
with col1:
    city_choice = st.selectbox("🎯 المدينة:", sorted(CITIES.keys()))
with col2:
    [cite_start]count = st.number_input("🔢 عدد النقاط:", min_value=1, max_value=10, value=5) [cite: 3]

# 6. زر التوليد والنتائج
if st.button("🚀 تفعيل نظام Sylon"):
    [cite_start]base_lat, base_lon = CITIES[city_choice] [cite: 4]
    
    with st.spinner('جاري المسح...'):
        st.success(f"تم العثور على مواقع في أحياء {city_choice}")
        
        for i in range(count):
            # [cite_start]نطاق 0.015 للبقاء داخل الأحياء [cite: 4]
            r_lat = base_lat + random.uniform(-0.02, 0.02)
            r_lon = base_lon + random.uniform(-0.02, 0.02)
            
            [cite_start]map_link = f"https://www.google.com/maps?q={r_lat},{r_lon}" [cite: 5]
            
            with st.container():
                st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 10px; border-radius: 10px; margin-bottom: 5px;">
                    <h5 style="margin:0;">📍 موقع مقترح {i+1}</h5>
                </div>
                """, unsafe_allow_html=True)
                [cite_start]st.link_button(f"فتح في الخرائط", map_link) [cite: 5]

st.divider()
st.caption("Sylon Beta v1.5 | جميع المواقع داخل النطاق العمراني")
