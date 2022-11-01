# Task objective
Recreate a jet-steam area in the map that could most benefit our flight route. 

## Our Map
![Task 2 map](/Task_2_map.png)

## How to achive
- Base on the scenario 1 in Task 1
- Create a reduce-cost area in the map (size: vertical lengths:5 , horizontal length:infinity [cyan in colour])
- Finding the lowest Trip Cost in pothntial.

## Caution
**All variable must be specified**
.In Task2.py some new variabl were created for jet stream area
1. jc_x    : "j"stand fof jet-steam , "c"stand for cost-intesive-area,"x"stand for x-coordinate
2. jc_y    :similar to 1, "y"stand for y-coordinate

**Take the scenario for Task 2 as scenario 4**

### Possable code we need
```python
# set cost intesive area 3(jet-steam) magenta in colour(i:horizontal , j:vertical)
    jc_x, jc_y = [], []
    for i in range(9, 14):
        for j in range(-11, 61):
            jc_x.append(i)
            jc_y.append(j)
```
### Modified area
```python
# Line 25
    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y, jc_x, jc_y):
# Line 48-49
        self.jc_x = jc_x #add variables for Task2 which set to be scenario 4
        self.jc_y = jc_y
# Line 53
        self.Delta_C3 = -0.05 # cost intensive area 3(jet steam)   |Magenta in colour
# Line 148-152
                # add more cost in cost intensive area 3
                if self.calc_grid_position(node.x, self.min_x) in self.jc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.jc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C3 * self.motion[i][2]
# Line 176
        return rx, ry, goal_node.cost
# Line 284-421
def main(scenario):
    Tbest = 0

    jc_x, jc_y = [], []
    if scenario == "4" :
        # set cost intesive area 3(jet-steam) cyan in colour(i:horizontal , j:vertical)magenta        
        for i in range(-10, 60):
            for j in range(9, 14):
                jc_x.append(i)
                jc_y.append(j)

        plt.plot(jc_x, jc_y, "_m") # plot the cost intensive area 3(jet-stream) magenta

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y, jc_x, jc_y)
    rx, ry, Tbest = a_star.planning(sx, sy, gx, gy)

    if scenario == '1' :
        Cost_A321 = (0.76*54*Tbest+15*Tbest+1800)*15
        Cost_A330 = (0.76*84*Tbest+21*Tbest+2000)*10
        Cost_A350 = (0.76*90*Tbest+27*Tbest+2500)*9

        print("The Trip Cost for A321neo is ${}".format(round(Cost_A321)))
        print("The Trip Cost for A330-900neo is ${}".format(round(Cost_A330)))
        print("The Trip Cost for A350-900 is ${}".format(round(Cost_A350)))
        print("A330-900neo has the lowest Trip Cost among them.")

    elif scenario == '2' :
        Cost_A321 = (0.88*54*Tbest+20*Tbest+1800)*7
        Cost_A330 = (0.88*84*Tbest+27*Tbest+2000)*5
        Cost_A350 = (0.88*90*Tbest+34*Tbest+2500)*4

        print("The Trip Cost for A321neo is ${}".format(round(Cost_A321)))
        print("The Trip Cost for A330-900neo is ${}".format(round(Cost_A330)))
        print("The Trip Cost for A350-900 is ${}".format(round(Cost_A350)))
        print("A350-900 has the lowest Trip Cost among them.")

    elif scenario == '3' :
        Cost_A321 = (0.95*54*Tbest+10*Tbest+1800)*13
        Cost_A330 = (0.95*84*Tbest+15*Tbest+2000)*9
        Cost_A350 = (0.95*90*Tbest+20*Tbest+2500)*7

        print("The Trip Cost for A321neo is ${}".format(round(Cost_A321)))
        print("The Trip Cost for A330-900neo is ${}".format(round(Cost_A330)))
        print("The Trip Cost for A350-900 is ${}".format(round(Cost_A350)))
        print("A3500-900 has the lowest Trip Cost among them.")

    elif scenario == '4' :
        Cost_A321 = (0.76*54*Tbest+15*Tbest+1800)*15
        Cost_A330 = (0.76*84*Tbest+21*Tbest+2000)*10
        Cost_A350 = (0.76*90*Tbest+27*Tbest+2500)*9

        print("The Trip Cost for A321neo is ${}".format(round(Cost_A321)))
        print("The Trip Cost for A330-900neo is ${}".format(round(Cost_A330)))
        print("The Trip Cost for A350-900 is ${}".format(round(Cost_A350)))
        print("A330-900neo has the lowest Trip Cost among them.")

    else :
        print("There are no scenario {}, plz enter a correct one. Thank You".format(scenario))

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.show() # show the plot



if __name__ == '__main__':
    scenario = input("Enter 1/2/3/4 for scenario1/scenario2/scenario3/Task_2 respectivelly :")
    main(scenario)

```
