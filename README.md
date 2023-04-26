# Internship_Dynatrace

recruitment project for internship

- to launch app on docker run 'docker compose up' in projects root directory
  (you will need docker running on your machine)
  - note: there is no image for api gateway like Nginx or Apache
  
- to launch app lockaly you will need a Python enviroment with dependancies:
  - flask
  - requests

- sample requests to API:
  - http://localhost:5000/average_exchange_rate?date=2020-01-02&currency_code=USD
  - ![image](https://user-images.githubusercontent.com/105457413/234606512-5486cdcd-8eb8-462a-8d71-50218b74b6bb.png)

  - http://localhost:5000/max_min_average?currency_code=USD&n=10
  - ![image](https://user-images.githubusercontent.com/105457413/234606677-a79d5888-ceb9-4ff6-b459-beb0859af6dd.png)

  - http://localhost:5000/major_difference?currency_code=USD&n=10
  - ![image](https://user-images.githubusercontent.com/105457413/234606758-c73c1d76-596e-49db-be94-c8371281fec6.png)

