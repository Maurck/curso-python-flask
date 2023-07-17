from flask import Flask, render_template
from models.user import User

app = Flask(__name__)

@app.route('/users')
def getUsersInfoView():
    users: User = [User("Pablito", 20, "pablito1@gmail.com"), User("Maria", 25, "maria1@gmail.com")]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)