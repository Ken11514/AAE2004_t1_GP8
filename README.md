# AAE2004_t1_GP8 Look gooood

<p align='center'>
<image src=images/Group_8_Banner.gif alt="Group 8 Banner">
</p>


<!-- TABLE OF CONTenT-->
<details open='open'>
  <summary><h2 style='display: inline-block'>Table of Content</h2></summary>
  <ol>
    <li>
      <a href='#1--background-of-path-planing-to-aviation-engineering'>Background of Path Planning to Aviation Engeering</a>
    </li>
    <li><a href='#2--theory-of-path-planning-algorithm'>Theory of Path Planning Algorithm</a>
    </li>
    <li><a href='#3--introduction-of-the-engineering-tools'>Introduction of the Engeering Tools</a>
    </li>
    <li>
      <a href='#4--task-1'>Task 1</a>
    </li>
    <li>
      <a href='#5--task-2'>Task 2</a>
    </li>
    <li>
      <a href='#6--task-3'>Task 3</a>
    </li>
    <li><a href='#7--additional-task-1'>Additional Task 1</a>
    </li>
    <li><a href='#8--additional-task-2'>Additional Task 2</a>
    </li>
    <li><a href='#9--additional-task-3'>Additional Task 3</a>
    </li>
    <li><a href='#10--reflective-essay'>Reflective Essay</a>
    </li>
    <li><a href='#11--references'>References</a></li>
    <li>
      <a href='#reference-source'>Reference source</a>
    </li>
    <li>
      <a href='#progess'>Task on progess</a>
    </li>
  </ol>
</details>

<!-- REPORT CONTACT-->


# **1 | Background of Path Planing to Aviation Engineering**


<p align='center'>
  In Aviation Industry, Path Planning has a importance place in Air Traffic Control, Airline Companies and Airports. ...

  <br>For Air Traffic Control,by calculating obstical and danger zone, Path Planning help operater adjust the flight route of aircrafts, in order to provide a safety flying experience. ...
  
  <br>For Airline Companies, by calculating the shortest route for airlines, Path Planning help companies reduce filght cost, in order to enhance their profit. ...

  <br>For Airports, by planning the take off and landing timing, Path Planning help Airports maximize the aircraft flow, in order to increase passenger flow. ...

  <br>
</p>

# **2 | Theory of Path Planning Algorithm**
- [ ] show how its work

Converting a maze problem into a grid, A-Star algorithm will assign a weight value which repersent the traveling cost on each coordinates. By calculating the lowest traveling cost between start point and end point, a shortest path can be collected.
<br>
Example for a maze problem is fitted into a grid format.

<table align='center'>
  <tr>
    <th>Maze Problem</th>
    <th>Grid Gormat</th>
  </tr>
  <tr>
    <td>
    <image src='images/Raw_sample.png'>
    </td>
    <td>
      <image src='images/Sample.png'>
    </td>
  </tr>
</table>
In grid format, all possabale path position are recognized as node, and can be assigned a weight to show the traveling cost, which show as follows.
<br>

Assume all traveling cost adjacently and diagonally are 1 and $\sqrt{2}$ respectively.
<br>
Step 1, calculate the traveling cost form start point to its adjacent and diagonal notes. Then base on each node, calculate heuristic estimated cost, the displacement, between itself and end point. After combine the traveling cost and heuristic estimated cost, a weight of the node can be obtainted.<br>
Step 2, select the lowest weight node as the position of the **first** step apporaching to the End Point. Then append them to a list which recorded evey step it moved to.<br>
Step 3, repeat Step 1 and Step 2 untill it reaches the End point, A list of the movement can be obtained.<br>
Step 4, Track back from the list of movement, a route of shortest path can be viewed.
<table align='center'>
  <tr>
    <th>Example</th>
  </tr>
  <tr>
    <td></td>
  </tr>
</table>




