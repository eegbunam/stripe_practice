from flask import Flask, render_template, jsonify, request
import json
import os
import stripe
from decouple import config


stripe.api_key = config('STRIPE_API_KEY') # create a .env file and add your key into that file. Name your key 'STRIPE_API_KEY'

app = Flask(__name__)

@app.route('/create-payment-intent', methods=['POST','GET'])
def create_payment():
    '''
    This function creates the payment intent using stripe's api and returns a client secret
    that can be used any client
    '''
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

if  __name__ == "__main__":
    app.run(debug=True , use_reloader = False)
