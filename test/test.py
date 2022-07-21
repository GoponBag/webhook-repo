from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def api_root():
#     return "Wellcome to Git web api"

@app.route('/', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        a = json.dumps(request.json)
        data = json.loads(a)
        print(type(data))
        # print(d)
        for key, values in data.items():
            
            print(key, " : ", values)
        print("=================================================================================================")
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug = True)