```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


# **3 | Introduction of the Engineering Tools**
## a. Python

## b. GitHub
<!-- TASK 1 -->
# **4 | Task 1**
## a. Methodology

<p align='center'>
explain how to achive and what skills we used
</p>

## b. Results

<p align='center'>
show our result and explain what does the result repersent
</p>

## c. Descussion

<p align='center'>
Talk about how the task related to aviation
</p>


<!-- Task 2 -->
# **5 | Task 2**
## a. Methodology

<p align='center'>
explain how to achive and what skills we used
</p>

## b. Results

<p align='center'>
show our result and explain what does the result repersent
</p>

## c. Descussion

<p align='center'>
Talk about how the task related to aviation
</p>

## Introduction
- [x] : How the task related to daily aviation

        The area designed in task 2 represents jet-stream area where aircrafts could consume relatively less fuel
        -> reduce the cost of flights
        
- [x] : Task objective

        Recreate a jet-steam area in the map that could most benefit our flight route. 
        
## Content
- [x] : Thhings to do

        Design a new cost area -> reduce the cost of the route of scenario 1 in task 1
         
- [x] : How and what we have done (explain with result)

        1 Base on the scenario 1 in Task 1
        2 Create a reduce-cost area in the map (size: vertical lengths:5 , horizontal length:infinity [cyan in colour])
        3 Finding the lowest Trip Cost in pothntial.


## Conclusion
- [ ] : result (1 line to cover it)
- [ ] : How to improve
<!-- Task 3 -->

# **6 | Task 3**
## a. Methodology

<p align='center'>
explain how to achive and what skills we used
</p>

## b. Results

<p align='center'>
show our result and explain what does the result repersent
</p>

## c. Descussion

<p align='center'>
Talk about how the task related to aviation
</p>

## Introduction
- [ ] : How the task related to daily aviation
- [ ] : Task objective
## Content
- [ ] : Thhings to do
- [ ] : How and What we have done (explain with result)

## Conclusion
- [ ] : result (1 line to cover it)
- [ ] : How to improve
<!-- updates -->

# **7 | Additional Task 1**
## a. Methodology

<p align='center'>
explain how to achive and what skills we used
</p>

## b. Results

<p align='center'>
show our result and explain what does the result repersent
</p>

## c. Descussion

<p align='center'>
Talk about how the task related to aviation
</p>

# **8 | Additional Task 2**
## a. Methodology

<p align='center'>
explain how to achive and what skills we used
</p>

## b. Results

<p align='center'>
show our result and explain what does the result repersent
</p>

## c. Descussion

<p align='center'>
Talk about how the task related to aviation
</p>

# **9 | Additional task 3**
## a. Methodology

<p align='center'>
explain how to achive and what skills we used
</p>

## b. Results

<p align='center'>
show our result and explain what does the result repersent
</p>

## c. Descussion

<p align='center'>
Talk about how the task related to aviation
</p>


# **10 | Reflective Essay**
## Shek Ho Ching Ken (22075211D)
```
  This project is my first GitHub project in my life ,also ......
```
## Put your Name here (student ID)
```
  Type your essay Here!!!
```

# **11 | References**
-  hi




<!-- TASK -->

## Progess  
### Week 8
- [x] familiarize with GitHub and VScode
### Week 9
- [x] finish task 1 by week 11
### Week 10
- [ ] report for Task_1 & Task_2
- [ ] [PowerPoint slide](https://connectpolyu-my.sharepoint.com/:p:/g/personal/22075211d_connect_polyu_hk/Ecv7NPHGFGtBt5Jk1Ql2RFoBYP0CGmmuKWjzxvsIqG_WnA?e=OU8kzx) for video
### week 11
- [ ] [MSWord]("https://connectpolyu-my.sharepoint.com/:w:/g/personal/22075211d_connect_polyu_hk/ESFi3BeMMBBJv2-l2V8ch4wBDD6baR5c8cD08VUSOuKRZA?e=avXK26") report 
- [ ] GitHub report
<!-- REFERCE -->
------
## Reference source

### YouTube video:
[How To Create Beautiful and Useful ReadMe Documents For GitHub](https://youtu.be/a8CwpGARAsQ)

### Web Site
[AAE GitHub Page](https://github.com/IPNL-POLYU/PolyU_AAE2004_Github_Project)

[basic syntax](https://www.markdownguide.org/basic-syntax)

