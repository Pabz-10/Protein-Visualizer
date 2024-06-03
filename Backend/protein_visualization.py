import pymol
from pymol import cmd

def visualizer(pdb_filename):
    pymol.finish_launching()
    cmd.load(pdb_filename)
    cmd.show("cartoon")
    cmd.color("cyan", "all")
    cmd.zoom()

pdb_filename = "protein.pdb"

if pdb_filename:
    visualizer(pdb_filename)
else:
    print("PDB file was not found. Visualization aborted.")