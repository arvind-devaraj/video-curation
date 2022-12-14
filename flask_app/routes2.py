from flask import Flask, render_template, request
import json

app = Flask(__name__)

 
# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
  
    return render_template('videos.html')


@app.route('/test')
def render_playlist():

     

    fp = open("../tv.json")
    items=json.load(fp)
    print(items)
    return render_template('videos.html',main_vid=items["Deep Learning"][0], vid_list=items["Deep Learning"])


if __name__ == '__main__':
    app.run(debug=True)
