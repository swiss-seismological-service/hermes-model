from datetime import datetime

from pydantic import BaseModel, ConfigDict


class GeometryExtent(BaseModel):
    bounding_polygon: str
    altitude_min: float
    altitude_max: float


class ModelInput(BaseModel):
    forecast_start: datetime
    forecast_end: datetime
    injection_well: dict | str | None = None
    injection_plan: dict | str | None = None
    geometry: GeometryExtent
    seismic_catalog: str
    model_parameters: dict

    model_config = ConfigDict(
        protected_namespaces=()
    )
