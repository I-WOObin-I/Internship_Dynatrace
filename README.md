# Internship_Dynatrace

recruitment project for internship

- to launch app on docker run 'docker compose up' in projects root directory
  (you will need docker running on your machine)
- to launch app lockaly you will need a Python enviroment with dependancies:
  - flask
  - requests

- sample requests to API:
  - http://localhost:5000/average_exchange_rate?date=2020-01-02&currency_code=USD
  - http://localhost:5000/max_min_average?currency_code=USD&n=10
  - http://localhost:5000/major_difference?currency_code=USD&n=10
