import streamlit as st

# ==========================================
# 1. إعداد الصفحة وهوية المتصفح
# ==========================================
st.set_page_config(
    page_title="Nasij Studio | استوديو نسيج للسجاد الذكي",
    page_icon="🧶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. الهوية البصرية الفاخرة (CSS)
# ==========================================
st.markdown("""
<style>
    /* الخلفية العامة للمنصة */
    .stApp {
        background-color: #0B0B0B;
        color: #FFFFF0;
        font-family: 'Cairo', sans-serif;
    }
    
    /* العناوين الرئيسية والفرعية */
    h1, h2, h3, h4 {
        color: #D4AF37 !important;
        font-weight: 700;
        text-align: right;
    }
    
    /* القائمة الجانبية */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-left: 1px solid #D4AF37;
    }
    
    /* النصوص داخل القائمة الجانبية */
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] label {
        color: #FFFFF0 !important;
    }
    
    /* صناديق الإحصائيات والمقاييس */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #151922, #0B0B0B);
        border: 1px solid #D4AF37;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.1);
        text-align: center;
    }
    div[data-testid="stMetricValue"] {
        color: #D4AF37 !important;
        font-size: 28px !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #FFFFF0 !important;
    }

    /* تحسين مظهر الأزرار */
    .stButton > button {
        background: linear-gradient(135deg, #D4AF37, #AA820A) !important;
        color: #0B0B0B !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0px 5px 15px rgba(212, 175, 55, 0.4) !important;
        color: #FFFFF0 !important;
    }

    /* صناديق المنتجات والتصاميم */
    .product-card {
        background: #111827;
        border: 1px solid #1E293B;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        transition: border 0.3s ease;
    }
    .product-card:hover {
        border-color: #D4AF37;
    }
    
    /* قوائم الاختيار */
    div[data-testid="stRadio"] label {
        font-size: 16px !important;
        padding: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. قواعد البيانات والأسعار
# ==========================================
prices = {
    "بوليستر": 80,
    "نايلون": 120,
    "صوف": 220,
    "حرير": 450
}

# ==========================================
# 4. القائمة الجانبية والتنقل
# ==========================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0;">
        <h1 style="font-size: 28px; margin-bottom: 0;">🧶 استوديو نسيج</h1>
        <p style="color: #AA820A; font-size: 14px; letter-spacing: 1px;">NASIJ STUDIO • PREMIUM</p>
    </div>
    <hr style="border-color: #D4AF37;">
    """, unsafe_allow_html=True)
    
    page = st.radio(
        "لوحة التحكم والمنصة",
        [
            "🏠 الرئيسية",
            "🎨 استوديو التصميم الذكي",
            "🧶 نسيج (الخامات)",
            "📚 الكاتالوج الفاخر",
            "💰 التسعير الفوري",
            "⭐ مشاريع العملاء",
            "📞 التواصل والطلب"
        ]
    )

# ==========================================
# 5. صفحة: 🏠 الرئيسية
# ==========================================
if page == "🏠 الرئيسية":
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #0F172A, #0B0B0B);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid #D4AF37;
        text-align: center;
        margin-bottom: 30px;
    ">
        <h1 style="color: #D4AF37; font-size: 45px; margin-bottom: 10px;">🧶 NASIJ STUDIO</h1>
        <h3 style="color: #FFFFF0; font-size: 24px; margin-bottom: 15px;">منصة تصميم السجاد الذكية</h3>
        <p style="font-size: 18px; color: #E2E8F0; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            تحويل عملية تصميم السجاد من الطريقة التقليدية إلى تجربة رقمية فريدة مدعومة بالذكاء الاصطناعي. صمم سجادتك الفاخرة من صورة، وصف، أو فكرة.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_b1, col_b2, col_b3, col_b4 = st.columns(4)
    with col_b1:
        st.button("🚀 ابدأ التصميم الآن")
    with col_b2:
        st.button("📚 استعرض الكاتالوج")
    with col_b3:
        st.button("💰 احسب السعر فوراً")
    with col_b4:
        st.button("📞 تواصل معنا")

    st.write("")
    st.markdown("### 📊 إحصائيات منصة نسيج")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="عدد التصاميم الذكية", value="1,250 +")
    with c2:
        st.metric(label="المشاريع المنفذة", value="180 مشروع")
    with c3:
        st.metric(label="طلبات المصنع الحالية", value="340 طلب")
    with c4:
        st.metric(label="تقييم رضا العملاء", value="99.2%")

    st.write("")
    st.markdown("### ⭐ المجموعات الأكثر طلباً هذا الأسبوع")
    st.markdown("---")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.markdown("""
        <div class="product-card">
            <h4>👑 المجموعة الملكية</h4>
            <p style="color: #cccccc; font-size: 14px;">سجاد فاخر مخصص للقصور والمجالس الكبرى بنقوش ثلاثية الأبعاد وخيوط ذهبية.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_p2:
        st.markdown("""
        <div class="product-card">
            <h4>🏡 المجموعة المنزلية</h4>
            <p style="color: #cccccc; font-size: 14px;">تصاميم عصرية، ألوان رملية هادئة، ومناسبة جداً للشقق والمنازل الحديثة.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_p3:
        st.markdown("""
        <div class="product-card">
            <h4>🏢 مجموعة الشركات والفنادق</h4>
            <p style="color: #cccccc; font-size: 14px;">تحمل شعارات رسمية، وبمقاومة عالية جداً للاستخدام الكثيف وبأنماط هندسية فاخرة.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 6. صفحة: 🎨 استوديو التصميم الذكي
# ==========================================
elif page == "🎨 استوديو التصميم الذكي":
    st.title("🎨 استوديو المحاكاة والتصميم الذكي")
    st.write("ارفع صورتك الخاصة أو اكتب وصفاً دقيقاً، وسيتولى المحرك الذكي تجهيز طلبك للمصنع.")
    st.markdown("---")

    col_studio_left, col_studio_right = st.columns([2, 1])

    with col_studio_left:
        uploaded_file = st.file_uploader(
            "📷 ارفع صورة التصميم (مثال: صورة حصان، صقر، شعار شركة، صورة مجلس، صورة شخصية)",
            type=["jpg", "jpeg", "png"]
        )
        
        description = st.text_area(
            "✍️ وصف التصميم بدقة (الذكاء الاصطناعي)",
            placeholder="مثال: حصان عربي أصيل يجري على شاطئ البحر مع غبار ذهبي متطاير ونقوش نجدية على الأطراف..."
        )
        
        col_inputs = st.columns(2)
        with col_inputs[0]:
            style = st.selectbox("🎨 اختر النمط المراد", ["ملكـي", "عربـي", "نجـدي", "إسلامـي", "مودرن"])
            width = st.number_input("العرض المطلوب (متر)", min_value=1.0, value=3.0, step=0.5)
        with col_inputs[1]:
            material = st.selectbox("🧶 خامة السجادة المفضلة", list(prices.keys()))
            height = st.number_input("الطول المطلوب (متر)", min_value=1.0, value=4.0, step=0.5)

    with col_studio_right:
        st.markdown("""
        <div style="background: #0F172A; padding: 20px; border-radius: 15px; border: 1px dashed #D4AF37; text-align: center;">
            <h4 style="margin-top:0;">👁️ معاينة ملف الماستر</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if uploaded_file:
            st.image(uploaded_file, caption="الصورة المرفوعة من العميل", use_container_width=True)
        else:
            st.caption("في انتظار رفع صورة أو الضغط على زر التوليد الذكي لإنشاء النسخة الحقيقية مستقبلاً...")

    st.write("")
    if st.button("🚀 إنشاء وتوليد التصميم"):
        st.success("🎉 تم معالجة طلب التصميم وحساب التكلفة التقديرية فوراً بنجاح!")
        area = width * height
        cost = area * prices[material]
        
        st.markdown(f"""
        <div style="background: #111827; padding: 25px; border-radius:15px; border: 1px solid #22C55E; text-align: right; direction: rtl;">
            <h3 style="color: #22C55E !important; margin-top:0;">📄 ملخص بيانات الإنتاج الذكي لمشروعك</h3>
            <p><b>النمط المعتمد:</b> {style}</p>
            <p><b>الخامة المقترحة:</b> {material} (سعر المتر: {prices[material]} ريال)</p>
            <p><b>المقاس المحسوب:</b> {width} م × {height} م (المساحة الإجمالية: {area:.2f} متر مربع)</p>
            <h4 style="color: #D4AF37 !important;">💰 السعر الإجمالي الفوري للإنتاج: {cost:,.2f} ريال سعودي</h4>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 7. صفحة: 🧶 نسيج (الخامات)
# ==========================================
elif page == "🧶 نسيج (الخامات)":
    st.title("🧶 دليل الخامات والمقاسات الاحترافي")
    st.markdown("---")

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown(f"""
        <div class="product-card">
            <h3 style="margin-top:0;">🧶 خامة البوليستر الذكي</h3>
            <p style="color: #D4AF37; font-size: 20px; font-weight: bold;">{prices['بوليستر']} ريال / متر مربع</p>
            <p>خيار اقتصادي ممتاز، يمتاز بسهولة فائقة في التنظيف ومقاومة عالية للبقع، ومناسب جداً للاستخدام اليومي المتكرر والغرف العائلية.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_m2:
        st.markdown(f"""
        <div class="product-card">
            <h3 style="margin-top:0;">🧶 خامة النايلون المقوى</h3>
            <p style="color: #D4AF37; font-size: 20px; font-weight: bold;">{prices['نايلون']} ريال / متر مربع</p>
            <p>يتميز بقدرة تحمل جبارة جداً ضد الاحتكاك وضغط الأثاث، خيار استراتيجي للممرات والمكاتب والشركات ذات الحركة المستمرة.</p>
        </div>
        """, unsafe_allow_html=True)

    col_m3, col_m4 = st.columns(2)
    with col_m3:
        st.markdown(f"""
        <div class="product-card">
            <h3 style="margin-top:0;">🐑 خامة الصوف الطبيعي النقي</h3>
            <p style="color: #D4AF37; font-size: 20px; font-weight: bold;">{prices['صوف']} ريال / متر مربع</p>
            <p>فخامة لا تضاهى، عزل حراري وصوتي ممتاز، يعطي ملمساً دافئاً ومريحاً للغاية، وهو المفضل للمجالس الملكية التراثية.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_m4:
        st.markdown(f"""
        <div class="product-card">
            <h3 style="margin-top:0;">👑 خامة الحرير الفاخر</h3>
            <p style="color: #D4AF37; font-size: 20px; font-weight: bold;">{prices['حرير']} ريال / متر مربع</p>
            <p>قمة درجات الفخامة والأناقة. خيوط حريرية ناعمة ذات بريق ساحر تعكس الضوء لتبين أدق تفاصيل النقوش واللوحات الفنية ثلاثية الأبعاد.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 8. صفحة: 📚 الكاتالوج الفاخر
# ==========================================
elif page == "📚 الكاتالوج الفاخر":
    st.title("📚 كاتالوج نسيج الفاخر للإنتاج المباشر")
    st.markdown("---")

    tab_royal, tab_home, tab_kids, tab_corporate = st.tabs([
        "👑 المجموعة الملكية", 
        "🏡 المجموعة المنزلية", 
        "🧒 مجموعة الأطفال", 
        "🏢 مجموعة الشركات"
    ])

    with tab_royal:
        r_col1, r_col2 = st.columns(2)
        with r_col1:
            st.markdown("""
            <div class="product-card">
                <h4>1. ملحمة الشموخ (🏇)</h4>
                <p><b>الوصف:</b> حصان عربي أصيل يجري على شاطئ ذهبي برمال متحركة وغبار متطاير بتصميم فريد ثلاثي الأبعاد يعطي إيحاءً بالحركة.</p>
            </div>
            <div class="product-card">
                <h4>2. الصقر الملكي (🦅)</h4>
                <p><b>الوصف:</b> صقر عربي ذهبي يتوسط خلفية سوداء داكنة محاط بزخارف ملكية دقيقة تعبر عن الأصالة والقوة.</p>
            </div>
            <div class="product-card">
                <h4>3. نور المحراب (🕌)</h4>
                <p><b>الوصف:</b> زخارف إسلامية متداخلة مستوحاة من القباب والمآذن مع هلال ذهبي مشع بطابع روحاني وإضاءة فاخرة.</p>
            </div>
            """, unsafe_allow_html=True)
            
        with r_col2:
            st.markdown("""
            <div class="product-card">
                <h4>4. المجلس الملكي (👑)</h4>
                <p><b>الوصف:</b> سجادة متكاملة تحاكي فخامة الثريات والزخارف الذهبية للقصور، صممت لتفرش بالكامل للمجالس الواسعة.</p>
            </div>
            <div class="product-card">
                <h4>5. تراث نجد (🏜️)</h4>
                <p><b>الوصف:</b> نقوش نجدية أصيلة مستوحاة من الأبواب التراثية والبيوت الطينية بألوان صحراوية دافئة تجسد الهوية السعودية.</p>
            </div>
            <div class="product-card">
                <h4>6. جمل الصحراء (🐪)</h4>
                <p><b>الوصف:</b> جمل عربي مزخرف يسير في صحراء ذهبية واسعة وخلفه خيمة عربية تقليدية وقت الغروب الفاخر.</p>
            </div>
            """, unsafe_allow_html=True)

    with tab_home:
        h_col1, h_col2 = st.columns(2)
        with h_col1:
            st.markdown("""
            <div class="product-card">
                <h4>7. أمواج الرمال</h4>
                <p>تموجات هادئة بألوان بيج ورملية متناسقة، تصميم اقتصادي وعملي يتماشى مع أثاث الصالات الحديثة.</p>
            </div>
            <div class="product-card">
                <h4>8. الواحة (🌿)</h4>
                <p>نقوش ناعمة لأشجار النخيل وأوراق الشجر بألوان مستوحاة من الطبيعة تضفي طابعاً مريحاً للعين.</p>
            </div>
            <div class="product-card">
                <h4>9. مودرن هندسي (🔷)</h4>
                <p>خطوط هندسية متقاطعة وعصرية جداً، مناسبة تماماً للشقق والبيوت ذات الطابع المودرن السريع.</p>
            </div>
            """, unsafe_allow_html=True)
        with h_col2:
            st.markdown("""
            <div class="product-card">
                <h4>10. النجمة العربية (⭐)</h4>
                <p>زخرفة إسلامية وعربية مبسطة جداً بألوان هادئة ومحايدة تناسب الممرات وغرف النوم.</p>
            </div>
            <div class="product-card">
                <h4>11. مجلس الضيافة (☕)</h4>
                <p>طابع منزلي تقليدي بألوان دافئة كالكراميل والأحمر الداكن، مخصصة لغرف جلوس العائلة واستقبال الضيوف.</p>
            </div>
            """, unsafe_allow_html=True)

    with tab_kids:
        st.markdown("""
        - **غابة الحيوانات (🦁🐘):** أسد وفيل مرحين بتصميم كرتوني مبهر.
        - **عالم الفضاء (🚀):** سفن فضاء، كواكب، ونجوم مضيئة في الظلام.
        - **سيارات السباق (🏎️):** مضمار سباق ممتد على كامل السجادة للعب التفاعلي.
        - **الديناصورات (🦖):** طابع ما قبل التاريخ المفضل لدى الأطفال.
        - **الأميرات (👸):** قلاع وردية ونقوش ناعمة تليق بغرف الفتيات.
        """)

    with tab_corporate:
        st.markdown("""
        - **هندسي فاخر:** خطوط مستقيمة حديثة وألوان رسمية تعكس الاحترافية.
        - **شعارات الشركات:** حياكة وتطريز شعار شركتك بدقة متناهية على سجاد المداخل الرئيسي وقاعات الاجتماعات.
        """)

# ==========================================
# 9. صفحة: 💰 التسعير الفوري
# ==========================================
elif page == "💰 التسعير الفوري":
    st.title("💰 محرك التسعير الفوري والذكي")
    st.markdown("---")

    col_calc, col_res = st.columns([1, 1])

    with col_calc:
        st.subheader("🧮 مدخلات القياس")
        selected_mat = st.selectbox("1. اختر نوع خامة الخيوط", list(prices.keys()), key="calc_mat")
        u_width = st.number_input("2. أدخل عرض السجادة (بالمتر)", min_value=0.5, value=4.0, step=0.5)
        u_height = st.number_input("3. أدخل طول السجادة (بالمتر)", min_value=0.5, value=6.0, step=0.5)

    with col_res:
        st.subheader("📊 تفصيل التكلفة المالي")
        calc_area = u_width * u_height
        price_per_meter = prices[selected_mat]
        calc_total = calc_area * price_per_meter
        
        st.metric(label="المساحة الإجمالية المحسوبة", value=f"{calc_area:.2f} م²")
        st.metric(label="سعر المتر المربع لهذه الخامة", value=f"{price_per_meter} ريال / م²")
        st.metric(label="السعر النهائي الإجمالي", value=f"{calc_total:,.2f} ريال سعودي")
        
        st.markdown(f"""
        <div style="background: #0F172A; padding: 15px; border-radius: 10px; border-left: 4px solid #D4AF37; margin-top: 15px; text-align: right; direction: rtl;">
            💡 <b>طريقة الحساب الثابتة:</b><br>
            {u_width} متر (عرض) × {u_height} متر (طول) = {calc_area:.1f} متر مربع.<br>
            {calc_area:.1f} م² × {price_per_meter} ريال = <b>{calc_total:,.2f} ريال سعودي</b>.
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 10. صفحة: ⭐ مشاريع العملاء
# ==========================================
elif page == "⭐ مشاريع العملاء":
    st.title("⭐ مشاريع العملاء وقصص النجاح")
    st.markdown("---")

    col_proj1, col_proj2 = st.columns(2)
    with col_proj1:
        st.markdown("""
        <div class="product-card">
            <h4 style="color: #D4AF37;">🏛️ قصر مجلس الضيافة الملكي - الرياض</h4>
            <p><b>التنفيذ:</b> سجاد من صوف طبيعي نقي يحمل نمط "تراث نجد" بمقاس 8×12 متر.</p>
            <p style="color: #22C55E;">⭐⭐⭐⭐⭐ "دقة في الألوان وسرعة إنتاج مذهلة تحاكي التراث تماماً"</p>
        </div>
        <div class="product-card">
            <h4 style="color: #D4AF37;">🏢 قاعة استقبال شركة استثمارية - جدة</h4>
            <p><b>التنفيذ:</b> سجاد نايلون مقوى بتصميم "هندسي فاخر" مدمج معه شعار الشركة بدقة ليزرية.</p>
            <p style="color: #22C55E;">⭐⭐⭐⭐⭐ "جودة ممتازة للمكاتب وتتحمل حركة الزوار اليومية"</p>
        </div>
        """, unsafe_allow_html=True)

    with col_proj2:
        st.markdown("""
        <div class="product-card">
            <h4 style="color: #D4AF37;">🏡 فيلا مودرن سكنية - الخبر</h4>
            <p><b>التنفيذ:</b> سجاد بوليستر ذكي يحمل تصميم "أمواج الرمال" متناسق مع الأثاث المودرن العاجي.</p>
            <p style="color: #22C55E;">⭐⭐⭐⭐⭐ "سهل التنظيف وملمسه ناعم جداً، ومناسب تماماً مع الإضاءة"</p>
        </div>
        <div class="product-card">
            <h4 style="color: #D4AF37;">🕌 مصلى خاص فاخر - المجمعة</h4>
            <p><b>التنفيذ:</b> نمط "نور المحراب" بخامات الحرير والصوف المدمج لإعطاء فخامة وبريق عند دخول الضوء.</p>
            <p style="color: #22C55E;">⭐⭐⭐⭐⭐ "تصميم روحاني مهيب وثلاثي الأبعاد يلفت الأنظار"</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 11. صفحة: 📞 التواصل والطلب
# ==========================================
elif page == "📞 التواصل والطلب":
    st.title("📞 مركز التواصل واستفسارات الإنتاج")
    st.markdown("---")

    col_form, col_info = st.columns([2, 1])

    with col_form:
        c_name = st.text_input("الاسم الكريم")
        c_phone = st.text_input("رقم الجوال")
        c_msg = st.text_area("تفاصيل رسالتك أو استفسارك الفني الخاص بالطلب")
        
        if st.button("📨 إرسال طلب التواصل للمصنع"):
            if c_name and c_phone:
                st.success(f"شكرًا لك. تم استلام طلبك بنجاح، وسيتواصل معك مهندس التصميم عبر الرقم {c_phone} خلال 24 ساعة.")
            else:
                st.error("فضلاً قم بتعبئة حقول الاسم ورقم الجوال لضمان تواصل الفريق معك.")

    with col_info:
        st.markdown("""
        <div style="background: #111827; padding: 20px; border-radius: 15px; border: 1px solid #D4AF37;">
            <h4 style="margin-top:0;">📍 المقر الرئيسي للمنصة</h4>
            <p>المملكة العربية السعودية</p>
            <p><b>استوديو التصميم:</b> نسيج الذكي المحدود</p>
            <p><b>ساعات العمل:</b> من الأحد إلى الخميس</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 12. تذييل الصفحة (Footer)
# ==========================================
st.markdown("<br><hr style='border-color: #D4AF37;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa; font-size: 14px;'>© 2026 Nasij Studio Premium Edition | المنصة السعودية الاحترافية لتصميم السجاد الذكي</p>", unsafe_allow_html=True)
