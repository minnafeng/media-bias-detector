"""Extracts all the latest articles from the technology section of the New York Times"""

import requests
from bs4 import BeautifulSoup as soup


def get_content_string(url):
    """Extracts a content dictionary from an HTML outline of the NY Times Tech Section."""

    # send GET request to url
    page = requests.get(url)

    # get all html of the page
    page_soup = soup(page.content, "html.parser")

    # get script tags of a certain type
    containers = page_soup.find_all("script", {"type": "application/ld+json"})

    # create an article list, a snippet of the HTML outline including all articles
    article_list = []
    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)
    article_list[0:2] = ["".join(article_list[0:2])]  # remove whitespace

    # extract first since the rest are duplicates
    content_string = article_list[0]

    # get only list items and not entire collection page
    article_index = content_string.index("itemListElement")
    content_string = content_string[article_index + 18 :]

    return content_string


def find_occurrences(content_string):
    """Finds the start and end of all correct article hyperlinks in the extracted content string."""

    # search for the common hyperlink beginning across all articles.
    start_indices = [
        i
        for i in range(len(content_string))
        if content_string.startswith("https://www.nytimes.com/2023", i)
    ]

    # search for the common ".html" extension at the end of each article hyperlink.
    end_indices = [
        i for i in range(len(content_string)) if content_string.startswith(".html", i)
    ]
    end_indices = [x + 5 for x in end_indices]  # move index past .html chars

    # equalize lengths of the start and end indices
    if len(start_indices) > len(end_indices):
        difference = len(start_indices) - len(end_indices)
        start_indices = start_indices[:difference]
    if len(end_indices) > len(start_indices):
        difference = len(end_indices) - (len(end_indices) - len(start_indices))
        end_indices = end_indices[:difference]

    return start_indices, end_indices


def get_all_urls(start_indices, end_indices, content_string):
    """Extracts all article hyperlinks from the content string."""
    url_list = []
    for i in range(len(start_indices)):
        url_list.append(content_string[start_indices[i] : end_indices[i]])
    return url_list
