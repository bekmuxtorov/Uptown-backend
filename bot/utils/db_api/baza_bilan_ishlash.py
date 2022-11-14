
import sqlite3

class Database:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db=path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql:str, parametrs: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parametrs:
            parametrs = ()
        
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parametrs)

        if commit:
            connection.commit()
        
        if fetchall:
            data = cursor.fetchall()

        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
            CREATE TABLE myfiles_teacher (
                id int NOT NULL,
                Name varchar(255) NOT NULL,
                email varchar(255),
                language varchar(3),
                PRIMARY KEY (id)
            );
        """

        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += " AND  ".join([
            f"{item} = ?" for item in parametrs
        ])
        return sql, tuple(parametrs.values())

    def add_user(self, id: int, name: str, email: str=None, language: str = "uz"):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name,email) VALUES(1, 'Jonh', 'binnasa@gamil.com')"

        sql = """
        INSERT INTO users(id, Name, email, language) VALUES(?, ?, ?, ?)

        """
        self.execute(sql, parametrs=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM myfiles_teacher WHERE "
        sql, parametrs =self.format_args(sql, kwargs)

        return self.execute(sql, parametrs=parametrs, fetchone=True)
    
    def count_user(self):
        return self.execute("SELECT COUNT(*) FROM foydalanuvchilar;", fetchone=True)

    def update_user_email(self,email, id):
        pass

    def foydalanuvchi_qoshish(self, first_name: str, username: str, tg_id: int, last_name: str=None):
        # SQL_EXAMPLE = "INSERT INTO myfiles_teacher(id, Name,email) VALUES(1, 'Jonh', 'binnasa@gamil.com')"

        sql = """
        INSERT INTO pages_user(first_name, last_name, username, tg_id) VALUES(?, ?, ?, ?)

        """
        self.execute(sql, parametrs=(first_name, last_name, username, tg_id), commit=True)

    def select_users(self):
        sql = """
            SELECT * FROM foydalanuvchilar
        """
        return self.execute(sql, fetchall=True)

    def foydalanuvchilar_soni(self):
        return self.execute("SELECT COUNT(*) FROM foydalanuvchilar;", fetchone=True)

    # OFFER BOOKS    
    def select_offer_works(self):
        sql = """
        SELECT * FROM pages_offerworks
        """
        return self.execute(sql, fetchall=True)

    # HAPPY CLIENTS
    def select_happy_clients(self):
        sql = """
        SELECT * FROM pages_happyclients 
        """
        return self.execute(sql, fetchall=True)

    # AGENTS
    def select_agents(self):
        sql = """
        SELECT * FROM pages_agents 
        """
        return self.execute(sql, fetchall=True)
       
    # ResentBlog
    def select_resent_blogs(self):
        sql = """
        SELECT * FROM pages_resentblog 
        """
        return self.execute(sql, fetchall=True)

    def select_auth_users(self):
        sql = """
        SELECT * FROM auth_user
        """

        return self.execute(sql, fetchall=True)
    

    def select_uzbek(self, **kwargs):
        sql = "SELECT * FROM uzbek_adabiyoti WHERE "
        sql, parametrs =self.format_args(sql, kwargs)

        return self.execute(sql, parametrs=parametrs, fetchone=True)

    
def logger(statement):
    print(f"""
    {'-'*20}
    Executing:
    {statement}
    {'-'*20}

    """)