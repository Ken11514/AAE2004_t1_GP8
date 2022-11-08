# Task Objective
Design a new aircraft by finding out its parameters based on the restrictions

## Our Map
![map](https://github.com/Ken11514/AAE2004_t1_GP8/blob/main/images/map.png)

## Things To Do 
• Design a new aircraft to best fit Scenario 1 in task 1

• Only consider cruise time of the flight

• Also design the passenger capacity of the aircraft,
for each 50 passenger (min 100 to max 450) increase
time cost by 2 $/min (Base C_{T} = 12 $/min)

• The base design is a twin-engine aircraft, if capacity >= 300, you must switch to a 4-engine aircraft

•  $C_{C}$ = 2000 for twin-engine aircrafts, 2500 for 4-
engine aircrafts

• Each engine consumes fuel at 20kg/min

• Follow the trip cost equation and materials design your aircraft:

![Second Week - Project tasks (updated) (2)](https://user-images.githubusercontent.com/115149687/199167780-406fd27b-c9f5-4db3-a158-67522affaef7.jpg)
$C_{F}$ = cost of fuel per kg

$C_{T}$ = time related cost per minute of flight

$C_{C}$ = fixed cost independent of time

$\Delta F$ = trip fuel

$T_{best}$ = trip time

## AIRCRAFT MODEL DESIGN (task3)
###  Introduction
To find out the best fit the situation.  We designed three models with diffenert Capacity (capacity per aircraft): 

Model 1: 250  

Model 2: 300 

Model 3: 450

### Table of value

According to the Rules of restrictions of TASK 3, 

the Value to find out the best fit model aircraft could be shown as this able:

| Airplane Capacity& Model |    $\Delta F$  |$T_{best}$ |  $C_{C}$ |  $C_{T}$   |  $C_{F}$ | Number of trip required  |   Total cost  |
| :--------         | :------- | :------- |:---------  | :--------- |:--------   | :--------| :--------|
| (Model 1) 250 | 40kg/min        | 77.1837664107356 /min  | 2000  $/flight   |  22  $/min        | 0.8823  $/kg         | 12   | $77064 |
| (Model 2) 300|  80kg/min        | 77.1837664107356    min| 2500   $/flight       |  24  $/min        | 0.8823 $/kg          | 10   | $98003 |                
| (Model 3) 450|  80kg/min        | 77.1837664107356   min  | 2500  $/flight    |  30  $/min        | 0.8823  $/kg | 7    | $71844 |              

### Trip cost calculations for each model

Model 1 (250) :77.183766410736*0.8823*40 + 2000*77.1837664107356 + 2000 = 77064

Model 2 (300) :77.183766410736*0.8823*80 + 2500*77.1837664107356 + 2500 = 98033

Model 3 (450) :77.183766410736*0.8823*80 + 2500*77.1837664107356 + 2500 = 71844


