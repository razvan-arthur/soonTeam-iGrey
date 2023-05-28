#!/bin/bash

# Variables
repo_url="https://github.com/razvan-arthur/soonTeam-iGrey"
json_file="query-data.json"
new_json_file="return_data.json"
business_name_script="Predictie_Controversat.py"
stock_name_script="checkVolatility.py"
domain_script="checktrend.py"
ceo_username_script="Cod_sentimental.py"

# Clone the Git repository
git clone "$repo_url" temp_repo
cd temp_repo || exit 1

# Retrieve JSON file
git checkout main # Replace "master" with your branch name if necessary
git pull origin main

# Extract values from JSON
business_name=$(jq -r '.business-name' "$json_file")
stock_name=$(jq -r '.stock-name' "$json_file")
domain=$(jq -r '.domain' "$json_file")
ceo_username=$(jq -r '.ceo-username' "$json_file")

# Execute Python scripts and capture outputs
business_name_output=$(python3 "$business_name_script" "$business_name")
 stock_name_output=$(python3 "$stock_name_script" "$stock_name")
 domain_output=$(python3 "$domain_script" "$domain")
 ceo_username_output=$(python3 "$ceo_username_script" "$ceo_username")

sentiment=$(cat sentimental-result.txt)
trend=$(cat trend-result.txt)
controversy=$(cat controversy-result.txt)
business=$(cat business-result.txt)

json="{\"sentiment\": $sentiment, \"trend\": $trend, \"controversy\": $controversy, \"business\": $business}"
# Commit and push the new JSON file
git add "$new_json_file"
git commit -m "Updated data"
git push origin main

# Clean up
cd ..
rm -rf temp_repo
