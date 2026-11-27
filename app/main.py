"""A small calculator web app that keeps a history.

What happens where:
- main.py      the web part: which address shows what (the "routes")
- storage.py   where the calculations are kept
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

app = FastAPI(title="Calculator")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


@app.get("/")
def show_list(request: Request):
    """The start page: the form and the history, optionally filtered."""
    operator = request.query_params.get("operator", "all")
    newest = request.query_params.get("newest") == "1"

    entries = storage.all_entries()
    if operator in ("+", "-", "*", "/"):
        entries = [entry for entry in entries if entry["operator"] == operator]
    else:
        operator = "all"
    if newest:
        entries = list(reversed(entries))

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "entries": entries,
            "stats": storage.stats(),
            "operator": operator,
            "newest": newest,
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


@app.post("/clear")
def clear():
    """Empty the history and go back to the start page."""
    storage.clear_entries()
    return RedirectResponse("/", status_code=303)


@app.post("/delete/{entry_id}")
def delete(entry_id: int):
    """Remove one calculation and go back to the start page."""
    storage.delete_entry(entry_id)
    return RedirectResponse("/", status_code=303)
