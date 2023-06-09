import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
from geometry_msgs.msg      import Point
import cv2 # OpenCV library
import numpy as np

from std_msgs.msg import String


class MinimalSubscriber(Node): #Change name of this class

    def __init__(self):
        super().__init__('rocket_detect')
        self.subscription = self.create_subscription(
            Image,
            'my_camera/image_raw',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        #Creating a publisher to output data
        self.pub = self.create_publisher(Point, '/detection_pos', 1)

        # Used to convert between ROS and OpenCV images
        self.br = CvBridge()

    def listener_callback(self, data):
        # self.get_logger().info('I hear %s"' % msg.data)
        # self.get_logger().info('Receiving video frame')
    
        # Convert ROS Image message to OpenCV image
        current_frame = self.br.imgmsg_to_cv2(data)

        hue_min = np.array([5, 20, 20],np.uint8)
        hue_max = np.array([20, 255, 255],np.uint8)

        frame_threshed = cv2.inRange(current_frame, hue_min, hue_max)
        masked = cv2.bitwise_and(current_frame,current_frame,mask=frame_threshed)
        # cv2.imwrite('output2.jpg', frame_threshed)
        frame_threshed = cv2.bitwise_not(frame_threshed)
        cv2.imshow("threshold", frame_threshed)
        cv2.imshow("mask",masked)

        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()

        # Filter by Area.
        params.filterByArea = True
        params.minArea = 1

        # Filter by Circularity
        params.filterByCircularity = False
        params.minCircularity = 0.1

        # Filter by Convexity
        params.filterByConvexity = False
        params.minConvexity = 0.87
            
        # Filter by Inertia
        params.filterByInertia = False
        params.minInertiaRatio = 0.1

        # Create a detector with the parameters
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3 :
            detector = cv2.SimpleBlobDetector(params)
        else : 
            detector = cv2.SimpleBlobDetector_create(params)


        # Detect blobs.
        keypoints = detector.detect(frame_threshed)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
        # the size of the circle corresponds to the size of blob

        im_with_keypoints = cv2.drawKeypoints(current_frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        # Show blobs
        
        
        point_out = Point()

        for i, kp in enumerate(keypoints):
            if i == 0:
                    x = kp.pt[0]
                    y = kp.pt[1]
                    s = kp.size
                    im_with_keypoints = cv2.line(im_with_keypoints, (320, 240),(int(x), int(y)), (0, 255, 0), 1)
            if (s > point_out.z):                    
                                point_out.x = x
                                point_out.y = y
                                point_out.z = s

        if (point_out.z > 0):
            self.pub.publish(point_out) 

        im_with_keypoints = cv2.rectangle(im_with_keypoints, (240, 180),(400, 300), (0, 255, 0), 1) #Box
        cv2.imshow("Detection", im_with_keypoints)

        try:self.get_logger().info(f"Pt {i}: ({x},{y},{s})")
        except:self.get_logger().info('failed')
        cv2.waitKey(1)



def main(args=None):
        rclpy.init(args=args)

        rocket_detect = MinimalSubscriber()

        rclpy.spin(rocket_detect)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        rocket_detect.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()