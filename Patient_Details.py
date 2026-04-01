
from calendar import error

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

patient_list = []


def add_patient(name, age, gender):
    patient = {
        "name": name,
        "age": age,
        "gender": gender
    }
    patient_list.append(patient)
    print("successfully added patient")


def view_patient():
    return patient_list


def remove_patient(delete_patient):
    for patient in patient_list:
        if patient["name"].lower() == delete_patient.lower():
            patient_list.remove(patient)
            print("successfully removed patient")
            break



@app.route('/')
def home():
    return render_template("index.html", patients=patient_list
@app.route('/add', methods=['POST'])

                           
def add():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']

    add_patient(name, age, gender)
    return redirect('/')



@app.route('/remove', methods=['POST'])
def remove():
    name = request.form['name']
    remove_patient(name)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
