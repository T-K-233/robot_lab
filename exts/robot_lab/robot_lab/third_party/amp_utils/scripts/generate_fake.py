import numpy as np


fl_hip_idx = 6
fl_toe_idx = 10
fr_hip_idx = 11
fr_toe_idx = 15
rl_hip_idx = 16
rl_toe_idx = 19
rr_hip_idx = 20
rr_toe_idx = 23

mocap_frames = np.zeros((200, 27, 3))
time_series = np.linspace(0, 1, 200)

# frames are in (-y, z, x) order

mocap_frames[:, 0, 2] = 0.4

mocap_frames[:, 3, 0] = .3
mocap_frames[:, 3, 2] = .4#  + np.sin(time_series * 2 * np.pi) * 0.1

mocap_frames[:, fl_hip_idx, 0] = .2
mocap_frames[:, fl_hip_idx, 1] = 0.1
mocap_frames[:, fl_hip_idx, 2] = 0.4

mocap_frames[:, fl_toe_idx, 0] = .2
mocap_frames[:, fl_toe_idx, 1] = 0.1
mocap_frames[:, fl_toe_idx, 2] = np.abs(np.sin(time_series * 2 * np.pi) * 0.2)

mocap_frames[:, fr_hip_idx, 0] = .2
mocap_frames[:, fr_hip_idx, 1] = -0.1
mocap_frames[:, fr_hip_idx, 2] = 0.4

mocap_frames[:, fr_toe_idx, 0] = .2
mocap_frames[:, fr_toe_idx, 1] = -0.1
mocap_frames[:, fr_toe_idx, 2] = np.abs(np.cos(time_series * 2 * np.pi) * 0.2)

mocap_frames[:, rl_hip_idx, 0] = -.2
mocap_frames[:, rl_hip_idx, 1] = 0.1
mocap_frames[:, rl_hip_idx, 2] = 0.4

mocap_frames[:, rl_toe_idx, 0] = -0.2
mocap_frames[:, rl_toe_idx, 1] = 0.1
mocap_frames[:, rl_toe_idx, 2] = 0.1

mocap_frames[:, rr_hip_idx, 0] = -.2
mocap_frames[:, rr_hip_idx, 1] = -0.1
mocap_frames[:, rr_hip_idx, 2] = 0.4

mocap_frames[:, rr_toe_idx, 0] = -0.2
mocap_frames[:, rr_toe_idx, 1] = -0.1
mocap_frames[:, rr_toe_idx, 2] = 0.1

# write as csv
filename = "/home/tk/Downloads/robot_lab/exts/robot_lab/robot_lab/third_party/amp_utils/datasets/keypoint_datasets/ai4animation/dog_donothing_joint_pos.txt"

# shuffle axis from (-y, z, x) to (x, y, z)
mocap_frames_coord = np.zeros_like(mocap_frames)
mocap_frames_coord[:, :, 0] = mocap_frames[:, :, 1]
mocap_frames_coord[:, :, 1] = mocap_frames[:, :, 2]
mocap_frames_coord[:, :, 2] = mocap_frames[:, :, 0]

mocap_frames = np.reshape(mocap_frames_coord, (-1, 27 * 3))

with open(filename, "w") as f:
    for frame in mocap_frames:
        for value in frame[:-1]:
            f.write(f"{value}, ")
        # remove the last comma
        f.write(f"{frame[-1]}")
        f.write("\n")

