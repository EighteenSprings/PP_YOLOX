from yolox.core import Trainer
from config import get_config
config = get_config('configs/yolox_nano.yml')
trainer = Trainer(config)
trainer.train()