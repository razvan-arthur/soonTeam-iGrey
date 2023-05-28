import json
# import git
import subprocess
from checktrend import check_trend_interest

# Clone the Git repository
# repo_url = "https://github.com/razvan-arthur/soonTeam-iGrey"  # Replace with your Git repository URL
# repo_dir = "repo"  # Directory where the repository will be cloned
# git.Repo.clone_from(repo_url, repo_dir)

# Load the JSON file
json_file_path = "query-data.json"  # Replace with the actual path to your JSON file
with open(json_file_path) as file:
    data = json.load(file)

# Extract values from JSON
business_name = "Apple"
stock_name = "AAPL"
domain = "IT"
ceo_username = "tim_cook"


check_trend_interest(domain)
# Process values using separate Python scripts
process_scripts = {
    "business-name": "Cod_sentimental.py",
    "stock-name": "checkVolatility.py",
    "domain": "checktrend.py",
    "ceo-username": "Predictie_Controversat.py",
}

processed_data = {}
for field, script in process_scripts.items():
    command = ["python3", script, data[field]]
    result = subprocess.run(command, capture_output=True, text=True)
    processed_data[field] = result.stdout.strip()

# Save processed data to a new JSON file
output_file_path = processed_data.json"
with open(output_file_path, "w") as file:
    json.dump(processed_data, file)

# Commit and push the changes to the Git repository
# repo = git.Repo(repo_dir)
# repo.git.add(output_file_path)
# repo.index.commit("Updated processed data")
# repo.remote().push()
