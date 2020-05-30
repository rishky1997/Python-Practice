#5. write any program   to achieve composition in Python

class engine:
    def __init__(s):
        print("engine is started")

class car(engine):#has-a realtionship
    def move(s):
        print("car is moving")

c=car()
c.move()
