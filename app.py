from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/aboutus')
def aboutus():
    return render_template('cryptoo.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']

        db = mysql.connector.connect(
            host='sql12.freesqldatabase.com',
            user='sql12624615',
            password='1HzdZwzDI7',
            database='sql12624615'
        )

        cursor = db.cursor()
        cursor.execute("INSERT INTO solution (name, number) VALUES (%s, %s)", (name, number))
        db.commit()
        cursor.close()
        db.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3306)
