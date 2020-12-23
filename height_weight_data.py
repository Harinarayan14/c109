import plotly.express as px
import plotly.figure_factory  as pff
import statistics
import pandas as pd
import csv
dataList1 = pd.read_csv("data.csv")
height_list= dataList1["Height(Inches)"].tolist()
weight_list= dataList1["Weight(Pounds)"].tolist()
dis_graph1 = pff.create_distplot([height_list],["Height Distribution Data"],show_hist=False)
dis_graph2 = pff.create_distplot([weight_list],["Weight Distribution Data"],show_hist=False)
dis_graph1.show()
dis_graph2.show()
height_list.pop(0)
mean1 = sum(height_list)/len(height_list)
median1 = statistics.median(height_list)
mode1 = statistics.mode(height_list)
stdev1 =  statistics.stdev(height_list)
range1 = mean1-stdev1
range2 = mean1+stdev1
required_count1=0
for i in height_list:
    if(range1<=float(i)<=range2):
        required_count1+=1
percentage1 = required_count1*100/len(height_list)
print(range1,range2)
print(f"Height :- Mean = {mean1}, Median = {median1}, Mode ={mode1}, Standard Deviation = {stdev1}, Percentage = {percentage1}")

weight_list.pop(0)
mean2 = sum(weight_list)/len(weight_list)
median2 = statistics.median(weight_list)
mode2 = statistics.mode(weight_list)
stdev2 =  statistics.stdev(weight_list)
range3 = mean2-stdev2
range4 = mean2+stdev2
required_count2=0
for i in weight_list:
    if(range3<=float(i)<=range4):
        required_count2+=1
percentage2 = required_count2*100/len(weight_list)
print(range3,range4)
print(f"Weight :- Mean = {mean2}, Median = {median2}, Mode ={mode2}, Standard Deviation = {stdev2}, Percentage = {percentage2}")
weight_list_within_sd=[result for result in weight_list if result>range3 and result<range4]
number1 = len(weight_list_within_sd)
percentage2 = number1*100/len(weight_list)
print(percentage2)