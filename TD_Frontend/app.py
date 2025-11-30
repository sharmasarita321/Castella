from flask import Flask, request, render_template
import requests

BACKEND_URL ="http://localhost:5000"
app =Flask(__name__)

@app.route('/')
def home():
     return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    try:
         request.post('http://localhost:5000/submit', json = form_data, timeout=5)

         return "Data submitted successfully!"
    except request. exceptions.connectionerror:
         return 'Error: could not connect to the backend',500
    except request. exceptions.timeout:
         return 'Error: backend request timed out',504
    
if __name__ == '__main__':
     app.run(host='localhost',port=9000,debug=True)
