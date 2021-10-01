from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import pymysql
import json
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'your-user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your-password'
app.config['MYSQL_DATABASE_DB'] = 'your-database'
app.config['MYSQL_DATABASE_HOST'] = 'your-host'
mysql.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        details = json.loads(request.data)

        email = details['username']
        password = details['password']
        print(email,password)
        if email and password and request.method == "POST":
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute('SELECT * FROM Users  WHERE email = %s',email)
            record = cursor.fetchone()
            print(record)
            if record['password'] == password :
                print('loggedin')
                response = jsonify({'message': 'successful login '})
            else:
                print('no')
                resp = jsonify({'message': 'failed login '})

            resp.status = 200
            return resp
    except Exception as e:
        print('hello',e)
    finally:
        conn.close()
        cursor.close()
    return "Done"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)