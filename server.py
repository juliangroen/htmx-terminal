#!/usr/bin/env python

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://localhost:\d+$",
    allow_methods=["*"],
    allow_headers=["*"],
)

items = [
    """<div class="text-red-400 mb-2">
        Your mother was a hamster and your father smelt of elderberries.
    </div>""",
    """<div class="text-slate-200 mb-2">
        We are the knights who say 'Ni'!
    </div>""",
    """<div class="text-slate-200 mb-2">
        What is the airspeed velocity of an unladen swallow?
    </div>""",
    """<div class="text-slate-200 mb-2">
        Listen, strange women lyin' in ponds distributin' swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.
    </div>""",
    """<div class="text-slate-200 mb-2">
        Help, help, I'm being repressed!
    </div>""",
    """<div class="text-slate-200 mb-2">
        On second thoughts, let's not go to Camelot. It is a silly place.
    </div>""",
]

counter = 0


@app.get("/python")
async def get_next_item():
    global counter
    if counter < len(items):
        item = items[counter]
        counter += 1
        return HTMLResponse(content=item)
    else:
        counter = 0
        # status_code 286 stops htmx from continuing to make requests.
        return HTMLResponse(content="", status_code=286)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)
