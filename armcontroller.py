import ikpy.utils.plot as plot_utils
import matplotlib.pyplot as plt
from armkinematics import ArmKinematics
from servocontroller import ServoController

class ArmController:
    def __init__(self, urdf_file, active_links_mask, pwm_freq=50, show_plot=True):
        self.servo_controller = ServoController(pwm_freq)
        self.arm_kinematics = ArmKinematics(urdf_file, active_links_mask)
        self.show_plot = show_plot
        if self.show_plot:
            self.fig, self.ax = self.init_3d_plot()

    @staticmethod
    def init_3d_plot():
        fig, ax = plot_utils.init_3d_figure()
        fig.set_figheight(9)
        fig.set_figwidth(13)
        return fig, ax

    def update_plot(self, target_position):
        if not self.show_plot:
            return
        self.ax.clear()
        self.arm_kinematics.plot_chain(self.ax, target_position)
        plt.xlim(-0.5, 0.5)
        plt.ylim(-0.5, 0.5)
        self.ax.set_zlim(0, 0.6)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def move(self, x, y, z):
        target_position = [x, y, z]
        target_orientation = [1, 1, 0]
        valuedict = self.arm_kinematics.inverse_kinematics(target_position, target_orientation)
        self.update_plot(target_position)

        pwm_map = {}
        for i in range(6):
            if i in [2]:
                pwm_map[i] = self.servo_controller.degrees_to_pwm(valuedict[i], degreelimits=(-360, 0))
            else:
                pwm_map[i] = self.servo_controller.degrees_to_pwm(valuedict[i])

        self.servo_controller.move_servos(pwm_map)

if __name__ == "__main__":
    arm_controller = ArmController("arm.urdf", active_links_mask=[False, True, True, True, True, True], show_plot=False)
    arm_controller.move(3, 0, 3)
    