#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import voltmeter as vl
import time

def publishVoltage(volt_mv):
    publisher = rospy.Publisher('m5stack_voltage_mv', Float64, queue_size=10)

    rospy.loginfo(volt_mv)
    publisher.publish(volt_mv)


def voltTalker():
    rospy.init_node('m5stack_voltmeter_node', anonymous=True)
    voltmeter = vl.Voltmeter()
    voltmeter.setGain(vl.ADS1115_PAG_1024) # max input voltage is 8V
    while not rospy.is_shutdown():
        # print(str(voltmeter.getVoltage()*0.001) + "[V]")
        publishVoltage(voltmeter.getVoltage())
        time.sleep(0.1)
    pass

if __name__ == "__main__":
    try:
        voltTalker()
    except rospy.ROSInterruptException: pass
