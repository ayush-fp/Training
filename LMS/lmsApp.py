from flask import jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from sqlalchemy.exc import IntegrityError
import bcrypt
from models import Admin, Librarian, Customer, Book, db
from settings import app

jwt = JWTManager(app)

@app.route("/")
def home():
    return "Forcepoint Library"

@app.route('/addBooks' , methods = ['POST'])
@jwt_required()
def addBooks():
    user = get_jwt_identity()
    role = user['role'] 
    if role != "Librarian" :
        return "Only Librarian Can Do This" 
    r = request.get_json()
    name = r["name"]
    author = r["author"]
    description = r["description"]
    publication = r["publication"]
    book = Book(name = name , author = author , description = description , publication = publication , isIssued = "No" , issuedBy = "-")
    db.session.add(book) 
    db.session.commit() 
    return "Added" 

@app.route('/allBooks' , methods = ['GET'])
def allBooks():
    listt = []
    for book in Book.query.all():
        listt.append(book.json())
    print(listt)
    return jsonify(listt) 

@app.route('/deleteBook' , methods = ['DELETE'])
@jwt_required()
def deleteBook():
    user = get_jwt_identity()
    role = user['role'] 
    if role != "Librarian" :
        return "Only Librarian Can Do This"
        
    r = request.get_json()
    id = r["id"]
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return "deleted"

@app.route('/updateBook' , methods = ['PUT'])
@jwt_required()
def updateBook():
    user = get_jwt_identity()
    role = user['role'] 
    if role != "Librarian" :
        return "Only Librarian Can Do This"

    r = request.get_json()
    id = r["id"]
    book = Book.query.filter_by(id=id).first()
    name = r["name"]
    author = r["author"]
    description = r["description"]
    publication = r["publication"]

    book.name = name
    book.author = author
    book.description = description 
    book.publication = publication 

    db.session.commit()
    return "updated"

@app.route('/issueBook' , methods = ['POST'])
@jwt_required()
def issueBook():
    token = get_jwt_identity()
    tokenrole = token['role']
    if tokenrole != "Customer" :
        return "Not a customer"
        
    tokenEmail = token['email']

    r = request.get_json()
    id = r["id"]
    book = Book.query.filter_by(id=id).first()
    if book.isIssued == 'No':
        book.issuedBy = tokenEmail
        book.isIssued = 'Yes'
        db.session.commit()
        return "updated"
    else:
        return "Already issued by someone"

@app.route('/returnBook' , methods = ['POST'])
@jwt_required()
def returnBook():
    token = get_jwt_identity()
    tokenrole = token['role']
    if tokenrole != "Customer" :
        return "Not a customer"
        
    tokenEmail = token['email']

    r = request.get_json()
    id = r["id"]
    book = Book.query.filter_by(id=id).first()

    if book.issuedBy != tokenEmail:
        return {"message" : "You dont have any such book"}

    book.isIssued = "No" 
    book.issuedBy = "-" 
    
    db.session.commit()
    return "returned"

