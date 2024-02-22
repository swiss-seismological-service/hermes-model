from functools import wraps

import pandas as pd
from hydws.parser import BoreholeHydraulics
from seismostats import Catalog, GRRateGrid
from seismostats.utils import _check_required_cols
from shapely import wkt

from ramsis.schemas import ModelInput


def validate_entrypoint(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        # check only one argument is passed
        if len(args) != 1:
            raise ValueError("Only one argument is allowed")

        model_input = ModelInput(**args[0])

        # check if hydraulics are in the right format
        try:
            if model_input.injection_well is not None:
                for well in model_input.injection_well:
                    BoreholeHydraulics(well)
        except BaseException:
            raise ValueError("Invalid format for injection well, "
                             "please use valid hydjson.")

        try:
            if model_input.injection_plan is not None:
                BoreholeHydraulics(model_input.injection_plan)
        except BaseException:
            raise ValueError("Invalid format for injection plan, "
                             "please use valid hydjson.")

        try:
            Catalog.from_quakeml(model_input.seismic_catalog)
        except BaseException:
            raise ValueError("Invalid format for seismic catalog, "
                             "please use valid quakeml.")

        try:
            wkt.loads(model_input.geometry.bounding_polygon)
        except BaseException:
            raise ValueError("Invalid format for bounding polygon, "
                             "please use valid WKT.")

        results = func(model_input, **kwargs)

        if not all(isinstance(r, GRRateGrid)
                   or isinstance(r, Catalog)
                   or isinstance(r, pd.DataFrame) for r in results):
            raise ValueError(
                "Results need to be of type (Forecast)GRRateGrid, "
                "(Forecast)Catalog or DataFrame.")

        if not all(
            _check_required_cols(r, Catalog._required_cols)
            for r in results) \
            and not all(
                _check_required_cols(r, GRRateGrid._required_cols)
                for r in results):
            raise ValueError("Results are missing required columns.")

        return results
    return wrapper
