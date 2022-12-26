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


@app.route('/test', methods=['POST'])
def test():
    print(request.json)
    tags=request.json["tags"]
    fp = open("../tv.json")
    items=json.load(fp)
    new_items={}
    for item in items:
        if (item in tags):
            new_items[item]=items[item]

    print(new_items)


    return render_template('videos.html',main_vid="", vid_list=new_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
