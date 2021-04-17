from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 7500


@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():


    
    country_list = ['Canada', 'China', 'Russia', 'Australia', 'US','France']

    gas_g = [1250, 2380, 1790, 1180, 2750, 1460]
   
    nuke_g=[1100,2100,1750,1150,2500,1400]
    hyd_g=[1000,1850,1500,1000,2350,1250]
    coal_g=[850,1550,1320,890,2010,1000]
                

    result_dict = {
        'countries': country_list,
        'title': 'Yearly energy production ',
        'subtitle': 'Source: ourworldindata.org',
        'gas_gen': gas_g,
        'nuke_gen': nuke_g,
        'hyd_gen': hyd_g,
        'coal_gen': coal_g,
        
    }

    return jsonify(result_dict)

    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
