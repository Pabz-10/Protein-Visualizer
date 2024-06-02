# TODO Fetch and prcoess protein data via uniport api 
import requests
import urllib.parse

def create_uniprot_url():
    protein_name = input("Please enter the name of the protein you want: ").strip()
    max_sequence_length = input("Please enter the maximum length of the seqeunce: ").strip()
    # gene_name = input("Please enter the gene name you are looking for ").strip()
    reviewed = input("Would you like only reviewed entries? (yes/no): ").strip().lower()

    # Convert reviewed to a boolean for the querys string
    reviewed = "true" if reviewed in ["yes", "y"] else "false"

    # Construct my query string 
    query = f"(protein_name:{protein_name}) AND " \
            f"(length: [{0} TO {max_sequence_length}])  AND " \
            f"(reviewed: {reviewed})"
    
    # URL-encode the query string so its safe to use in a URL
    encoded_query = urllib.parse.quote(query)

    # Create URL for API request
    url = f"https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=fasta&query={encoded_query}"
 
    # return the URL
    return url

# Get the url via user input
url = create_uniprot_url()

# Fetch data from the api

response = requests.get(url)

# Test
if response.status_code == 200:
    all_fastas = response.text
    print("Data fetched successfully.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# Print the first 500 characters of the fetched data to check
print(all_fastas[:500])