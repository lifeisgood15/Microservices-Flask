from flask import Flask, jsonify, request 
app = Flask(__name__)

emogis = [ {"emotion":"happy","emogi":":)"}, {"emotion":"sad","emogi":":("}, {"emotion":"funny","emogi":":P"},{"emotion":"wink","emogi":";)"},{"emotion":"kiss","emogi":":*"}]

@app.route('/emogi',methods=['GET'])
def getAllEmogis():
    return jsonify({'Emogis':emogis})

@app.route('/emogi/<string:emotion>',methods=['GET'])
def getOneEmogi(emotion):
    emo = [emogi for emogi in emogis if (emogi['emotion']==emotion)]
    return jsonify({"result":emo[0]})

@app.route('/emogi', methods=['POST'])
def addNewEmogi():
    newEmogi = {"emotion":request.json['emotion'], "emogi":request.json['emogi']}

    emogis.append(newEmogi)

    return jsonify({"Updated":emogis})

@app.route('/emogi/<string:emotion>',methods=['PUT'])
def updateOneEmogi(emotion):
    emogiToUpdate = [emogi for emogi in emogis  if(emogi['emotion']==emotion)]
    emogiToUpdate[0]['emogi'] = request.json['emogi']

    return jsonify({"Updated one emogi":emogiToUpdate[0]})

@app.route('/emogi/<string:emotion>',methods=['DELETE'])
def deleteOneEmogi(emotion):
    emogiToDelete = [emogi for emogi in emogis  if(emogi['emotion']==emotion)]
    emogis.remove(emogiToDelete[0])
    return jsonify({"Result after removal":emogis})


