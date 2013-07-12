#!/usr/bin/env python
import roslib; roslib.load_manifest('semi_static_transform_publisher')
import rospy, sys 
from std_msgs.msg import *
import semi_static_transform_publisher
from semi_static_transform_publisher.srv import *
import tf; from tf import *
from tf.transformations import *


class SemiStaticTransformPublisher():

  def __init__(self):
    self.args_ = rospy.myargv(argv=sys.argv)
    self.name_ = self.args_[1]
    self.xyz_  = [float(self.args_[2]),float(self.args_[3]),float(self.args_[4])]
    self.rpy_  = [float(self.args_[7]),float(self.args_[6]),float(self.args_[5])]
    self.parent_ = self.args_[8]
    self.child_ = self.args_[9]
    self.rate_ = int(self.args_[10])
    self.br_ = TransformBroadcaster()
    rospy.init_node('semi_static_transform_publisher', anonymous = True)

    print '[' + self.name_ + '] publishing xyz: [' + str(self.xyz_) + '], rpy: [' + str(self.rpy_) + '] with Parent: [' + self.parent_ + '] - Child: [' + self.child_ + ']' 

    self.update_transform_srv = rospy.Service('semi_static/'+self.name_+'/update_transform', 
                                              semi_static_transform_publisher.srv.update_transform, self.update_transform)

    r = rospy.Rate(self.rate_)
    while not rospy.is_shutdown():
      self.publish_transform()
      r.sleep()

  def update_transform(self,req):
    self.xyz_ = [req.x,req.y,req.z]
    self.rpy_ = [req.roll,req.pitch,req.yaw]
    rospy.loginfo('[' + self.name_ + '] Updated xyz:' + str(self.xyz_) + ', rpy: ' + str(self.rpy_))
    return 'SUCCESS: updated xyz to ' + str(self.xyz_) + ', rpy to ' + str(self.rpy_)

  def publish_transform(self):
    pass
    self.br_.sendTransform(self.xyz_, tf.transformations.quaternion_from_euler(self.rpy_[0], self.rpy_[1], self.rpy_[2]),
                     rospy.Time.now(), self.child_, self.parent_)


if __name__ == '__main__':
    xform = SemiStaticTransformPublisher()