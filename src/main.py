import pprint
import requests_html

from src import get_tasks


__all__ = [ "main" ]


# --->> Internal Functions

def get_all_avaliable_tasks(session) -> set:
    """Returns a set of all tasks implemented in Rosetta Code"""

    print("Fetching all tasks...")

    pages = session.get(
        "https://rosettacode.org/wiki/Category:Programming_Tasks")

    return get_tasks.from_category(pages)


def get_implemented_tasks(session, language: str) -> set:
    """Returns a set of tasks implemented in given language"""

    print(f"\nFetching tasks from {language}...")
    pages = session.get(
        "https://rosettacode.org/wiki/Category:{language}")

    return get_tasks.from_category(pages)


# --->> RUN !!!

def run():
    """The Poetry's Script entry"""

    task_session     = requests_html.HTMLSession()
    language_session = requests_html.HTMLSession()

    language = input("Type your language: ")
    tasks    = (
        get_all_avaliable_tasks(task_session),
        get_implemented_tasks(language_session, language)
    )

    pprint.pprint((tasks[0] - tasks[1]))