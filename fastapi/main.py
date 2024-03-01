from fastapi import FastAPI

app = FastAPI()


@app.get('/{item_id}')
async def read_item(item_id):
	if item_id == 'Aleksander':
		return 2+2
	elif item_id == 'Maksim':
		return 'AK47'
	else:
		return{'message': item_id }
