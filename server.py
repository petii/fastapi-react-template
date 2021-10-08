from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

app.mount('/app', StaticFiles(directory='./app/dist',html=True), name='spa')

@app.get('/hello')
async def read_root():
    return ['hello', 'world']

@app.middleware('http')
async def add_content_type_header_for_js(request: Request, call_next):
    response = await call_next(request)
    if request.url.path.find('.js') >= 0:
        response.headers['Content-type'] = 'text/javascript'
    return response