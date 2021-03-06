# Accessibility Heatmap

Showing the accessibility heatmap and candidate list.

## Author

- [Hu Chenglong @sonnyhcl](github.com/sonnyhcl)
- [Chen Xi @iamcxnoguigan](github.com/iamcxnoguigan)
- [Mao Chengtian @luvletter](github.com/luvletter)

## Deploy
```console
me@me:~$ git clone https://github.com/AdvancedServicesEngineeringFudan2018/Too-Hard-To-Find-A-Name
me@me:~$ cd Too-Hard-To-Find-A-Name
me@me:~/Too-Hard-To-Find-A-Name$ sudo -H pip install -r requirements.txt
me@me:~/Too-Hard-To-Find-A-Name$ PYTHONPATH=`pwd`/webapp python run.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 210-897-547
```
## Component

- **View** Mapbox
- **Model** Gaode API/Swarm
- **Controller** Tornado


## Diagram

![dataflow](image/ASEDataflowFramework.png)

## More
-   Scenario [Scenario.md](doc/Scenario.md)
-   Quality Of Data [QoD.md](doc/QoD.md)
-   TaskAssignment [TaskAssignment.md](doc/TaskAssignment.md)
-   FinalReport [FinalReport.pdf](doc/FinalReport.pdf)
