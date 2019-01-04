from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session



app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
	images = open("URLS.txt", "wb").read().split("\n")
	return render_template("template.html", images=images)

if __name__ == '__main__':
    app.run()
