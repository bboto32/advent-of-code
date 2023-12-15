import re

# part 1 #
sum_of_calibration_values = 0
with open('2023/input01', 'r') as inp:
    while True:
        line = inp.readline()
        if not line:
            break
        digits = re.findall('\d', line)
        sum_of_calibration_values += int(''.join([digits[0],digits[-1]]))

# part 2 #
sum_of_calibration_values = 0
mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
with open('2023/input01', 'r') as inp:
    while True:
        line = inp.readline()
        if not line:
            break
        digits = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', line)
        d0 = digits[0]
        d1 = digits[-1]
        sum_of_calibration_values += int(''.join([d0 if len(d0)==1 else mapping[d0], d1 if len(d1)==1 else mapping[d1]]))
