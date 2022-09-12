from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/credit", response_class=HTMLResponse)
async def login_home(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})