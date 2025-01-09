from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router

app = FastAPI()

# Подключаем маршруты из других модулей
app.include_router(task_router)
app.include_router(user_router)


@app.get("/", tags=["Root"])
async def root():
	return {"message": "Welcome to Taskmanager"}
