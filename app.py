import streamlit as st
import os

# 1. تهيئة الصفحة
st.set_page_config(
    page_title="استوديو نسيج الفاخر - NASIJ STUDIO",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# إدارة الصفحات (تأخذ القيمة من الروابط المخصصة)
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 الرئيسية"

# تفعيل التنقل عند الضغط على أزرار القائمة الجانبية المخصصة
query_params = st.query_params
if "p" in query_params:
    st.session_state.current_page = query_params["p"]

# 2. هندسة الواجهة البرمجية بالـ CSS لمنع ظهور أي تشوهات وتحقيق الشفافية للأزرار
st.markdown("""
    <style>
    /* تصفير الخلفيات والخطوط لتطابق الهوية */
    .stApp {
        background-color: #0B0B0C !important;
        color: #E5E5E5 !important;
        font-family: 'Cairo', sans-serif;
    }
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        text-align: center;
        font-weight: 700;
    }
    
    /* إخفاء شريط التنقل الجانبي الافتراضي البشع لستريمليت بالكامل */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    [data-testid="stSidebar"] {
        background-color: #0B0B0C !important;
        border-right: 1px solid #D4AF37 !important;
    }

    /* تصميم القائمة الجانبية الفاخرة المطلوبة */
    .custom-sidebar {
        padding: 10px;
        text-align: right;
    }
    .sidebar-item {
        display: block;
        padding: 12px 15px;
        color: #B3B3B3;
        text-decoration: none;
        font-size: 16px;
        margin-bottom: 8px;
        border-radius: 6px;
        transition: all 0.3s ease;
    }
    .sidebar-item:hover, .sidebar-item.active {
        color: #D4AF37 !important;
        background-color: rgba(212, 175, 55, 0.08);
        box-shadow: inset 4px 0px 0px #D4AF37;
        padding-right: 22px;
    }
    
    /* تصميم صندوق مستشار التصميم أسفل القائمة */
    .sidebar-advisor {
        border: 1px solid #D4AF37;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        background-color: #121214;
        margin-top: 50px;
    }

    /* === الفكرة العبقرية: الأزرار الشفافة التفاعلية فوق الصورة الرئيسية === */
    .image-container {
        position: relative;
        width: 100%;
        max-width: 500px; /* العرض التقريبي المتناسق للهواتف */
        margin: 0 auto;
    }
    .image-container img {
        width: 100%;
        display: block;
    }
    
    /* جعل أزرار ستريمليت المدمجة هنا شفافة بالكامل وغير مرئية وتطفو فوق أزرار الصورة */
    .transparent-btn-1 div, .transparent-btn-2 div {
        position: absolute;
        width: 80% !important;
        left: 10%;
        height: 50px;
        opacity: 0.01; /* شفافة تماماً ولا ترى بالعين المجردة */
    }
    /* زر ابدأ التصميم (يقع تقريباً في النصف السفلي من الصورة) */
    .transparent-btn-1 div {
        bottom: 22%;
    }
    /* زر استعرض الكاتلوج (يقع أسفله مباشرة) */
    .transparent-btn-2 div {
        bottom: 12%;
    }
    
    /* تنسيق كروت الكاتلوج */
    .luxury-card {
        background-color: #121214;
        border: 1px solid #D4AF37;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        text-align: center;
    }
    .design-title {
        font-size: 20px;
        font-weight: bold;
        color: #D4AF37;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# دالة فحص أسماء الصور المحلية
def get_image_file(base_name):
    possible_names = [f"{base_name}.png", f"{base_name}.png.png", f"{base_name}.jpg", f"{base_name}.jpeg"]
    for name in possible_names:
        if os.path.exists(name):
            return name
    return None

# ==================== بناء الشريط الجانبي المطابق للتصميم تماماً ====================
with st.sidebar:
    st.markdown("<h2 style='margin-bottom: 0;'>👑 N</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 18px; margin-top: 5px; margin-bottom: 0;'>NASIJ STUDIO</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 10px; letter-spacing: 2px;'>SMART CARPET DESIGN</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # القائمة الجانبية الفاخرة بـ HTML نقي متصل برابط لتغيير الصفحة
    pages_definition = [
        {"name": "🏠 الرئيسية", "slug": "🏠 الرئيسية"},
        {"name": "🎨 استوديو التصميم", "slug": "🎨 استوديو التصميم"},
        {"name": "🧶 نسيج (الخامات)", "slug": "🧶 نسيج (الخامات)"},
        {"name": "📚 الكاتلوج الفاخر", "slug": "📚 الكاتلوج الفاخر"},
        {"name": "💰 التسعير الفوري", "slug": "💰 التسعير الفوري"},
        {"name": "📞 التواصل والطلب", "slug": "📞 التواصل والطلب"}
    ]
    
    st.markdown('<div class="custom-sidebar">', unsafe_allow_html=True)
    for p in pages_definition:
        active_class = "active" if st.session_state.current_page == p['slug'] else ""
        # استخدام روابط الجلسة لتغيير الحالة البرمجية بسلاسة عند الضغط
        if st.button(p['name'], key=f"side_{p['slug']}", use_container_width=True):
            st.session_state.current_page = p['slug']
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # صندوق مستشار التصميم
    st.markdown("""
        <div class="sidebar-advisor">
            <div style="font-size: 24px; color: #D4AF37;">🎧</div>
            <div style="color: #D4AF37; font-size: 15px; font-weight: bold; margin-top: 5px;">مستشار التصميم</div>
            <div style="color: #888; font-size: 11px; line-height: 1.4;">متاح لمساعدتك في اختيار أفضل تصميم لمساحتك.</div>
        </div>
    """, unsafe_allow_html=True)


# ==================== منطق عرض الصفحات ====================

# 1. صفحة الرئيسية (تفعيل الأزرار المدمجة داخل الصورة)
if st.session_state.current_page == "🏠 الرئيسية":
    st.markdown("<h1>منصة تصميم السجاد الذكية</h1>", unsafe_allow_html=True)
    
    main_img = get_image_file("main_luxury")
    if main_img:
        # إنشاء الحاوية التي تدمج الصورة مع الأزرار الشفافة فوقها بالضبط
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(main_img, use_container_width=True)
        
        # الزر الشفاف الأول: يركب فوق زر "ابتدئ بالتصميم" المدمج في الصورة
        st.markdown('<div class="transparent-btn-1">', unsafe_allow_html=True)
        if st.button("تفعيل زر التصميم المدمج", key="hidden_btn_design"):
            st.session_state.current_page = "🎨 استوديو التصميم"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # الزر الشفاف الثاني: يركب فوق زر "ويب كاتلوج" المدمج في الصورة
        st.markdown('<div class="transparent-btn-2">', unsafe_allow_html=True)
        if st.button("تفعيل زر الكاتلوج المدمج", key="hidden_btn_catalog"):
            st.session_state.current_page = "📚 الكاتلوج الفاخر"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("⚠️ لم يتم العثور على صورة الواجهة الرئيسية باسم main_luxury.png")

# 2. صفحة استوديو التصميم
elif st.session_state.current_page == "🎨 استوديو التصميم":
    st.markdown("<h1>استوديو التصميم الذكي عبر AI</h1>", unsafe_allow_html=True)
    prompt = st.text_area("✍️ صِف السجادة التي تحلم بها:")
    uploaded_file = st.file_uploader("🖼️ أو ارفع صورة للإلهام:", type=["jpg", "png", "jpeg"])
    if st.button("✨ توليد التصميم الفاخر"):
        st.warning("🔄 يتم الآن تحليل النمط وتوليد عينات نسيجية...")

# 3. صفحة نسيج (الخامات)
elif st.session_state.current_page == "🧶 نسيج (الخامات)":
    st.markdown("<h1>خامات النسيج الفاخرة</h1>", unsafe_allow_html=True)
    col_mat1, col_mat2 = st.columns(2)
    with col_mat1:
        st.markdown("<div class='luxury-card'><div class='design-title'>🧶 صوف نيوزيلندي فاخر</div><p>أقوى أنواع الصوف الطبيعي للحفاظ على بريق الألوان.</p></div>", unsafe_allow_html=True)
    with col_mat2:
        st.markdown("<div class='luxury-card'><div class='design-title'>✨ الحرير الطبيعي</div><p>لمعان ملكي يتغير بنعومة مع زوايا الإضاءة.</p></div>", unsafe_allow_html=True)

# 4. صفحة الكاتلوج الفاخر (روابط الصور الفردية الصحيحة والمباشرة)
elif st.session_state.current_page == "📚 الكاتلوج الفاخر":
    st.markdown("<h1>مجموعة التصاميم الحصرية للسجاد الفخم</h1>", unsafe_allow_html=True)
    
    catalog_img = get_image_file("catalog_dashboard")
    if catalog_img:
        st.image(catalog_img, use_container_width=True)
        
    st.markdown("<br><h3>🎯 تصفح اللوحات الفردية للإنتاج المباشر</h3>", unsafe_allow_html=True)
    
    # الروابط المباشرة الخام الصحيحة بنسبة 100% لضمان العرض الفوري
    individual_designs = [
        {"title": "ملحمة الشموخ", "desc": "حصان عربي أصيل بتصميم ثلاثي الأبعاد وغبار متطاير فخم.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_06_00%20%D9%85.png"},
        {"title": "الصقر الملكي", "desc": "صقر عربي ذهبي يتوسط خلفية سوداء داكنة هيبة وأصالة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_10_16%20%D9%85.png"},
        {"title": "نور المحراب", "desc": "زخارف إسلامية مستوحاة من روعة العمارة الأندلسية والمساجد.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_33_04%20%D9%85.png"},
        {"title": "تراث نجد", "desc": "نقوش هندسية أصيلة تدمج عراقة الماضي بفخامة الحاضر الساحر.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_29_59%20%D9%85.png"},
        {"title": "سفينة الصحراء", "desc": "لوحة الأصالة العربية المتمثلة في الجمل مع خلفية القلاع العريقة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_37_19%20%D9%85.png"},
        {"title": "المجلس الملكي", "desc": "تصميم فاخر جداً مخصص للقصور والمجالس الرسمية الكبرى والأنيقة.", "url": "https://raw.githubusercontent.com/Sedeq123/-4/main/ChatGPT%20Image%207%20%D9%AA%D9%A0%D9%A2%D9%A6%D8%8C%2007_34_59%20%D9%85.png"}
    ]
    
    col1, col2 = st.columns(2)
    for index, d in enumerate(individual_designs):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            st.markdown(f"<div class='luxury-card'><div class='design-title'>{d['title']}</div><p>{d['desc']}</p></div>", unsafe_allow_html=True)
            # عرض الصورة مباشرة عبر الروابط الثابتة من المستودع
            st.image(d['url'], use_container_width=True)
            if st.button(f"🛒 طلب إنتاج {d['title']}", key=f"prod_{index}"):
                st.success(f"👑 تم تسجيل طلبك لتصميم {d['title']}!")

# 5. صفحة التسعير الفوري
elif st.session_state.current_page == "💰 التسعير الفوري":
    st.markdown("<h1>حاسبة التسعير الفوري والذكي</h1>", unsafe_allow_html=True)
    length = st.number_input("📏 طول السجادة (متر):", min_value=1.0, value=3.0)
    width = st.number_input("📐 عرض السجادة (متر):", min_value=1.0, value=2.0)
    if st.button("🧮 احسب التكلفة التقديرية"):
        st.success(f"السعر التقديري الحصري: {length * width * 500:,.2f} ريال سعودي")

# 6. صفحة التواصل والطلب
elif st.session_state.current_page == "📞 التواصل والطلب":
    st.markdown("<h1>قنوات التواصل والطلب المباشر</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'><p>📍 المقر الرئيسي: الرياض، حي السليمانية</p><p>👑 استوديو نسيج - فخامة تليق بمساحتك الملكية</p></div>", unsafe_allow_html=True)
    
