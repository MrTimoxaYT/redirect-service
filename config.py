from os import getenv
from dotenv import load_dotenv
load_dotenv()

db_host=getenv('db_host')
db_name=getenv('db_name')
db_user=getenv('db_user')
db_user_pass=getenv('db_user_pass')
flask_secret_key = getenv('flask_secret_key')

