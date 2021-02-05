import json
from flask import request
import numpy as np
import requests
import pandas as pd

# creating a preprocessing function to transform the input from json format
def preprocessing_function(request_data) -> np.array:
    """
    Converts the input format from json data to numpy array in order to use for the trained model later on.

    Parameters:
    request_data (str): data in json format arriving with request made with json.dumps function

    Returns:
    list transformed into 2D numpy array
    """
    return np.asarray(json.loads(request.data)["inputs"])
