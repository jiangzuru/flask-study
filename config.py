#coding:utf-8

class Config(object):
	SECRET_KEY = "983UERiuwiueiuw"
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://lincox:655334linkong@localhost:3306/stu"


	@staticmethod
	def init_app(app):
		pass

class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_ECHO = True


config = {'default':DevConfig}