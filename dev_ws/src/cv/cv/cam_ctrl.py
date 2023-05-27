import rclpy
from rclpy.node import Node
from geometry_msgs.msg      import Point
from std_msgs.msg import Float64MultiArray

from std_msgs.msg import String

import time


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('cam_ctrl')
        self.subscription = self.create_subscription(
            Point,
            '/detection_pos',
            self.listener_callback,
            10)
        
        # self.subscription = self.create_subscription(
        #     String,
        #     '/joint_states',
        #     self.listener_set,
        #     10)
        # self.subscription 

        self.publisher = self.create_publisher(
            Float64MultiArray, 
            '/forward_position_controller/commands',
            10)
        
        self.i = 0
        self.x = 0
        self.y = 0

        self.Az = 0
        self.Al = 0

        #Define boundry 
        self.xlimit = float(20.0)
        self.ylimit = float(20.0)
        
        #Timer for search
        self.lastRX = time.time() 
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    # def listener_set(self,msg):
    #     msg.position
    #     self.get_logger().info('"%s"' % msg.positio)
    
    #Searching for the rocket
    def timer_callback(self):
        if self.lastRX + 1 < time.time():
            self.get_logger().info('Last Received %ss ago searching...' %(time.time()-self.lastRX))
            
            self.Az = self.Az + 0.001

            msg = Float64MultiArray()
            msg.data = [float(self.Az), float(self.Al)] # Z(Azimuth) Y(Altitude)
            self.publisher.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)


    
    #Main control
    def listener_callback(self, msg):

        #Pull Rocket postion
        self.x = msg.x - 320.0
        self.y = msg.y - 240.0


        #Is it +x or -x boundry
        if self.x > self.xlimit:
            self.Az = self.Az - 0.001
            self.get_logger().info('x outside+"%s"' % self.x)
        elif self.x < -self.xlimit:
            self.Az = self.Az + 0.001
            self.get_logger().info('x outside-"%s"' % self.x)
        else:
            self.get_logger().info('x inside"%s"' % self.x)

        

        #Is it +y/-y boundry
        if self.y > self.ylimit:
            self.Al = self.Al - 0.001
            self.get_logger().info('y outside+"%s"' % self.y)
        elif self.y < -self.ylimit:
            self.Al = self.Al + 0.001
            self.get_logger().info('y outside-"%s"' % self.y)
        else:
            self.get_logger().info('y inside"%s"' % self.y)

        if self.Al < 0:
            self.Al = 0

        # if self.Az < 0:
        #     self.Az = 0


        # Publish
        msg = Float64MultiArray()
        msg.data = [float(self.Az), float(self.Al)] # Z(Azimuth) Y(Altitude)
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        # self.i += float(0.0001)
        self.lastRX = time.time() 

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()