"""Derivation of variable `rlus`."""
"""The variable 'rlus' (Surface Upwelling Longwave Radiation) is stored in """
"""the EMAC variable 'tradsu_ave',"""
"""and needs to be multiplied with -1. to represent the CMOR standard."""
"""(following the recipe from the DKRZ CMIP6 Data Request WebGUI)"""
"""(https://c6dreq.dkrz.de/)"""

from . import var_name_constraint


def derive(cubes):
    rlus_cube = -1. * cubes.extract_strict(var_name_constraint('tradsu_ave'))

return rlus_cube