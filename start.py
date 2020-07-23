from roboglia.base import BaseRobot
from roboglia.dynamixel import DynamixelBus
from ui.ui import MainUI
import logging
import time
import os


format = '%(asctime)s %(levelname)-7s %(threadName)-18s %(name)-32s %(message)s'
logging.basicConfig(format=format,
                    # file = 'test.log',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)

logging.getLogger('roboglia.dynamixel.sync').setLevel(logging.CRITICAL)

if __name__ == '__main__':

    path = os.path.dirname(__file__)
    r = BaseRobot.from_yaml(os.path.join(path,'config/mh5.yml'))
    r.start()

    ui = MainUI(r)
    ui.start()

    while ui.running:
        time.sleep(0.5)

    r.stop()
