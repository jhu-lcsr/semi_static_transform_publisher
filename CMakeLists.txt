cmake_minimum_required(VERSION 2.8.3)
project(semi_static_transform_publisher)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_runtime
  message_generation
)


## Generate services in the 'srv' folder
add_service_files(
  FILES
  UpdateTransform.srv
)

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES std_msgs # Or other packages containing msgs
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES instructor
  CATKIN_DEPENDS std_msgs message_runtime
#  DEPENDS system_lib
)
