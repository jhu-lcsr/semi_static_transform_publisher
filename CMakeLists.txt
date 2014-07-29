cmake_minimum_required(VERSION 2.8.3)
project(semi_static_transform_publisher)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  geometry_msgs)

catkin_python_setup()


# Generate services in the 'srv' folder
add_service_files(
  FILES
  update_transform.srv
)

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(
	CATKIN_DEPENDS message_runtime
)