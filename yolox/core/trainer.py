"""
Update:
    Date: 2021/12/31
    Msg: Megvii YOLOX got an good project template, so I decide
         to imitate(copy) it (●'◡'●)
"""
import os
from loguru import logger
from yolox.utils import (
    setup_logger, 
    get_rank
)



class Trainer:
    def __init__(self, config):
        self.config = config
        self.rank = get_rank()
        self.file_name = os.path.join(config.OUTPUT_DIR, config.EXP_NAME)
        setup_logger(
            self.file_name,
            distributed_rank=self.rank,
            filename="train_log.txt",
            mode='a'
        )

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


    # all round
    def before_train(self):
        logger.info("config: \n{}".format(str(self.config)))
        
    
    def after_train(self):
        pass

    # epoch
    def before_epoch(self):
        pass

    def after_epoch(self):
        pass
    
    # iter
    def before_iter(self):
        pass
    
    def after_iter(self):
        pass

if __name__=="__main__":
    from config import get_config
    config = get_config('configs/yolox_nano.yml')
    trainer = Trainer(config)
    trainer.train()