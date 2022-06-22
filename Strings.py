import datetime
today = datetime.date.today()
data = [
{
'name': 'Erika Mustermann',
'endung': '',
'anrede': 'Frau',
'betrag': 100,
'datum': today + datetime.timedelta(14),
},
{
'name': 'Max Mustermann',
'endung': 'r',
'anrede': 'Herr',
'betrag': 150,
'datum': today + datetime.timedelta(30),
},
]
template = """
Sehr gehrte{endung} {anrede} {name},
Sie schulden mir noch {betrag}.
Bitte überweisen Sie den Betrag von {betrag:5.2f} bis zum {datum:%d.%m.%Y}.
Viele Grüße
Der Eintreiber
"""
text = "DassollinderMittestehen"
print(text.isdigit())
print(text.isalpha())

text = "Das soll in der Mitte stehen"

print(text.center(100,"!"))

lst = text.split(" ")
print("_".join(lst))

for entry in data:
    print('#' * 80)
    print(template.format(**entry))
