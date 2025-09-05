import matplotlib.pyplot as plt
import seaborn as sns

data = [[0,0],[1,1],[2,2],[3,3],[-1,-1],[-2,-2],[-3,-3]]
 #splitting into x and y axis
x=[point[0] for point in data]
y=[point[1] for point in data]

#plotting the graph
sns.scatterplot(x=x,y=x,color='blue')
# Plot line connecting the points
sns.lineplot(x=x, y=y, color='red')
#Show plot

# Move spines to zero
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xlabel("X-Axis")
plt.ylabel("Y-axis")
plt.show()