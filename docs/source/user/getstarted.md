# Getting Started

## Entrypoint
All you need to in order to make your model compatible is to define an entry point, a simple function, for your model. With a predefined format for input and output from this entrypoint, RAMSIS is able to execute your model and store the results in the database.

## Installation
You don't necessarily need to install anything, but you can use this package to help you if you wish so. To install, you can run the following command:

```bash
pip install git+https://gitlab.seismo.ethz.ch/indu/ramsis-model.git
```

You can reference the dependency in your requirements.txt or setup.cfg file as well:

```bash
ramsis-model @ git+https://gitlab.seismo.ethz.ch/indu/ramsis-model.git
```

## Dependencies
The data formats we rely on are HYDJSON for the models forecasting induced seismicity, and QUAKEML for the events data. To work with those formats, we use the two packages `hydws-client` and `SeismoStats` respectively. It is not required to use them as well, but this package uses them to validate the input and output data, and they are very handy to work with quakeml and hydjson.