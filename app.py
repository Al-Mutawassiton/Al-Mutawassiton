import streamlit as st
import google.generativeai as genai
import requests

# --- الإعدادات الأساسية (املا بياناتك هنا) ---
GEMINI_KEY = "AIzaSyDr2pI_9-eSfRiEBFnUyJEFnSbOd0FEMxc"
TELEGRAM_TOKEN = "8661222733:AAFuSvSslYseY6LE8MC-S72UGuWxwlAatGk"
CHAT_ID = "8484233133"

genai.configure(api_key=GEMINI_KEY)

# --- تصميم الواجهة الخلابة (CSS) ---
st.markdown("""
    <style>
    @keyframes move_bg { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
    .main { background: linear-gradient(-45deg, #0b0d17, #1a1c2c, #000000); background-size: 400% 400%; animation: move_bg 15s ease infinite; color: white; }
    .stButton>button { background: linear-gradient(90deg, #ffd700, #b8860b); color: black; font-weight: bold; border-radius: 30px; border: none; padding: 10px 25px; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0px 5px 15px rgba(255, 215, 0, 0.4); }
    h1 { color: #ffd700; text-shadow: 2px 2px 4px #000; }
    </style>
    """, unsafe_allow_html=True)

# شريط متحرك
st.markdown("<marquee style='font-family: Arial; color: #ffd700; font-size: 20px;'>🚀 منصة المتوسطون التعليمية الذكية .. بوابتك للتفوق والنجاح في كل المواد 🎓</marquee>", unsafe_allow_html=True)

st.title("🎓 منصة المتوسطون")
st.subheader("مساعدك الشخصي في الكيمياء والفيزياء والرياضيات")

# --- نظام التتبع والـ 3 محاولات ---
if 'counter' not in st.session_state:
    st.session_state.counter = 0

def notify_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url)
    except:
        pass

# محاولة معرفة الـ IP (تقريبي عبر Streamlit)
if st.session_state.counter == 0:
    notify_telegram("🚨 شخص جديد دخل المنصة الآن!")

# الواجهة الرئيسية
if st.session_state.counter < 3:
    st.info(f"لديك {3 - st.session_state.counter} محاولات مجانية متبقية.")
    
    user_input = st.text_area("ضع سؤالك أو مسألتك هنا:", placeholder="مثلاً: ما هي معادلة أكسدة الحديد؟")
    
    if st.button("احصل على الحل فوراً"):
        if user_input:
            with st.spinner('جاري تفكير العقل الاصطناعي...'):
                try:
                    st.session_state.counter += 1
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(f"أنت مدرس خبير في المنهج، اشرح للطلب بوضوح حل هذا السؤال: {user_input}")
                    
                    st.success("الإجابة:")
                    st.write(response.text)
                    
                    # إرسال التقرير للتلجرام
                    notify_telegram(f"📩 سؤال جديد تم حله:\n{user_input}")
                except Exception as e:
                    st.error("عذراً، حدث خطأ في الاتصال بالذكاء الاصطناعي.")
        else:
            st.warning("أدخل سؤالاً أولاً يا بطل!")
else:
    st.error("⚠️ عذراً! لقد استهلكت جميع محاولاتك المجانية.")
    st.markdown("🔒 سجل دخولك الآن بحساب الجيميل لفتح وصول غير محدود وحفظ دروسك.")
    if st.button("التسجيل عبر Google"):
        st.info("سيتم توجيهك لصفحة الربط بـ Firebase قريباً...")

st.markdown("---")
st.caption("حقوق الملكية محفوظة لمنصة المتوسطون © 2026")
