"""
Update:
    Date: 2021/12/31
    Msg: Megvii YOLOX got an good project template, so I decide
         to imitate(copy) it (●'◡'●)
"""
from loguru import logger
from yolox.utils import setup_logger


class Trainer:
    def __init__(self):
        pass

    def train(self):
        self.before_train()
        try:
            self.train_in_epoch()
        except Exception:
            raise
        finally:
            self.after_train()

    def train_in_epoch(self):
        for self.epoch in range(self.start_epoch, self.max_epoch):
            self.before_epoch()
            self.train_in_iter()
            self.after_epoch()

    def train_in_iter(self):
        for self.iter in range(self.max_iter):
            self.before_iter()
            self.train_one_iter()
            self.after_iter()

    def train_one_iter(self):
        pass


    # detail
    
    