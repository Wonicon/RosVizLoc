#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import roslib
import rospy
# Get this msg from (rostopic info /camera/rgb/image_raw)
import sensor_msgs.msg
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os

label = 1
orient = 1
base = "/home/aicrobo/test"

if not os.path.exists(base):
    os.mkdir(base)
fp = open(base + "/svm_train", "a")
# http://answers.ros.org/question/210294/ros-python-save-snapshot-from-camera/
# for saving image
# Callback only exec once!

bridge = CvBridge()

def main_loop():
    global label
    global base
    global orient
    global bridge

    cmd = raw_input("capture?")
    if cmd == "exit":
        return 1

    msg = rospy.wait_for_message("/camera/rgb/image_raw",
            sensor_msgs.msg.Image)

    path = "%s/%s" % (base, label)
    if not os.path.exists(path):
        os.makedirs("%s/%s" % (base, label))
    filename = "%s/%s/%s.jpeg" % (base, label, orient)

    print "writing %s.jpeg"
    cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imwrite(filename, cv2_img)

    print "Add svm training data"
    fp.write("label %s\n" % label)
    fp.write("%s" % cv2_img)
    fp.write("\n")

    orient = orient + 1
    if orient == 5:
        label = label + 1
        orient = 1
    print "unsubscribe"
    
if __name__ == '__main__':
    rospy.init_node('get_image')
    while True:
        ret = main_loop()
        if ret == 1:
            break
    fp.close()
