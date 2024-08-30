import pymol
from pymol import cmd

def visualizer(pdb_filename):
    pymol.finish_launching()
    cmd.load(pdb_filename)

    # Hide presets
    cmd.hide("everything")

    #show chains as a cartoon and show all lines and sticks
    cmd.show("cartoon", "all")
    cmd.show("lines", "all")
    cmd.show("sticks", "all")

    #Color molecule red
    cmd.color("red", "all")

    #zoom to fit entire molecule
    cmd.zoom()

pdb_filename = "protein.pdb"

if pdb_filename:
    visualizer(pdb_filename)
else:
    print("PDB file was not found. Visualization aborted.")