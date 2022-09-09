import datetime
import sys
from datetime import date
from os.path import exists


def earlymorning(wakeuptime):
    # getting current index
    file_exists = exists("log.csv")

    if file_exists:  # when file already exists
        with open("log.csv") as file:
            for line in file:
                pass
            last_line = line
        current_index = str(int(last_line.split(",")[0]) + 1)
        file.close()
    else:  # create new file if file does not exists
        f = open("log.csv", "a")
        f.write("index,date,time")
        current_index = "1"
        f.close()

    # getting today's date
    d = date.today().strftime("%b-%d-%Y")

    # getting the time parameter
    hr_input = int(wakeuptime.split(":")[0])
    minute_input = int(wakeuptime.split(":")[1])
    time = datetime.time(hr_input, minute_input)
    hr = time.strftime("%I")
    minute = time.strftime("%M")
    final_time = hr + ":" + minute
    print(final_time)

    # writing into file
    f = open("log.csv", "a")
    towrite = '\n' + current_index + ',' + d + ',' + final_time
    f.write(towrite)
    f.close()

    # greetings
    print(f"Entry #{current_index}: Today is {d}, and you woke up at {final_time}.")


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])

