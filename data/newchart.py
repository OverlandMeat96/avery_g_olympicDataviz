import matplotlib.pyplot as plt

hours = [4, 0]
activities = ['Sleep', 'Work']
colors = ['r', 'g']

plt.pie(hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()

