import psycopg2,random,string
from flask import Flask, redirect, render_template, request, url_for,flash,session
from config import db_host,db_name,db_user,db_user_pass, flask_secret_key
from datetime import date,datetime
from flask_login import LoginManager, login_required, login_user, logout_user
from user_login_class import UserLogin
from md5_hash import calculate_md5_hash



app = Flask(__name__)

app.secret_key = flask_secret_key  #секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_user_pass}@{db_host}/{db_name}'
db = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
db.autocommit = True

login_manager = LoginManager(app)



@app.route('/', methods=['POST','GET'])
def create_short_url():
    cursor = db.cursor()
    
    if request.method=='POST':
        user_url = str(request.form['url_from_user']).replace('ㅤ','').replace(' ','')

        cursor.execute(f"select search_id from short_url where url_forward ='{user_url}'")
        try:
            url_search_id = cursor.fetchone()[0]
        except:
            url_search_id=''
        
        if bool(len(url_search_id)):
            redirect_url = f'https://cringe.fun/{url_search_id}'
            flash(f' {str(redirect_url)}')
        else:
            
            now = datetime.now()
            now_date = str(now.date())
            redirect_url_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
            
            redirect_url = f'https://cringe.fun/{redirect_url_id}'
            cursor.execute(f"insert into short_url(search_id,url_forward,add_date) values ('{redirect_url_id}','{user_url}','{now_date}')")
            flash(f' {str(redirect_url)}')
            
        return render_template('index.html')
    else:
        return render_template('index.html')




@app.route('/<string:search_id>')
def redirect_to_full_url(search_id):
    cursor = db.cursor()
    cursor.execute(f"select url_forward from short_url where search_id = '{search_id}'")
    url_before = cursor.fetchone()
    
    if url_before == None:
        return render_template('404.html')
    else:    
        try:
            url = 'https://'+ url_before[0].replace('https://','').replace('http://','')
        except:
            url = f'https://{url_before[0]}'
        return redirect(f'{url}')



@app.route('/login', methods=['POST','GET'])
def admin_login():
    cursor = db.cursor()    
    if request.method=='POST':
        user_login_input = request.form['form__input_login']
        cursor.execute(f"select login from users where login='{user_login_input}'")
        if cursor.fetchone():
            user_pass = request.form['form__input_pass']
            cursor.execute(f"select * from users where login='{user_login_input}' and password='{calculate_md5_hash(user_pass)}'")
            user_data = cursor.fetchone()
            if user_data:
                user_login = UserLogin().create(user_login_input)
                login_user(user_login)
                return redirect('/admin')
            else:
                flash(f'The password is incorrect')
                return  render_template('login.html') 
        else:
            flash(f'The user does not exist')
            return render_template('login.html')       
    else:
        return render_template('login.html') 



@app.route('/admin', methods=['POST','GET'])
@login_required
def admin_panel():
    cursor = db.cursor()    
    if request.method=='POST':
        pass
    
    else:
        return render_template('admin.html')
        



@app.route('/logout')
@login_required
def user_logout():
    logout_user()
    return redirect('/')




@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().from_DB(user_id, db.cursor())




# 404 page
@app.errorhandler(404)
# @app.errorhandler(AttributeError)
# @app.errorhandler(UnicodeEncodeError)
# @app.errorhandler(TypeError)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')