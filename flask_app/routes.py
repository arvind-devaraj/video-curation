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

    #vids =get_vid_list(pl_id)
    items=[{"vid":"ZVR2Way4nwQ","tags":["abc","def"]},
          {"vid":"sgQAhG5Q7iY"},
          {"vid":"YaKMeAlHgqQ"},
          {"vid":"h0e2HAPTGF4"},
          {"vid":"ofM8LE9Zeaw"} ]

    fp = open("out.json")
    items=json.load(fp)
    print(items)
    return render_template('videos.html',main_vid=items[0]["vid"], vid_list=items)


if __name__ == '__main__':
    app.run(debug=True)
