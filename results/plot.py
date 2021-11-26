#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
import seaborn as sns
# %%
# sns.set()
sns.set_style("ticks")
# sns.set_style("white")
# sns.set_style("whitegrid")
sns.set_context("paper", 1.9)

labels = ['Pass agent', 'Rule-based agent']
men_means = [8.874, 13.587]
women_means = [1241.311, 13830.488]

x = np.array([2.0, 6.0]) # np.arange(len(labels))  # the label locations
width = 1.2 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Mjx (ours)')
rects2 = ax.bar(x + width/2, women_means, width, label='Mjai')

# remove frames
right_side = ax. spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_yscale('log')
ax.set_ylabel('log10 (sec)', fontsize=16)
ax.set_yticks([10, 100, 1000, 10000, 10**5])
# ax.set_yticklabels([10, 100, 1000, 10000])
# ax.set_yticklabels()
# ax.set_title('Average time for 100 games')
ax.set_xlim((0.0, 8.0))
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=15)
ax.grid(axis="y", linestyle="dotted")
ax.legend(frameon=False, fontsize=16, ncol=2, loc='upper center', bbox_to_anchor=(0.5, 1.20))

# ax.bar_label(rects1, padding=3, size=13)
# ax.bar_label(rects2, padding=3, size=13)
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    fontsize=13,
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.savefig("speed_benchmark.pdf")
plt.savefig("speed_benchmark.png")
# %%
