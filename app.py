from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        prediction = model.predict([[age]])
        return render_template('result.html', prediction=prediction[0])
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(port=8081, host="0.0.0.0")
