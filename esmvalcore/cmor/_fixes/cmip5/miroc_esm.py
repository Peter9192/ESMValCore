"""Fixes for MIROC ESM model."""

from iris.coords import DimCoord
from iris.exceptions import CoordinateNotFoundError

from ..fix import Fix


class Tro3(Fix):
    """Fixes for tro3."""

    def fix_data(self, cube):
        """
        Fix data.

        Fixes discrepancy between declared units and real units

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        metadata = cube.metadata
        cube *= 1000
        cube.metadata = metadata
        return cube


class Co2(Fix):
    """Fixes for co2."""

    def fix_metadata(self, cubes):
        """
        Fix metadata.

        Fixes error in cube units

        Parameters
        ----------
        cube: iris.cube.CubeList

        Returns
        -------
        iris.cube.Cube

        """
        self.get_cube_from_list(cubes).units = '1.0e-6'
        return cubes


class AllVars(Fix):
    """Common fixes to all vars."""

    def fix_metadata(self, cubes):
        """
        Fix metadata.

        Fixes error in air_pressure coordinate, sometimes called AR5PL35

        Parameters
        ----------
        cube: iris.cube.CubeList

        Returns
        -------
        iris.cube.CubeList

        """
        for cube in cubes:
            try:
                old = cube.coord('AR5PL35')
                dims = cube.coord_dims(old)
                cube.remove_coord(old)

                plev = DimCoord.from_coord(old)
                plev.var_name = plev
                plev.standard_name = 'air_pressure'
                plev.long_name = 'Pressure '
                cube.add_dim_coord(plev, dims)
            except CoordinateNotFoundError:
                pass

        return cubes
