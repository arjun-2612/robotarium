# robotarium

Collection of robot descriptions for all robots. Contains URDF, MJCF, and USD formats.

```
robotarium/
└── cobra/
    ├── urdf/
    │   ├── cobra.urdf.xacro
    │   ├── cobra.urdf
    │   └── assets/
    │       ├── bodyModule.dae
    │       └── ...
    ├── mjcf/
    │   ├── cobra.xml
    │   ├── scene.xml
    │   └── assets/
    │       ├── bodyModule_0.obj
    │       └── ...
    ├── usd/
    │   ├── cobra.usda
    │   └── configuration/
    │       ├── cobra_base.usdc
    │       ├── cobra_physics.usda
    │       ├── cobra_robot.usda
    │       └── cobra_sensor.usda
    ├── husky-b/
    │   └── ...
    └── ...
```

## Generate meshes
```sh
uv run meshify.py meshes
```
