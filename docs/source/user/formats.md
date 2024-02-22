# Input and Output Formats

## Entrypoint
The entrypoint of the model should be a simple python function, that takes a dictionary as an argument.

```python	
def entrypoint(input: dict) -> list:
    # Your model code here
    return output
```

## Input Format
The input dictionary has the following fields with the respective types:

```
forecast_start: datetime.datetime
```
Date and time from when on the forecast should be made.

```
forecast_end: datetime.datetime
```
Date and time until when the forecast should be made.

```
injection_well: str | dict # HYDJSON format
```
A list of dictionaries in the HYDJSON format, containing the history of injections into the well.

```
injection_plan: str | dict # HYDJSON format
```
A dictionary in the HYDJSON format, containing the planned injections.

```
seismic_catalog: str # QUAKEML format
```
An XML string in the QUAKEML format, containing the seismic events catalog.

```
model_parameters: dict
```
A dictionary containing the parameters for the model. The keys are the names of the parameters, and the values are the values of the parameters.

```
geometry: dict # containing the following keys:
    bounding_polygon: str # WKT format
    altitude_min: float
    altitude_max: float
```
The geometry of the area of interest. The bounding_polygon is a string in the WKT format, and the altitude_min and altitude_max are m.a.s.l.
It is the model's responsibility to discretize the area of interest and to calculate the forecast for each discretized volume.


## Output Format
The output of the entrypoint should be a list of forecasts, where each entry in the list represents the forecast for one timestep. The forecasts can be one of two types, either Catalogs of events, including their magnitude, location and time, or a a parametric description of the seismicity, including at least `a`, `b` and `mc` values.

Each forecast should be returned either as a `pd.DataFrame()` object, or, if using the `SeismoStats` package, as a `(Forecast)Catalog` object or a `(Forecast)GRRateGrid` object. 

In any case, they each need two attributes, `starttime` and `endtime`, which are `datetime.datetime` objects defining the timestep for which the forecast is made.
```
def entrypoint(input: dict) -> list:
    catalog = pd.DataFrame(#your data here)
    catalog.starttime = datetime.datetime(2020, 11, 24, 14, 47, 9)
    catalog.endtime = datetime.datetime(2020, 11, 24, 15, 47, 9)
    return [catalog]
```


### Catalog
If returning a Catalog of events, the returned object should have at least the following columns:

```
                          time longitude   latitude        depth  magnitude
0   2020-11-24 14:47:09.823149  8.474492  46.509983  1294.102992      -2.82
1   2020-11-24 15:28:54.648949  8.474545  46.510010  1268.102992      -2.94
2   2020-11-24 15:31:42.411869  8.474323  46.509967  1265.102992      -3.03
3   2020-11-24 15:35:01.114360  8.474359  46.509832  1260.102992      -2.95
4   2020-11-24 15:35:07.995789  8.474372  46.509814  1261.102992      -2.94
```

It is possible to return multiple realizations of catalogs for one timestep. In this case a `grid_id` column is required, to distinguish between the different realizations:

```
                          time longitude   latitude        depth  magnitude  grid_id
0   2020-11-24 14:47:09.823149  8.474492  46.509983  1294.102992      -2.82        0
1   2020-11-24 15:28:54.648949  8.474545  46.510010  1268.102992      -2.94        0
2   2020-11-24 15:31:42.411869  8.474323  46.509967  1265.102992      -3.03        0
3   2020-11-24 15:35:01.114360  8.474359  46.509832  1260.102992      -2.95        1
4   2020-11-24 15:35:07.995789  8.474372  46.509814  1261.102992      -2.94        1
```




### GRRateGrid
If using a grid of Gutenberg-Richter rates, the returned object should have at least the following columns:
```
 longitude_min longitude_max latitude_min latitude_max depth_min depth_max    a   b    mc
0    8.472518      8.476478    46.508451    46.511185  1121.433  1421.434 -26.1 2.1 -2.91
```

Additional columns are allowed. Currently `number_events`, `alpha` are also stored if available.

Similar to the catalog, `grid_id` can be used to return probabilistic forecast, returning multiple possible realizations of a grid per timestep:

```
 longitude_min  longitude_max  latitude_min  latitude_max depth_min depth_max a     alpha   b   mc  grid_id
0  8.472518       8.476478     46.508451     46.511185  1121.434  1421.434    -26.1 -5.3  2.1 -2.91       0
1  8.472518       8.476478     46.508451     46.511185  1121.434  1421.434    -26.1 -5.3  2.1 -2.91       1
2  8.472518       8.476478     46.508451     46.511185  1121.434  1421.434    -26.1 -5.3  2.1 -2.91       2
3  8.472518       8.476478     46.508451     46.511185  1121.434  1421.434    -26.1 -5.3  2.0 -2.91       3
```

