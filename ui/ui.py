from snack import SnackScreen
from roboglia.base import BaseThread
from ui.ui_joints import JointUI
import time


class MainUI(BaseThread):

    def __init__(self, robot, frequency=2.0):
        super().__init__(name='UI')
        self.robot = robot
        self.period = 1.0 / frequency
        self.currentUI = None

    def setup(self):
        self.screen = SnackScreen()
        self.screen.pushHelpLine('[p]Pos [l]Load [t]Temp [s]Status')
        self.jointUI = JointUI(self.screen, self.robot)
        self.currentUI = self.jointUI

    def run(self):
        resp =' '
        while not self.stopped and resp != 'q':
            if self.paused:
                # paused
                time.sleep(self.period)
            else:
                resp = self.currentUI.update()
                time.sleep(self.period)

    def teardown(self):
        self.screen.finish()

