from fastapi import FastAPI, HTTPException

app = FastAPI()

LOG_PATH = "/var/log/sysmonitor.log"

@app.get("/logs/")
async def get_logs():
    try:
        with open(LOG_PATH, "r") as file:
            logs = file.readlines()
        return {"logs": logs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading logs: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)