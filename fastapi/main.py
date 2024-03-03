from fastapi import FastAPI

app = FastAPI()


@app.get('/{item_id:path}')
async def read_file(file_path: str):
	return {'File_path': file_path}
