from flask import Flask, render_template, request, send_file, redirect
from mimetypes import guess_type
from modules.download_file import download_file
from modules.utils import sizeof
from os.path import join, getsize
from os import listdir, unlink

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto'] 
        return render_template('/descargando.html', texto = texto)
    else:
        return render_template('index.html')
    
@app.route('/downloads/<path:nombre_archivo>')
def descargar_archivo(nombre_archivo):
    print(nombre_archivo)
    ruta_archivo = join('downloads', nombre_archivo)    
    mimetype = guess_type(ruta_archivo)[0]
    return send_file(ruta_archivo, as_attachment=True, mimetype=mimetype, download_name=nombre_archivo)


@app.route('/descargando')
def cargando():
    texto = request.args.get('texto')
    download_file(texto)
    return redirect('/files')



@app.route('/files')
def ver_archivos():
    elementos = []
    for num, file in enumerate(listdir('downloads')):
        elementos.append( (num+1, 
                           'downloads/' + file, 
                           file, 
                           sizeof(getsize(join('downloads', file)))) )
        
    return render_template('archivos.html', elementos=elementos)


@app.route('/borrar')
def borrar():
    file = request.args.get('file')
    unlink(file)
    return redirect('/files')



if __name__ == '__main__':
    app.run(debug=True)