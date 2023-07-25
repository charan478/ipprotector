from flask import Flask
app = Flask(__name__)

@app.route('/validate/<licenceId>')
def hello_name(licenceId):
    if(licenceId == "test123poc"):
        return 'abc123'
    else:
        return 'Invalid Id'

if __name__ == '__main__':
    app.run()
