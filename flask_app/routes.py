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

     

    fp = open("out.json")
    items=json.load(fp)
    print(items)
    return render_template('videos.html',main_vid=items[0]["vid"], vid_list=items[:10])


if __name__ == '__main__':
    app.run(debug=True)
