#!/usr/bin/python
import rospy
from control_msgs.msg import JointTrajectoryGoal, JointTrajectoryAction
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import actionlib

if __name__=='__main__':
    rospy.init_node('commando')

    client = actionlib.SimpleActionClient('/r2/r_arm_controller/joint_trajectory_action',
JointTrajectoryAction)
    client.wait_for_server()
    goal = JointTrajectoryGoal()
    t = goal.trajectory
    t.header.stamp = rospy.Time.now()
    t.joint_names = ['/r2/right_arm/joint%d'%i for i in range(7)]
    for i in range(0, 10):
        pt = JointTrajectoryPoint()
        pt.positions = [0.0]*7
        pt.positions[0] = -1.5 + i * 3.0/10
        pt.time_from_start = rospy.Duration(i)
        t.points.append(pt)
    client.send_goal(goal)
    client.wait_for_result()
    print client.get_result()
    rospy.spin()
