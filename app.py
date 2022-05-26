from flask import Flask, render_template, request
import utils
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        open = float(request.form['Open'])
        high = float(request.form['High'])
        low = float(request.form['Low'])
        volume = float(request.form['Volume'])
        predicts = utils.predict_price(open, high, low, volume)
        value = str(predicts)[1:-1]
    return render_template('index.html', prediction_text='Predicted Stock Price: ${}'.format(value))


if __name__ == '__main__':
    app.run(debug=True)
