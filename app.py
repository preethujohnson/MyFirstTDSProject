#/// script
#requires-python = ">3.13"
#dependencies = [
#    "fastapi",
#    "uvicom",
#    "requests",
#    ]
#///

from fastapi import fastAPI

app = FastAPI () 

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET','POST'],
    allow_headers=['*']
)

@app.get("/")
def home():
	return{"Yay TDS is awesome"}

if __name__=='__main__':
	import uvicorn
	uvicorn.run(app,host="0.0.0.0",port=8000)
