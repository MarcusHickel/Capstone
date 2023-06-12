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

        self.AzAdj = 1.2 #Azimuth adjustment value (z axis) left right (Scales how velocity change)
        self.AlAdj = 4 #Altitude adjustment value (y axis) up down

        self.Altemp = 0
        self.Aztemp = 0

        self.Aldiff = 0 #Change in velcoity
        self.Azdiff = 0

        #Define boundry 
        self.xlimit = float(5.0)
        self.ylimit = float(5.0)
        
        #Timer for search
        self.lastRX = time.time() 
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    # def listener_set(self,msg):
    #     msg.position
    #     self.get_logger().info('"%s"' % msg.positio)
    
    #Searching for the rocket
    def timer_callback(self):
        if self.lastRX + 5 < time.time():
            self.get_logger().info('Last Received %gs ago return to origin' %(time.time()-self.lastRX))
            
            # self.Az = self.Az + 0.001

            msg = Float64MultiArray()
            msg.data = [float(1.0), float(-1.0)] # Z(Azimuth) Y(Altitude)
            self.publisher.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
        elif self.lastRX + 1 < time.time():
            self.get_logger().info('Last Received %gs ago searching...' %(time.time()-self.lastRX))
            

        


    
    #Main control
    def listener_callback(self, msg):

        #Pull Rocket postion
        self.x = msg.x - 320.0 #X pos
        self.y = msg.y - 240.0 #Y pos

        self.Altemp = self.AlAdj*(self.y**2)*0.000017361 # Scale factor which is was found by getting finding where a parabola =1 at the edge of screen (480px)
        self.Aztemp = self.AzAdj*(self.x**2)*0.000009766 # Scale factor which is was found by getting finding where a parabola =1 at the edge of screen (640px)

        self.Aldiff = self.Al - self.Altemp
        self.Azdiff = self.Az - self.Aztemp

        #Is it +x or -x boundry 
        if self.x > self.xlimit:
            self.Az = -self.Aztemp
            self.get_logger().info('x +outside "%d" Velo Adjustment %f %f' % (self.x, self.Azdiff, self.Az))
        elif self.x < -self.xlimit:
            self.Az = +self.Aztemp
            self.get_logger().info('x -outside "%d" Velo Adjustment %f %f' % (self.x, self.Azdiff, self.Az))
        else:
            self.get_logger().info('x inside   "%d"' % self.x)

        

        #Is it +y/-y boundry
        if self.y > self.ylimit:
            self.Al = -self.Altemp
            self.get_logger().info('y +outside "%d" Velo Adjustment %f %f' % (self.y, self.Aldiff, self.Al))
        elif self.y < -self.ylimit:
            self.Al =  +self.Altemp
            self.get_logger().info('y -outside "%d" Velo Adjustment %f %f' % (self.y, self.Aldiff, self.Al))
        else:
            self.get_logger().info('y inside   "%d"' % self.y)

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