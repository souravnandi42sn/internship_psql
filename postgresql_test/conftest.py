import os
import pytest
from generate_report import provide_report 
import psycopg2

address={"sourav":"kolkata","anil":""}

@pytest.mark.fixture(scope='module')
def get_fixture():
    con=psycopg2.connect(host="localhost",database="test",user="postgres",password="test123")
    return con

def pytest_addoption(parser):
    #parser.addoption("--address1",action="store",dest="addr1",help="provide a sourav address")
    parser.addoption("--address2",action="store",dest="addr2",help="provide a anil address")

def pytest_configure(config):
    address["anil"]=config.option.addr2
    report_html_path=os.path.join(os.getcwd(),"postgresql_test","report_summary.html")
    print("===========================")
    print(report_html_path)
    print("=================================")
    if(os.path.exists(report_html_path)):
        os.remove("report_summary.html")

def pytest_unconfigure(config):
    provide_report()


