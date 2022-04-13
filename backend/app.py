import os
from flask import Flask, flash, request, redirect, url_for
import pandas as pd

UPLOAD_FOLDER = '.\\UploadedData'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/fileupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "No selected file"
        if file and allowed_file(file.filename):
            # save file to temp directory
            fname = file.filename
            file.save(fname)
            # read file
            df = pd.read_csv(fname)
            print(df)
            # calculate
            # get the result
            # remove file from temp directory
            os.remove(fname)
            return "Success!"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


app.run(debug=True)
