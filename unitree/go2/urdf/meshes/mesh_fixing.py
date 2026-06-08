import trimesh

meshes_dir = '/home/arjun-laptop/Documents/husky-b-rl/husky_beta_ros2/go2/meshes'
meshes = ['base.stl', 'hip.stl', 'thigh.stl', 'calf.stl', 'foot.stl']

densities = {
    "onyx": 1230, 
    "carbon_fiber": 1600,
    "pla": 1240,
    "aluminum": 2700,
    "hsp": 1200
} # in kg/m^3

stl_file = f"{meshes_dir}/{meshes[0]}"
with open(stl_file, 'rb') as f:
    mesh = trimesh.load_mesh(file_obj=f, file_type='stl')

# Compute the inertia matrix about the center of mass
inertia = mesh.moment_inertia * densities["hsp"]
center_of_mass = mesh.center_mass
volume = mesh.volume
mass = volume * densities["hsp"] 

print(f"####################################### {meshes[0]} #######################################")
print("Mass:", mass)
print("Volume:", volume)
print("Center of Mass:", center_of_mass)
print("Inertia Matrix:\n", inertia)

stl_file = f"{meshes_dir}/{meshes[1]}"
with open(stl_file, 'rb') as f:
    mesh = trimesh.load_mesh(file_obj=f, file_type='stl')

# Compute the inertia matrix about the center of mass
inertia = mesh.moment_inertia * densities["hsp"]
center_of_mass = mesh.center_mass
volume = mesh.volume
mass = volume * densities["hsp"] 

print(f"####################################### {meshes[1]} #######################################")
print("Mass:", mass)
print("Volume:", volume)
print("Center of Mass:", center_of_mass)
print("Inertia Matrix:\n", inertia)

stl_file = f"{meshes_dir}/{meshes[2]}"
with open(stl_file, 'rb') as f:
    mesh = trimesh.load_mesh(file_obj=f, file_type='stl')

# Compute the inertia matrix about the center of mass
inertia = mesh.moment_inertia * densities["aluminum"]
center_of_mass = mesh.center_mass
volume = mesh.volume
mass = volume * densities["aluminum"] 

print(f"####################################### {meshes[2]} #######################################")
print("Mass:", mass)
print("Volume:", volume)
print("Center of Mass:", center_of_mass)
print("Inertia Matrix:\n", inertia)

stl_file = f"{meshes_dir}/{meshes[3]}"
with open(stl_file, 'rb') as f:
    mesh = trimesh.load_mesh(file_obj=f, file_type='stl')

# Compute the inertia matrix about the center of mass
inertia = mesh.moment_inertia * densities["aluminum"]
center_of_mass = mesh.center_mass
volume = mesh.volume
mass = volume * densities["aluminum"] 

print(f"####################################### {meshes[3]} #######################################")
print("Mass:", mass)
print("Volume:", volume)
print("Center of Mass:", center_of_mass)
print("Inertia Matrix:\n", inertia)

stl_file = f"{meshes_dir}/{meshes[4]}"
with open(stl_file, 'rb') as f:
    mesh = trimesh.load_mesh(file_obj=f, file_type='stl')

# Compute the inertia matrix about the center of mass
inertia = mesh.moment_inertia * densities["hsp"]
center_of_mass = mesh.center_mass
volume = mesh.volume
mass = volume * densities["hsp"] 

print(f"####################################### {meshes[4]} #######################################")
print("Mass:", mass)
print("Volume:", volume)
print("Center of Mass:", center_of_mass)
print("Inertia Matrix:\n", inertia)