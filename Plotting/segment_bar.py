import matplotlib.pyplot as plt

# Read the data from the fixed trim file
with open('/Users/dylanwalsh/Code/AccentRecognition_Dylan/results/fixed_trim_19_Apr.txt', 'r') as f:
    fixed_trim_data = eval(f.read())

# Read the data from the word trim file
with open('/Users/dylanwalsh/Code/AccentRecognition_Dylan/results/multi_word_fbe_number_19_Apr.txt', 'r') as f:
    word_trim_data = eval(f.read())

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.set_box_aspect(5/3)

# Set the title of the first subplot and create a bar chart
ax1.set_title('Time Segmented')
ax1.bar(fixed_trim_data.keys(), fixed_trim_data.values(), color='orange', width=0.7)
ax1.set_xlabel('Seconds')
ax1.set_ylabel('Accuracy')
ax1.set_ylim([0, 1])

# Display the value of each bar on the first subplot
for i, v in enumerate(fixed_trim_data.values()):
    ax1.text(i-0.1, v+0.05, "{:.2f}".format(v), color='black')

# Set the title of the second subplot and create a bar chart
ax2.set_title('Word Segmented')
ax2.bar(word_trim_data.keys(), word_trim_data.values(), color='green', width=0.7)
ax2.set_xlabel('Number of Words')
ax2.set_ylim([0, 1])
# hide y-axis
ax2.get_yaxis().set_visible(False)

# Display the value of each bar on the second subplot
for i, v in enumerate(word_trim_data.values()):
    ax2.text(i + 1 - 0.125, v + 0.01, str(v)[:4], color='black')

# Set the overall title for the figure and adjust the layout
fig.suptitle('Segmented Data Model Accuracy Comparison', fontsize=14, fontweight='bold')
fig.text(0.5, 0.01, 'Segment Length', ha='center', fontsize=12)
fig.tight_layout()

# Show the plot
plt.show()
