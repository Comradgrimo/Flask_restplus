import pytest
import requests

url = "http://192.168.15.164:5010/people"

people = [{'fio': 'Лазарев Лукьян Чеславович', 'birthday': '1970-02-10', 'office': 'Технолог', 'employment': '2011-01-11'},
{'fio': 'Федотов Марк Харлампьевич', 'birthday': '1993-12-11', 'office': 'Лоцман', 'employment': '2018-03-11'},
{'fio': 'Громова Варвара Антоновна', 'birthday': '1982-09-15', 'office': 'Программист', 'employment': '2009-01-27'},
{'fio': 'Громова Октябрина Владимировна', 'birthday': '1959-10-27', 'office': 'Программист', 'employment': '2004-01-22'},
{'fio': 'Тарасова Антонина Игоревна', 'birthday': '1979-01-17', 'office': 'Орнитолог', 'employment': '2009-12-18'},
{'fio': 'Кулагин Аполлон Валерьевич', 'birthday': '1969-12-10', 'office': 'Особист', 'employment': '2002-04-18'},
{'fio': 'Воронова Синклитикия Леоновна', 'birthday': '1988-06-21', 'office': 'Юрист', 'employment': '2003-11-17'},
{'fio': 'Крюкова Наина Богдановна', 'birthday': '1996-11-25', 'office': 'Скульптор', 'employment': '2012-07-13'},
{'fio': 'Туров Демьян Ефимьевич', 'birthday': '1982-04-19', 'office': 'Конвоир', 'employment': '2008-12-07'},
{'fio': 'Алексеев Евлампий Адамович', 'birthday': '1990-05-22', 'office': 'Инженер-акустик', 'employment': '2005-02-03'}]

def test_del_all():
    r = requests.get(url)
    print('\n')
    for i in range(1,len(r.json())+1):
        r=requests.delete(url +'/%d' % i)
        print(r.json())
    assert r.status_code == 200

def test_add_all():
    for i in range(10):
        r = requests.put(url,json={"fio": people[i].get('fio'),
                                   "birthday": people[i].get('birthday'),
                                   "office": people[i].get('office'),
                                   "employment": people[i].get('employment')
                                   }
                         )
        print(r.json())
        assert r.status_code == 201

def test_get_all():
    r = requests.get(url)
    print(r.json())

    assert r.status_code == 200

def test_get_all_for():
    r = requests.get(url)
    print('\n')
    for i in range(1, len(r.json())+1):
        r=requests.get(url +'/%d' % i)
        print('Считаны люди №' , r.json().get('person_id'))
        assert r.status_code == 200

def test_update_all_for():
    r = requests.get(url)
    print('\n')
    for i in range(1, len(r.json())+1):
        r = requests.post(url + '/%d' % i, json={"fio": people[i].get('fio'),
                                   "birthday": people[i].get('birthday'),
                                   "office": people[i].get('office'),
                                   "employment": people[i].get('employment')
                                   }
                         )
        print(r.json())
        assert r.status_code == 200
def test_filter1():
    r = requests.get(url + '/filter', params=('olderThan=30'))
    print(r.json())
    assert r.status_code == 200
def test_filter2():
    r = requests.get(url + '/filter', params=('yongerThan=30'))
    print(r.json())
    assert r.status_code == 200
def test_filter3():
    r = requests.get(url + '/filter', params=('exp1=10'))
    print(r.json())
    assert r.status_code == 200
def test_filter4():
    r = requests.get(url + '/filter', params=('exp2=10'))
    print(r.json())
    assert r.status_code == 200
def test_filter5():
    r = requests.get(url + '/filter', params=('office=Программист'))
    print(r.json())
    assert r.status_code == 200
def test_all_filter():
    r = requests.get(url + '/filter', params=('olderThan=30&yongerThan=100&exp1=10&exp2=100&office=Программист'))
    print(r.json())
    assert r.status_code == 200