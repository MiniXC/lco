# **L**ight **Co**nfig (lco)

Load a config file once and use it as you would use enviroment variables from anywhere in your code.

Somewhere:
```python
import lco

lco.init("some_config.yml")
```
You can also set the enviroment variable ``LCO_CONFIG`` instead.

Somewhere else entirely, 10 layers deep in some object.
```python
import lco

lco["some_value"]
lco["some_group"]["some_value"]
```

This works across threads and processes.

## Installation

You can use ``pip install lco`` as well.
But this is such a small package, it might be best to just copy the code below into your own ``lco.py``.
<details>
  <summary>Show Code</summary>
  
  ```python
  import os
  import sys
  import yaml

  class LCO(object):
    def __init__(self):
      global _lco_obj
      if "_lco_obj" not in globals():
        if "LCO_CONFIG" in os.environ:
          config = os.environ["LCO_CONFIG"]
          if os.path.exists(config):
            with open(config, "r") as f:
              _lco_obj = yaml.safe_load(f)
          else:
            raise ValueError("LCO_CONFIG is not a file: %s" % config)

    def init(self, config):
      global _lco_obj
      if "_lco_obj" not in globals():
        with open(config, "r") as f:
          _lco_obj = yaml.safe_load(f)
        os.environ["LCO_CONFIG"] = config

    def __getitem__(self, name):
      global _lco_obj
      if name not in _lco_obj:
        raise KeyError("No such key: %s" % name)
      return _lco_obj[name]

  sys.modules["lco"] = LCO()
  ```
</details>


## But why?

This is mostly useful for research code, MVPs or Prototypes, where on doesn't want to pass configuration variables from object to object or across scopes. I wouldn't recommend this for production code as you're essentially using global variables.

## What filetypes are supported?

So far, only yaml. Feel free to open a pull request with the filetype of your choice.

## 
