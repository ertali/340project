#!/bin/bash

# Create the directory if it doesn't exist
mkdir -p "front_pages"

# Start and end dates
start_date="2024-01-01"
end_date="2025-03-17"

# Convert start_date to seconds since epoch
current_date="$start_date"

while [[ "$current_date" != "$(date -I -d "$end_date + 1 day")" ]]; do
    # Format the output filename
    output_file="front_pages/${current_date}.pdf"
    
    # Construct the URL
    url="https://static01.nyt.com/images/$(date -d "$current_date" +%Y/%m/%d)/nytfrontpage/scan.pdf"
    
    # Download the file using curl
    echo "Downloading: $url -> $output_file"
    curl -s -o "$output_file" "$url"
    
    # Move to the next day
    current_date=$(date -I -d "$current_date + 1 day")
done

echo "Download complete."
