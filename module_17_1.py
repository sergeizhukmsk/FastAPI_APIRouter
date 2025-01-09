from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel



# Создаем экземпляр приложения FastAPI
app = FastAPI(debug=True)




# Чтобы запустить приложение, используйте команду:
# uvicorn module_17_1:app --reload
# uvicorn module_17_1:app --host 127.0.0.1 --port 5000 --reload
# uvicorn module_17_1:app --host 127.0.0.1 --port 8000 --reload
