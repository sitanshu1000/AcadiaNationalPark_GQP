# AcadiaNationalPark_GQP
GQP Code Repository for the Acadia National Park Project Team

## Introduction
Acadia National Park is one of the top ten most popular parks in the US with 3.5 Million visitors annually. Cadillac Mountain is one of the most popular summits on the mountain and often suffers from overcrowding and lack of parking, leading to road closures, increased noise pollution, diminishing resources, and impacts to visitor experiences. Beginning in October of 2020 and continuing into the summer of 2021, Acadia implemented a reservation system to help mitigate the current issues on the summit. Our research aims to help the current reservation to help maximize visitors while minimizing overcrowding. To complete the research, we set out to accomplish three main goals: calculate visitor volume and dwell time, research various factors that impact visitor traffic and dwell time, and develop an optimization model to predict volume levels and dwell time.    
For the first goal, data was used from Acadia Park to estimate car volume and data from StreetLight was used to estimate pedestrian dwell time. To accomplish the second goal, we then collect data from OpenWeather to help correlate weather attributes to traffic patterns on the mountain. All the data plus various calculated features, such as federal and school holidays, were used to build prediction models to estimate the volume and dwell time on the mountain. Each model was built through an investigation of models and feature selection. Lastly, these models were built into a web interface that allows the park to input daily information and download the predicted volume and dwell time. At the end of this research, the team put together a set of recommendations to guide Acadia Park through future iterations of this research. 


## Data
[![image](https://raw.githubusercontent.com/sitanshu1000/AcadiaNationalPark_GQP/main/Images/weather.png)]
[![image](https://raw.githubusercontent.com/sitanshu1000/AcadiaNationalPark_GQP/main/Images/park%20data.png)]

## Models


## Web Application
The application provides an interface for people to upload a .csv file containing the weather data for 15 days and retun a result. It provides a data table for people to view and see the numbers and a visualization section where people can see a line chart and a box plot on the analysis of predicted results.
