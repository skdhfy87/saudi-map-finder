import streamlit as st
import random
import time
from geopy.geocoders import Nominatim

# إعدادات الصفحة
st.set_page_config(page_title="كشاف السعودية", page_icon="📍")

st.title("📍 كشاف المواقع الهادئة")

# قائمة المدن
SAUDI_CITIES = ["الرياض", "جدة", "مكة المكرمة", "المدينة المنورة", "الدمام", "الهفوف", "الطائف", "تبوك", "بريدة", "حائل", "نجران", "أبها", "ينبع", "جيزان"]

city_choice = st.selectbox("اختر المدينة:", sorted(SAUDI_CITIES))
count = st.slider("عدد النقاط:", 1, 10, 5)
distance_km = st.slider("المسافة عن المركز (كم):", 5, 20, 10)

if st.button("توليد مواقع"):
    # استخدام User Agent فريد لتجنب الحظر
    geolocator = Nominatim(user_agent="my_unique_explorer_app_123")
    
    try:
        location = geolocator.geocode(city_choice + ", Saudi Arabia")
        if location:
            base_lat = location.latitude
            base_lon = location.longitude
            
            st.success(f"تم تحديد مركز {city_choice}. جاري اختيار نقاط في الأطراف...")
            
            for i in range(count):
                # تحويل الكيلومترات إلى إحداثيات (تقريبياً)
                offset = distance_km / 111.0
                r_lat = base_lat + random.uniform(-offset, offset)
                r_lon = base_lon + random.uniform(-offset, offset)
                
                link = f"https://www.google.com/maps?q={r_lat},{r_lon}"
                
                with st.expander(f"📍 موقع مقترح {i+1}"):
                    st.write(f"الإحداثيات: `{r_lat:.5f}, {r_lon:.5f}`")
                    st.link_button("فتح في خرائط جوجل", link)
        else:
            st.error("لم يتم العثور على المدينة، حاول مرة أخرى.")
    except Exception as e:
        st.error(f"حدث خطأ بسيط، يرجى المحاولة مرة أخرى بعد ثوانٍ.")
