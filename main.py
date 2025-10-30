from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import cloudinary
from cloudinary.uploader import upload
from bson import ObjectId


load_dotenv()
app = FastAPI()


client = MongoClient("mongodb+srv://shiva:shiva333666@cluster0.yrymvfe.mongodb.net/shiva?retryWrites=true&w=majority")
db = client['shiva']
collection = db['photos_detail']

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload/")
async def upload_images(files: list[UploadFile] = File(...)):
    uploaded_data = []

    for file in files:
        upload_result = cloudinary.uploader.upload(file.file, folder="fastapi_uploads")

        image_data = {
            "filename": file.filename,
            "url": upload_result.get("secure_url"),
            "public_id": upload_result.get("public_id")
        }

        result = collection.insert_one(image_data)


        image_data["_id"] = str(result.inserted_id)
        uploaded_data.append(image_data)

    return {"message": "Uploaded successfully!", "data": uploaded_data}



@app.get("/success", response_class=HTMLResponse)
async def success_page(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})


@app.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request):
    images = list(collection.find({}, {"_id": 0}))
    return templates.TemplateResponse("gallery.html", {"request": request, "images": images})

