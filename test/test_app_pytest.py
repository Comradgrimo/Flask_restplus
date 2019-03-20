import pytest
import requests
from faker import Faker
fake = Faker('ru_Ru')

url = "http://192.168.15.164:5010/people"


def test_del_all():
    r = requests.get(url)
    print('\n')
    for i in range(1,len(r.json())+1):
        r=requests.delete(url +'/%d' % i)
        print(r.json())
    assert r.status_code == 200

def test_add_all():
    for i in range(5):
        fio = fake.name()
        birthday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=65)
        employment = fake.date_this_century(before_today=True, after_today=False)
        office = fake.job()
        r = requests.put(url,
                         json={"fio": fio, "birthday": str(birthday), "office": office, "employment": str(employment)})
        print(r.json())
        assert r.status_code == 201

# def test_get_all():
#     r = requests.get(url)
#     print(r.json())
#     print(array)
#     assert r.status_code == 200
#
#
# def test_get_one():
#     r = requests.get(url)
#     print('\n')
#     for i in range(1,len(r.json())+1):
#         r=requests.get(url +'/%d' % i)
#         print('Считаны люди №' , r.json().get('person_id'))
#         assert r.status_code == 200
# #def test_get_one():




