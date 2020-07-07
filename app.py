from flask import Flask, request,  render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)*100
                  
    if output > 15:
        return render_template('index.html',pred= 'You have a Higher Risk of developing a CVD.Consult a Cardiologist today!')
    else:
        return render_template('index.html',pred='You are at a Low Risk of having Heart Disease.Checkout the exercises to improve your heart health!')
    

@app.route('/Consult_Doctor',methods=['GET', 'POST'])
def Consult_Doctor():
    return render_template('appointment.html')


@app.route('/Check_Health_Chart',methods=['GET', 'POST'])
def Check_Health_Chart():
    return render_template('Html1.html')
    

@app.route('/Excercises',methods=['GET', 'POST'])
def Excercises():
    return render_template('exercise.html')
 

    
if __name__ == "__main__":
    app.run(debug=True)
    

