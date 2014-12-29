from flask import Flask, request
from PIL import Image
from pytesseract import image_to_string

app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def hello():
    try:
        pic = request.files['image'];
        #print pic
        image = Image.open(pic);
        text = image_to_string(image);
        return text+"\n"
    except:
        return "Hello World"

if __name__ == "__main__":
    #app.debug = True
    app.run(port=6501)
