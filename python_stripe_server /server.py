from flask import Flask, render_template, jsonify, request
import json
import os
import stripe
from decouple import config


stripe.api_key = config('STRIPE_API_KEY')


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World Stripe</h1>"



@app.route('/create-payment-intent', methods=['POST','GET'])
def create_payment():
    try:
        data = json.loads(request.data)
        print(data)
        intent = stripe.PaymentIntent.create(
            amount= 10000,
            currency='usd'
        )
        print(intent)
        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/test') #Automatically makes it a GET request if no Method parameters are passed
def test_Method():
    return "<h1>This is a test Method to check the health of my Flask server </h1>"

if  __name__ == "__main__":
    app.run(debug=True , use_reloader = False)
