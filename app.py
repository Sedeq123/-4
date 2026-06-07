import streamlit as st
import os

# 1. تهيئة الصفحة وإعدادات العرض الشاملة
st.set_page_config(
    page_title="استوديو نسيج الفاخر - NASIJ STUDIO",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. حقن الـ CSS المخصص لتحويل التطبيق بالكامل إلى هوية "الأسود والذهبي الفاخر"
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق بالكامل وشريط التمرير */
    .stApp {
        background-color: #0B0B0C !important;
        color: #E5E5E5 !important;
    }
    
    /* تنسيق العناوين بالذهبي الملكي وخط مميز */
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        font-family: 'Cairo', sans-serif;
        text-align: center;
        font-weight: 700;
    }
    
    /* تصميم بطاقات الخامات والأقسام الأخرى */
    .luxury-card {
        background-color: #121214;
        border: 1px solid #D4AF37;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .luxury-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 6px 22px rgba(212, 175, 55, 0.18);
    }
    
    .design-title {
        font-size: 20px;
        font-weight: bold;
        color: #D4AF37;
        margin-top: 15px;
        margin-bottom: 8px;
        font-family: 'Cairo', sans-serif;
    }
    .design-desc {
        font-size: 14px;
        color: #B3B3B3;
        line-height: 1.6;
        font-family: 'Cairo', sans-serif;
    }
    
    /* تخصيص أزرار الـ Streamlit لتصبح ذهبية ملكية */
    .stButton>button {
        background-color: transparent !important;
        color: #D4AF37 !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 8px !important;
        width: 100%;
        padding: 10px 20px !important;
        font-weight: bold !important;
        font-family: 'Cairo', sans-serif;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #D4AF37 !important;
        color: #0B0B0C !important;
        border: 1px solid #D4AF37 !important;
        box-shadow: 0px 0px 12px #D4AF37 !important;
    }
    
    /* تخصيص شريط القائمة الجانبية بالكامل */
    [data-testid="stSidebar"] {
        background-color: #0D0D0F !important;
        border-left: 1px solid #262629 !important;
    }
    
    /* تخصيص نصوص الراديو والقوائم الجانبية */
    .stRadio > label {
        color: #D4AF37 !important;
        font-family: 'Cairo', sans-serif;
        font-weight: bold;
    }
    
    /* تصميم الصناديق النصية والحقول */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #121214 !important;
        color: #FFFFFF !important;
        border: 1px solid #262629 !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)


