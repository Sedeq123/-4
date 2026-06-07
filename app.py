import streamlit as st
import os

# 1. إعدادات الصفحة الكلية
st.set_page_config(
    page_title="استوديو نسيج الفاخر - NASIJ STUDIO",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# إدارة حالة التنقل بين التبويبات
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 الرئيسية"

# 2. هندسة الـ CSS الملكية الصافية (طمس تام للتشوهات والافتراضيات)
st.markdown("""
    <style>
    /* خلفية التطبيق الكلية */
    .stApp {
        background-color: #0B0B0C !important;
        color: #E5E5E5 !important;
        font-family: 'Cairo', sans-serif;
    }
    
    /* العناوين الذهبية */
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        text-align: center;
        font-weight: 700;
    }
    
    /* إخفاء تام وعزل كامل لأي عناصر تنقل افتراضية من ستريمليت */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    [data-testid="stSidebar"] {
        background-color: #0B0B0C !important;
        border-right: 1px solid #D4AF37 !important;
    }
    
    /* تحويل أزرار ستريمليت في القائمة الجانبية إلى روابط نصية فخمة ومحاذية تماماً */
    .sidebar-container .stButton>button {
        background-color: transparent !important;
        color: #B3B3B3 !important;
        border: none !important;
        text-align: right !important;
        width: 100% !important;
        padding: 12px 15px !important;
        font-size: 16px !important;
        font-family: 'Cairo', sans-serif;
        display: block !important;
        transition: all 0.25s ease-in-out;
    }
    
    /* تأثير التوهج الذهبي والإزاحة عند تمرير الماوس فوق خيارات القائمة */
    .sidebar-container .stButton>button:hover {
        color: #D4AF37 !important;
        background-color: rgba(212, 175, 55, 0.06) !important;
        box-shadow: inset 4px 0px 0px #D4AF37 !important;
    }

    /* صندوق مستشار التصميم الفخم في الأسفل */
    .sidebar-advisor {
        border: 1px solid #D4AF37;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        background-color: #121214;
        margin-top: 40px;
    }

    /* === حاوية الصورة الرئيسية والأزرار الشفافة التفاعلية فوقها === */
    .main-image-box {
        position: relative;
        width: 100%;
        max-width: 480px;
        margin: 0 auto;
    }
    
    /* جعل أزرار ستريمليت هنا شفافة بالكامل (حجم زر مخفي راكب فوق الصورة) */
    .hitbox-design button, .hitbox-catalog button {
        position: absolute !important;
        width: 76% !important;
        left: 12% !important;
        height: 48px !important;
        background-color: transparent !important;
        color: transparent !important;
        border: none !important;
        cursor: pointer !important;
        z-index: 999 !important;
    }
    
    /* إسقاط الزر الشفاف الأول فوق "ابتدئ بالتصميم" */
    .hitbox-design button {
        bottom: 21.5% !important;
    }
    /* إسقاط الزر الشفاف الثاني فوق "ويب كاتلوج" */
    .hitbox-catalog button {
        bottom: 11.5% !important;
    }
    
    /* كروت الكاتلوج الفاخرة للقطع الفردية */
    .luxury-card {
        background-color: #121214;
        border: 1px solid #D4AF37;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 15px;
        text-align: center;
    }
    .design-title {
        font-size: 20px;
        font-weight: bold;
        color: #D4AF37;
        margin-bottom: 5px;
    }
    
    /* تنسيق أزرار طلب الإنتاج الفاخرة للقطع الفردية */
    .order-btn-box .stButton>button {
        background-color: #121214 !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        font-weight: bold !important;
        border-radius: 6px !important;
        width: 100% !important;
    }
    .order-btn-box .stButton>button:hover {
        background-color: #D4AF37 !important;
        color: #0B0B0C !important;
    }
    </style>
""", unsafe_allow_html=True)

# دالة ذكية لفحص وجود الصورة المحلية بأي امتداد (مفرد أو مكرر من الهاتف)
def find_local_image(base_name):
    for ext in [".png", ".png.png", ".jpg", ".jpeg"]:
        full_name = base_name + ext
        if os.path.exists(full_name):
            return full_name
    return None


# ==================== بناء الشريط الجانبي الملكي النظيف ====================
with st.sidebar:
    st.markdown("<h2 style='margin-bottom: 0;'>👑 N</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 18px; margin-top: 5px; margin-bottom: 0;'>NASIJ STUDIO</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 10px; letter-spacing: 2px;'>SMART CARPET DESIGN</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # القائمة الجانبية الأنيقة المحاذية لليمين
    st.markdown('<div class="sidebar-container">', unsafe_allow_html=True)
    
    if st.button("🏠 الرئيسية", key="menu_home"):
        st.session_state.current_page = "🏠 الرئيسية"
        st.rerun()
    if st.button("🎨 استوديو التصميم", key="menu_design"):
        st.session_state.current_page = "🎨 استوديو التصميم"
        st.rerun()
    if st.button("🧶 نسيج (الخامات)", key="menu_materials"):
        st.session_state.current_page = "🧶 نسيج (الخامات)"
        st.rerun()
    if st.button("📚 الكاتلوج الفاخر", key="menu_catalog"):
        st.session_state.current_page = "📚 الكاتلوج الفاخر"
        st.rerun()
    if st.button("💰 التسعير الفوري", key="menu_price"):
        st.session_state.current_page = "💰 التسعير الفوري"
        st.rerun()
    if st.button("📞 التواصل والطلب", key="menu_contact"):
        st.session_state.current_page = "📞 التواصل والطلب"
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    # بطاقة مستشار التصميم الثابتة بأسفل القائمة الجانبية
    st.markdown("""
        <div class="sidebar-advisor">
            <div style="font-size: 24px; color: #D4AF37;">🎧</div>
            <div style="color: #D4AF37; font-size: 15px; font-weight: bold; margin-top: 5px;">مستشار التصميم</div>
            <div style="color: #888; font-size: 11px; line-height: 1.4;">متاح لمساعدتك في اختيار أفضل تصميم لمساحتك.</div>
        </div>
    """, unsafe_allow_html=True)


# ==================== إدارة عرض الصفحات بدقة ====================

# 1. صفحة الرئيسية (تفعيل الأزرار المدمجة داخل الصورة بشكل مخفي تماماً)
if st.session_state.current_page == "🏠 الرئيسية":
    st.markdown("<h1>منصة تصميم السجاد الذكية</h1>", unsafe_allow_html=True)
    
    main_img = find_local_image("main_luxury")
    if main_img:
        st.markdown('<div class="main-image-box">', unsafe_allow_html=True)
        st.image(main_img, use_container_width=True)
        
        # الزر الشفاف الأول المتموضع جغرافياً بدقة فوق "ابتدئ بالتصميم"
        st.markdown('<div class="hitbox-design">', unsafe_allow_html=True)
        if st.button("hidden_design_click", key="go_to_design_tab"):
            st.session_state.current_page = "🎨 استوديو التصميم"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # الزر الشفاف الثاني المتموضع جغرافياً بدقة فوق "ويب كاتلوج"
        st.markdown('<div class="hitbox-catalog">', unsafe_allow_html=True)
        if st.button("hidden_catalog_click", key="go_to_catalog_tab"):
            st.session_state.current_page = "📚 الكاتلوج الفاخر"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ يرجى التأكد من رفع صورة الواجهة الرئيسية باسم main_luxury.png")

# 2. صفحة استوديو التصميم
elif st.session_state.current_page == "🎨 استوديو التصميم":
    st.markdown("<h1>استوديو التصميم الذكي عبر AI</h1>", unsafe_allow_html=True)
    prompt = st.text_area("✍️ صِف السجادة التي تحلم بها بالتفصيل للذكاء الاصطناعي:")
    uploaded_file = st.file_uploader("🖼️ أو ارفع صورة نمطية للإلهام:", type=["jpg", "png", "jpeg"])
    st.markdown('<div class="order-btn-box">', unsafe_allow_html=True)
    if st.button("✨ ابدأ التوليد الفاخر"):
        st.warning("🔄 يتم الآن تحليل النمط والنقوش الموصوفة...")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. صفحة نسيج (الخامات)
elif st.session_state.current_page == "🧶 نسيج (الخامات)":
    st.markdown("<h1>خامات النسيج الفاخرة</h1>", unsafe_allow_html=True)
    col_mat1, col_mat2 = st.columns(2)
    with col_mat1:
        st.markdown("<div class='luxury-card'><div class='design-title'>🧶 صوف نيوزيلندي فاخر</div><p>أقوى وأمتن أنواع الصوف الطبيعي للحفاظ على رونق الألوان ونعومة النسيج.</p></div>", unsafe_allow_html=True)
    with col_mat2:
        st.markdown("<div class='luxury-card'><div class='design-title'>✨ الحرير الطبيعي مائة بالمائة</div><p>لمعان ملكي فاخر تتغير تموجاته الساحرة بنعومة بالغة مع زوايا الإضاءة.</p></div>", unsafe_allow_html=True)

# 4. صفحة الكاتلوج الفاخر (روابط الصور الفردية الصحيحة والمباشرة لتفادي الاختفاء)
elif st.session_state.current_page == "📚 الكاتلوج الفاخر":
    st.markdown("<h1>مجموعة التصاميم الحصرية للسجاد الفخم</h1>", unsafe_allow_html=True)
    
    catalog_img = find_local_image("catalog_dashboard")
    if catalog_img:
        st.image(catalog_img, use_container_width=True)
        
    st.markdown("<br><h3>🎯 تصفح اللوحات الفردية للإنتاج المباشر</h3>", unsafe_allow_html=True)
    
    # روابط الصور الخام الثابتة مباشرة لضمان التحميل الفوري في الكاتلوج الفردي
    individual_designs = [
        {"title": "ملحمة الشموخ", "desc": "حصان عربي أصيل بتصميم ثلاثي الأبعاد فخم.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_06_00%20%D9%85.png"},
        {"title": "الصقر الملكي", "desc": "صقر عربي ذهبي يتوسط خلفية سوداء داكنة هيبة وأصالة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_10_16%20%D9%85.png"},
        {"title": "نور المحراب", "desc": "زخارف إسلامية مستوحاة من روعة المساجد الأندلسية العريقة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_33_04%20%D9%85.png"},
        {"title": "تراث نجد", "desc": "نقوش هندسية أصيلة تدمج عراقة الماضي بفخامة الحاضر.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_29_59%20%D9%85.png"},
        {"title": "سفينة الصحراء", "desc": "لوحة الأصالة العربية المتمثلة في الجمل مع خلفية القلاع العريقة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_37_19%20%D9%85.png"},
        {"title": "المجلس الملكي", "desc": "تصميم فاخر جداً مخصص للقصور والمجالس الرسمية الكبرى والأنيقة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_34_59%20%D9%85.png"}
    ]
    
    col1, col2 = st.columns(2)
    st.markdown('<div class="order-btn-box">', unsafe_allow_html=True)
    for index, d in enumerate(individual_designs):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            st.markdown(f"<div class='luxury-card'><div class='design-title'>{d['title']}</div><p>{d['desc']}</p></div>", unsafe_allow_html=True)
            st.image(d['url'], use_container_width=True)
            if st.button(f"🛒 طلب إنتاج {d['title']}", key=f"prod_{index}"):
                st.success(f"👑 تم تسجيل طلبك لتصميم {d['title']} بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. صفحة التسعير الفوري
elif st.session_state.current_page == "💰 التسعير الفوري":
    st.markdown("<h1>حاسبة التسعير الفوري والذكي</h1>", unsafe_allow_html=True)
    length = st.number_input("📏 طول السجادة (متر):", min_value=1.0, value=3.0)
    width = st.number_input("📐 عرض السجادة (متر):", min_value=1.0, value=2.0)
    st.markdown('<div class="order-btn-box">', unsafe_allow_html=True)
    if st.button("🧮 احسب التكلفة التقديرية"):
        st.success(f"السعر التقديري الحصري: {length * width * 500:,.2f} ريال سعودي")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. صفحة التواصل والطلب
elif st.session_state.current_page == "📞 التواصل والطلب":
    st.markdown("<h1>قنوات التواصل والطلب المباشر</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'><p>📍 المقر الرئيسي: الرياض، حي السليمانية</p><p>👑 استوديو نسيج - فخامة تليق بمساحتك الملكية</p></div>", unsafe_allow_html=True)
        
