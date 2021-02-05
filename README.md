# project-24


[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]https://github.com/Folkas/project_24/blob/main/LICENSE)

## Table of contents:
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Other](#other)

## General info:

This repository contains a Flask API for Turing College module 2 spring 4 final assignment. The application predicts car price based on six car attributes:
manufacturing date, engine size (in liters), engine power (in kW), mileage (in km), automatic gearbox (0/1) and manual gearbox (0/1).

## Setup

To run this app, please send a ```POST``` or ```GET``` request (through Postman) to the following address: 
```
https://folkas-project24.herokuapp.com/cars
```
An exemplary ```POST``` request to predict 10 car prices looks as follows:
```
{"inputs": [[2016.0, 1.5, 70.0, 188928.0, 0.0, 1.0],
 [2011.0, 1.6, 68.0, 150000.0, 0.0, 1.0],
 [2004.0, 3.0, 160.0, 303800.0, 1.0, 0.0],
 [2016.0, 1.5, 88.0, 188987.0, 0.0, 1.0],
 [2016.0, 1.5, 88.0, 113090.0, 0.0, 1.0],
 [2016.0, 1.5, 85.0, 173162.0, 1.0, 0.0],
 [2012.0, 3.0, 195.0, 207000.0, 1.0, 0.0],
 [2013.0, 2.0, 180.0, 145000.0, 1.0, 0.0],
 [2012.0, 3.0, 190.0, 344000.0, 1.0, 0.0],
 [2016.0, 2.0, 85.0, 218243.0, 1.0, 0.0]]}
 ```

## Features

```GET``` method:

Returns 10 most recent requests and responses in JSON format.

```POST``` method:

Predicts car price for the input data. Firstly, the function preprocesses the input parameters for the request data using standard scalling.
Then it passes the input to the trained model and returns predicted price.

Parameters:

    * Six car price features put into a list: ManufacturingDate (int), Engine_l (float), Power_kW (float), Mileage_km (float),
    Gearbox_Automatic (binary: 0 for no, 1 for yes) and Gearbox_Manual (binary: 0 for no, 1 for yes)

    Returns:

    * Predicted car price in euros (int)
## Other
Can't wait to get over this module.
