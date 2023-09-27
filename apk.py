from flask import Flask, render_template, request, redirect,jsonify, url_for

app = Flask(__name__)

# Database sederhana untuk menyimpan data pasien
patients = []

class Patient:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

@app.route('/')
def index():
    return render_template('index.html', patients=patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    id = len(patients) + 1
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    
    patient = Patient(id, name, age, gender)
    patients.append(patient)
    return render_template('pasien.html', patients=patients)
    

@app.route('/search', methods=['POST'])
def search():
    search_name = request.form.get('search_name')
    search_result = [patient for patient in patients if search_name.lower() in patient.name.lower()]
    return render_template('search.html', search_result=search_result, search_name=search_name)

if __name__ == '__main__':
    app.run(debug=True)
