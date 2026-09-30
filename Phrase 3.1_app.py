from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="PocketSmartAI")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/home-budget")
def handle_home_budget(budget: float = Form(...)):
    model = genai.GenerativeModel("gemini-1.5-flash-pro")
    prompt = f"Suggest home decor items from IKEA/Amazon within a budget of {budget} in JSON format."
    response = model.generate_content(prompt)
    return {"recommendations": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)