from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uploader


app = FastAPI()
app.mount("/Static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="Templates")


@app.get("/memes", response_class=HTMLResponse)
def read_memes(request: Request):
    files = uploader.main()
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id, "files": files}
    )


@app.get("/memes/{meme_id}", response_class=HTMLResponse)
def read_meme(request: Request, meme_id: int):
    files = uploader.main(meme_id=meme_id)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id, "files": files}
    )


@app.post("/memes", response_class=HTMLResponse)
async def post_meme(request: Request, file: UploadFile = File(alias="file")):
    files = uploader.main("post", file=file)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id, "files": files}
    )


@app.put("/memes/{meme_id}", response_class=HTMLResponse)
def put_meme(request: Request, meme_id: int):
    files = uploader.main("put", meme_id=meme_id)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id, "files": files}
    )


@app.delete("/memes/{meme_id}", response_class=HTMLResponse)
def delete_meme(request: Request, meme_id: int):
    files = uploader.main("delete", meme_id=meme_id)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id, "files": files}
    )
