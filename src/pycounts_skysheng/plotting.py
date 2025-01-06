import matplotlib.pyplot as plt

""" old code
def plot_words(word_counts, n=10):
    
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig
"""


def plot_words(word_counts, n=10):
    """Plot a bar chart of word counts."""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)

    # Create a new figure and axes
    fig, ax = plt.subplots()
    ax.bar(range(n), count)
    ax.set_xticks(range(n))
    ax.set_xticklabels(word, rotation=45)
    ax.set_xlabel("Word")
    ax.set_ylabel("Count")

    return fig
