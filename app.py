import streamlit as st
import os

# 1. تهيئة الصفحة وإعدادات العرض
st.set_page_config(
    page_title="استوديو نسيج الفاخر - NASIJ STUDIO",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تصميم الواجهة باللون الأسود والذهبي الملكي
st.markdown("""
    <style>
    .stApp {
        background-color: #0B0B0C !important;
        color: #E5E5E5 !important;
    }
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        font-family: 'Cairo', sans-serif;
        text-align: center;
        font-weight: 700;
    }
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
        min-height: 55px;
    }
    .stButton>button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 8px !important;
        width: 100%;
        padding: 10px 20px !important;
        font-weight: bold !important;
    }
    .stButton>button:hover {
        background-color: #D4AF37 !important;
        color: #0B0B0C !important;
    }
    [data-testid="stSidebar"] {
        background-color: #0D0D0F !important;
        border-left: 1px solid #262629 !important;
    }
    </style>
""", unsafe_allow_html=True)

# دالة ذكية للبحث عن الصورة بالاسم المكرر أو المفرد لتفادي المشكلة تماماً
def get_image_file(base_name):
    possible_names = [f"{base_name}.png", f"{base_name}.png.png", f"{base_name}.jpg", f"{base_name}.jpeg"]
    for name in possible_names:
        if os.path.exists(name):
            return name
    return None

# 3. شريط التنقل الجانبي
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>👑 استوديو نسيج</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 12px;'>NASIJ STUDIO • PREMIUM</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    choice = st.sidebar.radio(
        label="اختر الوجهة:",
        options=["🏠 الرئيسية", "🎨 استوديو التصميم الذكي", "🧶 نسيج (الخامات)", "📚 الكاتلوج الفاخر", "💰 التسعير الفوري", "📞 التواصل والطلب"],
        label_visibility="collapsed"
    )

# ==================== صفحة الرئيسية ====================
if choice == "🏠 الرئيسية":
    st.markdown("<h1>منصة تصميم السجاد الذكية</h1>", unsafe_allow_html=True)
    
    main_img = get_image_file("main_luxury")
    if main_img:
        st.image(main_img, use_container_width=True)
    else:
        st.warning("⚠️ يرجى رفع صورة الواجهة الرئيسية إلى الـ GitHub.")

# ==================== صفحة استوديو التصميم الذكي ====================
elif choice == "🎨 استوديو التصميم الذكي":
    st.markdown("<h1>استوديو التصميم الذكي عبر AI</h1>", unsafe_allow_html=True)
    prompt = st.text_area("✍️ صِف السجادة التي تحلم بها:")
    uploaded_file = st.file_uploader("🖼️ أو ارفع صورة للإلهام:", type=["jpg", "png", "jpeg"])
    if st.button("✨ توليد التصميم الفاخر"):
        st.warning("🔄 يتم الآن تحليل النمط وتوليد عينات نسيجية...")

# ==================== صفحة نسيج (الخامات) ====================
elif choice == "🧶 نسيج (الخامات)":
    st.markdown("<h1>خامات النسيج الفاخرة</h1>", unsafe_allow_html=True)
    col_mat1, col_mat2 = st.columns(2)
    with col_mat1:
        st.markdown("<div class='luxury-card'><div class='design-title'>🧶 صوف نيوزيلندي فاخر</div><div class='design-desc'>أقوى أنواع الصوف الطبيعي ويحافظ على بريق الألوان.</div></div>", unsafe_allow_html=True)
    with col_mat2:
        st.markdown("<div class='luxury-card'><div class='design-title'>✨ الحرير الطبيعي</div><div class='design-desc'>يعطي لمعاناً ساحراً يتغير مع زوايا الإضاءة.</div></div>", unsafe_allow_html=True)

# ==================== صفحة الكاتلوج الفاخر ====================
elif choice == "📚 الكاتلوج الفاخر":
    st.markdown("<h1>مجموعة التصاميم الحصرية للسجاد الفخم</h1>", unsafe_allow_html=True)
    
    catalog_img = get_image_file("catalog_dashboard")
    if catalog_img:
        st.image(catalog_img, use_container_width=True)
    else:
        st.warning("⚠️ يرجى رفع صورة لوحة الكاتلوج إلى الـ GitHub.")
        
    st.markdown("<h3>🎯 تصفح اللوحات الفردية للإنتاج المباشر</h3>", unsafe_allow_html=True)
    
    # قائمة المنتجات والصور الفردية الرائعة التي أرسلتها
    individual_designs = [
        {"title": "ملحمة الشموخ", "desc": "حصان عربي أصيل يجسد القوة والحرية بتصميم ثلاثي الأبعاد.", "file": "horse"},
        {"title": "الصقر الملكي", "desc": "صقر عربي ذهبي يتوسط خلفية سوداء داكنة تعبر عن الأصالة والهيبة.", "file": "falcon"},
        {"title": "نور المحراب", "desc": "زخارف إسلامية مستوحاة من روعة العمارة الأندلسية والمساجد التاريخية.", "file": "mihrab"},
        {"title": "تراث نجد", "desc": "نقوش نجدية هندسية أصيلة تدمج عراقة الماضي بفخامة الحاضر.", "file": "najd"},
        {"title": "سفينة الصحراء", "desc": "لوحة الأصالة العربية المتمثلة في الجمل مع خلفية القلاع العريقة ووقت الغروب الساحر.", "file": "camel"},
        {"title": "المجلس الملكي", "desc": "تصميم فاخر جداً مخصص للقصور والمجالس الرسمية بأعلى درجات الفخامة.", "file": "majlis"}
    ]
    
    col1, col2 = st.columns(2)
    for index, d in enumerate(individual_designs):
        current_col = col1 if index % 2 == 0 else col2
        with current_col:
            st.markdown(f"<div class='luxury-card'><div class='design-title'>{d['title']}</div><div class='design-desc'>{d['desc']}</div></div>", unsafe_allow_html=True)
            img_file = get_image_file(d['file'])
            if img_file:
                st.image(img_file, use_container_width=True)
            else:
                st.caption(f"ℹ️ ارفع صورة لـ {d['title']} باسم '{d['file']}' لتظهر هنا بصورتها الفردية.")
            if st.button(f"🛒 طلب إنتاج {d['title']}", key=f"prod_{index}"):
                st.success(f"👑 تم تسجيل طلبك لتصميم {d['title']}!")

# ==================== صفحة التسعير الفوري ====================
elif choice == "💰 التسعير الفوري":
    st.markdown("<h1>حاسبة التسعير الفوري والذكي</h1>", unsafe_allow_html=True)
    length = st.number_input("📏 طول السجادة (متر):", min_value=1.0, value=3.0)
    width = st.number_input("📐 عرض السجادة (متر):", min_value=1.0, value=2.0)
    if st.button("🧮 احسب التكلفة"):
        st.markdown(f"<div style='text-align:center;'><h3>التكلفة التقديرية: {length * width * 500:,.2f} ريال سعودي</h3></div>", unsafe_allow_html=True)

# ==================== صفحة التواصل والطلب ====================
elif choice == "📞 التواصل والطلب":
    st.markdown("<h1>قنوات التواصل والطلب المباشر</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'><p>📍 المقر الرئيسي: الرياض، المملكة العربية السعودية</p><p>📞 رقم خدمة العملاء: 9200XXXXX</p></div>", unsafe_allow_html=True)
    
