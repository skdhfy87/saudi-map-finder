import streamlit as st
import random
import time
from geopy.geocoders import Nominatim

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="كشاف السعودية", page_icon="📍")

st.title("📍 كشاف المواقع الهادئة")
st.write("اختر المدينة للحصول على إحداثيات في أطرافها بعيداً عن النشاط التجاري.")

# قائمة المدن
SAUDI_CITIES = [
    "الرياض", "جدة", "مكة المكرمة", "المدينة المنورة", "الدمام", "الهفوف", 
    "الطائف", "تبوك", "بريدة", "خميس مشيط", "الجبيل", "حائل", "نجران", 
    "حفر الباطن", "أبها", "الخرج", "ينبع", "جيزان", "الباحة", "القصيم"
]

city_choice = st.selectbox("اختر المدينة:", sorted(SAUDI_CITIES))
count = st.slider("عدد النقاط:", 1, 10, 5)
distance_km = st.slider("المسافة عن المركز (كم):", 5, 25, 10)

if st.button("توليد مواقع مقترحة"):
    geolocator = Nominatim(user_agent="saudi_explorer_v3")
    
    with st.spinner(f"جاري تحديد مواقع في {city_choice}..."):
        try:
            location = geolocator.geocode(city_choice + ", Saudi Arabia")
            if location:
                base_lat, base_lon = location.latitude, location.longitude
                
                for i in range(count):
                    # تحويل المسافة لإحداثيات
                    offset = distance_km / 111.0
                    r_lat = base_lat + random.uniform(-offset, offset)
                    r_lon = base_lon + random.uniform(-offset, offset)
                    
                    map_link = f"https://www.google.com/maps?q={r_lat},{r_lon}"
                    
                    st.markdown(f"---")
                    st.write(f"### 📍 موقع رقم {i+1}")
                    st.write(f"الإحداثيات: `{r_lat:.5f}, {r_lon:.5f}`")
                    st.link_button(f"فتح في خرائط جوجل", map_link)
            else:
                st.error("لم يتم العثور على إحداثيات المدينة.")
        except:
            st.error("حدث خطأ في الاتصال، يرجى المحاولة مرة أخرى.")
