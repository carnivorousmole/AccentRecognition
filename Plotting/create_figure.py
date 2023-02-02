import matplotlib.pyplot as plt
import numpy as np

# Lists for the data
accuracies = [0.6815729141235352, 0.7396759390830994, 0.7888386249542236, 0.7723773121833801, 0.6904385089874268,0.816530168056488]


languages = ["Spanish", "Russian", "Mandarin", "Korean", "French", "Arabic"]
colours = ['c','r','m','b','g','y']
# Create the bar chart

accuracies, languages,colours = zip(*sorted(zip(accuracies, languages,colours)))





fig, ax = plt.subplots()
bars = ax.bar(languages, accuracies, color = colours)

ax.bar_label(bars, fmt = "%.2f")
# Add axis labels
plt.xlabel('L1 Language')
plt.ylabel('Accuracy')
plt.title('Binary Classification Accuracy (for Accent Paired with Native English)')


# Show the chart
# plt.show()
plt.savefig('./Plotting/languages_comp.png')




# Number Of sample in each language

# Lists for the data
numbers = [200,         651,        85,         97    ,   156   ,      81        ,     235]
languages = ["Arabic", "English", "French", "Korean", "Mandarin" ,"Russian",  "Spanish"]
# colours = ['c','r','m','b','g','y']
# Create the bar chart

# accuracies, languages,colours = zip(*sorted(zip(accuracies, languages,colours)))





fig, ax = plt.subplots()
bars = ax.bar(languages, numbers)

ax.bar_label(bars, fmt = "%d")
# Add axis labels
plt.xlabel('Speaker\'s L1 Language')
plt.ylabel('Number Of Samples')
plt.title('Accent Sample Distribution')


# Show the chart
# plt.show()
plt.savefig('./Plotting/samples_comp.png')

# accuracies comparison


# Example data for two sets of accuracy results
languages =         ["Arabic"  ,  "French",    "Korean",  "Mandarin" ,   "Russian",     "Spanish"]
accuracies_set1 =   [0.816,       0.69,        0.772,     0.788,         0.739,         0.681]
hilbert_set2 =      [0.804,       0.701,       0.736,     0.811,         0.76,          0.763]
hilbert_only_set3 = [0.748,       0.701,       0.696,     0.715,         0.714,          0.702]



languages = ["Spanish", "Russian", "Mandarin", "Korean", "French", "Arabic"]
# Create a bar chart
x = np.arange(len(languages))  # the label locations
width = 0.25  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width, accuracies_set1, width, label='Linear Mel-Spectrogram')
rects2 = ax.bar(x, hilbert_set2, width, label='Linear Mel-Spectrogram + Hilbert Spectrogram')
rects3 = ax.bar(x + width, hilbert_only_set3, width, label='Hilbert Spectrogram')

# Add labels and title
ax.set_ylabel('Accuracy')
ax.set_ylim(top = 1.2)
ax.set_xticks(x)
ax.set_xticklabels(languages)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 3, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', size=6)
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.savefig('./Plotting/hilbert_comp.png')
