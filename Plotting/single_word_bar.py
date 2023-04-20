import matplotlib.pyplot as plt

# Read the data from the file
with open('/Users/dylanwalsh/Code/AccentRecognition_Dylan/results/single_word_fbe_19_Apr.txt', 'r') as f:
    data = eval(f.read())

# Extract the words and accuracies from the data
words = list(data.keys())
accuracies = list(data.values())

# Create a bar chart
fig, ax = plt.subplots()
rects = ax.bar(words, accuracies)

# Set the y-axis limit to be between 0 and 1
plt.ylim(0, 1)

# Set the title and labels
plt.title('Accuracy by Single Word')
plt.xlabel('Word')
plt.ylabel('Accuracy')

# Add accuracy values to the tops of the bars
for i, rect in enumerate(rects):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height, str(round(accuracies[i], 2)), ha='center', va='bottom')

# Display the plot
plt.show()
