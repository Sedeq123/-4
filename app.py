import streamlit as st
import os

# 1. تهيئة الصفحة وإعدادات العرض
st.set_page_config(
    page_title="استوديو نسيج الفاخر - NASIJ STUDIO",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# إدارة حالة التنقل بين الصفحات عبر الأزرار (Session State)
if "current_page" not in st.session_state:
    st.session_state.current_page = "الرئيسية"

# 2. تصميم الواجهة باللون الأسود والذهبي الملكي الشامل وطمس راديو ستريمليت التقليدي
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق بالكامل للأسود الفاخر */
    .stApp {
        background-color: #0B0B0C !important;
        color: #E5E5E5 !important;
    }
    
    /* تصميم العناوين */
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        font-family: 'Cairo', sans-serif;
        text-align: center;
        font-weight: 700;
    }
    
    /* الكروت الفاخرة */
    .luxury-card {
        background-color: #121214;
        border: 1px solid #D4AF37;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.08);
    }
    .design-title {
        font-size: 20px;
        font-weight: bold;
        color: #D4AF37;
        margin-top: 15px;
        margin-bottom: 8px;
    }
    .design-desc {
        font-size: 14px;
        color: #B3B3B3;
        line-height: 1.6;
    }
    
    /* === تصميم القائمة الجانبية الملكية المخصصة المستوحاة من الصورة === */
    [data-testid="stSidebar"] {
        background-color: #0B0B0C !important;
        border-right: 1px solid #D4AF37 !important;
        padding-top: 10px;
    }
    
    /* لوحة "مستشار التصميم" في أسفل القائمة */
    .sidebar-advisor {
        border: 1px solid #D4AF37;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        background-color: #121214;
        margin-top: 40px;
    }
    .advisor-title {
        color: #D4AF37;
        font-size: 15px;
        font-weight: bold;
        margin-top: 5px;
    }
    .advisor-desc {
        color: #888;
        font-size: 11px;
        line-height: 1.4;
    }

    /* جعل أزرار التنقل الجانبية برمجياً تبدو كروابط نصية فاخرة وبدون إطار تقليدي */
    .sidebar-nav-container .stButton>button {
        background-color: transparent !important;
        color: #B3B3B3 !important;
        border: none !important;
        text-align: right !important;
        width: 100% !important;
        padding: 10px 15px !important;
        font-size: 16px !important;
        font-family: 'Cairo', sans-serif;
        transition: all 0.3s ease-in-out;
        border-radius: 4px !important;
        display: flex;
        align-items: center;
    }
    
    /* تفتيح الإضاءة الذهبية عند تمرير الماوس فوق التبويب أو عندما يكون نشطاً */
    .sidebar-nav-container .stButton>button:hover {
        color: #D4AF37 !important;
        background-color: rgba(212, 175, 55, 0.05) !important;
        padding-right: 25px !important; /* حركة إزاحة ناعمة */
        box-shadow: inset 4px 0px 0px #D4AF37 !important;
    }
    
    /* تصميم خاص بالأزرار الرئيسية في الصفحة لتطابق الفخامة */
    .main-btn .stButton>button {
        background-color: #121214 !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 8px !important;
        width: 100%;
        padding: 12px 20px !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    .main-btn .stButton>button:hover {
        background-color: #D4AF37 !important;
        color: #0B0B0C !important;
        box-shadow: 0px 0px 15px #D4AF37 !important;
    }
    </style>
""", unsafe_allow_html=True)

# دالة للبحث عن الصور المحلية (الواجهة والكاتلوج الرئيسي)
def get_image_file(base_name):
    possible_names = [f"{base_name}.png", f"{base_name}.png.png", f"{base_name}.jpg", f"{base_name}.jpeg"]
    for name in possible_names:
        if os.path.exists(name):
            return name
    return None

# ==================== بناء الشريط الجانبي الفاخر المستوحى من صورتك ====================
with st.sidebar:
    # الشعار والنصوص العلوية الملكية
    st.markdown("<h2 style='text-align: center; margin-bottom: 0; font-size: 28px; letter-spacing: 1px;'>👑 N</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 18px; margin-top: 5px; margin-bottom: 0;'>NASIJ STUDIO</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 10px; letter-spacing: 2px;'>SMART CARPET DESIGN</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # حاوية الأزرار لتطبيق التصاميم الفاخرة عليها
    st.markdown('<div class="sidebar-nav-container">', unsafe_allow_html=True)
    
    # الأزرار الذكية البديلة لأزرار الراديو التقليدية مع إضاءة الخيار الحالي
    pages = [
        {"name": "الرئيسية", "icon": "🏠"},
        {"name": "استوديو التصميم", "icon": "🎨"},
        {"name": "الخامات", "icon": "🧶"},
        {"name": "التسعير", "icon": "💰"},
        {"name": "الكتالوج الفاخر", "icon": "📚"},
        {"name": "الطلبات", "icon": "🗂️"},
        {"name": "التواصل", "icon": "📞"}
    ]
    
    for p in pages:
        # إذا كانت الصفحة الحالية هي النشطة، نظهر لها علامة ذهبية مميزة
        label = f"{p['icon']} {p['name']}"
        if st.session_state.current_page == p['name']:
            label = f"✨ {p['icon']} {p['name']} "
            
        if st.button(label, key=f"nav_{p['name']}"):
            st.session_state.current_page = p['name']
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
    
    # لوحة "مستشار التصميم" المخصصة أسفل الشريط تماماً كالصورة
    st.markdown("""
        <div class="sidebar-advisor">
            <div style="font-size: 24px; color: #D4AF37;">🎧</div>
            <div class="advisor-title">مستشار التصميم</div>
            <div class="advisor-desc">متاح لمساعدتك في اختيار أفضل تصميم لمساحتك.</div>
        </div>
    """, unsafe_allow_html=True)


# ==================== إدارة عرض الصفحات بناءً على خيار الشريط الجانبي ====================

# 1. صفحة الرئيسية
if st.session_state.current_page == "الرئيسية":
    st.markdown("<h1>منصة تصميم السجاد الذكية</h1>", unsafe_allow_html=True)
    
    main_img = get_image_file("main_luxury")
    if main_img:
        st.image(main_img, use_container_width=True)
    else:
        st.warning("⚠️ يرجى التأكد من وجود صورة الواجهة الرئيسية في المستودع.")
        
    st.markdown("<h3 style='margin-top:20px;'>🚀 الانتقال السريع للمنصة</h3>", unsafe_allow_html=True)
    st.markdown('<div class="main-btn">', unsafe_allow_html=True)
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🎨 ابدأ التصميم الآن"):
            st.session_state.current_page = "استوديو التصميم"
            st.rerun()
    with col_btn2:
        if st.button("📚 استعرض الكاتلوج الفاخر"):
            st.session_state.current_page = "الكتالوج الفاخر"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 2. صفحة استوديو التصميم
elif st.session_state.current_page == "استوديو التصميم":
    st.markdown("<h1>استوديو التصميم الذكي عبر AI</h1>", unsafe_allow_html=True)
    prompt = st.text_area("✍️ صِف السجادة التي تحلم بها بالتفصيل:")
    uploaded_file = st.file_uploader("🖼️ أو ارفع صورة للإلهام:", type=["jpg", "png", "jpeg"])
    st.markdown('<div class="main-btn">', unsafe_allow_html=True)
    if st.button("✨ توليد التصميم الفاخر"):
        st.warning("🔄 يتم الآن تحليل النمط وتوليد عينات نسيجية فريدة...")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. صفحة الخامات
elif st.session_state.current_page == "الخامات":
    st.markdown("<h1>خامات النسيج الفاخرة</h1>", unsafe_allow_html=True)
    col_mat1, col_mat2 = st.columns(2)
    with col_mat1:
        st.markdown("<div class='luxury-card'><div class='design-title'>🧶 صوف نيوزيلندي فاخر</div><div class='design-desc'>أقوى أنواع الصوف الطبيعي ويحافظ على بريق الألوان وقوة النسيج على المدى الطويل.</div></div>", unsafe_allow_html=True)
    with col_mat2:
        st.markdown("<div class='luxury-card'><div class='design-title'>✨ الحرير الطبيعي</div><div class='design-desc'>يعطي لمعاناً ساحراً يتغير بشكل مذهل مع زوايا الإضاءة المختلفة في الغرفة.</div></div>", unsafe_allow_html=True)

# 4. صفحة التسعير
elif st.session_state.current_page == "التسعير":
    st.markdown("<h1>حاسبة التسعير الفوري والذكي</h1>", unsafe_allow_html=True)
    length = st.number_input("📏 طول السجادة (متر):", min_value=1.0, value=3.0)
    width = st.number_input("📐 عرض السجادة (متر):", min_value=1.0, value=2.0)
    st.markdown('<div class="main-btn">', unsafe_allow_html=True)
    if st.button("🧮 احسب التكلفة"):
        st.markdown(f"<div style='text-align:center;'><h3>التكلفة التقديرية: {length * width * 500:,.2f} ريال سعودي</h3></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 5. صفحة الكتالوج الفاخر
elif st.session_state.current_page == "الكتالوج الفاخر":
    st.markdown("<h1>مجموعة التصاميم الحصرية للسجاد الفخم</h1>", unsafe_allow_html=True)
    
    catalog_img = get_image_file("catalog_dashboard")
    if catalog_img:
        st.image(catalog_img, use_container_width=True)
    else:
        st.warning("⚠️ يرجى التأكد من وجود صورة لوحة الكاتلوج الرئيسية في المستودع.")
        
    st.markdown("<h3>🎯 تصفح اللوحات الفردية للإنتاج المباشر</h3>", unsafe_allow_html=True)
    
    individual_designs = [
        {"title": "ملحمة الشموخ", "desc": "حصان عربي أصيل يجسد القوة والحرية بتصميم ثلاثي الأبعاد وغبار متطاير.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_06_00%20%D9%85.png"},
        {"title": "الصقر الملكي", "desc": "صقر عربي ذهبي يتوسط خلفية سوداء داكنة محاط بزخارف ملكية دقيقة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_10_16%20%D9%85.png"},
        {"title": "نور المحراب", "desc": "زخارف إسلامية فاخرة مستوحاة من روعة العمارة الإسلامية تحت ضوء القمر.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_33_04%20%D9%85.png"},
        {"title": "تراث نجد", "desc": "نقوش نجدية هندسية أصيلة مدمجة في تصميم عصري يجمع بين عراقة الماضي وفخامة الحاضر.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_29_59%20%D9%85.png"},
        {"title": "سفينة الصحراء", "desc": "لوحة الأصالة العربية المتمثلة في الجمل مع خلفية القلاع العريقة ووقت الغروب الساحر الفخم.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_37_19%20%D9%85.png"},
        {"title": "المجلس الملكي", "desc": "تصميم سجادة فاخرة جداً مخصصة للقصور والمجالس الرسمية الكبرى بأعلى درجات الفخامة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_34_59%20%D9%85.png"}
    ]
    
    col1, col2 = st.columns(2)
    st.markdown('<div class="main-btn">', unsafe_allow_html=True)
    for index, d in enumerate(individual_designs):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            st.markdown(f"<div class='luxury-card'><div class='design-title'>{d['title']}</div><div class='design-desc'>{d['desc']}</div></div>", unsafe_allow_html=True)
            st.image(d['url'], use_container_width=True)
            if st.button(f"🛒 طلب إنتاج {d['title']}", key=f"prod_{index}"):
                st.success(f"👑 تم تسجيل طلبك لتصميم {d['title']}!")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. صفحة الطلبات
elif st.session_state.current_page == "الطلبات":
    st.markdown("<h1>لوحة متابعة الطلبات الخاصة بك</h1>", unsafe_allow_html=True)
    st.info("📦 لا توجد طلبات نشطة حالياً. بمجرد طلب أي تصميم من الكاتلوج سيظهر تقدم الإنتاج هنا.")

# 7. صفحة التواصل
elif st.session_state.current_page == "التواصل":
    st.markdown("<h1>قنوات التواصل والطلب المباشر</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-size:18px;'><p>📍 المقر الرئيسي: الرياض، المملكة العربية السعودية</p><p>👑 استوديو نسيج الذكي - فخامة تليق بمساحتك</p></div>", unsafe_allow_html=True)
    
