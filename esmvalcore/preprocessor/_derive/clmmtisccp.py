"""Derivation of variable `clmmtisccp`."""

from iris import Constraint

from ._baseclass import DerivedVariableBase
from ._shared import cloud_area_fraction


class DerivedVariable(DerivedVariableBase):
    """Derivation of variable `clmmtisccp`."""

    # Required variables
    required = [{'short_name': 'clisccp'}]

    @staticmethod
    def calculate(cubes):
        """Compute ISCCP middle level medium-thickness cloud area fraction."""
        tau = Constraint(
            atmosphere_optical_thickness_due_to_cloud=lambda t: 3.6 < t <= 23.)
        plev = Constraint(air_pressure=lambda p: 44000. < p <= 68000.)

        return cloud_area_fraction(cubes, tau, plev)
