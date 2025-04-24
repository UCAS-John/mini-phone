import pandas as pd

def read_csv(path):
    try:
        df = pd.read_csv(path)
        if not df.empty:
            return df
        else:
            print(f"No data found in {path}.")
            return None
    except Exception as e:
        print(f"Error reading CSV file {path}: {e}")
        return None

def save_csv(path, data):
    try:
        df = pd.DataFrame(data)
        df.to_csv(path, index=False)
        print(f"Data saved to {path}.")
    except Exception as e:
        print(f"Error saving CSV file {path}: {e}")