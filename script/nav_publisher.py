#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from actionlib_msgs.msg import GoalStatus
from actionlib_msgs.msg import GoalStatusArray

def move_base_goal_publisher():
  # ROS 노드 초기화
  rospy.init_node('move_base_goal_publisher', anonymous=True)
  # Publisher 설정
  goal_publisher = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=10)
  # 도착 상태를 확인하기 위한 Subscriber 설정
  goal_status_subscriber = rospy.Subscriber('/move_base/status', GoalStatusArray, goal_status_callback)


  if flag == 1:
    # MoveBaseActionGoal 메시지 생성
    
    goal_msg = MoveBaseActionGoal()
    goal_msg.header = Header()
    goal_msg.goal.target_pose = PoseStamped()
    goal_msg.goal.target_pose.header = Header()
    goal_msg.goal.target_pose.header.frame_id = 'map'
    goal_msg.goal.target_pose.pose = Pose(Point(1.0, 2.5, 0.0), Quaternion(0.0, 0.0, 0.75, 0.66))
    # goal 데이터 publish
    goal_publisher.publish(goal_msg)
    # 도착 확인을 위한 루프
    rate = rospy.Rate(10)  # 10 Hz로 루프 설정
  
  if flag ==2:
    goal_msg = MoveBaseActionGoal()
     goal_msg.header = Header()
     goal_msg.goal.target_pose = PoseStamped()
     goal_msg.goal.target_pose.header = Header()
     goal_msg.goal.target_pose.header.frame_id = 'map'
     goal_msg.goal.target_pose.pose = Pose(Point(2.0, 2.5, 0.0), Quaternion(0.0, 0.0, 0.75, 0.66))
     # goal 데이터 publish
     goal_publisher.publish(goal_msg)
     # 도착 확인을 위한 루프
     rate = rospy.Rate(10)  # 10 Hz로 루프 설정
  
  if flag ==3:
     goal_msg = MoveBaseActionGoal()
     goal_msg.header = Header()
     goal_msg.goal.target_pose = PoseStamped()
     goal_msg.goal.target_pose.header = Header()
     goal_msg.goal.target_pose.header.frame_id = 'map'
     goal_msg.goal.target_pose.pose = Pose(Point(3.0, 2.5, 0.0), Quaternion(0.0, 0.0, 0.75, 0.66))
     # goal 데이터 publish
     goal_publisher.publish(goal_msg)
     # 도착 확인을 위한 루프
     rate = rospy.Rate(10)  # 10 Hz로 루프 설정
  
  if flag ==4:
     goal_msg = MoveBaseActionGoal()
     goal_msg.header = Header()
     goal_msg.goal.target_pose = PoseStamped()
     goal_msg.goal.target_pose.header = Header()
     goal_msg.goal.target_pose.header.frame_id = 'map'
     goal_msg.goal.target_pose.pose = Pose(Point(4.0, 2.5, 0.0), Quaternion(0.0, 0.0, 0.75, 0.66))
     # goal 데이터 publish
     goal_publisher.publish(goal_msg)
     # 도착 확인을 위한 루프
     rate = rospy.Rate(10)  # 10 Hz로 루프 설정
  
  if flag ==5:
     goal_msg = MoveBaseActionGoal()
     goal_msg.header = Header()
     goal_msg.goal.target_pose = PoseStamped()
     goal_msg.goal.target_pose.header = Header()
     goal_msg.goal.target_pose.header.frame_id = 'map'
     goal_msg.goal.target_pose.pose = Pose(Point(5.0, 2.5, 0.0), Quaternion(0.0, 0.0, 0.75, 0.66))
     # goal 데이터 publish
     goal_publisher.publish(goal_msg)
     # 도착 확인을 위한 루프
     rate = rospy.Rate(10)  # 10 Hz로 루프 설정

  if flag ==6:
     goal_msg = MoveBaseActionGoal()
     goal_msg.header = Header()
     goal_msg.goal.target_pose = PoseStamped()
     goal_msg.goal.target_pose.header = Header()
     goal_msg.goal.target_pose.header.frame_id = 'map'
     goal_msg.goal.target_pose.pose = Pose(Point(6.0, 2.5, 0.0), Quaternion(0.0, 0.0, 0.75, 0.66))
     # goal 데이터 publish
     goal_publisher.publish(goal_msg)
     # 도착 확인을 위한 루프
     rate = rospy.Rate(10)  # 10 Hz로 루프 설정
  
     
  ef goal_status_callback(msg):
     global flag=1
     for status in msg.status_list:
         if status.status == GoalStatus.SUCCEEDED:
             flag += 1
             return
  
if __name__ == '__main__':
    try:
        flag = 0  # flag 변수 초기화
        move_base_goal_publisher()
    except rospy.ROSInterruptException:
        pass
