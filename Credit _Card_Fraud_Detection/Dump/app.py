from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    form_data = [float(request.form.get(f'V{i}')) for i in range(1, 29)]
    amount = float(request.form.get('Amount'))

    # Make prediction using your model (replace with actual prediction logic)
    # For example, `prediction = model.predict([form_data + [amount]])`
    prediction = 0  # Replace with actual prediction logic

    # Convert prediction to readable format
    if prediction == 0:
        result = "Normal Transaction"
        color = "green"
    else:
        result = "Fraudulent Transaction"
        color = "red"
    # Redirect to the result page with the prediction result
    return redirect(url_for('result', prediction=result))

@app.route('/result')
def result():
    prediction = request.args.get('prediction')
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
