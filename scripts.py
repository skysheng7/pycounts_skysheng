from pycounts_skysheng.pycounts_skysheng import count_words
from pycounts_skysheng.plotting import plot_words
import matplotlib.pyplot as plt
counts = count_words("zen.txt")
fig = plot_words(counts, 10)
# Save the figure as a PNG file
output_path = "word_counts.png"
fig.savefig(output_path, bbox_inches="tight")