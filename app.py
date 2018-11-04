import os
from flask import Flask, render_template, request, url_for
import file

UPLOAD_FOLDER = 'static/doc'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'doc' in request.files:
        data=request.files['doc']
        data.save(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
#        filename = docs.save(request.files['doc'])
        file.start(data.filename)
        url=url_for('static', filename='Awesomevideo.mp4')
        return render_template('results.html', link=url)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
