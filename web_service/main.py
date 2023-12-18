from fastapi import FastAPI

from data_request_model import Entry

app = FastAPI()


@app.get("/")
async def read_root():
	return {"Message" : "NV-Testcase web-service"}


@app.get("/all")
async def get_all_entries():
	return {"Message" : "All entries"}
