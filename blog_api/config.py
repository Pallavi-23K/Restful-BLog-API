
class Config:
    DB_USERNAME = 'root'
    DB_PASSWORD = 'Karthik@26'
    DB_HOST = 'localhost'
    DB_NAME = 'blog_db'

    # Make sure '@' is encoded as '%40' in the password for the connection string
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:Karthik%4026@localhost/blog_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   
    SECRET_KEY = "my_super_secret_key_123"
    JWT_SECRET_KEY = "my_jwt_secret_key_123"




'''import os

class Config:
    DB_USERNAME = 'root'
    DB_PASSWORD = 'Karthik@26'
    DB_HOST = 'localhost'
    DB_NAME = 'blog_db'

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD.replace('@', '%40')}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = "super-secret-key" ''' # better keep in .env
