## Introduction
Although most of the fights do not always follow the same route, it is important for airlines to find the shortest route to reach their destination as it not only saves time but also saves money by decreasing fuel consumption. Additionally, the most efficient aircraft model is selected based on the route that helps minimize the flight cost. In this task, we are going to find the best aircraft models with minimum cost for the shortest route found for the given challenge keeping the needs of passsengers in mind. 

## Our Map
![Task%201/map.png](https://github.com/Ken11514/AAE2004_t1_GP8/blob/main/images/map.png)

## Cost Speciffication
| key | A321neo | A330-900neo | A350-900|
| :---: | :---: | :---: | :---: |
|Fuel Consumption rate(kg/min)|54|84|90|
|Passenger Capacity|200|300|350|![Screenshot T1 2](https://user-images.githubusercontent.com/116112237/200491442-e117a05f-a5b2-470b-a705-dfc6e9e5bf76.png)

|Time cost (Low)($/min)|10|15|20|
|Time cost (Medium)($/min)|15|21|27|
|Time cost (High)($/min)|20|27|34|
|Fixed Cost($)|1800|2000|2500|

$Cost=C_{Fuel} \cdot \Delta F \cdot T_{best} +C_{Time}\cdot T_{best}+C_{Fixed}$

## Breakdown of codes
![ScreenshotT1 1](https://user-images.githubusercontent.com/116112237/200486556-fa67a1bf-db18-45af-89ea-85db1bedc027.png)

It is the definition of **“main()”**. It require user to input a variable during the usage, in later part the input was use as a indicator to direct and run the corresponding code for different task and scenario.
Both the starting point and the goal point are set as variables.

sx: starting point x-coordinate

sy: starting point y-coordinate

gx: goal point x-coordinate

gy: goal point y-coordinate

Tbest: time-best

“AStarPlanner” is a set of function which contains 3 parts (1.variable defining)(2.”Node”defining )(3.”planning( )”function)


### Scenario 
1. 3000 Passengers  with in this week
2. 12 flights maximum per week
3. Time cost = medium and Fuel cost = 0.76$/kg

According to the results of coding,

### Scenario 2 
1. 125 Passengers  with in this month
2. 5 flights maximum per week
3. Time cost = high and Fuel cost = 0.88$/kg

### Scenario 3
1. 2500 Passengers  with in this week
2. 25 flights maximum per week
3. Time cost = low and Fuel cost = 0.95$/kg
