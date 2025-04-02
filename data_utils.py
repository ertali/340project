import pandas as pd

def add_percent_change(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(f'data/{csv_file}', parse_dates=['timestamp'])

    # Sort by timestamp to ensure chronological order
    df.sort_values(by='timestamp', inplace=True)
    
    # Calculate percent change in closing price
    df['percent_change'] = df['close'].pct_change() * 100
    
    return df

print(add_percent_change("DIA.csv"))

def write_percent_change(csv_file):
    df = add_percent_change(csv_file)
    df.to_csv(f"data/updated/{csv_file}")

def update_all(l):
    for stock in l:
        write_percent_change(stock)

lst = ["DIA.csv", "IEF.csv", "IWM.csv", "QQQ.csv", "SPY.csv", "TLT.csv", "VT.csv"]
update_all(lst)