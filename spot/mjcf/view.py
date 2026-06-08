import mujoco
import mujoco.viewer
import time 
from pathlib import Path

ROOT = Path(__import__("subprocess").check_output(["git","rev-parse","--show-toplevel"], text=True).strip())
model = mujoco.MjModel.from_xml_path(f"{ROOT}/sslab-robots/spot/mjcf/scene.xml")
data  = mujoco.MjData(model)

# Start from a known state (optional)
mujoco.mj_resetData(model, data)
mujoco.mj_forward(model, data)

with mujoco.viewer.launch_passive(model, data) as viewer:
    # run roughly in real time
    while viewer.is_running():
        step_start = time.time()

        # advance physics by 1 step
        mujoco.mj_step(model, data)

        # IMPORTANT: update the viewer
        viewer.sync()

        # sleep so we don't run faster than real time
        dt = model.opt.timestep
        sleep = dt - (time.time() - step_start)
        if sleep > 0:
            time.sleep(sleep)