class UserLogin():
    
    def from_DB(self, user_login, cursor):
        cursor.execute(f"select * from users where login='{user_login}'")
        self.__user = cursor.fetchone()
        return self
    
    def create(self, user):
        self.__user = user
        return self
    
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.__user[0])