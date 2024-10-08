# Overview 

This protein visualizer is a program that allows users to fetch and visualize protein structures using their PDB (Protein Data Bank) IDs. 
The program uses PyMOL a molecular visualization tool thats used to render the 3D structure of proteins.

# Features 

- Fetch Protein Data: Users can input a protein ID, and the app fetches the corresponding PDB file from the RCSB Protein Data Bank.
  
- 3D Visualization: The fetched protein structure is displayed in 3D using PyMOL, allowing for detailed examination of molecular structures.
  
# Requirements 
- Python 3.1
  
- PyMOL (Students can get free access to the educational license required to use PyMOL by signing up [here](https://pymol.org/edu/))
  
- 'requests' library used to fetch the PDB files
  
# Installation
1. Clone the repo and cd into the Backend directory
```
git clone https://github.com/Pabz-10/protein-visualizer.git
```
2. Install PyMOL
3. Install the requests library
```
pip install requests
```
# Usage 
To run the program, make sure you're in the Backend directory and enter the command below in the terminal
```
python protein_visualization.py
```
# License
This project is licensed under the [MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) License.
