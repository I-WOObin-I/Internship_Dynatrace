# Internship_Dynatrace

recruitment project for internship

1. you will need docker running on your machine
2. to launch container with the app run 'docker compose up' in projects root directory
3. make requests to api for example:
  - http://localhost:5000/average_exchange_rate?date=2020-01-02&currency_code=USD
  - http://localhost:5000/max_min_average?currency_code=USD&n=10
  - http://localhost:5000/major_difference?currency_code=USD&n=10
