from datetime import datetime, date
import requests
from faker import Faker
fake = Faker('ru_Ru')
# fio = fake.name()
# birthday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=65)
# employment = fake.date_this_century(before_today=True, after_today=False)
# office = fake.job()
# print(fio,birthday,office, employment)




url = "http://192.168.15.164:5010/people"

# a =[{"fio": "Иванов И.И", "birthday": datetime.strptime('11-01-1965', '%d-%m-%Y').date(), "office": "Инженер", "employment": datetime.strptime('10-10-2001', '%d-%m-%Y').date()},
# {"fio": "Петров П.П", "birthday": datetime.strptime('06-10-1985', '%d-%m-%Y').date(), "office": "Уборщик",
#  "employment": datetime.strptime('12-07-2003', '%d-%m-%Y').date()},
# {"fio": "Сидоров С.С", "birthday": datetime.strptime('21-07-1991', '%d-%m-%Y').date(), "office": "Главбух",
#  "employment": datetime.strptime('21-09-2005', '%d-%m-%Y').date()}]
for i in range(5):
    fio = fake.name()
    birthday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=65)
    employment = fake.date_this_century(before_today=True, after_today=False)
    office = fake.job()
    print({"fio": fio, "birthday": birthday, "office": office, "employment": employment})
    r = requests.put(url, json= {"fio": fio, "birthday": str(birthday), "office": office, "employment": str(employment)})

# print(array)
# print(a)