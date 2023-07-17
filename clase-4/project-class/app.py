from flask import Flask, render_template
from models.user import User

app = Flask(__name__)

@app.route('/users')
def getUsers():
    users: User = [
        User("nombre1", 20, "email1@gmail.com"),
        User("nombre2", 21, "email2@gmail.com")
    ]

    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)