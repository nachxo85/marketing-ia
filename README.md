# IA on Digital Marketing on SPA clients
This is the TFM for Kschool Master degree in Data science and it's based on SPAs predicting optimal price based on old prices in the same services and predict the sales numbers and the sales revenue.

## Objective
This project has the goal of know the optimal price for every service based on the elastic price (contrast price vs number of sales).
Also, it's has a second goal, does a prediction about the number of sales and revenue of sales.

## Project Overview
The project contains the following steps(that match on each notebook):
* 0.Adquisition Data: Get the data from the private api and dump to csv (example, as is but not functional, because the api is from a private company).
* 1.Markets Insigths: market study about the keywords (on diferent countries, for study correlation of keywords and customers come from )
* 2.Exploration_and_services_analytics: Exploring data and analysis of service historic.
* 3.Forecast revenue and sales: Building and training the model to predict revenue and number of sales.
* 4.Forecast Optimal price based on cash disconts history: Building and training the model to predict the better optimal price based on cash discounts history.
* 5.Model tuning evaluation: Evaluation of the models performance.

## Installation guide 
These are the steeps for run the project for development and testing purposes.

## Prerequisites
This scripts run on Python 3.x all the others libraries needed are on the script lines by !pip install <library>
Because, you haven't got access to the api(the adquision data notebook is only for education purposes and show how get data from api and it's not run),  I left on the data folder the csv for work.

## Installing
All notebooks are ready to runing on google colab, just clone the repo in local and upload it to Google Colab.
To clone the repository to your local machine use the following command:
```
$ git clone https://github.com/nachxo85/marketing-ia
```

## Execution
You can execute in any order all the proyect notebooks. The data is on Data folder, the file data.csv contains all the historic data for work.


## Author
Ignacio Palomino Barranco