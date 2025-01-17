from flask import Flask, render_template
import psycopg2

def create_app():
    app = Flask(__name__)

    def get_db_connection():
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='postgres',
            host='db'
        )
        return conn

    @app.route("/test")
    def hello():
        return "<h1 style='color:blue'>Hello There!</h1>"

    @app.route("/")
    def dasboard():
        return render_template("index.html")
    
    @app.route("/db_test")
    def db_test():
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT 1')
            cur.close()
            conn.close()
            return "<h1 style='color:green'>Database connection successful!</h1>"
        except Exception as e:
            return f"<h1 style='color:red'>Database connection failed: {e}</h1>"
    
    return app