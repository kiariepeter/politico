from flask import Flask,request,jsonify,Response

app = Flask(__name__)

@app.route('/add_party',methods = ['POST'])
def add_party():
    parties = {1:'Union Party',2:'Freedom party'}
    try:
        if request.method == "POST":
            if request.form['party_name']:
                parties.update({3:request.form['party_name']})
                return jsonify({'status':200,'parties':parties})
            else:
                return jsonify({'status':409,'message':'please enter party name'})
        else: 
            return jsonify({'status':405,'message':'The method is not allowed for the requested URL'}) 
    except Exception as e:
        return jsonify({'status':400,'message':'Bad Request kindly enter key values'})
    return jsonify({'status':500,'message':'Internal server error'})


if __name__ == "__main__":
    app.run(debug=True)