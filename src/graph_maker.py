"""
Makes them good looking charts.
"""

import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Main method (for testing)
    """

    average_polarity = pd.read_csv('../dump/RC_2016-11-polarity.csv')

    average_subjectivity = pd.read_csv('../dump/RC_2016-11-subjectivity.csv')

    average_compound = pd.read_csv('../dump/RC_2016-11-compound.csv')

    polarity_plot = average_polarity.plot(
        kind='bar',
        x='subreddit',
        y='average',
        legend=False)

    polarity_plot.set_title('Average Polarity per Subreddit', fontsize=30)

    polarity_plot.set_xlabel('subreddit', fontsize=28)

    polarity_plot.set_ylabel('average polarity', fontsize=28)

    polarity_plot.legend(['subreddit'])

    polarity_plot.set_xticklabels(polarity_plot.get_xticklabels(), rotation=0)

    polarity_plot.get_legend().remove()

    plt.xticks(size=24)

    plt.yticks(size=24)

    subjectivity_plot = average_subjectivity.plot(
        kind='bar',
        x='subreddit',
        y='average',
        legend=False)

    subjectivity_plot.set_title(
        'Average Subjectivity per Subreddit', fontsize=30)

    subjectivity_plot.set_xlabel('subreddit', fontsize=28)

    subjectivity_plot.set_ylabel('average subjectivity', fontsize=28)

    subjectivity_plot.legend(['subreddit'])

    subjectivity_plot.set_xticklabels(
        subjectivity_plot.get_xticklabels(), rotation=0)

    subjectivity_plot.get_legend().remove()

    plt.xticks(size=24)

    plt.yticks(size=24)

    compound_plot = average_compound.plot(
        kind='bar',
        x='subreddit',
        y='average',
        legend=False)

    compound_plot.set_title('Average Compound per Subreddit', fontsize=30)

    compound_plot.set_xlabel('subreddit', fontsize=28)

    compound_plot.set_ylabel('average compound', fontsize=28)

    compound_plot.legend(['subreddit'])

    compound_plot.set_xticklabels(compound_plot.get_xticklabels(), rotation=0)

    compound_plot.get_legend().remove()

    plt.xticks(size=24)

    plt.yticks(size=24)

    plt.show()


if __name__ == '__main__':
    main()
