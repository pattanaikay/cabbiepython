from fastapi import FastAPI

app = FastAPI()

# Define a function to handle GET requests to the root path "/"
@app.get("/")
async def root():
  # Return a simple JSON message
  return {"message": "Hello World!"}

# Run the API using Uvicorn (install with pip install uvicorn)
if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host="0.0.0.0", port=8000)
