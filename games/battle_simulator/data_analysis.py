# Data Analysis

# This lets us use the library pandas to be able to load characters data into a DataFrame and get character attributes
import pandas as pd

def analyze_characters(characters):
    # Creates a DataFrame from the list of character dictionaries
    df = pd.DataFrame(characters)

    # Checks if the DataFrame is empty
    if df.empty:
        print("No character data available for analysis.")
        return
    
    # Select only numeric columns for analysis
    numeric_df = df.select_dtypes(include=['number'])

    # Perform statistical analysis on numeric columns
    print("Mean stats:")
    print(numeric_df.mean())
    print("\nMedian stats:")
    print(numeric_df.median())
    print("\nMax stats:")
    print(numeric_df.max())
    print("\nMin stats:")
    print(numeric_df.min())
