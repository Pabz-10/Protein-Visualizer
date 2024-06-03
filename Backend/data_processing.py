# TODO Fetch and prcoess protein data via uniport api 
import requests


def create_pdb_url():
    # Prompt user for protein entry id 
    entry_id = input("Please enter the entry id of the organism you want: ").strip()
    # Create URL for the pbd file
    url = f"https://files.rcsb.org/download/{entry_id}.pdb"
    return url

def fetch_pdb_file():
    # Get the url via user input
    pdb_url = create_pdb_url()

    # Fetch data from the api
    response = requests.get(pdb_url)
    print(pdb_url)

# Check that data was obtained and store it in a protein pdb file
    if response.status_code == 200:
        pdb_filename = "protein.pdb"
        # Write the structure data from the api into the file
        with open(pdb_filename, "w") as file:
            file.write(response.text)
        print(f"PDB file saved successfully as {pdb_filename}.")
        return pdb_filename
    else:
        print(f"Failed to fetch PDB file. Status code: {response.status_code}")
        return None


pdb_filename = fetch_pdb_file()