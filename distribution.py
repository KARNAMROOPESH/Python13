import pandas as pd 
import plotly.figure_factory as pf 
import statistics

data = pd.read_csv('./height-weight.csv')

heigth = data['Height(Inches)'].tolist()
mean = statistics.mean(heigth)
median = statistics.median(heigth)
mode = statistics.mode(heigth)
stan = statistics.stdev(heigth)

# caluculating percentage of data in the first mean range
heigth1 = []
lowermean1 = mean-stan
uppermean1 = mean+stan
for i in heigth:
    if(i > lowermean1 and i < uppermean1):
        heigth1.append(i)
percentage = (len(heigth1)/len(heigth))*100 
print(percentage)

# caluculating percentage of data in the second mean range
heigth2 = []
lowermean2 = mean-(2*stan)
uppermean2 = mean+(2*stan)
for i in heigth:
    if(i > lowermean2 and i < uppermean2):
        heigth2.append(i)
percentage2 = (len(heigth2)/len(heigth))*100 
print(percentage2)

# caluculating percentage of data in the third mean range
heigth3 = []
lowermean3 = mean-(3*stan)
uppermean3 = mean+(3*stan)
for i in heigth:
    if(i > lowermean3 and i < uppermean3):
        heigth3.append(i)
percentage3 = (len(heigth3)/len(heigth))*100 
print(percentage3)


fig = pf.create_distplot([heigth] , ["Heigth"] , show_hist=False)
fig.show()


w = data['Weight(Pounds)'].tolist()
meanw = statistics.mean(w)
medianw = statistics.median(w)
modew = statistics.mode(w)
stanw = statistics.stdev(w)

# caluculating percentage of data in the first mean range
w1 = []
lowermean1w = meanw-stanw
uppermean1w = meanw+stanw
for i in w:
    if(i > lowermean1w and i < uppermean1w):
        w1.append(i)
percentagew = (len(w1)/len(w))*100 
print(percentagew)

# caluculating percentage of data in the second mean range
w2 = []
lowermean2w = meanw-(2*stanw)
uppermean2w = meanw+(2*stanw)
for i in w:
    if(i > lowermean2w and i < uppermean2w):
        w2.append(i)
percentage2w = (len(w2)/len(w))*100 
print(percentage2w)

# caluculating percentage of data in the third mean range
w3 = []
lowermean3w = meanw-(3*stanw)
uppermean3w = meanw+(3*stanw)
for i in w:
    if(i > lowermean3w and i < uppermean3w):
        w3.append(i)
percentage3w = (len(w3)/len(w))*100 
print(percentage3w)


