#qn1
def _2darray():

    array =[[1, 2],[4, 5], [7, 8]]

    return array[1][1]


print(_2darray())





#qn2
arr =[12,1,2,3,4,55,78,9,8]
print("The array: " +str(arr))
print("the array sorted in ascending order:" +str(sorted(arr)))

#qn9
import sys

if len(sys.argv) == 2:
   my_list =sys.argv[1].split(',')
   print ((my_list))
   print(tuple(my_list))
else:("pass a comma separated list of numbers as a commandline argument")


#7
rows = int(input('enter the number of rows'))
for i in range (rows):
    for j in range(i):
        print ('*', end ='')
    print('')

#qn6
def check_speed_of_drivers(speed):

    if speed < 70:
        print('ok')

    demerit_points = 0
    speed_tmp = 70
    if speed > 70:
        while speed_tmp <= speed:
            demerit_points = demerit_points + 1
            speed_tmp = speed_tmp + 5
        demerit_points = demerit_points - 1
        print(f"points: {demerit_points}")
        if demerit_points > 200:
            print("license suspended")

check_speed_of_drivers(85)

#qn5

def get_email_file(txt_file):
    the_email = None
    f = open(txt_file, "r")
    for line in f.readlines():
        if '@' in line:
            the_email = line.strip()
    return the_email

print(get_email_file("txt_file.txt"))   

#qn4
from audioop import add
import math
sub = int(input("enter the number of subjects you sat for: "))
marks = list(map(int, input("enter marks got for all the five subjects: ") .split()))
total = sum(marks)
print ("the total marks got is:" + str(total))
percentage =(total/500) *100
print ("the percentage total mark got is:" +str(percentage)+ "%")
if percentage < 50:
    print("your grade is 'c' ")
elif percentage == 50 or percentage < 80:
    print("your grade is 'B'")
elif percentage == 80 or percentage > 80:
    print ("your grade is 'A' ")
else:
    print("failed")

