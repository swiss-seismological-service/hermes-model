# Validated Entrypoint

If you would like to have some kind of validation of the input and output of your entrypoint, you can install this package as described above.

The changes to the entrypoint are minimal:

```python	
from ramsis import validate_entrypoint, ModelInput

@validate_entrypoint(induced=True)
def entrypoint(model_input: ModelInput):
    # Call and execute your model here.
    return output
```

The `validate_entrypoint` decorator will validate the input and output of the entrypoint, and raise an error if the input or output is not valid. The `induced` parameter is optional, and defaults to `False`. If set to `True` the input fields `injection_well` and `injection_plan` will be validated as well.
