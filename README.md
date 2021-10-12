# Vehicle History MapReduce Hadoop Project

## Overview
Utilize data from an automobile tracking platform that tracks the history of important incidents after the initial sale of a new vehicle. Such incidents include subsequent private sales, repairs, and accident reports. The platform provides a good reference for second-hand buyers to understand the vehicles they are interested in.

## Input
A .csv dataset with a history report of various vehicles.

## Output
A MapReduce program to produce a report of the total number of accidents per make and
year of the car.

## Shell scripts for execution
### Bash
```
cat data.csv | python src/autoinc_mapper1.py | sort | python src/autoinc_reducer1.py | python src/autoinc_mapper2.py | sort | python src/autoinc_reducer2.py
```