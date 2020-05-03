# %matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


columns = ['title', 'category', 'content_text']
df = pd.DataFrame(columns=columns)


for page_url in page_urls: