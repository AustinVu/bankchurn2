import sys

import pandas as pd
from fastapi.encoders import jsonable_encoder

sys.path.append("..")
from schema import ChurnInfo


def format_input_data(data: ChurnInfo):
    """Format the input data to a prediction data structure

    Args:
        data (HouseInfo): Information about a house

    Returns:
        A Pandas DataFrame: Convert the input data into a Pandas DataFrame
    """
    return pd.DataFrame(jsonable_encoder(data), index=[0])