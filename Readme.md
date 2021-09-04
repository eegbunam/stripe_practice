##### `source` [hackmd.io](https://hackmd.io/KvUOvAAtSCy79-6_4yMwww?both)
##### tags:  `tech` `React` `Python` `Flask` `Grafana` `ios` `Mobile Development` `Swift`

# Stripe with an iOS Application


## Introduction
- About a year ago I built a food delivery app that needed to integrate payment. I quickly learned about stripe and tried to integrate this service into my iOS application. The process of integrating stripe into my application was an unpleasant one because I had very little development experience at the time and there was no tutorial out there that properly helped me integrate stripe. As a teacher now and an avid learner I hope for this repository to serve as a resource for students/developers looking to integrate stripe into their applications


### Table of Contents

- [Web Server](#Server)
    - [Setup on replit](#Setup-on-replit)
    - [Setup Locally](#Running-Locally)
- [iOS Client](#Client)
- [Authors](#Author)

## Graphical Representation 

![](https://i.imgur.com/IGIdwwK.png)


#### Application Summary


- Before your iOS Client Application can submit a payment to stripe it must create a payment-intent with a client secret that can only be generated using server side code. Once the client seceret is generated, your server sends it back to your client iOS Application. Your iOS Client uses that client secret  to create a payment-intent. Using that payment intent the iOS Application can now proceed to making a payment.


## Server

### Setup on replit



**1. Install dependencies**

1. On repl, go to your `Shell` option on the top left
  - ![](https://i.imgur.com/UgSVAoE.png)
2. Run the following commands to install the necessary packages for running a Flask server
    
    ::: warning
    
      - `pip freeze > requirements.txt`
      - `pip install Flask`
      - `pip install requests`
      - `pip install stripe`

    :::


**2. Copy the template Stripe API Code to your Repl**

``` python=

#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe
# This is your real test secret API key.
stripe.api_key = "sk_my api key"

from flask import Flask, render_template, jsonify, request

#creates the slack application 
app = Flask(__name__, static_folder=".",
            static_url_path="", template_folder=".")


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400

#The @app.route() tells flask what fucntion to run when a particular route is requested
@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    '''
    This funnction create a payment Intent that stripe then uses on the client side to finalize payments
    '''
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd'
        )

        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__': #checks if the file name is being called
    app.run(host="0.0.0.0") # runs the app 
```

**3. Run you Flask server**

1. On repl, go to your `Shell` option on the top left and run:
    - `python app.py`


### Running Locally 
::: warning
 Be sure you have gone through the [Slides](https://docs.google.com/presentation/d/1mrHnMqVBasNG5_VF576c9o81Qxx25vR17HArpSuRLCw/edit?usp=sharing) first before following this instructions
:::
1.  **Create** a Python file name it app.py
4. Start your Virtual Env ==IMPORTANT==
    - Start a virtual env 
      - `python3 -m venv env`
    - Activate your virtual environment 
      - `source env/bin/activate`
5.  Now that you’re in your virtual environment you can install packages. Let’s install the Requests library from the Python Package Index (PyPI): 

    - ```pip3 install Flask```
    - ```pip3 install requests```
    - ```pip3 install stripe```
    - ```python3 -m pip3 install --user virtualenv```
    - ```pip3 freeze > requirements.txt```


     
5.  Head [here](https://dashboard.stripe.com/login?redirect=https://stripe.com/docs) and sign up or login into stripe
6. Then head to [iOS SDK Integrations](https://stripe.com/docs/payments/integration-builder)
    - You should have all these options selected
        - ![](https://i.imgur.com/BPJTBDB.png)
    - Add all the python code into your main.py file
        - To see the python file make sure you have all the options above selected 
7. Your file should look like what we have below but with  your api key
    - :warning: Stripe will fill in your api key for you in the file after you sign up
        
``` python=

#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe
# This is your real test secret API key.
stripe.api_key = "sk_my api key"

from flask import Flask, render_template, jsonify, request

#creates the slack application 
app = Flask(__name__, static_folder=".",
            static_url_path="", template_folder=".")


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400

#The @app.route() tells flask what fucntion to run when a particular route is requested
@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    '''
    This funnction create a payment Intent that stripe then uses on the client side to finalize payments
    '''
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd'
        )

        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__': #checks if the file name is being called
    app.run(host="0.0.0.0") # runs the app 
```


6. Run the command below in your terminal:
     ```bash=
     python3 app.py
     ```
     - You should have something like this show up on your terminal:
        ![](https://i.imgur.com/dL7jWTy.png)
        
    - Head to [localhost 5000](http://127.0.0.1:5000) you should see a hello world message. This means that your Flask web server is now up and runing at that url above.
        - :warning: Make sure to run your application or your local host will not show anything when you head to the link above
        
            

## Client


:x: **If you have never built an iOS application before be sure to follow this tutorial [here](https://www.youtube.com/watch?v=bZNAFkkUeKs) to get started.**


1. Head back to [iOS SDK Integrations](https://stripe.com/docs/payments/integration-builder)
2. Create a simple iOS Application
3. Copy and paste the code in **CheckoutViewController.swift** into your ViewController.swift(Replace Everything in your ViewController.swift)
    - Change the:
    - ```swift=
      class CheckoutViewController: UIViewController {}
        ```
        - to 
    - ```swift=
      class ViewController: UIViewController {}
        ```
    - Change the `backendUrl` to ```http://127.0.0.1:5000```
        - The backendUrl is a variable in your ViewController.swift
4. Run Your iOS Application
5. Make a test payment
6. Use a test card number to try your integration. These card numbers work in test mode with any CVC, postal code, and future expiry date. Stripe also has a set of international test cards to test specific postal code formats (e.g. only allow numerical values for U.S. zip codes).
    ```

    Payment succeeds

    4242 4242 4242 4242
    Payment requires authentication

    4000 0025 0000 3155
    Payment is declined

    4000 0000 0000 9995
    ```
7. Final Client Side Outcome should look like this:
    - ![](https://i.imgur.com/0VDkBOF.png)


## Author
- [Ebuka Egbunam](https://www.linkedin.com/in/ebukaegb/)

        
        
