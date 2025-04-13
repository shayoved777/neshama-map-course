import streamlit as st
import random
from datetime import datetime
from pyluach import dates

mazalot = ['טלה', 'שור', 'תאומים', 'סרטן', 'אריה', 'בתולה', 'מאזניים', 'עקרב', 'קשת', 'גדי', 'דלי', 'דגים']
sfirot = ['כתר', 'חכמה', 'בינה', 'חסד', 'גבורה', 'תפארת', 'נצח', 'הוד', 'יסוד', 'מלכות']

psukim = {
    'כתר': ['"בראשית ברא אלוהים את השמים ואת הארץ" (בראשית א\')'],
    'חכמה': ['"ה׳ בחכמה יסד ארץ" (משלי ג\')'],
    'בינה': ['"ותבונה בשמים" (איוב כ"ח)'],
    'חסד': ['"עולם חסד יבנה" (תהילים פ"ט)', '"חסדי ה׳ כי לא תמנו" (איכה ג\')'],
    'גבורה': ['"אזור בגבורה מתניך" (איוב ל"ח)', '"ה׳ עוז לעמו יתן" (תהילים כ"ט)'],
    'תפארת': ['"והדרת פני זקן" (ויקרא י"ט)', '"פאר תחת אפר" (ישעיהו ס"א)'],
    'נצח': ['"וגם נצח ישראל לא ישקר" (שמואל א׳ ט"ו)', '"נצחוני בני נצחוני" (בבא מציעא נ"ט)'],
    'הוד': ['"הוד והדר לפניו" (דברי הימים א׳ ט"ז)', '"הודי נהפך עלי למשחית" (דניאל י\')'],
    'יסוד': ['"צדיק יסוד עולם" (משלי י\')', '"וסולם מוצב ארצה וראשו מגיע השמימה" (בראשית כ"ח)'],
    'מלכות': ['"ומלכותו בכל משלה" (תהילים ק"ג)', '"מלכותך מלכות כל עולמים" (תהילים קמ"ה)']
}

personal_traits = {
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

def generate_soul_map(gregorian_date):
    date = datetime.strptime(str(gregorian_date), "%Y-%m-%d")
    heb_date = dates.HebrewDate.from_pydate(date)
    mazal = get_mazal(heb_date.month)
    sfira = get_sfira(heb_date.month)
    pasuk = random.choice(psukim[sfira])
    traits = personal_traits[mazal]

    personal_message = (
        f"נולדת בתאריך העברי {heb_date.day} בחודש {heb_date.month_name()} בשנת {heb_date.year}.\n"
        f"המזל שלך הוא {mazal}, המסמל: {traits}.\n"
        f"שורש נשמתך בספירת {sfira}.\n"
        f"הפסוק המאיר לך: {pasuk}\n"
    )

    return personal_message

st.title('מפת הנשמה האישית שלך')

birthdate = st.date_input(
    'בחר את תאריך הלידה שלך',
    min_value=datetime(1920, 1, 1),
    max_value=datetime.today()
)

if st.button('קבל את מפת הנשמה'):
    result = generate_soul_map(birthdate)
    st.write(result)
