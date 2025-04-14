
import streamlit as st
import random
from datetime import datetime
from pyluach import dates

st.set_page_config(
    page_title="מפת הנשמה שלך",
    page_icon="🌟",
    layout="centered",
)

mazalot = ['טלה', 'שור', 'תאומים', 'סרטן', 'אריה', 'בתולה', 'מאזניים', 'עקרב', 'קשת', 'גדי', 'דלי', 'דגים']
sfirot = ['כתר', 'חכמה', 'בינה', 'חסד', 'גבורה', 'תפארת', 'נצח', 'הוד', 'יסוד', 'מלכות']

psukim = {
    'כתר': ['בראשית ברא אלוהים את השמים ואת הארץ (בראשית א\')'],
    'חכמה': ['"ה׳ בחכמה יסד ארץ" (משלי ג')'],
    'בינה': ['"ותבונה בשמים" (איוב כ"ח)'],
    'חסד': ['"עולם חסד יבנה" (תהילים פ"ט)', '"חסדי ה׳ כי לא תמנו" (איכה ג')'],
    'גבורה': ['"אזור בגבורה מתניך" (איוב ל"ח)', '"ה׳ עוז לעמו יתן" (תהילים כ"ט)'],
    'תפארת': ['"והדרת פני זקן" (ויקרא י"ט)', '"פאר תחת אפר" (ישעיהו ס"א)'],
    'נצח': ['"וגם נצח ישראל לא ישקר" (שמואל א׳ ט"ו)', '"נצחוני בני נצחוני" (בבא מציעא נ"ט)'],
    'הוד': ['"הוד והדר לפניו" (דברי הימים א׳ ט״ז)', '"הודי נהפך עלי למשחית" (דניאל י')'],
    'יסוד': ['"צדיק יסוד עולם" (משלי י')', '"וסולם מוצב ארצה וראשו מגיע השמימה" (בראשית כ"ח)'],
    'מלכות': ['"ומלכותו בכל משלה" (תהילים ק"ג)', '"מלכותך מלכות כל עולמים" (תהילים קמ"ה)']
}

traits = {
    'טלה': 'יצירתיות, מנהיגות, התחלה חדשה',
    'שור': 'יציבות, התמדה, חושניות',
    'תאומים': 'תקשורת, גמישות, סקרנות',
    'סרטן': 'רגישות, אמפתיה, ביתיות',
    'אריה': 'נדיבות, כריזמה, ביטחון עצמי',
    'בתולה': 'דייקנות, אנליטיות, אחריות',
    'מאזניים': 'הרמוניה, איזון, יופי',
    'עקרב': 'עומק, תשוקה, אינטואיציה',
    'קשת': 'הרפתקנות, חופש, אופטימיות',
    'גדי': 'שאפתנות, משמעת, אחריות',
    'דלי': 'מקוריות, חדשנות, אידיאליזם',
    'דגים': 'רוחניות, דמיון, חמלה'
}

def get_mazal(hebrew_month):
    return mazalot[hebrew_month - 1]

def get_sfira(hebrew_month):
    return sfirot[(hebrew_month - 1) % len(sfirot)]

def generate_teaser(name, mother, birthdate, question):
    date = datetime.strptime(str(birthdate), "%Y-%m-%d")
    heb = dates.HebrewDate.from_pydate(date)
    mazal = get_mazal(heb.month)
    sfira = get_sfira(heb.month)
    pasuk = random.choice(psukim[sfira])
    midot = traits[mazal]

    msg = f""" 
✨ שלום {name} בן/בת {mother}, נולדת ב-{heb} ({birthdate.strftime("%d/%m/%Y")})
🔯 מזלך הוא {mazal} – {midot}
🌿 שורש נשמתך בספירת {sfira}
🕯 הפסוק שלך: {pasuk}
❓ השאלה ששאלת: "{question}"

📌 יש עוד עומק שלא נגלה כאן.
📥 קבל את מפת הנשמה המלאה – הכוללת הסברים מהקבלה, הזוהר והאר״י.

[ 🔓 לחצו כאן לרכישה >> ]
"""
    return msg

st.markdown("<h1 style='text-align: center;'>מפת הנשמה החינמית</h1>", unsafe_allow_html=True)
st.markdown("### מלא את פרטיך והמערכת תפיק עבורך תשובה מותאמת אישית:")

with st.form("soul_form"):
    name = st.text_input("שם פרטי")
    mother = st.text_input("שם האם")
    birthdate = st.date_input("תאריך לידה")
    question = st.text_area("שאלה פתוחה שמעסיקה אותך")
    submitted = st.form_submit_button("שלח וקבל תשובה חינמית")

if submitted:
    result = generate_teaser(name, mother, birthdate, question)
    st.success(result)
