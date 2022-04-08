from flask import Flask, render_template
import pickle

app = Flask(__name__)

def load_model():
    filepath = 'ml_src/hepatitis.pkl'
    return pickle.load(filepath)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 