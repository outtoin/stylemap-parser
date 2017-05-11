from flask import Flask, render_template, request, url_for, send_from_directory, redirect
from werkzeug import secure_filename
import sys, os

sys.path.insert(0, '../stylemap-work/')

UPLOAD_FOLDER = 'file/'
ALLOWED_EXTENSIONS = set(['xlsx', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/return-files')
def return_files():
 	return send_from_directory(directory='file', filename='Variable_Product.csv', as_attachment=True)

@app.route('/')
def main():
	return redirect('/upload')

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   	if request.method == 'POST':
	  	file = request.files['file']

	  	if file and allowed_file(file.filename): 
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			columnSize = request.form['column_size']
			rowSize = request.form['row_size']
			import stylemap
			stylemap.run(os.path.join(app.config['UPLOAD_FOLDER'], filename), app.config['UPLOAD_FOLDER'], columnSize, rowSize)

	return render_template('upload_complete.html')
		
if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=5000)