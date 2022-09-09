# wake-up-time-checker

A terminal command which can be run from anywhere on system and creates a .csv to record the wake-up times in the mornings.

NOTE: There is no need to create a file log.csv file manually. 

Place the python file anywhere you want and run ti with following command. 

```python
python PATH_TO_FILE earlymoring TIME
```

TIME argument must be entered in 24 hr format.

```python
python /User/shubhdeepsarkar/Developer/habit_checker/main.py earlymoring 7:30
> Entry #1: Today is Sep-09-2022, and you woke up at 10:30.
```

It is recommended to create an alias of this command for ease of use.
