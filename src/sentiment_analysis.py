"""
Provides static helper functions for analyzing the sentiment of Reddit comments.
"""


from textblob import TextBlob


def get_comment_polarity(comment):
    """
    Given a comment, return a tuple of comment, and its sentiment score.
    """
    comment = TextBlob(comment)

    return (comment, comment.sentiment.polarity)


def get_comment_subjectivity(comment):
    """
    Given a comment, return a tuple of comment, and its polarity score.
    """
    comment = TextBlob(comment)

    return (comment, comment.sentiment.subjectivity)


if __name__ == '__main__':
    sentiment = get_comment_polarity(
        'Textblob is amazingly simple to use. What great fun!')

    polarity = get_comment_subjectivity(
        'Textblob is amazingly simple to use. What great fun!')

    print(sentiment)

    print(polarity)
