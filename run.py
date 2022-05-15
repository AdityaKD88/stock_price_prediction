from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('ml_src/model_v1.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def index():
    if request.method=="POST":
        form=request.form
        high = float(form.get('high'))
        low = float(form.get('low'))
        open = float(form.get('open'))
        close = float(form.get('close'))
        adj_close = float(form.get('adj_close'))
        userinp = [[high,low,open,close,adj_close]]
        prediction = model.predict(userinp)
        output = round(prediction[0], 2)
        return render_template('index.html',high=high,low=low,open=open,close=close,adj_close=adj_close, output=output)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)