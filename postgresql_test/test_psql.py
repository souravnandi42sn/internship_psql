
import psycopg2
import pytest
import json
from conftest import address
from collections import defaultdict

report_data=defaultdict(list)

def convert_data():
    l=[]
    for i,v in address.items():
        l.append((i,v))
    return l
test_data=convert_data()

@pytest.mark.parametrize("user,address",test_data)
def test_psql(user,address):
    con=psycopg2.connect(host="localhost",database="test",user="postgres",password="test123")
    cur=con.cursor()
    cur.execute("select address from company where name=\'"+user+"\';")
    res=cur.fetchall()
    with open("postgresql_test/build/new_data.json","w") as file:
        try:
            assert res[0][0].strip()==address
            report_data[user]={"status":"passsed"}
            json.dump(report_data,file)
        except:
            report_data[user]={"status":"failed"}
            json.dump(report_data,file)


