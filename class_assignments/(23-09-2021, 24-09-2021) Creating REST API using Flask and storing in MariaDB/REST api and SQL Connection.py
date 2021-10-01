'''
PROGRAM  :Create API REST server using python flask which:-
	      1) displays the entire content of the data which has been deleted
	      2) In update function, display which data has been updated to what(data before updation and after updation).
'''
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 23-09-2021,24-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None


from flask import Flask
from flask import render_template
from flask import jsonify
from flask import redirect
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:jwala1330@localhost:3309/guvi"
app.config['SECRET_KEY'] = 'jwala1330'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

# create a table inside our database
class APIUserModel(db.Model):
    __tablename__ = 'guvi_data_sciences'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))

# insert data into SQL
@app.route('/write', methods = ['POST'])
def write():
	
    # Requesting name and email from POSTMAN i.e.,frontend
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    api_user_model = APIUserModel(name = name, email = email)
    save_to_database = db.session()
    try:
        save_to_database.add(api_user_model)
	
	# After data is added successfully we have to commit the DB to save 
        save_to_database.commit()
    except:
	
	# If insertion was not done properly we have to rollback and go the previous stage where DB is consistency(last savepoint or commit)
        save_to_database.rollback()
	# Flush is used to free memory
        save_to_database.flush()
	
    # Returning the jsonify object as response to confirm data is inserted
    return jsonify({"message":"success"})


# fetch data from server
@app.route('/', methods=['GET'])
def fetch_all():
    data = APIUserModel.query.all()
    data_all = []
    for data in data:
        data_all.append({"id":data.id, "name":data.name, "email":data.email})
    return jsonify(data_all)

# fetch data based on ID
@app.route('/display/<int:id>', methods=['GET'])
def fetch_by_id(id):
    try:
        data = APIUserModel.query.filter_by(id=id).first()
        return jsonify({"id":data.id, "name":data.name, "email":data.email})
    except:
        return jsonify({"message":"error"})

#update data
@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
	
    # update = insert + fetch by id
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    save_to_database = db.session
    try:
        api_user_model = APIUserModel.query.filter_by(id=id).first()
        data=APIUserModel.query.filter_by(id=id).first()
	
        #data which has to deleted is stored in temp1 variable
        temp1= {"id":data.id, "name":data.name, "email":data.email}

        api_user_model.name = name
        api_user_model.email = email

        data=APIUserModel.query.filter_by(id=id).first()
	
        #data which have been updated is stored in temp variable
        temp= {"id":data.id, "name":data.name, "email":data.email}
        save_to_database.commit()
        id=api_user_model.id
        data=APIUserModel.query.filter_by(id=id).first()
        return jsonify([temp1,temp])
    except:
        save_to_database.rollback()
        save_to_database.flush()
        return jsonify({"message":"error in updating data"})


#delete data
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        save_to_database = db.session
        data=APIUserModel.query.filter_by(id=id).first()
	
        #data which have been deleted is stored in temp variable
        temp= jsonify({"id":data.id, "name":data.name, "email":data.email})
        APIUserModel.query.filter_by(id=id).delete()
        save_to_database.commit()
        return temp
    except:
        return jsonify({"message":"error in deleting data"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)
