from fastapi import FastAPI

app = FastAPI()


@app.get('/items/{item_id}')
async def read_item(item_id):
	return{'message': item_id }
