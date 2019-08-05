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
        kind='bar', title='Average Polarity per Subreddit', x='subreddit', y='average')

    polarity_plot.set_xlabel('subreddit')

    polarity_plot.set_ylabel('average polarity')

    polarity_plot.legend(['subreddit'])

    subjectivity_plot = average_subjectivity.plot(
        kind='bar', title='Average Subjectivity per Subreddit', x='subreddit', y='average')

    subjectivity_plot.set_xlabel('subreddit')

    subjectivity_plot.set_ylabel('average subjectivity')

    subjectivity_plot.legend(['subreddit'])

    compound_plot = average_compound.plot(
        kind='bar', title='Average Compound per Subreddit', x='subreddit', y='average')

    compound_plot.set_xlabel('subreddit')

    compound_plot.set_ylabel('average compound')

    compound_plot.legend(['subreddit'])

    plt.show()


if __name__ == '__main__':
    main()
