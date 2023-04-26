# Internship_Dynatrace

recruitment project for internship

- to launch app on docker run 'docker compose up' in projects root directory
  (you will need docker running on your machine)
  - note: there is no image for api gateway like Nginx or Apache
  
- to launch app lockaly you will need a Python enviroment with dependancies:
  - flask
  - requests

- sample requests to API (response format is json):
  - http://localhost:5000/average_exchange_rate?date=2020-01-02&currency_code=USD
  - {
      "average_exchange_rate": 3.8
    }

  - http://localhost:5000/max_min_average?currency_code=USD&n=10
  - {
      "max_average": 4.2261,
      "max_average_date": "2023-04-17",
      "min_average": 4.1557,
      "min_average_date": "2023-04-26"
    }

  - http://localhost:5000/major_difference?currency_code=USD&n=10
  - {
      "major_difference": 0.08499999999999996
    }

