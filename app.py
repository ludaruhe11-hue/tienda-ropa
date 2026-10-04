from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'clave_secreta_123'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        if usuario == 'admin' and contrasena == '1234':
            session['usuario'] = usuario
            return redirect('/tienda')
        else:
            return "Usuario o contraseña incorrectos <a href='/'>Volver</a>"
    return render_template('login.html')

@app.route('/tienda')
def tienda():
    if 'usuario' not in session:
        return redirect('/')
    productos = [
        {"nombre": "Playera Negra", "precio": 299, "img": "/static/playera.jpg"},
        {"nombre": "Jeans Azul", "precio": 599, "img": "/static/jeans.jpg"},
        {"nombre": "Sudadera Gris", "precio": 499, "img": "/static/sudadera.jpg"},
    ]
    return render_template('tienda.html', productos=productos, usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)