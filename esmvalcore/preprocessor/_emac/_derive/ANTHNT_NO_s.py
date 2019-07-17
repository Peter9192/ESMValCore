"""Derivation of variable `ANTHNT_NO_s`.

The variable 'ANTHNT_NO_s' is an EMAC variable that is used for monitoring EMAC
output. It is here summed over all available levels. The variable is stored in
the EMAC CMIP6 channel 'import_grid'.

ANTHNT_NO_s: Anthropogenic NO, summed.

"""

from scipy.constants import N_A

from ._shared import sum_over_level


def derive(cubes):
    """Derive `ANTHNT_NO_s`."""
    molar_mass_no2 = 46.0055  # g mol-1
    mass_per_molecule_no2 = molar_mass_no2 / N_A * 1e-3  # kg
    return sum_over_level(cubes,
                          'ANTHNT_NO',
                          scale_factor=mass_per_molecule_no2)