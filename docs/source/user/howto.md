# How To

```{toctree}
:maxdepth: 1
:hidden:

formats
validated
```

## Entrypoint
To use a model with RT-RAMSIS, an entrypoint has to be created in the source code of your model. This entrypoint is a simple function, that takes a dictionary with predefined fields as input, and returns the forecast in a predefined format as output. This function is then used by RT-RAMSIS to execute the model and store the results in the database.

## Format Definitions
The description of the formats used for the input and output of the entrypoint can be found in the {doc}`formats` section. If you want, you can stop there, as RT-RAMSIS doesn't need anything else. If you would like to have some kind of validation of the input and output of your entrypoint, you can {doc}`install <getstarted>` this package and continue reading the {doc}`validated` section.