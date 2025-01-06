from pycounts_skysheng.pycounts_skysheng import count_words
from pycounts_skysheng.plotting import plot_words
import matplotlib.pyplot as plt
counts = count_words("zen.txt")
fig = plot_words(counts, 10)
plt.show()