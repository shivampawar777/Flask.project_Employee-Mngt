from sqlalchemy import create_engine, text


#create engine from engine object
engine = create_engine("mysql+pymysql://root:root@localhost/test1?charset=utf8mb4")


#add data to database
def add_emp(data):
    with engine.connect() as conn:
        query = text("INSERT INTO empdata(emp_id, jdate, dept, name, phone, address, state, idproof) VALUES(:empid, :jdate, :dept, :name, :phone, :add, :state, :idproof)")
                     
        conn.execute(query, empid=data['empid'], jdate=data['jdate'], dept=data['dept'], name=data['name'], phone=data['phone'], add=data['add'], state=data['state'], idproof=data['idproof'])



#update the data
def update_data(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from empdata where id = :val"), {'val':id})
        updata = []
        
        updata = result.all()
        return dict(updata[0])



#access the data
def view_data():
    with engine.connect() as conn:
        result = conn.execute(text("select * from empdata"))
        empdata = []
        for row in result.all():
            empdata.append(dict(row._mapping))
        
        return empdata


