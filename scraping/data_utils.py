import pandas as pd
import os

def add_prev_day_change(csv_file):
    df = pd.read_csv(f'data/{csv_file}', parse_dates=['timestamp'])

    # Sort by timestamp to ensure chronological order
    df.sort_values(by='timestamp', inplace=True)

    close_two_days_ago = df['close'].shift(2)
    close_one_day_ago = df['close'].shift(1)

    # Calculate percent change from two days ago to one day ago
    df['prev_day_percent_change'] = ((close_one_day_ago - close_two_days_ago) / close_two_days_ago) * 100

    return df

def write_prev_day_change(csv_file):
    df = add_prev_day_change(csv_file)
    os.makedirs("data/prev_day_change", exist_ok=True)
    df.to_csv(f"data/prev_day_change/{csv_file}", index=False)

def update_all_prev_day_change(file_list):
    for stock in file_list:
        write_prev_day_change(stock)

# List of CSVs to update
lst = ["DIA.csv", "IEF.csv", "IWM.csv", "QQQ.csv", "SPY.csv", "TLT.csv", "VT.csv"]
update_all_prev_day_change(lst)
