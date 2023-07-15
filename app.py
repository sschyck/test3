import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, render_template

# Load credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', ['https://www.googleapis.com/auth/spreadsheets'])

# Authenticate and open the Google Sheet
client = gspread.authorize(credentials)
sheet = client.open('Sarah_Defense').sheet1  # Replace 'Your Google Sheet Name' with the actual name of your Google Sheet

app = Flask(__name__)

@app.route('/rsvp', methods=['POST'])
def rsvp():
    name = request.form.get('name')
    email = request.form.get('email')
    attending = request.form.get('attending')
    guests = request.form.get('guests')
    event = request.form.get('event')

    # Prepare the row of data
    row = [name, email, attending, guests, event]

    # Append the row to the Google Sheet
    sheet.append_row(row)

    return 'RSVP data received and added to Google Sheets!'

if __name__ == '__main__':
    app.run(debug=True)
