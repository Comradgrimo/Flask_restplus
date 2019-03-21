from datetime import datetime, date
import requests
from faker import Faker
# fake = Faker('ru_Ru')
# fio = fake.name()
# birthday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=65)
# employment = fake.date_this_century(before_today=True, after_today=False)
# office = fake.job()
# #print(fio,birthday,office, employment)
#
#
#
#
# url = "http://192.168.15.164:5010/people"
# r = requests.post(url+'/1', json={"fio": fio, "birthday": str(birthday), "office": office, "employment": str(employment)})
# print(r.json())

# a =[{"fio": "Иванов И.И", "birthday": datetime.strptime('11-01-1965', '%d-%m-%Y').date(), "office": "Инженер", "employment": datetime.strptime('10-10-2001', '%d-%m-%Y').date()},
# {"fio": "Петров П.П", "birthday": datetime.strptime('06-10-1985', '%d-%m-%Y').date(), "office": "Уборщик",
#  "employment": datetime.strptime('12-07-2003', '%d-%m-%Y').date()},
# {"fio": "Сидоров С.С", "birthday": datetime.strptime('21-07-1991', '%d-%m-%Y').date(), "office": "Главбух",
#  "employment": datetime.strptime('21-09-2005', '%d-%m-%Y').date()}]
# for i in range(5):
#     fio = fake.name()
#     birthday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=65)
#     employment = fake.date_this_century(before_today=True, after_today=False)
#     office = fake.job()
#     print({"fio": fio, "birthday": birthday, "office": office, "employment": employment})
#     r = requests.put(url, json= {"fio": fio, "birthday": str(birthday), "office": office, "employment": str(employment)})

# print(array)
# print(a)
people = [{'fio': 'Лазарев Лукьян Чеславович', 'birthday': '1970-02-10', 'office': 'Технолог', 'employment': '2011-01-11'},
{'fio': 'Федотов Марк Харлампьевич', 'birthday': '1993-12-11', 'office': 'Лоцман', 'employment': '2018-03-11'},
{'fio': 'Громова Варвара Антоновна', 'birthday': '1982-09-15', 'office': 'Продавец', 'employment': '2009-01-27'},
{'fio': 'Громова Октябрина Владимировна', 'birthday': '1959-10-27', 'office': 'Программист', 'employment': '2004-01-22'},
{'fio': 'Тарасова Антонина Игоревна', 'birthday': '1979-01-17', 'office': 'Орнитолог', 'employment': '2009-12-18'},
{'fio': 'Кулагин Аполлон Валерьевич', 'birthday': '1969-12-10', 'office': 'Особист', 'employment': '2002-04-18'},
{'fio': 'Воронова Синклитикия Леоновна', 'birthday': '1988-06-21', 'office': 'Юрист', 'employment': '2003-11-17'},
{'fio': 'Крюкова Наина Богдановна', 'birthday': '1996-11-25', 'office': 'Скульптор', 'employment': '2012-07-13'},
{'fio': 'Туров Демьян Ефимьевич', 'birthday': '1982-04-19', 'office': 'Конвоир', 'employment': '2008-12-07'},
{'fio': 'Алексеев Евлампий Адамович', 'birthday': '1990-05-22', 'office': 'Инженер-акустик', 'employment': '2005-02-03'}]

print(people[0].get('fio'))