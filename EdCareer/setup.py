import numpy as np
import pandas as pd
#import preprocessor as p
import counselor
from tensorflow.keras.models import load_model
import joblib
from pathlib import Path
import nltk
import os

directory = os.getcwd() + "\\nltk_data\\"

nltk.download("wordnet", "nltk_data/")