# 3. شريط التنقل الجانبي (Sidebar)
with st.sidebar:
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>👑 استوديو نسيج</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 12px; letter-spacing: 1px;'>NASIJ STUDIO • PREMIUM</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 📍 لوحة التحكم والمنصة")
    choice = st.radio(
        label="اختر الوجهة:",
        options=[
            "🏠 الرئيسية", 
            "🎨 استوديو التصميم الذكي", 
            "🧶 نسيج (الخامات)", 
            "📚 الكاتلوج الفاخر", 
            "💰 التسعير الفوري", 
            "📞 التواصل والطلب"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
        <div style="border: 1px solid #D4AF37; padding: 15px; border-radius: 8px; background-color: #121214; text-align: center;">
            <p style="color: #D4AF37; font-weight: bold; margin-bottom: 5px;">🎧 مستشار التصميم</p>
            <p style="color: #888; font-size: 12px; margin-bottom: 0;">متاح لمساعدتك في اختيار أفضل نسيج وتصميم لمساحتك.</p>
        </div>
    """, unsafe_allow_html=True)


# ==================== صفحة الرئيسية ====================
if choice == "🏠 الرئيسية":
    st.markdown("<h1>منصة تصميم السجاد الذكية</h1>", unsafe_allow_html=True)
    
    # إضافة الصورة المرجعية الأولى المتمثلة في ChatGPT Image 7 يونيو 2026، 06_56_49 م.png
    main_image_path = "main_luxury.png"
    if os.path.exists(main_image_path):
        st.image(main_image_path, use_column_width=True)
    else:
        st.warning("⚠️ يرجى التأكد من وضع صورة الواجهة الرئيسية باسم 'main_luxury.png' في مجلد المشروع لتظهر هنا.")
        
    st.markdown("<p style='text-align:center; color:#B3B3B3; font-size:16px; margin-top: 20px;'>مرحباً بك في عالم الفخامة الرقمية. صمم سجادتك الفريدة من فكرة أو تصفح المجموعات المتاحة فوراً.</p>", unsafe_allow_html=True)


# ==================== صفحة استوديو التصميم الذكي ====================
elif choice == "🎨 استوديو التصميم الذكي":
    st.markdown("<h1>استوديو التصميم الذكي عبر AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>اكتب فكرتك أو ارفع نمطاً معيناً ليقوم الذكاء الاصطناعي بنسج ملامح لوحتك القادمة</p>", unsafe_allow_html=True)
    
    prompt = st.text_area("✍️ صِف السجادة التي تحلم بها (مثال: نقش أندلسي بخيوط ذهبية وخلفية ملكية سوداء):")
    uploaded_file = st.file_uploader("🖼️ أو ارفع صورة للإلهام أو النمط المراد محاكاته (Pattern):", type=["jpg", "png", "jpeg"])
    
    if st.button("✨ توليد التصميم الفاخر"):
        if prompt or uploaded_file:
            st.warning("🔄 يتم الآن تحليل النمط وتوليد عينات نسيجية عالية الدقة... (هذه ميزة تجريبية متصلة بالـ AI)")
        else:
            st.error("الرجاء كتابة وصف أو رفع صورة أولاً لكي نتمكن من بدء محاكاة التصميم.")


# ==================== صفحة نسيج (الخامات) ====================
elif choice == "🧶 نسيج (الخامات)":
    st.markdown("<h1>خامات النسيج الفاخرة</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>جودة النسيج هي أساس الفخامة؛ نعتمد أرقى الخامات العالمية المستدامة</p>", unsafe_allow_html=True)
    
    col_mat1, col_mat2 = st.columns(2)
    with col_mat1:
        st.markdown("""
            <div class='luxury-card'>
                <div class='design-title'>🧶 صوف نيوزيلندي فاخر</div>
                <div class='design-desc'>أقوى أنواع الصوف الطبيعي، يتميز بمقاومته العالية للبقع وقدرته الاستثنائية على الحفاظ على بريق الألوان الذهبية والداكنة عبر السنين.</div>
            </div>
        """, unsafe_allow_html=True)
    with col_mat2:
        st.markdown("""
            <div class='luxury-card'>
                <div class='design-title'>✨ الحرير الطبيعي والمدمج</div>
                <div class='design-desc'>يعطي لمعاناً ساحراً يتغير مع زوايا الإضاءة في المجالس والقصور، مثالي جداً لتبريز التفاصيل الدقيقة مثل الخطوط والنقوش الملكية.</div>
            </div>
        """, unsafe_allow_html=True)


# ==================== صفحة الكاتلوج الفاخر (المطورة بناءً على طلبك الجديد) ====================
elif choice == "📚 الكاتلوج الفاخر":
    st.markdown("<h1>مجموعة التصاميم الحصرية للسجاد الفخم</h1>", unsafe_allow_html=True)
    
    # إضافة الصورة المرجعية الثانية المتمثلة في ChatGPT Image 7 يونيو 2026، 07_02_34 م_2.png
    catalog_image_path = "catalog_dashboard.png"
    if os.path.exists(catalog_image_path):
        st.image(catalog_image_path, use_column_width=True)
    else:
        st.warning("⚠️ يرجى التأكد من وضع صورة لوحة الكاتلوج باسم 'catalog_dashboard.png' في مجلد المشروع لتظهر هنا بكامل فخامتها.")
        
    st.markdown("<p style='text-align:center; color:#888; margin-top:20px;'>* للطلبات الخاصة أو التعديل على أحد التصاميم المعروضة أعلاه، يمكنك الانتقال مباشرة لقسم التواصل والطلب أو استخدام نموذج التسعير الفوري.</p>", unsafe_allow_html=True)


# ==================== صفحة التسعير الفوري ====================
elif choice == "💰 التسعير الفوري":
    st.markdown("<h1>حاسبة التسعير الفوري والذكي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>احسب التكلفة التقديرية لسجادتك المخصصة فوراً بناءً على الأبعاد ونوع النسيج</p>", unsafe_allow_html=True)
    
    st.write("")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        length = st.number_input("📏 طول السجادة المطلوبة (بالمتر):", min_value=1.0, max_value=20.0, value=3.0, step=0.5)
        width = st.number_input("📐 عرض السجادة المطلوبة (بالمتر):", min_value=1.0, max_value=20.0, value=2.0, step=0.5)
    with col_p2:
        material_type = st.selectbox("🧵 اختر نوع الخامة والنسيج الأساسي:", ["صوف نيوزيلندي فاخر", "حرير طبيعي دقيق", "دمج صوف وحرير فاخر"])
        density = st.selectbox("💎 دقة وكثافة العقد في المتر المربع:", ["معيارية كلاسيكية", "عالية الكثافة (ملكي فخم)"])
        
    if st.button("🧮 احسب التكلفة التقديرية الحالية"):
        area = length * width
        base_price_per_meter = 450 if "صوف" in material_type else 800
        if "ملكي" in density: base_price_per_meter += 250
        
        total_estimation = area * base_price_per_meter
        
        st.markdown(f"""
            <div style="border: 1px dashed #D4AF37; background-color: #121214; padding: 20px; border-radius: 8px; text-align: center; margin-top: 20px;">
                <p style="color: #888; margin-bottom: 5px;">المساحة الإجمالية: {area:.2f} متر مربع</p>
                <h3 style="margin: 0; color: #D4AF37;">السعر التقديري الحصري: {total_estimation:,.2f} ريال سعودي</h3>
                <p style="color: #666; font-size: 11px; margin-top: 8px;">* الأسعار تشمل التوصيل الفاخر المجاني وضمان الجودة الممتد لـ 5 سنوات</p>
            </div>
        """, unsafe_allow_html=True)


# ==================== صفحة التواصل والطلب ====================
elif choice == "📞 التواصل والطلب":
    st.markdown("<h1>قنوات التواصل والطلب المباشر</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="max-width: 600px; margin: 0 auto; background-color: #121214; border: 1px solid #262629; padding: 30px; border-radius: 12px; text-align: center;">
            <p style="color: #D4AF37; font-size: 24px; font-weight: bold; margin-bottom: 20px;">👑 خيارات الدعم والمتابعة الملكية</p>
            <p style="color: #B3B3B3; margin-bottom: 15px;">📍 <b>المقر الرئيسي:</b> الرياض، حي السليمانية، المملكة العربية السعودية</p>
            <p style="color: #B3B3B3; margin-bottom: 15px;">📞 <b>رقم خدمة العملاء:</b> 9200XXXXX</p>
            <p style="color: #B3B3B3; margin-bottom: 25px;">✉️ <b>البريد الإلكتروني المباشر:</b> premium@nasij.studio</p>
            <hr style="border-color: #262629;">
            <p style="color: #888; font-size: 13px; margin-top: 20px;">✨ دعم فني ومتابعة دقيقة على مدار الساعة طوال أيام الأسبوع لضمان مطابقة أدق تفاصيل النسيج المطلوبة.</p>
        </div>
    """, unsafe_allow_html=True)
    
