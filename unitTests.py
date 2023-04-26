''' unit tests for the application in app.py'''
import unittest
from app import app
import requests

URL_HEAD = 'http://localhost:5000/'

USD_TEST_EXCHANGE_RATE = 3.8
USD_TEST_EXCHANGE_RATE_DATE = '2020-01-02'
CHF_TEST_EXCHANGE_RATE = 4.1355
CHF_TEST_EXCHANGE_RATE_DATE = '2021-03-15'



class Test(unittest.TestCase):

    # starting the app
    def setUp(self):
        #self.app = app.run()
        pass

    # testing get_average_exchange_rate() function
    def test_get_average_exchange_rate(self):
        # test for correct response from localhost
        response = requests.get(f'{URL_HEAD}average_exchange_rate?date={USD_TEST_EXCHANGE_RATE_DATE}&currency_code=USD')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        avg_exch_rate = data['average_exchange_rate']
        self.assertEqual(avg_exch_rate, USD_TEST_EXCHANGE_RATE)

        # test for CHF currency code
        response = requests.get(f'{URL_HEAD}average_exchange_rate?date={CHF_TEST_EXCHANGE_RATE_DATE}&currency_code=CHF')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        avg_exch_rate = data['average_exchange_rate']
        self.assertEqual(avg_exch_rate, CHF_TEST_EXCHANGE_RATE)


    # testing get_max_min_average() function
    def test_get_max_min_average(self):
        # test for correct response format not checking values (those cannot be checked because they change every day)
        # test for USD
        response = requests.get(f'{URL_HEAD}max_min_average?currency_code=USD&n=10')
        self.assertEqual(response.status_code, 200)

        # test for CHF
        response = requests.get(f'{URL_HEAD}max_min_average?currency_code=GBP&n=15')
        self.assertEqual(response.status_code, 200)

        # test for CHF
        response = requests.get(f'{URL_HEAD}max_min_average?currency_code=EUR&n=5')
        self.assertEqual(response.status_code, 200)


    # testing get_major_difference() function
    def test_get_major_difference(self):
        # test for correct response format not checking values (those cannot be checked because they change every day)
        # test for USD
        response = requests.get(f'{URL_HEAD}major_difference?currency_code=USD&n=10')
        self.assertEqual(response.status_code, 200)

        # test for EUR
        response = requests.get(f'{URL_HEAD}major_difference?currency_code=EUR&n=10')
        self.assertEqual(response.status_code, 200)

        # test for wrong currency code
        response = requests.get(f'{URL_HEAD}major_difference?currency_code=xyzabc&n=10')
        self.assertEqual(response.status_code, 404)

