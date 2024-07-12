class ArmKinematics:
    def __init__(self, urdf_file, active_links_mask):
        self.chain = ikpy.chain.Chain.from_urdf_file(urdf_file, active_links_mask=active_links_mask)
        self.ik = np.zeros(len(self.chain.links))

    def inverse_kinematics(self, target_position, target_orientation):
        old_position = self.ik.copy()
        self.ik = self.chain.inverse_kinematics(target_position, target_orientation, orientation_mode="Z", initial_position=old_position)
        value_dict = {index: math.degrees(value) for index, value in enumerate(self.ik.tolist()[1:])}
        return value_dict

    def forward_kinematics(self):
        return self.chain.forward_kinematics(self.ik)

    def plot_chain(self, ax, target_position):
        self.chain.plot(self.ik, ax, target=target_position)