@app.route('/registerAdmin', methods=['POST'])
def registerAdmin():
    try:

        email = request.json.get('email', None)
        password = request.json.get('password', None)
        name = request.json.get('name', None)
        role = request.json.get('role', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        if role == "Admin":
            user = Admin( email=email, hash=hashed , name = name , role = role )
            db.session.add(user)
            db.session.commit()
            access_token = create_access_token(identity={"email" : email , "role" : role})
            return {"access_token": access_token}, 200
        else :
            return {"message" : "Error"} 
    except IntegrityError:
        db.session.roleback()
        return 'Admin Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

@app.route('/registerLibrarian', methods=['POST'])
@jwt_required()
def registerLibrarian():
    try:

        token = get_jwt_identity()
        tokenEmail = token['role']
        if tokenEmail != "Admin" :
            return {"message" : "Only Admins Can add Librarian"}

        email = request.json.get('email', None)
        password = request.json.get('password', None)
        name = request.json.get('name', None)
        role = request.json.get('role', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        if role == "Librarian":
            user = Librarian( email=email, hash=hashed , name = name , role = role )
            db.session.add(user)
            db.session.commit()
            access_token = create_access_token(identity={"email" : email , "role" : role})
            return {"access_token": access_token}, 200
        else :
            return {"message" : "Error Occoured"}  
    except IntegrityError:
        db.session.roleback()
        return 'Librarian Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

@app.route('/registerCustomer', methods=['POST'])
@jwt_required()
def registerCustomer():
    try:

        token = get_jwt_identity()
        tokenEmail = token['role']
        if tokenEmail != "Admin" :
            return {"message" : "Only Admins Can add Users"}

        email = request.json.get('email', None)
        password = request.json.get('password', None)
        name = request.json.get('name', None)
        role = request.json.get('role', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        if role == "Customer":
            user = Customer( email=email, hash=hashed , name = name , role = role )
            db.session.add(user)
            db.session.commit()
            access_token = create_access_token(identity={"email" : email , "role" : role})
            return {"access_token": access_token}, 200
        else :
            return {"message" : "Error Occoured"}  
    except IntegrityError:
        db.session.roleback()
        return 'User Already Exists', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

@app.route('/loginLibrarian', methods=['POST'])
def loginLibrarian():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        
        user = Librarian.query.filter_by(email=email).first()
        if not user:
            return 'User Not Found!', 404
        
        if bcrypt.checkpw(password.encode('utf-8'), user.hash) and user.role == "Librarian":
            access_token = create_access_token(identity={"email": email , "role" : user.role})
            return {"access_token": access_token}, 200
        else:
            return 'Invalid Login Info!', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

@app.route('/loginAdmin', methods=['POST'])
def loginAdmin():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        
        user = Admin.query.filter_by(email=email).first()
        if not user:
            return 'User Not Found!', 404
        
        if bcrypt.checkpw(password.encode('utf-8'), user.hash) and user.role == "Admin":
            access_token = create_access_token(identity={"email": email , "role" : user.role})
            return {"access_token": access_token}, 200
        else:
            return 'Invalid Login Info!', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

@app.route('/loginCustomer', methods=['POST'])
def loginCustomer():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        
        if not email:
            return 'Missing email', 400
        if not password:
            return 'Missing password', 400
        
        user = Customer.query.filter_by(email=email).first()
        if not user:
            return 'User Not Found!', 404
        
        if bcrypt.checkpw(password.encode('utf-8'), user.hash) and user.role == "Customer":
            access_token = create_access_token(identity={"email": email , "role" : user.role})
            return {"access_token": access_token}, 200
        else:
            return 'Invalid Login Info!', 400
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body', 400

@app.route('/allCustomers', methods=['GET'])
@jwt_required()
def allCustomer():
    user = get_jwt_identity()
    role = user['role'] 
    if role != "Admin" :
        return "Only Admin Can Do This"
    listt = []
    for customer in Customer.query.all():
        listt.append(customer.json())
    print(listt)
    return jsonify(listt)

@app.route('/allLibrarians', methods=['GET'])
@jwt_required()
def allLibrarians():
    user = get_jwt_identity()
    role = user['role'] 
    if role != "Admin" :
        return "Only Admin Can Do This"
    listt = []
    for customer in Librarian.query.all():
        listt.append(customer.json())
    print(listt)
    return jsonify(listt)

@app.route('/checkAccount' , methods = ['GET'])
@jwt_required()
def checkAccount():
    token = get_jwt_identity()
    tokenrole = token['role']
    if tokenrole != "Customer" :
        return "Not a customer"
        
    tokenEmail = token['email']

    book = Book.query.filter_by(issuedBy = tokenEmail)

    listt = []
    for b in book:
        listt.append(b.json())
    print(listt)
    
    return jsonify(listt)

@app.route('/test', methods=['GET'])
@jwt_required()
def test():
    user = get_jwt_identity()
    email = user['email']
    return f'Welcome to the protected route {email}!', 200

def generate_schema():
    db.create_all()

if __name__ == '__main__':
    generate_schema()
    app.run(port=5000)
    print("End of server")