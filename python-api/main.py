from fastapi import FastAPI, HTTPException
import os 


app = FastAPI()

def read_log_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

@app.get("/logs/")
async def get_logs():
    log_path = "/var/log/sysmonitor.log"  # Your specific log file path
    try:
        logs = read_log_file(log_path)
        return {"logs": logs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading logs: {str(e)}")

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)