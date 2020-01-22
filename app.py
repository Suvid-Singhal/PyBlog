from flask import Flask, render_template, request, flash, url_for
from data import Articles
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getcwd()+'/articles'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Articles = Articles()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', articles=Articles)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part!')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file!')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            text = request.form['text']
            filename = secure_filename(text+".txt")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully!')
        else:
            flash('Please Select Text (.txt) Files!')
    return render_template('upload.html')

@app.route('/articles/<int:id>/')
def articles(id):
    text = open("articles/"+Articles[id-1].get("title",""), 'r+')
    content = text.read()
    text.close()
    return render_template('content.html', text=content,title=Articles[id-1].get("title",""))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()
