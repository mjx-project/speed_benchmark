#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
import seaborn as sns
# %%
sns.set_style("white")

labels = ['Pass agent', 'Rule-based agent']
men_means = [8.874, 13.587]
women_means = [1241.311, 13830.488]

x = np.array([0, 0.4]) # np.arange(len(labels))  # the label locations
width = 0.15 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Mjx')
rects2 = ax.bar(x + width/2, women_means, width, label='Mjai')

# remove frames
right_side = ax. spines["right"]
right_side. set_visible(False)
right_side = ax. spines["top"]
right_side. set_visible(False)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_yscale('log')
ax.set_ylim((0, 5 * 10**4))
ax.set_ylabel('log10(sec)')
# ax.set_title('Average time for 100 games')
ax.set_xlim((-0.25, 0.65))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.grid(axis="y", linestyle="dotted")
ax.legend(frameon=False, loc=2)

ax.bar_label(rects1, padding=3, size=13)
ax.bar_label(rects2, padding=3, size=13)

fig.tight_layout()

plt.savefig("speed_benchmark.pdf")

# %%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

# %%
sns.set()
import matplotlib.pyplot as plt
import seaborn as sns

titanic_dataset = sns.load_dataset("titanic")

sns.barplot(x = "class", y = "age", hue = "embark_town", data = titanic_dataset)
plt.show()
# %%
titanic_dataset
# %%
