import pandas as pd

# Load the data
spy_df = pd.read_csv("data/prev_day_change/SPY.csv")
dia_df = pd.read_csv("data/prev_day_change/DIA.csv")
ief_df = pd.read_csv("data/prev_day_change/IEF.csv")
iwm_df = pd.read_csv("data/prev_day_change/IWM.csv")
qqq_df = pd.read_csv("data/prev_day_change/QQQ.csv")
tlt_df = pd.read_csv("data/prev_day_change/TLT.csv")
vt_df = pd.read_csv("data/prev_day_change/VT.csv")
embeddings_df = pd.read_csv("full_features_combined_clean.csv")

# combine all stock data but only prev_day_percent_change
spy_df = spy_df[['timestamp', 'prev_day_percent_change']].rename(columns={'timestamp': 'Date', 'prev_day_percent_change': 'SPY'})
dia_df = dia_df[['timestamp', 'prev_day_percent_change']].rename(columns={'timestamp': 'Date', 'prev_day_percent_change': 'DIA'})
ief_df = ief_df[['timestamp', 'prev_day_percent_change']].rename(columns={'timestamp': 'Date', 'prev_day_percent_change': 'IEF'})
iwm_df = iwm_df[['timestamp', 'prev_day_percent_change']].rename(columns={'timestamp': 'Date', 'prev_day_percent_change': 'IWM'})
qqq_df = qqq_df[['timestamp', 'prev_day_percent_change']].rename(columns={'timestamp': 'Date', 'prev_day_percent_change': 'QQQ'})
tlt_df = tlt_df[['timestamp', 'prev_day_percent_change']].rename(columns={'timestamp': 'Date', 'prev_day_percent_change': 'TLT'})
vt_df = vt_df[['timestamp', 'prev_day_percent_change']].rename(columns={'timestamp': 'Date', 'prev_day_percent_change': 'VT'})

# Merge all stock dataframes into one
combined_df = pd.merge(spy_df, dia_df, on='Date', how='outer')
combined_df = pd.merge(combined_df, ief_df, on='Date', how='outer')
combined_df = pd.merge(combined_df, iwm_df, on='Date', how='outer')
combined_df = pd.merge(combined_df, qqq_df, on='Date', how='outer')
combined_df = pd.merge(combined_df, tlt_df, on='Date', how='outer')
combined_df = pd.merge(combined_df, vt_df, on='Date', how='outer')
combined_df['Date'] = pd.to_datetime(combined_df['Date'])
embeddings_df['Date'] = pd.to_datetime(embeddings_df['Date'])

# Merge the dataframes on the Date column
merged_df = pd.merge(embeddings_df, combined_df, on='Date', how='inner')

merged_df.to_csv("new_better_cleaned_embeddings.csv", index=False)
