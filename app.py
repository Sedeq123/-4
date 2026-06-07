import streamlit as st
import os

# 1. إعدادات الصفحة الكلية
st.set_page_config(
    page_title="استوديو نسيج الفاخر - NASIJ STUDIO",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# إدارة التنقل الداخلي بين التبويبات عبر الـ Session State لضمان عدم التجمد
if "page" not in st.session_state:
    st.session_state.page = "الرئيسية"

# 2. اللمسات البصرية العلوية (الألوان الملكية الأسود والذهبي)
st.markdown("""
    <style>
    /* تغيير الخلفية الكلية للتطبيق */
    .stApp {
        background-color: #0B0B0C !important;
        color: #E5E5E5 !important;
        font-family: 'Cairo', sans-serif;
    }
    
    /* العناوين الملكية */
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        text-align: center;
        font-weight: 700;
    }
    
    /* ضبط تنسيق القائمة الجانبية وإخفاء الراديو القديم */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    [data-testid="stSidebar"] {
        background-color: #0B0B0C !important;
        border-right: 1px solid #D4AF37 !important;
    }
    
    /* جعل أزرار القائمة الجانبية مصفوفة جهة اليمين بشكل أنيق وفخم */
    .stSidebar .stButton>button {
        background-color: transparent !important;
        color: #B3B3B3 !important;
        border: none !important;
        text-align: right !important;
        width: 100% !important;
        padding: 12px 15px !important;
        font-size: 16px !important;
        display: block !important;
        transition: all 0.3s ease;
    }
    
    /* تأثير التوهج الذهبي عند التمرير في القائمة الجانبية */
    .stSidebar .stButton>button:hover {
        color: #D4AF37 !important;
        background-color: rgba(212, 175, 55, 0.08) !important;
        box-shadow: inset 4px 0px 0px #D4AF37 !important;
    }

    /* صندوق مستشار التصميم في أسفل القائمة الجانبية */
    .advisor-box {
        border: 1px solid #D4AF37;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        background-color: #121214;
        margin-top: 30px;
    }

    /* تنسيق كروت عرض التصاميم الفردية في الكتالوج */
    .luxury-card {
        background-color: #121214;
        border: 1px solid #D4AF37;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
    }
    .design-title {
        font-size: 20px;
        font-weight: bold;
        color: #D4AF37;
        margin-bottom: 5px;
    }

    /* أزرار الانتقال والإنتاج الفاخرة المضمونة */
    .premium-btn .stButton>button {
        background-color: #121214 !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100% !important;
        padding: 10px 20px !important;
    }
    .premium-btn .stButton>button:hover {
        background-color: #D4AF37 !important;
        color: #0B0B0C !important;
        box-shadow: 0px 0px 10px #D4AF37 !important;
    }
    </style>
""", unsafe_allow_html=True)

# دالة برمجية مرنة لفحص وجود ملف الصورة المحلية بأي امتداد متاح
def get_local_image(base_name):
    for ext in [".png", ".png.png", ".jpg", ".jpeg"]:
        full_name = base_name + ext
        if os.path.exists(full_name):
            return full_name
    return None


# ==================== بناء القائمة الجانبية الملكية المضمونة ====================
with st.sidebar:
    st.markdown("<h2 style='margin-bottom: 0;'>👑 N</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 18px; margin-top: 5px; margin-bottom: 0;'>NASIJ STUDIO</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 10px; letter-spacing: 2px;'>SMART CARPET DESIGN</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # أزرار القائمة الجانبية المباشرة والمحاذية لليمين بنجاح
    if st.button("🏠 الرئيسية", key="btn_nav_home"):
        st.session_state.page = "الرئيسية"
        st.rerun()
    if st.button("🎨 استوديو التصميم", key="btn_nav_design"):
        st.session_state.page = "استوديو التصميم"
        st.rerun()
    if st.button("🧶 نسيج (الخامات)", key="btn_nav_mats"):
        st.session_state.page = "الخامات"
        st.rerun()
    if st.button("📚 الكاتلوج الفاخر", key="btn_nav_catalog"):
        st.session_state.page = "الكتالوج"
        st.rerun()
    if st.button("💰 التسعير الفوري", key="btn_nav_price"):
        st.session_state.page = "التسعير"
        st.rerun()
    if st.button("📞 التواصل والطلب", key="btn_nav_contact"):
        st.session_state.page = "التواصل"
        st.rerun()
        
    # إضافة بطاقة مستشار التصميم الفاخرة أسفل القائمة
    st.markdown("""
        <div class="advisor-box">
            <div style="font-size: 24px; color: #D4AF37;">🎧</div>
            <div style="color: #D4AF37; font-size: 15px; font-weight: bold; margin-top: 5px;">مستشار التصميم</div>
            <div style="color: #888; font-size: 11px; line-height: 1.4;">متاح لمساعدتك في اختيار أفضل تصميم لمساحتك.</div>
        </div>
    """, unsafe_allow_html=True)


# ==================== عرض محتوى الصفحات بناءً على الاختيار المستقر ====================

# 1. صفحة الرئيسية
if st.session_state.page == "الرئيسية":
    st.markdown("<h1>منصة تصميم السجاد الذكية</h1>", unsafe_allow_html=True)
    
    main_img = get_local_image("main_luxury")
    if main_img:
        st.image(main_img, use_container_width=True)
    else:
        st.warning("⚠️ يرجى التأكد من وجود صورة الواجهة الرئيسية باسم main_luxury.png")
        
    # تفعيل الانتقال الآمن والمباشر أسفل الصورة مباشرة بدلاً من الأزرار الشفافة المعلقة
    st.markdown("<h3 style='margin-top:25px;'>🚀 الانتقال السريع للمنصة</h3>", unsafe_allow_html=True)
    st.markdown('<div class="premium-btn">', unsafe_allow_html=True)
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🎨 ابدأ تجربة التصميم الذكي الآن"):
            st.session_state.page = "استوديو التصميم"
            st.rerun()
    with col_btn2:
        if st.button("📚 تصفح الكاتلوج الفاخر الحصري"):
            st.session_state.page = "الكتالوج"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 2. صفحة استوديو التصميم
elif st.session_state.page == "استوديو التصميم":
    st.markdown("<h1>استوديو التصميم الذكي عبر AI</h1>", unsafe_allow_html=True)
    prompt = st.text_area("✍️ صِف السجادة أو النقوش التي تحلم بها بالتفصيل:")
    uploaded_file = st.file_uploader("🖼️ أو ارفع صورة نمطية للإلهام وبناء النقش:", type=["jpg", "png", "jpeg"])
    st.markdown('<div class="premium-btn">', unsafe_allow_html=True)
    if st.button("✨ توليد التصميم الملكي"):
        st.warning("🔄 يتم الآن تحليل النمط والمحاكاة الذكية...")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. صفحة الخامات
elif st.session_state.page == "الخامات":
    st.markdown("<h1>خامات النسيج الفاخرة المعتمدة</h1>", unsafe_allow_html=True)
    col_mat1, col_mat2 = st.columns(2)
    with col_mat1:
        st.markdown("<div class='luxury-card'><div class='design-title'>🧶 صوف نيوزيلندي فاخر</div><p>يتميز بمتانته الفائقة وقدرته العالية على الاحتفاظ بنصوع وبريق الألوان الأصيلة عبر السنين.</p></div>", unsafe_allow_html=True)
    with col_mat2:
        st.markdown("<div class='luxury-card'><div class='design-title'>✨ الحرير الطبيعي 100%</div><p>يعطي لمعاناً ملكياً دافئاً تتغير تموجاته الساحرة بنعومة بالغة تماشياً مع زوايا الإضاءة.</p></div>", unsafe_allow_html=True)

# 4. صفحة الكاتلوج الفاخر مع القطع الفردية وروابطها المستقرة
elif st.session_state.page == "الكتالوج":
    st.markdown("<h1>مجموعة التصاميم الحصرية للسجاد الفخم</h1>", unsafe_allow_html=True)
    
    catalog_img = get_local_image("catalog_dashboard")
    if catalog_img:
        st.image(catalog_img, use_container_width=True)
        
    st.markdown("<br><h3>🎯 اللوحات الفردية الفاخرة للإنتاج المباشر</h3>", unsafe_allow_html=True)
    
    # قائمة اللوحات الفردية الفاخرة وروابطها المباشرة السليمة هندسياً
    individual_designs = [
        {"title": "ملحمة الشموخ", "desc": "حصان عربي أصيل بتصميم ثلاثي الأبعاد وغبار متطاير فخم يجسد القوة والحرية.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_06_00%20%D9%85.png"},
        {"title": "الصقر الملكي", "desc": "صقر عربي ذهبي يتوسط خلفية سوداء داكنة مع نقوش حواف ملكية بالغة الدقة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_10_16%20%D9%85.png"},
        {"title": "نور المحراب", "desc": "زخارف هندسية وإسلامية عريقة مستوحاة من عمق العمارة الأندلسية تحت ضوء القمر الفاتن.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_33_04%20%D9%85.png"},
        {"title": "تراث نجد", "desc": "نقوش نجدية تراثية أصيلة أعيد صياغتها بأسلوب عصري فريد يجمع بين الماضي والحاضر الفخم.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_29_59%20%D9%85.png"},
        {"title": "سفينة الصحراء", "desc": "لوحة الأصالة والمجد العربي المتمثلة في الجمل العربي الممتد مع خلفية قلاع تاريخية وقت الغروب.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_37_19%20%D9%85.png"},
        {"title": "المجلس الملكي", "desc": "تصميم سجادة فخم وحصري للغاية مخصص للقصور الفارهة والمجالس الرسمية الكبرى بأعلى دقة نسيجية.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_34_59%20%D9%85.png"}
    ]
    
    col1, col2 = st.columns(2)
    st.markdown('<div class="premium-btn">', unsafe_allow_html=True)
    for index, d in enumerate(individual_designs):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            st.markdown(f"<div class='luxury-card'><div class='design-title'>{d['title']}</div><p style='color:#B3B3B3; font-size:14px;'>{d['desc']}</p></div>", unsafe_allow_html=True)
            # عرض الصورة المباشرة من الروابط المستقرة للمستودع
            st.image(d['url'], use_container_width=True)
            if st.button(f"🛒 طلب إنتاج {d['title']}", key=f"prod_click_{index}"):
                st.success(f"👑 تم تسجيل طلبك الفاخر لتصميم ({d['title']}) بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. صفحة التسعير الفوري
elif st.session_state.page == "التسعير":
    st.markdown("<h1>حاسبة التسعير الفوري والذكي</h1>", unsafe_allow_html=True)
    length = st.number_input("📏 طول السجادة المطلوب (متر):", min_value=1.0, value=3.0)
    width = st.number_input("📐 عرض السجادة المطلوب (متر):", min_value=1.0, value=2.0)
    st.markdown('<div class="premium-btn">', unsafe_allow_html=True)
    if st.button("🧮 احسب التكلفة الإجمالية"):
        st.success(f"السعر التقديري الحصري للإنتاج: {length * width * 500:,.2f} ريال سعودي")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. صفحة التواصل والطلب
elif st.session_state.page == "التواصل":
    st.markdown("<h1>قنوات التواصل والطلب المباشر</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-size:18px;'><p>📍 المقر الرئيسي: الرياض، حي السليمانية</p><p>👑 استوديو نسيج - فخامة تليق بمساحتك وعراقتك</p></div>", unsafe_allow_html=True)
    
