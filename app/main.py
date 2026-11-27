"""Things to bring: the starting point of your team project.

This is an example. Replace the topic with your own: change the fields,
the texts and the page. Grow it one pull request at a time.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- storage.py   where the entries are kept
- templates/   the HTML page
- static/      the stylesheet
"""

from pathlib import Path
from urllib.parse import quote

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import storage

HERE = Path(__file__).parent

app = FastAPI(title="Things to bring")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


@app.get("/")
def show_list(request: Request):
    """The start page: the form and all entries."""
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "entries": storage.all_entries(),
            "error": request.query_params.get("error"),
        },
    )


def calculate(a, operator, b):
    """Apply one of the four basic operators."""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b
    raise ValueError("Unknown operator: {}".format(operator))


def error_redirect(message):
    """Send the user back with a readable error message."""
    return RedirectResponse("/?error=" + quote(message), status_code=303)


@app.post("/add")
def add(a: str = Form(...), operator: str = Form(...), b: str = Form(...)):
    """The form on the start page sends its fields here."""
    try:
        left, right = float(a), float(b)
    except ValueError:
        return error_redirect("Please enter a number in both fields.")

    try:
        result = calculate(left, operator, right)
    except ZeroDivisionError:
        return error_redirect("Cannot divide by zero.")
    except ValueError:
        return error_redirect("Please choose one of the four operators.")

    storage.add_entry(a=left, operator=operator, b=right, result=result)
    # Back to the start page. 303 tells the browser: load it with GET.
    return RedirectResponse("/", status_code=303)
