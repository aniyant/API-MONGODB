#Task2,
# write a function to fetch data from mongodb table via api

from API_DB_task2 import makeConn,make_collection,find_data
from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/show',methods=['GET','POST'])
def showData():
    """
    This function takes public requests and authenticate  it and provides with data to valid users
    :return: json data
    """
    if (request.method == 'POST'):
        user = request.json['user']
        password = request.json['password']

    # Authenticating the user
    if user == "sunny" and password == "HappyCoding":

        ## make connection with database and fetch data
        makeConn()
        make_collection()
        data = find_data()

        return jsonify(str(data))

if __name__ == '__main__':
    app.run(port=9000)