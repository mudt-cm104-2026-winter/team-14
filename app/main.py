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
        request, "index.html", {"entries": storage.all_entries()}
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


@app.post("/add")
def add(a: float = Form(...), operator: str = Form(...), b: float = Form(...)):
    """The form on the start page sends its fields here."""
    storage.add_entry(a=a, operator=operator, b=b, result=calculate(a, operator, b))
    # Back to the start page. 303 tells the browser: load it with GET.
    return RedirectResponse("/", status_code=303)
