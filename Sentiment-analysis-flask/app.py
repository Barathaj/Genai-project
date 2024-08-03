from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()
model = genai.GenerativeModel(model_name='gemini-1.0-pro')


app = Flask(__name__)

def prompt(feedback):
    prompt_template=f"""
        ### Role:
        - You are Sentiment Classification model. 

        ### feedback:
        {feedback}

        ### Task :
        - Classify feedback into "P" or "N" category.

        ### Guidelines:
        - return only category in output .
        
        ### Example:
        1.feedback : what a lovely product.
        sentiment:P
        2. feedback : poor quality product.
        sentiment:N

    """
    res=model.generate_content(prompt_template)
    return res.text
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('thankyou', name=name))

@app.route('/thankyou')
def thankyou():
    name = request.args.get('name')
    result=prompt(name)
    return render_template('thankyou.html', name=result)

if __name__ == '__main__':
    app.run(debug=True)