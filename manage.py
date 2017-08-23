#coding:utf-8

from app import stapp
from flask_script import Manager, Shell

app = stapp('default')
manager = Manager(app)


#-------------------------------------
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	name = db.Column(db.String(32), primary_key=True)
	email = db.Column(db.String(32))



def adddata():
	user = User()
	user.name = "toloog"
	user.email = "admin@toloog.com"
	db.session.add(user)
	db.session.commit()

#------------------------------------------
def make_shell_context():
	return dict(app=app, db=db, User=User)

manager.add_command("shell", 
	Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()