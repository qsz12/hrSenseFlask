from flask import Flask,request
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Employee

app=Flask(__name__)
Base=declarative_base()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/job'
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(bind=engine)
conn=engine.connect()
metadata = sqlalchemy.MetaData()
Session = sessionmaker(bind=engine)
sess=Session()



@app.route("/",methods=['GET'])
def index():
    return "Home Page"


@app.route('/add',methods=['POST'])
def create():
    try:
        data=request.get_json()
        print('\n\n\n',data,'\n\n\n')

        title=data.get('title',"")
        dept=data.get('department',"")
        country=data.get('country',"")
        state=data.get('state',"")
        city=data.get('city',"")
        remote=data.get('remote',False)
        desc=data.get('description',"")
        require=data.get('requirements',"")
        ben=data.get('benifits',"")
        c_i=data.get('company_industry',"")
        j_f=data.get('job_function',"")
        e_t=data.get('employment_type',"")
        exp=data.get('experience')
        edu=data.get('education',"")
        keyword=data.get('keywords',"")
        salary_from=data.get('salary_from',0)
        salary_to=data.get('salary_to',0)
        currency=data.get('currency',"indian rupee")

        if title=="":
            raise Exception('ERROR title is empty')
        if exp==None:
            raise Exception('ERROR experience is empty')

        emp=Employee(title=title,department=dept,country=country,state=state,city=city,remote=remote,description=desc,requirements=require,benifits=ben,company_industry=c_i,job_function=j_f,employment_type=e_t,experience=exp,education=edu,keywords=keyword,salary_from=salary_from,salary_to=salary_to,currency=currency)
        sess.add(emp)
        sess.commit()
        return {"data":{"title":title,"dept":dept,"country":country,"state":state,"city":city,"remote":remote,"description":desc,"requirements":require,"benifit":ben,"comind":c_i,"job_fun":j_f,"employee_type":e_t,"experience":exp,"education":edu,"keywords":keyword,"salaryFrom":salary_from,"salaryTo":salary_to,"currency":currency}}
    except Exception as e:
        return {"error":str(e)}


@app.route('/<int:id>/del',methods=['GET'])
def dele(id):
    try:
        emp=sess.query(Employee).filter_by(id=id).first()
        if emp==None:
            return "User Doesn't Exist!!!"
        sess.delete(emp)
        sess.commit()
        return "Deleted!!!"
    except Exception as e:
        return {"error":str(e)}


@app.route('/<int:id>/update',methods=['POST'])
def update_data(id):
    try:
        emp=sess.query(Employee).filter_by(id=id).first()
        data=request.get_json()
        print('\n\n\n',data,'\n\n\n')

        if data.get('title'):
            emp.title=data.get('title')
        if data.get('department'):
            emp.department=data.get('department')
        if data.get('country'):
            emp.country=data.get('country')
        if data.get('state'):
            emp.state=data.get('state')
        if data.get('city'):
            emp.city=data.get('city')
        if data.get('remote'):
            emp.remote=data.get('remote')
        if data.get('description'):
            emp.description=data.get('description')
        if data.get('requirements'):
            emp.requirements=data.get('requirements')
        if data.get('benifits'):
            emp.benifits=data.get('benifits')
        if data.get('company_industry'):
            emp.company_industry=data.get('company_industry')
        if data.get('job_function'):
            emp.job_function=data.get('job_function')
        if data.get('employment_type'):
            emp.employment_type=data.get('employment_type')
        if data.get('experience'):
            emp.experience=data.get('experience')
        if data.get('education'):
            emp.education=data.get('education')
        if data.get('keywords'):
            emp.keywords=data.get('keywords')
        if data.get('salary_from'):
            emp.salary_from=data.get('salary_from')
        if data.get('salary_to'):
            emp.salary_to=data.get('salary_to')
        if data.get('currency'):
            emp.currency=data.get('currency')    

        sess.commit()
        return "Updatedddd!!!"
    except Exception as e:
        return {"error":str(e)}


@app.route('/<int:id>/fetch',methods=['GET'])
def fet(id):
    try:
        emp=sess.query(Employee).filter_by(id=id).first()
        if emp==None:
            return "User Doesn't Exist!!!"
        return {"id":id,"data":{"title":emp.title,"dept":emp.department,"country":emp.country,"state":emp.state,"city":emp.city,"remote":emp.remote,"description":emp.description,"requirements":emp.requirements,"benifit":emp.benifits,"comind":emp.company_industry,"job_fun":emp.job_function,"employment_type":emp.employment_type,"experience":emp.experience,"education":emp.education,"keywords":emp.keywords,"salaryFrom":emp.salary_from,"salaryTo":emp.salary_to,"currency":emp.currency}}
    except Exception as e:
        return {"Error":str(e)}


@app.route('/fetchall',methods=['GET'])
def fetch():
    try:
        emp=sess.query(Employee).all()
        if len(emp)==0:
            return "Empty DataBase"
        return {"data":[i.title for i in emp]}
    except Exception as e:
        return {"Error":str(e)}


if __name__=="__main__":
    app.run(debug=True)