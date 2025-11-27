from flask import Flask,request, render_template, json

app = Flask(__name__)

@app.route('/api')
def home():

    name = request.values.get('Name')
    age  = request.values.get('Age')
    email_Id = request.values.get('Email')
    age = int(age)

    Details ={
        'Name' : name,
        'Age'  : age,
        'email' : email_Id
              }
    file_path = "data.json"

    with open(file_path, 'w') as f:
            json.dump(Details , f, indent=4) 

    with open(file_path, 'r') as f:
        response = json.load(f)
        print("Loaded dictionary:", response)
    return response
    
if __name__ == '__main__':
    app.run(debug=True)

