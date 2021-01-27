from flask import Flask, request, jsonify
from pyngrok import ngrok
from models.donor import Donor
from database import Database

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/donor', methods=['POST'])
def api_add_donor():
    donor_values = request.get_json(force=True)

    donor_values_parsed = Donor(
        email=donor_values['email'],
        name=donor_values['name'],
        gender=donor_values['gender'],
        blood_type=donor_values['blood_type'],
        phone=donor_values['phone'],
        birthdate=donor_values['birthdate'],
        donations=donor_values['donations']
    )

    Database.execute_query('insert into Donors values (?,?,?,?,?,?)', donor_values_parsed.get_object())
    [
        Database.execute_query(
            'insert into DonorsDonations values (?,?)',
            (donor_values_parsed.email, donation)
        )
        for donation in donor_values_parsed.donations
    ]

    return '', 200

@app.route('/api/donation', methods=['POST'])
def api_request_donation():
    pass

@app.route('/api/test', methods=['GET'])
def api_test():
    return 'Test!', 200



# Start ngrok.
url = ngrok.connect(5000)
print(' * Tunnel URL:', url)

app.run(port=5000)