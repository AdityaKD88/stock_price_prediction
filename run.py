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
        high = int(form.get('high'))
        low = int(form.get('low'))
        open = int(form.get('open'))
        close = int(form.get('close'))
        adj_close = int(form.get('adj_close'))
        userinp = [[high,low,open,close,adj_close]]
        prediction = model.predict(userinp)
        return render_template('index.html',high=high,low=low,open=open,close=close,adj_close=adj_close, prediction=prediction)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)