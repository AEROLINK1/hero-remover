from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove

app = FastAPI()

@app.post("/remove")
async def remove_bg(file: UploadFile = File(...)):
    # leer bytes
    contents = await file.read()
    # remover fondo
    result = remove(contents)
    # regresar PNG
    return Response(content=result, media_type="image/png")
