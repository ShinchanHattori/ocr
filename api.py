from fastapi import FastAPI, File, UploadFile
import easyocr
import uvicorn

app = FastAPI()

# Initialize the EasyOCR reader with English and Hindi languages
reader = easyocr.Reader(['en', 'hi'])

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Read text from the image using EasyOCR
    try:
        output = reader.readtext(contents)
        result = [text[1] for text in output]
        return {"text": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
