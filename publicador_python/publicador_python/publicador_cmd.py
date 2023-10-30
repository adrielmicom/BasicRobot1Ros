#/cmd_vel [geometry_msgs/msg/Twist] donde voy a querer publicar, necesito el mismo mensaje

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from geometry_msgs.msg import Twist


class PublicadorCMD(Node):

    def __init__(self):
        super().__init__('publicador_cmd')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)     #tipo de mensaje, nombre del topic, Qos ros2 nodos mismo para comunicarse
        timer_period = 0.01  # tiempo cada cual se ejecuta la siguiente funcion/  se ejecuta la publicacion ddel mensaje cada ese tiempo
        self.timer = self.create_timer(timer_period, self.timer_callback)    #se ejecuta la funcion timmer callbacn cada timer period

    def timer_callback(self):
        msg = Twist()
        msg.linear.x= 0.1
        #msg.angular.z
        #AQUI YA PODRIA CRERAR TRAYECTORIAS, ese sera el mensaje, o voy mandando
        self.publisher_.publish(msg)    #publca el mensaje
        self.get_logger().info('Publishing: "%s"' % msg)   #como un print get_logger para mostrar por pantalla



def main(args=None):
    rclpy.init(args=args)  #para implementar nodos con pyton

    publicador_cmd = PublicadorCMD()  #creas una variable de esa clase

    rclpy.spin(publicador_cmd) #corre la clase

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publicador_cmd.destroy_node()
    rclpy.shutdown()






# class MinimalPublisher(Node):

#     def __init__(self):
#         super().__init__('minimal_publisher')
#         self.publisher_ = self.create_publisher(String, 'topic', 10)     #tipo de mensaje, nombre del topic, Qos ros2 nodos mismo para comunicarse
#         timer_period = 0.01  # tiempo cada cual se ejecuta la siguiente funcion/  se ejecuta la publicacion ddel mensaje cada ese tiempo
#         self.timer = self.create_timer(timer_period, self.timer_callback)    #se ejecuta la funcion timmer callbacn cada timer period
#         self.i = 0

#     def timer_callback(self):
#         msg = String()
#         msg.data = 'Hello World: %d' % self.i
#         self.publisher_.publish(msg)    #publca el mensaje
#         self.get_logger().info('Publishing: "%s"' % msg.data)   #como un print get_logger para mostrar por pantalla
#         self.i += 1


# def main(args=None):
#     rclpy.init(args=args)  #para implementar nodos con pyton

#     minimal_publisher = MinimalPublisher()  #creas una variable de esa clase

#     rclpy.spin(minimal_publisher) #corre la clase

#     # Destroy the node explicitly
#     # (optional - otherwise it will be done automatically
#     # when the garbage collector destroys the node object)
#     minimal_publisher.destroy_node()
#     rclpy.shutdown()


if __name__ == '__main__':
    main()
