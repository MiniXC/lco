import os
import sys

import yaml

import lco

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

sys.modules[__name__] = LCO()