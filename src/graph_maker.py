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

    polarity_plot = average_polarity.plot(
        kind='bar', title='Average Polarity per Subreddit', x='subreddit', y='average')

    polarity_plot.set_xlabel('subreddit')

    polarity_plot.set_ylabel('average polarity')

    polarity_plot.legend(['subreddit'])

    subjectivity_plot = average_subjectivity.plot(
        kind='bar', title='Average Subjectivity per Subreddit', x='subreddit', y='average')

    subjectivity_plot.set_xlabel('subreddit')

    subjectivity_plot.set_ylabel('average polarity')

    subjectivity_plot.legend(['subreddit'])

    plt.show()


if __name__ == '__main__':
    main()
