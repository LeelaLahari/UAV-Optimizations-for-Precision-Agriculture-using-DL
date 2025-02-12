from dronesim import Drone, IMUSensor, GPSSensor, CameraSensor

# Initialize the drone
drone = Drone()

# Attach sensors
imu = IMUSensor()
gps = GPSSensor()
camera = CameraSensor()

drone.add_sensor(imu)
drone.add_sensor(gps)
drone.add_sensor(camera)

# Fixed initial position (Location A)
initial_position = (0, 0, 0)  # (x, y, z) coordinates

# User inputs for destination (Location B)
destination_x = float(input("Enter destination X coordinate: "))
destination_y = float(input("Enter destination Y coordinate: "))
destination_z = float(input("Enter destination Z coordinate (altitude): "))
destination = (destination_x, destination_y, destination_z)

# User inputs for flight parameters
speed = float(input("Enter desired speed (m/s): "))
direction = float(input("Enter desired direction (degrees from north): "))


import numpy as np

def calculate_path(start, end, speed, direction):
    # Calculate distance
    distance = np.linalg.norm(np.array(end) - np.array(start))
    
    # Calculate number of steps based on speed
    steps = int(distance / speed)
    
    # Generate waypoints
    waypoints = []
    for i in range(steps + 1):
        waypoint = (
            start[0] + i * (end[0] - start[0]) / steps,
            start[1] + i * (end[1] - start[1]) / steps,
            start[2] + i * (end[2] - start[2]) / steps,
        )
        waypoints.append(waypoint)
    
    return waypoints

# Generate waypoints
path = calculate_path(initial_position, destination, speed, direction)


import time

for waypoint in path:
    drone.move_to(waypoint)
    print(f"Moving to waypoint: {waypoint}")
    time.sleep(1)  # Adjust based on simulation requirements

print("Destination reached.")



# Example: Retrieve IMU data
imu_data = imu.get_data()
print(f"IMU Data: {imu_data}")

# Example: Retrieve GPS data
gps_data = gps.get_data()
print(f"GPS Data: {gps_data}")

# Example: Capture image from camera
image = camera.capture_image()
#image.save("drone_view.png")



