from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    mensagem = "Comunicação entre Front End e Back End funcionando com Python + Flask!"
    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)