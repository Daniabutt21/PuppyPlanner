from fastapi import Request, HTTPException
from fastapi.responses import FileResponse
import os
from pathlib import Path
from mangum import Mangum

async def handler(request: Request, context):
    """Handle static file requests for Vercel"""
    try:
        # Extract file path from request
        path = request.url.path
        if path.startswith('/static/'):
            file_path = path[8:]  # Remove '/static/' prefix
        else:
            file_path = path
        
        # Build full path to static file
        static_dir = Path(__file__).parent.parent / "static"
        full_path = static_dir / file_path
        
        if full_path.exists() and full_path.is_file():
            return FileResponse(full_path)
        else:
            raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error serving file: {str(e)}")

# Create Mangum handler for Vercel
from fastapi import FastAPI
static_app = FastAPI()

@static_app.get("/{path:path}")
async def serve_static(path: str):
    """Serve static files"""
    static_dir = Path(__file__).parent.parent / "static"
    full_path = static_dir / path
    
    if full_path.exists() and full_path.is_file():
        return FileResponse(full_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

# Vercel handler
static_handler = Mangum(static_app, lifespan="off")
