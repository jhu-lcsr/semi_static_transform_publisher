semi_static_transform_publisher
===============================

This is a lightweight transform publisher, similar to static_transform_publisher, which can be updated with a new transformation at runtime using a service call.  This is useful for creating an initial static transform, which later improves because of sensing.

Usage in a launch file:

```xml
<launch>
    <node pkg="semi_static_transform_publisher" 
          type="semi_static_transform_publisher.py" 
          name="world_to_test_frame"  
          args="world_to_test_frame  1 2 1  3.1415 1.5707 -3.1415 /world /test_frame 10" 
          output="screen"/>
</launch>
```

Note the only difference between semi_static and static transform launch arguments is the addition of the node name as the first argument.

To call the update_transform service:

```bash
you@your-machine:~$ rosservice call /semi_static/world_to_test_frame/update_transform "{x: 1.0, y: 1.0, z: 0.0, roll: 0.0, pitch: 0.0, yaw: 0.0}" 

```
