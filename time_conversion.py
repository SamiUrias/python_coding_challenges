# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
# Complete the timeConversion function below.
# Sample Input: 07:05:45PM
# Sample Output: 19:05:45
def timeConversion(s):
    #
    # Write your code here.
    #
    new_hour = 0
    new_hour = int(s[:2])
    if s[-2:] == 'PM':
        if int(s[:2]) < 12:
            new_hour = str( int(s[:2]) + 12)

    new_hour = str(new_hour) + s[2:-2]
    return new_hour

if __name__ == '__main__':
    s = '01:05:45PM'

    result = timeConversion(s)

    print(result)