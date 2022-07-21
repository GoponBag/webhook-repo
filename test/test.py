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
        print("###############################################################################################")
        # for key, values in data.items():
        #     print(key, " : ", values)
        # if data["commits"] :
        #     print(data["commits"][0]['author']['username'])
        #     print(data['ref'])
        #     print(data['commits'][0]['timestamp'])
        #     print("commit===========================================================================================")
        # if data["pull_request"]:
        #     print("AUTHOR")
        #     print(data["pull_request"]["base"]['label'])
        #     print("TO -" )
        #     print(data["pull_request"]["head"]["ref"]  )
        #     print("FROM - ")
        #     print(data["pull_request"]["base"]["ref"])
        #     print( 'Time')
        #     print(data["pull_request"]["updated_at"])
        #     print('Pull Request ==============================================================================================')
        # else:
        #     print (a)
        
        

        print( a )
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug = True)

