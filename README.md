# wake-up-time-checker

A terminal command which can be run from anywhere on system and creates a .csv to record the wake-up times in the mornings.

Place the python file anywhere you want and run it the with following command. 

```python
python PATH_TO_FILE earlymoring TIME
```

TIME argument must be entered in 24 hr format.

```python
python /User/shubhdeepsarkar/Developer/habit_checker/main.py earlymorning 7:30
```
```
> Entry #1: Today is Sep-09-2022, and you woke up at 7:30.
```

It is recommended to create an alias of this command for ease of use.

NOTE: There is no need to create a file log.csv file manually. 
