from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, send_file
from selenium import webdriver
from util import fetch_image_urls

app = Flask(__name__)
CORS(app)  # to bypass CORS in browser

DRIVER_PATH = "./chromedriver.exe"  # path or chrome web driver
NO_OF_IMAGES = 10  # no of images to download


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/images", methods=["POST"])
@cross_origin()
def images():
    # fetch query string from form submitted
    query = request.form['query']

    # initialise chrome web driver of selenium
    with webdriver.Chrome(executable_path=DRIVER_PATH) as wd:
        # fetch all image urls
        urls = fetch_image_urls(query, wd=wd, no_of_images=NO_OF_IMAGES)

    return render_template("images.html", urls=urls)


if __name__ == '__main__':
    app.run(debug=True)
