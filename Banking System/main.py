from fastapi import FastAPI

from routers.accounts import router as accounts_router


app=FastAPI()


app.include_router(accounts_router)

