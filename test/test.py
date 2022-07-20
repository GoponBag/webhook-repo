from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
    return "Wellcome to Git web api"

@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        a = json.dumps(request.json)
        print(a)
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug = True)

