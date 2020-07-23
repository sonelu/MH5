from snack import GridForm, Textbox, Listbox, Scale, Label

class JointUI():

    def __init__(self, screen, robot, info='Pos'):
        self.switch(info)
        self.robot = robot
        self.screen = screen
        # main grid 2 (v) x 3 (h)
        self.grid = GridForm(screen, self.title, 2, 3)
        # top labels
        self.grid.add(Label('Right Side'), 0, 0)
        self.grid.add(Label('Left Side'), 1, 0)
        # list boxes
        self.lbl = Listbox(height=12, width=18)
        self.lbr = Listbox(height=12, width=18)
        for i in range(11):
            self.lbl.append('Dummy', i+1)
            self.lbr.append('Dummy', i+1)
        self.grid.add(self.lbl, 0, 1)
        self.grid.add(self.lbr, 1, 1)
        # bottom
        self.btxt = Label(f'Battery:   ({10:4.1f}V)')
        self.grid.add(self.btxt, 0, 2)
        self.bscl = Scale(18, 15)
        self.grid.add(self.bscl, 1, 2)
        self.grid.setTimer(50)      # 50ms
        self.grid.addHotKey('q')

    def switch(self, info):
        if info == 'Pos':
            self.title = 'Position'
            self.attr = 'position'
        if info == 'Load':
            self.title = 'Load'
            self.attr = 'load'

    def update(self):
        # joint info
        left_joints = ['head_y', 'r_shoulder_p', 'r_shoulder_r', 'r_elbow_y',
                       'r_elbow_p', 'r_hip_y', 'r_hip_r', 'r_hip_p',
                       'r_knee_p', 'r_ankle_p', 'r_ankle_r']
        right_joints = ['head_p', 'l_shoulder_p', 'l_shoulder_r', 'l_elbow_y',
                        'l_elbow_p', 'l_hip_y', 'l_hip_r', 'l_hip_p',
                        'l_knee_p', 'l_ankle_p', 'l_ankle_r']
        joints = self.robot.joints
        for index, name in enumerate(left_joints):
            value = getattr(joints[name], self.attr, None)
            if name[0] in ['l', 'r']:
                name = name[2:]
            text = f'{name:10} {value:6.1f}'
            self.lbl.replace(text, index+1)
        for index, name in enumerate(right_joints):
            value = getattr(joints[name], self.attr)
            if name[0] in ['l', 'r']:
                name = name[2:]
            text = f' {value:6.1f} {name:>10}'
            self.lbr.replace(text, index+1)
        self.screen.refresh()
        return self.grid.run()
