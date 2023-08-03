from Project_app.utils  import medicalInsurance
from Project_app import config
from flask import Flask,jsonify,render_template,request


app = Flask(__name__)

@app.route('/')
def insurance_model():
    print("welcome to insurance prdictor")
    return render_template('index.html')


@app.route('/predict_charges', methods = ['GET','POST'])
def get_insurance_charges():
    if request.method =='POST':
        data = request.form
        age = eval(data["age"])
        sex = data["sex"]
        bmi = eval(data['bmi'])
        children = eval(data["children"])
        smoker = data['smoker']
        region = data['region']

        med_ins = medicalInsurance(age, sex, bmi, children, smoker, region)
        Charges = med_ins.get_predicted_charges()
        return jsonify({'Result': f"Charges for Medical Insurance are : RS. {round(Charges[0], 2)}"})
    else:
        data1 = request.args
        age = eval(data1.get("age"))
        sex = data1.get("sex")
        bmi = eval(data1.get('bmi'))
        children = eval(data1.get("children"))
        smoker = data1.get('smoker')
        region = data1.get('region')

        med_ins1 = medicalInsurance(age, sex, bmi, children, smoker, region)
        Charges1 = med_ins1.get_predicted_charges()
        return jsonify({'Result': f"Charges for Medical Insurance are : RS. {round(Charges1[0], 2)}"})



    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=True)