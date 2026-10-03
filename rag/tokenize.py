import re, unicodedata
STOP={
 've','veya','ile','bu','bir','için','icin','mi','mı','mu','mü','de','da','the','a','an','and','or','of','to','in','for','is','are','on','with'
}
def tokens(text):
    text=unicodedata.normalize('NFKC',text).lower()
    out=re.findall(r"[0-9a-zçğıöşü_.+-]+",text,re.I)
    return [x for x in out if len(x)>1 and x not in STOP]
