from flask import Flask

app = Flask(__name__)

@app.get('/post')
def index():
    # crea post
    # adada
    return {
        'action': 'create_post',
        'user': {
            'email': 'a'
        }
    }

@app.get('/me_llamo_tal')
def me_llamo_tal():
    return 'me llamo tal'

if __name__ == "__main__":
    app.run(debug=True)
