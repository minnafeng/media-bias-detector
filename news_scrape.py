"""Scrapes and summarizes news articles from the New York Times."""

from newspaper import Article
import nltk


def summarize_article(url):
    """Summarizes the article and provides valuable information regarding the article metadata, including images and attributions."""
    article = Article(url)

    # download article and parse
    article.download()
    article.parse()

    # download sentence tokenizer to extract/detect words
    nltk.download("punkt")

    # allow for natural language processing
    article.nlp()

    # get the author(s) of the article
    author_string = "Author(s): "
    for author in article.authors:
        author_string += (
            author  # adds all authors (if more than 1) to the author string.
        )
    print(author_string)

    # get the publishing date of the article
    date = article.publish_date
    print("Publish Date: " + str(date.strftime("%m/%d/%Y")))

    # get the top image of the article
    print("Top Image URL: " + str(article.top_image))

    # get the article images
    image_string = "All Images: "
    for image in article.images:
        image_string += (
            "\n\t" + image
        )  # adds a newline and a tab before each image is printed
    print(image_string)
    print()

    # get the article summary
    print("A Quick Article Summary")
    print("----------------------------------------")
    print(article.summary)

    return article.summary
