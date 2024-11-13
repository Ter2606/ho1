from fastapi import FastAPI, datetime

app = FastAPI()

@app.get("/")
async def root(request: Request):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    d_text = f"Today's Date: {date}"
    return d_text