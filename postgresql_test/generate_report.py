import os
from jinja2 import Environment,FileSystemLoader,select_autoescape
import json

def provide_report():
    print("===========================")
    curr_path=os.getcwd()
    html_template_path = os.path.join(curr_path,'postgresql_test','templates')
    print(html_template_path)
    print("===================================")
    env=Environment(loader=FileSystemLoader(html_template_path),autoescape=select_autoescape(['html', 'xml'],),extensions=['jinja2.ext.loopcontrols'])
    template=env.get_template("home.html")
    file_name=os.path.join(curr_path,"postgresql_test","build","report_summary.html")
    report=open("report_summary.html","w")
    json_name=os.path.join(curr_path,"postgresql_test","build","new_data.json")
    print("==============================")
    print(json_name)
    print("=================================")
    with open(json_name,"r") as file:
        data=json.load(file)
    file.close()
    report.write(template.render(report_data=data))

