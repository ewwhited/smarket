# smarket

Files used in learning SQL server, SQLite, Tableau

csv - the csv documents used for structuring data, "smarket.csv" is the initial raw data, "smarket_new.csv" is the final data stored in database, which includes predictions from the regression models

python - the source code used to create a binary logistic regression model using "Lag1" and "Volume" as a predictor of "Direction", as well as the source code for creating a sqlite database from the csv files

sql - the query used in creating the smarket table in a private database

tableau - data visualization: clusters of up/down based upon the prediction of the binary logistic regression model on a plot of Volume vs. Lag 1. the source data for the tableau doc was from the private sql database, but it is identical to if it was done via the smarket_new.csv
