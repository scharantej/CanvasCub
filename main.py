
# main.py
from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Route to submit drawing
@app.route('/submit_drawing', methods=['POST'])
def submit_drawing():
    drawing = request.files['drawing']
    filename = drawing.filename
    drawing.save(os.path.join('static', filename))
    return redirect(url_for('gallery'))

# Gallery route
@app.route('/gallery')
def gallery():
    images = os.listdir('static')
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
