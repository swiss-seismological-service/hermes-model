from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ModelInput(BaseModel):
    forecast_start: datetime
    forecast_end: datetime

    injection_observation: list[dict | None] | None = None
    injection_plan: dict | None = None

    seismic_observation: str

    bounding_polygon: str
    depth_min: float
    depth_max: float

    model_parameters: dict

    model_config = ConfigDict(
        protected_namespaces=()
    )
