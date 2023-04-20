import matplotlib.pyplot as plt
import numpy as np

from constants import LANGUAGES, FEATURES

# Read in .txt file
with open("lang_features_test_rounded.txt", "r") as f:
    data = eval(f.read())

# Group the data by language and feature type
grouped_data = {}
for key, value in data.items():
    language_codes = key[0].split('_')[:-2]
    languages = '\n'.join([LANGUAGES[code].capitalize() for code in language_codes])
    if not isinstance(languages, list):
        languages = [languages]
    feature_type = key[1]
    for language in languages:
        if language not in grouped_data:
            grouped_data[language] = {feature_type: value}
        else:
            grouped_data[language][feature_type] = value

# Plot the grouped bar chart
x_labels = list(grouped_data.keys())
mfcc_values = [grouped_data[lang].get('mfcc', 0) for lang in x_labels]
fbe_values = [grouped_data[lang].get('fbe', 0) for lang in x_labels]
hil_values = [grouped_data[lang].get('hil', 0) for lang in x_labels]

x = np.arange(len(x_labels))
width = 0.2
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(x, mfcc_values, width, label=FEATURES['mfcc'], color='tab:blue', edgecolor='black')
ax.bar(x + width, fbe_values, width, label=FEATURES['fbe'], color='tab:orange', edgecolor='black')
ax.bar(x + 2*width, hil_values, width, label=FEATURES['hil'], color='tab:green', edgecolor='black')

ax.set_xticks(x + width)
ax.set_xticklabels(x_labels, fontsize=10)
ax.set_ylabel('Accuracy', fontsize=14)
ax.set_ylim([0, 1])

ax.legend(fontsize=14)
ax.set_yticks(np.arange(0, 1.1, 0.1))

# move the plot up a bit

ax.set_xlabel('Native Languages in Dataset', fontsize=14, labelpad=20,fontweight='bold')
ax.xaxis.set_label_coords(0.5, -0.2)
# move the rest of the plot up
ax.set_position([0.1, 0.2, 0.8, 0.7])

# Add title and caption
plt.title('Accent Classification Accuracy of Model by Dataset and Feature Type', fontsize=16, fontweight='bold', pad=20)

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# add padding to outside
plt.subplots_adjust(bottom=0.2)

plt.show()
