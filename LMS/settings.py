from datetime import timedelta
import os
from flask import Flask


app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
print(project_dir)
db_file = "sqlite:///{}".format(os.path.join(project_dir, "lms.db"))
print(db_file)

app.secret_key = "ForcePoint"
app.config['SQLALCHEMY_DATABASE_URI'] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=300)