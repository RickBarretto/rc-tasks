"""Gets all tasks from a category

Public function: from_category(page) -> set
"""

from requests_html import HTML, HTMLResponse

__all__ = [
    "from_category"
]


# --->> Internal Functions

def is_valid_page(html: HTML) -> bool:
    """Validades the page
    Note: This url is returned from loop when all pages are finished
    """
    return html.url !=  \
        "https://rosettacode.org/wiki/Help:Introduction"


def print_url(html: HTML):
    """Just prints some info in terminal
    It avoids to uncertain if the program is running or not
    """
    print(f"    - Fetching from: {html.url}")


def find_tasks(html: HTML) -> list:
    """Returns list of tasks's elements from the page."""
    return html.find(".mw-category-group > ul > li")


# --->> Public function

def from_category(page: HTMLResponse) -> set:
    """Gets all tasks from a page's Category

    
    Note that this function doesn't fetch only one page,
    but every page from the same category. It's possible
    because of the iterator, that iterates to the next page.

    When the category ends, it's returned an Introduction page
    from the loop. 
    Because of it, We use the `is_valid_page(url)`
    to check the current page, and return the tasks's set.    
    """
    tasks: set = set()
    for html in page.html:
        print_url(html)
        if is_valid_page(html):
            [
                tasks.add(element.text)
                for element in
                find_tasks(html)
            ]
        else:
            return tasks