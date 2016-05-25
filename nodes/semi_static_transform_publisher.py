#!/usr/bin/env python
'''
BSD LICENSE ------------------------------------------
Copyright (c) 2016, Kelleher Guerin
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

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
