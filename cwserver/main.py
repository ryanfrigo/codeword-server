from fastapi import FastAPI, Request
import os

app = FastAPI(title="Codeword Server")

@app.post("/retell/codeword")
async def get_codeword(_: Request):
    codeword = os.getenv("CODEWORD", "BANANA PHONE")
    return {"ok": True, "codeword": codeword}
