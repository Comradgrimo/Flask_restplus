from sqlalchemy import create_engine
eng = create_engine("sqlite:///people.db")
conn = eng.connect()
result = conn.execute('''select name from person ''')
print(result.first())






PEOPLE = [
    {"id": "1", "fio": "Иванов И.И", "birthday": "11.01.11", "office": "Инженер"},
    {"id": "2", "fio": "Петров П.П", "birthday": "12.02.12", "office": "Уборщик"},
    {"id": "3", "fio": "Сидоров С.С", "birthday": "13.03.13", "office": "Главбух"},
 ]

lang = [x for x in PEOPLE if x['id'] == '1']
print(lang)