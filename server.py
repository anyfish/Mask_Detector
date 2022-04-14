from flask import Flask
from flask import render_template, request, url_for

app = Flask(__name__)
PORT = 5000
DEBUG = True

# Ruta si el archivo no se encuentra
@app.errorhandler(404)
def not_found(error):
    return "Not Found"

# Ruta de la visualización
@app.route('/', methods=['GET'])
def index():
    name ="Luis"
    ap="Estrada"
    return render_template('index3.html', name=name, ap= ap)
    #return render_template('index.html')

@app.route('/home', methods=['POST'])
def Home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=PORT,debug=DEBUG)
