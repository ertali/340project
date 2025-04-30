#!/bin/bash

# Create the directory if it doesn't exist
mkdir -p "front_pages"

start_date="2013-01-26"
end_date="2023-08-27"

# Convert start_date to seconds since epoch
current_date="$start_date"

while [[ "$current_date" != "$(date -I -d "$end_date + 5 day")" ]]; do
    output_file="front_pages/${current_date}.pdf"
    url="https://static01.nyt.com/images/$(date -d "$current_date" +%Y/%m/%d)/nytfrontpage/scan.pdf"
    echo "Downloading: $url -> $output_file"
    curl -s -o "$output_file" "$url"
    
    # Move to the next day
    current_date=$(date -I -d "$current_date + 5 day")
done

echo "Download complete."
