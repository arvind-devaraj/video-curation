from flask import Flask, render_template, request
import json

app = Flask(__name__)

 
# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    phrase = request.args.get("phrase")

    fp = open("../tv.json")
    items=json.load(fp)
    print(items)
    return render_template('videos.html',main_vid="", vid_list=items)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
