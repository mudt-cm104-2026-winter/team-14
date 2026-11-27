# How to run the app locally

These steps work on macOS, Linux, and Windows. You need Python 3.10 or newer and Git installed.

## 1. Get the code

```bash
git clone git@github.com:mudt-cm104-2026-winter/team-14.git
cd team-14
```

If SSH is not set up on your computer, clone with HTTPS instead:

```bash
git clone https://github.com/mudt-cm104-2026-winter/team-14.git
```

## 2. Create a virtual environment

Run this from the `team-14` folder, not from inside `app`:

```bash
python3 -m venv .venv
```

On Windows, use `py -3 -m venv .venv` if `python3` is not recognised.

## 3. Activate it

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows (Command Prompt):

```bat
.venv\Scripts\activate.bat
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of your prompt. That means the environment is active.

## 4. Install the packages

```bash
pip install -r requirements.txt
```

The versions are pinned in `requirements.txt`, so everyone installs the same ones.

## 5. Start the server

```bash
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000> in your browser. The `--reload` flag makes the server restart when you change a file.

To check it works, enter two numbers, pick an operation, and press Calculate. The result shows up in the history. You can filter by operator, tick "Newest first", delete one row, or clear the whole list.

## 6. Stop it

Press `Ctrl+C` in the terminal. Type `deactivate` if you also want to leave the virtual environment.

## Things that often trip people up

- The history is kept in memory, so restarting the server empties it. That is expected at this stage.
- If port 8000 is already in use, start with `uvicorn app.main:app --reload --port 8001` and open <http://127.0.0.1:8001>.
- If `pip` installs into the wrong place, check that `(.venv)` is showing before running step 4.
