from flask import Flask, request, jsonify
from pyngrok import ngrok
from models.donor import Donor
from models.donation_request import Request
from database import Database
from mailer import Mailer

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
    request_values = request.get_json(force=True)

    request_values_parsed = Request(
        description=request_values['description'],
        blood_types=request_values['blood_types'],
        phone=request_values['phone'],
        donations=request_values['donations'],
        email=request_values['email'],
        date=request_values['date']
    )

    sql_query = request_values_parsed.create_sql_query()
    print(sql_query)
    donors_details = Database.send_query(sql_query)
    for donor in donors_details:
        Mailer.send_mail(
            donor.Email,
            'התקבלה בקשה לתרומה ממאגר התורמים',
            ('שלום, ' + '{}').format(donor.Name) + '\n\n' +
            str(request_values_parsed)
        )

    return '', 200

# Start ngrok.
url = ngrok.connect(5000)
print(' * Tunnel URL:', url)

app.run(port=5000)