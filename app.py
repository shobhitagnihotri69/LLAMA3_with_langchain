from fastapi import FastAPI
app = FastAPI()
@app.post('/hell')
async  def hell():
     return hell
