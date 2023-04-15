from flask import Flask, jsonify, request
app = Flask(__name__)
contacts = [{'Name':'Ram', 'Number':'2123'}, {'Name':'Geeta','Number':'9034'},{'Name':'Mukesh','Number':'3139'}]

@app.route('/get-contact')

def getContacts():
    return jsonify({'contact':contacts})

@app.route('/add-contact', methods = ['POST'])

def addContacts():
    if not request.json:
        return jsonify({'status':'error', 'message':'Please provide the data'}, 400)
    contact = {'Name':request.json['Name'], 'Number':request.json['Number']}
    contacts.append(contact)
    return jsonify({'status':'Success', 'message':'Contact Added Sucessfully'})
if __name__ == '__main__':
    app.run(debug = True)
print(contacts)