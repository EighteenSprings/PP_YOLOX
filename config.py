"""
configuration
config for data, model architecture, and training, etc.
"""
import os
from yacs.config import CfgNode as CN
import yaml

_C = CN()
_C.BASE = ['']

# global
_C.OUTPUT_DIR = 'output'
_C.EXP_NAME = 'yolox_nano'

_C.DATA = CN()
_C.DATA.TYPE = 'coco'
_C.DATA.NUM_CLASSES = 80
_C.DATA.INPUT_SIZE = (640,640)
_C.DATA.RANDOM_SCALE = (15,24)

_C.MODEL = CN()
_C.MODEL.DEPTH = 1.0
_C.MODEL.WIDTH = 1.0
_C.MODEL.DEPTHWISE = True
_C.MODEL.ACT = 'silu'

def _update_config_from_file(config, cfg_file):
    config.defrost()
    with open(cfg_file, 'r') as infile:
        yaml_cfg = yaml.load(infile, Loader=yaml.FullLoader)

    for cfg in yaml_cfg.setdefault('BASE', ['']):
        if cfg:
            _update_config_from_file(
                config, os.path.join(os.path.dirname(cfg_file), cfg)
            )
    print('merging config from {}'.format(cfg_file))
    config.merge_from_file(cfg_file)
    config.freeze()


def update_config(config, args):
    """Update config by ArgumentParser
    Args:
        args: ArgumentParser contains options
    Return:
        config: updated config
    """
    if args.cfg:
        _update_config_from_file(config, args.cfg)
    config.defrost()
    
    return config

def get_config(cfg_file=None):
    """Return a clone of config or load from yaml file"""
    config = _C.clone()
    if cfg_file:
        _update_config_from_file(config, cfg_file)
    return config

if __name__ == "__main__":
    config = get_config(cfg_file="configs/yolox_x.yml")
    print(config)