from flask import Flask, request, render_template
from database import add_emp, view_data, update_data

app = Flask(__name__, template_folder='templates')


#home page
@app.route('/home')
def index():
    return render_template('home.html')


#add employee to database
@app.route('/emp-add', methods=['GET', 'POST'])
def emp_add():
    if request.method == 'POST':
        data = request.form
        add_emp(data)
        return render_template('emp-add.html')
    
    return render_template('emp-add.html')


#show employee details
@app.route('/emp-data', methods=['GET','POST'])
def emp_data():
    empdata = view_data()
    return render_template('emp-data.html', empdata=empdata)


#update employee to database
@app.route('/emp-update/<id>', methods=['GET', 'POST'])
def emp_update(id):
    updata = update_data(id)
    return render_template('emp-update.html', updata=updata)




#main function call
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

