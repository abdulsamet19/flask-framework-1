from  flask  import  Flask 
app = Flask(__name__)
@app.route("/")
def head():
    return "hello word clarusway-18"

if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)