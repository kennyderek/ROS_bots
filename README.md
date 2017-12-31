Uses two nodes (a Runner and an Observer).
The Runner creates the desired number, passed in as a command line argument, of 'bots'
and assigns random position functions to their x, y and z coordinates. Runner publishes
the (x, y, z) coordinates of each bot to a ROS topic (called 'pos_topic'),
which gets read & printed by the Observer.


To build project:
- the program was written in Python 2.7.12 (the only way my linux VM works)
  For python 3.5, the print statements in the code will need to be changed to include parenthesis.
  Print statements are located in observer.py and runner.py in the scripts folder.

- create a catkin_ws if one is not already created (I used ROS kinetic)
 (follow instructions here: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
 
- in the src folder of your workspace, enter 'git clone https://github.com/kennyderek/ROS_bots.git' on terminal

- in catkin_ws, enter 'source devel/build'


How to run:

we will now need 3 different terminal tabs to run the Runner/Observer nodes
- first terminal:
    --> roscore
- second terminal:
    --> rosrun jetbrains_task runner.py         (if you just wish to run one bot)
    OR
    --> rosrun jetbrains_task runner.py _numbots:=100        (creates 100 bots to keep track of. Can change number as desired)
- third terminal:
    --> rosrun jetbrains_task observer.py 


In the runner.py terminal you will see:

creating 10 bots
Publishing locations
[INFO] [1514675657.532913]: time elapsed: 0.002120971
[INFO] [1514675658.033852]: time elapsed: 0.502940177
[INFO] [1514675658.533420]: time elapsed: 1.002565145
[INFO] [1514675659.033450]: time elapsed: 1.502618074
...


In the terminal in which the observer.py was run, you will see:

[INFO] [1514675662.035074]: Bot 1 at (x, y, z) coordinates: (-0.9781627058982849, 20.27720832824707, 20.27720832824707)
[INFO] [1514675662.035713]: Bot 2 at (x, y, z) coordinates: (20.27720832824707, -0.9781627058982849, -0.9781627058982849)
[INFO] [1514675662.036069]: Bot 3 at (x, y, z) coordinates: (-0.9781627058982849, 20.27720832824707, -0.20784056186676025)
[INFO] [1514675662.036355]: Bot 4 at (x, y, z) coordinates: (20.27720832824707, -0.9781627058982849, -0.9781627058982849)
[INFO] [1514675662.036628]: Bot 5 at (x, y, z) coordinates: (20.27720832824707, -0.9781627058982849, -0.9781627058982849)
[INFO] [1514675662.037012]: Bot 6 at (x, y, z) coordinates: (-0.9781627058982849, -0.20784056186676025, -0.20784056186676025)
[INFO] [1514675662.037214]: Bot 7 at (x, y, z) coordinates: (-0.9781627058982849, 20.27720832824707, -0.9781627058982849)
[INFO] [1514675662.037419]: Bot 8 at (x, y, z) coordinates: (-0.9781627058982849, -0.20784056186676025, -0.9781627058982849)
[INFO] [1514675662.037608]: Bot 9 at (x, y, z) coordinates: (-0.9781627058982849, -0.20784056186676025, 20.27720832824707)
[INFO] [1514675662.037803]: Bot 10 at (x, y, z) coordinates: (20.27720832824707, -0.9781627058982849, 20.27720832824707)
********
[INFO] [1514675662.534759]: Bot 1 at (x, y, z) coordinates: (-0.9581419825553894, 25.02745819091797, 25.02745819091797)
[INFO] [1514675662.535173]: Bot 2 at (x, y, z) coordinates: (25.02745819091797, -0.9581419825553894, -0.9581419825553894)
[INFO] [1514675662.535464]: Bot 3 at (x, y, z) coordinates: (-0.9581419825553894, 25.02745819091797, 0.28629350662231445)
[INFO] [1514675662.535739]: Bot 4 at (x, y, z) coordinates: (25.02745819091797, -0.9581419825553894, -0.9581419825553894)
[INFO] [1514675662.536008]: Bot 5 at (x, y, z) coordinates: (25.02745819091797, -0.9581419825553894, -0.9581419825553894)
[INFO] [1514675662.536275]: Bot 6 at (x, y, z) coordinates: (-0.9581419825553894, 0.28629350662231445, 0.28629350662231445)
[INFO] [1514675662.536544]: Bot 7 at (x, y, z) coordinates: (-0.9581419825553894, 25.02745819091797, -0.9581419825553894)
[INFO] [1514675662.537532]: Bot 8 at (x, y, z) coordinates: (-0.9581419825553894, 0.28629350662231445, -0.9581419825553894)
[INFO] [1514675662.537860]: Bot 9 at (x, y, z) coordinates: (-0.9581419825553894, 0.28629350662231445, 25.02745819091797)
[INFO] [1514675662.538592]: Bot 10 at (x, y, z) coordinates: (25.02745819091797, -0.9581419825553894, 25.02745819091797)
********
...

