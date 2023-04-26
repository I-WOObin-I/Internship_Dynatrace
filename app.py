import requests
from flask import Flask, jsonify, request, abort

URL_HEAD = "http://api.nbp.pl/api/exchangerates/rates/"

app = Flask(__name__)

# Given a date and currency code, provide the average exchange rate
@app.route('/average_exchange_rate')
def get_average_exchange_rate():

    # get parameters from request
    date = request.args.get('date')
    currency_code = request.args.get('currency_code')

    # get data from NBP API
    url = f'{URL_HEAD}a/{currency_code}/{date}/'

    try:
        url_response = requests.get(url)
    except requests.exceptions.RequestException as e:
        abort(404)

    if url_response.status_code == 404:
        abort(404)

    data = url_response.json()

    # get average exchange rate from data returned by NBP API
    avg_exch_rate = data['rates'][0]['mid']

    response = {
        'average_exchange_rate': avg_exch_rate
    }

    return jsonify(response)


# Given a currency code and the number of last quotations N, provide the max and min average values
@app.route('/max_min_average')
def get_max_min_average():

    # get parameters from request
    currency_code = request.args.get('currency_code')
    n = int(request.args.get('n'))

    # get data from NBP API
    url = f'{URL_HEAD}a/{currency_code}/last/{n}/'

    # try to get data from NBP API and return 404 if failed or got 404 from NBP API
    try:
        url_response = requests.get(url)
    except requests.exceptions.RequestException as e:
        abort(404)

    if url_response.status_code == 404:
        abort(404)

    data = url_response.json()

    # get start values for max and min average from first quotation
    rates = data['rates']
    max_avg = rates[0]['mid']
    max_avg_date = rates[0]['effectiveDate']
    min_avg = rates[0]['mid']
    min_avg_date = rates[0]['effectiveDate']

    # iterate through all quotations and update max and min average if needed
    for rate in rates:

        # get values from quotation
        mid = rate['mid']
        effectiveDate = rate['effectiveDate']

        # update max and min average if needed
        if mid > max_avg:
            max_avg = mid
            max_avg_date = effectiveDate
        if mid < min_avg:
            min_avg = mid
            min_avg_date = effectiveDate

    response = {
        'max_average_date': max_avg_date,
        'max_average': max_avg,
        'min_average_date': min_avg_date,
        'min_average': min_avg
    }
    return jsonify(response)


# Given a currency code and the number of last quotations N, provide the major difference between the buy and ask rate
@app.route('/major_difference')
def get_major_difference():

    # get parameters from request
    currency_code = request.args.get('currency_code')
    n = int(request.args.get('n'))

    # get data from NBP API
    url = f'{URL_HEAD}c/{currency_code}/last/{n}/'

    # try to get data from NBP API, if currency code is invalid return 404
    try:
        url_response = requests.get(url)
    except requests.exceptions.RequestException as e:
        abort(404)

    if url_response.status_code == 404:
        abort(404)

    data = url_response.json()

    rates = data['rates']
    biggest_major_difference = 0

    # iterate through all quotations and update major difference if needed
    for rate in rates:

        # get values from quotation
        ask = rate['ask']
        bid = rate['bid']

        # update major difference if needed
        current_major_difference = abs(ask - bid)
        if abs(ask - bid) > biggest_major_difference:
            biggest_major_difference = current_major_difference

    response = {
        'major_difference': biggest_major_difference
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
