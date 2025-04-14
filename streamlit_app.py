import streamlit as st
import random
from datetime import datetime
from pyluach import dates

# הגדרת כותרת, אייקון והפריסה
st.set_page_config(
    page_title="מפת הנשמה שלך",
    page_icon="🌟",
    layout="centered",
)

# עיצוב בסיסי בטקסט (CSS) בגווני כחול וזהב
page_bg = """
<style>
body {
    background: linear-gradient(to bottom right, #01295F, #6E6E6D);
    color: #FFD700;
    font-family: Arial, sans-serif;
}
h1, h2, h3, h4 {
    color: #FFD700;
}
div.stForm {
    background-color: rgba(255, 215, 0, 0.2);
    padding: 20px;
    border-radius: 12px;
}
div.stForm button {
    background-color: #014f86 !important;
    border: none;
    color: #FFD700 !important;
    font-size: 16px;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
}
div.stForm button:hover {
    background-color: #013567 !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# רשימות לשימוש במפה
mazalot = [
    'טלה', 'שור', 'תאומים', 'סרטן',
    'אריה', 'בתולה', 'מאזניים', 'עקרב',
    'קשת', 'גדי', 'דלי', 'דגים'
]

sfirot = [
    'כתר', 'חכמה', 'בינה', 'חסד', 'גבורה',
    'תפארת', 'נצח', 'הוד', 'יסוד', 'מלכות'
]

psukim = {
    'כתר':   ['"בראשית ברא אלוהים את השמים ואת הארץ" (בראשית א׳)'],
    'חכמה':  ['"ה׳ בחכמה יסד ארץ" (משלי ג׳)'],
    'בינה':  ['"ותבונה בשמים" (איוב כח)'],
    'חסד':   ['"עולם חסד יבנה" (תהילים פ״ט)', '"חסדי ה׳ כי לא תמנו" (איכה ג׳)'],
    'גבורה': ['"אזור בגבורה מתניך" (איוב לח)', '"ה׳ עוז לעמו יתן" (תהילים כ״ט)'],
    'תפארת': ['"והדרת פני זקן" (ויקרא י״ט)', '"פאר תחת אפר" (ישעיהו ס״א)'],
    'נצח':   ['"וגם נצח ישראל לא ישקר" (שמואל א׳ ט״ו)', '"נצחוני בני נצחוני" (ב״מ נט)'],
    'הוד':   ['"הוד והדר לפניו" (דברי הימים א׳ ט״ז)', '"הודי נהפך עלי למשחית" (דניאל י׳)'],
    'יסוד':  ['"צדיק יסוד עולם" (משלי י׳)', '"וסולם מוצב ארצה וראשו מגיע השמימה" (בראשית כח)'],
    'מלכות': ['"ומלכותו בכל משלה" (תהילים ק״ג)', '"מלכותך מלכות כל עולמים" (תהילים קמ״ה)']
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
    heb_date = dates.HebrewDate.from_pydate(date)
    mazal = get_mazal(heb_date.month)
    sfira = get_sfira(heb_date.month)
    pasuk = random.choice(psukim[sfira])
    midot = traits[mazal]

    msg = f'''
**שלום {name} בן/בת {mother},**
נולדת ב־**{heb_date}** ({birthdate.strftime("%d/%m/%Y")})

**מזלך** הוא **{mazal}** – {midot}  
**שורש נשמתך** בספירת **{sfira}**  
**הפסוק שלך:** {pasuk}

השאלה ששאלת: "{question}"

יש עוד עומק שלא נגלה כאן.  
קבל את מפת הנשמה המלאה – הכוללת הסברים מהקבלה, הזוהר והאר״י.

[🔓 לחצו כאן לרכישה >>]
'''
    return msg

# כותרת ראשית
st.markdown("<h1 style='text-align: center;'>מפת הנשמה החינמית</h1>", unsafe_allow_html=True)

# הסבר קצר
st.markdown("#### מלא את פרטיך, והמערכת תפיק עבורך תשובה מותאמת אישית:")

with st.form("soul_form"):
    name = st.text_input("שם פרטי")
    mother = st.text_input("שם האם")
    birthdate = st.date_input(
    "תאריך לידה",
    min_value=datetime(1900, 1, 1),
    max_value=datetime.today()
)
    question = st.text_area("שאלה פתוחה שמעסיקה אותך")
    submitted = st.form_submit_button("שלח וקבל תשובה חינמית")

if submitted:
    if not name or not mother:
        st.error("אנא מלא גם שם פרטי וגם שם האם.")
    else:
        result = generate_teaser(name, mother, birthdate, question)
        st.info(result)

