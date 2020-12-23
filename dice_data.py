import random
import plotly.express as px
import plotly.figure_factory  as pff
import statistics
randomList=[]
countList=[]
for i in range(0,1000):
    random1 = random.randint(1,6)
    random2 = random.randint(1,6)
    random3 = random1+random2
    randomList.append(random3)
    countList.append(i)
print(randomList)
mean1 = sum(randomList)/len(randomList)
median1 = statistics.median(randomList)
mode1 = statistics.mode(randomList)
squared_list=[]
for number in randomList:
    a = int(number) - mean1
    a= a**2
    squared_list.append(a)

sum =0
for i in squared_list:
    sum =sum + i

result = sum/ (len(randomList)-1)

std_deviation = statistics.sqrt(result)
range1 = mean1-std_deviation
range2 = mean1+std_deviation
required_count=0
for i in randomList:
    if(range1<=float(i)<=range2):
        required_count+=1
percentage1 = required_count/10
print(range1,range2)
print(f"Mean = {mean1}, Median = {median1}, Mode ={mode1}, Standard Deviation = {std_deviation}, Percentage = {percentage1}")
dis_plot1 = pff.create_distplot([randomList],["Dice Data Distribution"])
dis_plot1.show()