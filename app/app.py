from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>Hello, World</h1>'
    cursos = ['Python', 'Flask', 'Django', 'Ruby', 'Java']
    data = {
        'titulo': 'Home',
        'bienvenida': 'Bienvenido a mi sitio web',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)