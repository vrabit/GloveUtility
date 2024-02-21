from controller import Robot,Keyboard

robot = Robot()
timestep = int(robot.getBasicTimeStep())


motor1 = robot.getDevice("m1_motor")  
motor2 = robot.getDevice("m2_motor")  
motor3 = robot.getDevice("m3_motor")  
motor4 = robot.getDevice("m4_motor")  

keyboard = Keyboard()
keyboard.enable(timestep)


motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
motor3.setPosition(float('inf'))
motor4.setPosition(float('inf'))


velocity = 1
motor1.setVelocity(velocity)
motor2.setVelocity(velocity)
motor3.setVelocity(velocity)
motor4.setVelocity(velocity)

holder = 55.4
second = 0
forward = 0.001
while robot.step(timestep) != -1:
    key = keyboard.getKey()
    second +=1
    if second > 75:
        if ((second // 10)) % 2 != 0:
           holder = 55.3359
        else:
           holder = 55.4
    holder1 = -(holder)
    holder2= holder
    holder3 = -(holder)
    holder4 = holder
    
    if key == Keyboard.UP:
        holder1 = holder1 + forward
        holder2 = holder2 - forward
        holder3 = holder3 - forward
        holder4 = holder4 + forward
    elif key == Keyboard.DOWN:
        holder1 = holder1 - forward
        holder2 = holder2 + forward
        holder3 = holder3 + forward
        holder4 = holder4 - forward
    elif key == Keyboard.LEFT:
        holder1 = holder1 + forward
        holder2 = holder2 + forward
        holder3 = holder3 - forward
        holder4 = holder4 - forward
    elif key == Keyboard.RIGHT:
        holder1 = holder1 - forward
        holder2 = holder2 - forward
        holder3 = holder3 + forward
        holder4 = holder4 + forward
    
    
    
    
    motor1.setVelocity(holder1)
    motor2.setVelocity(holder2)
    motor3.setVelocity(holder3)
    motor4.setVelocity(holder4)
        
