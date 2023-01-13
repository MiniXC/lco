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

## But why?

This is mostly useful for research code, MVPs or Prototypes, where on doesn't want to pass configuration variables from object to object or across scopes. I wouldn't recommend this for production code as you're essentially using global variables.

## What filetypes are supported?

So far, only yaml. Feel free to open a pull request with the filetype of your choice.

## 