import pandas as pd
import pandas as pd

def load_csv(file_path):
    try:
        return pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        # If utf-8 encoding fails, try a different encoding
        return pd.read_csv(file_path, encoding='ISO-8859-1')
