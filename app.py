# Copyright (c) 2025 Carlos Kvasir (https://kvasir.dev) | https://mozilla.org/MPL/2.0/
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.

import logging
import os
from typing import Any, Dict, Optional

from fastapi import Body, FastAPI, Header
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("stub-api")

# Get port from PORT environment variable (default 8000 if not defined)
PORT = int(os.environ.get("PORT", 8000))

app = FastAPI(title="Stub API", version="0.1.0")

@app.get("/v1/test")
def read_test():
    """Generic test endpoint."""
    return {"message": "Generic test endpoint working"}

@app.get("/check")
def read_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.get("/message")
def read_message():
    """Endpoint that returns a test message."""
    return {"message": "This is a test message from the API"}

@app.post("/v1/logs")
async def create_log_entry(
    payload: Dict[str, Any] = Body(...),
    authorization: Optional[str] = Header(None)
):
    """
    Endpoint that receives a token and JSON data, then logs them.
    This follows RESTful conventions by:
    - Being placed under a version path (/v1/)
    - Using a noun ('logs') as the resource
    - Using POST verb to create a new log entry
    
    Args:
        payload: The JSON body of the request
        authorization: The Authorization header containing the token
    
    Returns:
        A confirmation message
    """
    # Log the token and payload
    logger.info(f"Received token: {authorization}")
    logger.info(f"Received payload: {payload}")
    
    return {"status": "success", "message": "Data received and logged successfully"}

# Run the application with Uvicorn if the script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
