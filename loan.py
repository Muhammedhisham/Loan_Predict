from flask import Flask,request,render_template
import pickle
app=Flask(__name__)


with open(r'C:\Users\hisha\Desktop\Python\Loan_Predicter\Loan.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = float(request.form['Gender'])
        Married = float(request.form['Married'])
        Dependents = float(request.form['Dependents'])
        Education = float(request.form['Education'])
        Self_Employed = float(request.form['Self_Employed'])
        Property_Area = float(request.form['Property_Area'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        LoanAmount = float(request.form['LoanAmount'])
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed, Property_Area, Property_Area, Loan_Amount_Term, LoanAmount, ApplicantIncome, CoapplicantIncome]])
        prediction = int(prediction[0])
        print('prediction=', prediction)
        Loan=''
        if prediction==0:
            Loan='NOT APPROVED'
        else:
            Loan="LOAN APPROVED"
        return render_template('index.html', prediction=Loan)


if __name__ == '__main__':
    app.run(debug=True, port=5002)