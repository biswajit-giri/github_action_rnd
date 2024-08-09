from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/external-api")
def call_external_api():
    # Example API: JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
