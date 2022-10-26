# Task objecttive
 Find an appropriate aircraft model that acheve minimun cost for each scenario for the challenge assigned 

## Our Map
![Task%201/map.png](https://github.com/Ken11514/AAE2004_t1_GP8/blob/Branch-for-MAIN/image/map.png))
## Objective
- Find the **shortest route**
- Determine which aircraft type for each scenario to **achive minimun cost** while **satisfying passenger needs**

### Cost Speciffication
| key | A321neo | A330-900neo | A350-900|
| :---: | :---: | :---: | :---: |
|Fuel Consumption rate(kg/min)|54|84|90|
|Passenger Capacity|200|300|350|
|Time cost (Low)($/min)|10|15|20|
|Time cost (Medium)($/min)|15|21|27|
|Time cost (High)($/min)|20|27|34|
|Fixed Cost($)|1800|2000|2500|

<details open='open'>
  <summary><h2 style='display: inline-block'>Cost Speciffication</h2></summary>
  <ol>
    <li>
      <p align="center">
       <h3 align="center">Cost Speciffication</h3>
        <table align="center">
          <tr>
            <th>key</th>
            <th>A321neo</th>
            <th>A330-900neo</th>
            <th>AA350-900</th>
          </tr>
          <tr>
            <td>Fuel Consumption rate(kg/min)</td>
            <td>54</td>
            <td>84</td>
            <td>90</td>
          </tr>
          <tr>
            <td>Passenger Capacity</td>
            <td>200</td>
            <td>300</td>
            <td>350</td>
          </tr>
          <tr>
            <td>Time cost (low)($/min)</td>
            <td>10</td>
            <td>15</td>
            <td>20</td>
          </tr>
          <tr>
            <td>Time cost (Medium)($/min)</td>
            <td>15</td>
            <td>21</td> 
            <td>27</td>
          </tr>
          <tr>
            <td>Time cost (High)($/min)</td>
            <td>20</td>
            <td>27</td>
            <td>34</td>
          </tr>
          <tr>
            <td>Time cost (High)($/min)</td>
            <td>20</td>
            <td>27</td>
            <td>34</td>
          </tr>
        </table>
      </p>
    </li>
    <li> 
      <p align="center">
        <h3 align="center"> The Cost Function</h3>
        $$
        \C = C_{F}\bullet \delta F \bullet T_{best} \sum C_{T} \bullet \delta T_{best} \sum C_{c}
        $$
      </p>
    </li>
    
  </ol>
</details>
