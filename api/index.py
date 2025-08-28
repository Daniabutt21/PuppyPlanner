from http.server import BaseHTTPRequestHandler
import json
import os
from pathlib import Path

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL path
        path = self.path
        print(f"DEBUG: Requested path: {path}")  # Debug log
        
        if path == "/":
            # Redirect root to login page
            self.send_response(302)
            self.send_header('Location', '/login')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_response = """
            <!DOCTYPE html>
            <html>
            <head><title>Redirecting to Login</title></head>
            <body>
                <p>Redirecting to login page...</p>
                <p><a href="/login">Click here if you are not redirected automatically.</a></p>
            </body>
            </html>
            """
            self.wfile.write(html_response.encode())
            
        elif path == "/login":
            # Serve your existing login.html template
            try:
                template_path = Path(__file__).parent.parent / "templates" / "pages" / "login.html"
                with open(template_path, 'r', encoding='utf-8') as f:
                    login_html = f.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(login_html.encode())
                
            except FileNotFoundError:
                # Fallback if template not found
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('Login template not found'.encode())
            except Exception as e:
                # Error handling
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Error loading template: {str(e)}'.encode())
            
        elif path.startswith("/static/"):
            # Serve static files (CSS, JS, images)
            print(f"DEBUG: Static file request: {path}")  # Debug log
            try:
                # Remove /static/ prefix and build file path
                file_path = path[8:]  # Remove '/static/' prefix
                static_dir = Path(__file__).parent.parent / "static"
                full_path = static_dir / file_path
                
                print(f"DEBUG: File path: {file_path}")  # Debug log
                print(f"DEBUG: Static dir: {static_dir}")  # Debug log
                print(f"DEBUG: Full path: {full_path}")  # Debug log
                print(f"DEBUG: File exists: {full_path.exists()}")  # Debug log
                print(f"DEBUG: Is file: {full_path.is_file()}")  # Debug log
                
                if full_path.exists() and full_path.is_file():
                    # Determine content type based on file extension
                    if file_path.endswith('.css'):
                        content_type = 'text/css'
                    elif file_path.endswith('.js'):
                        content_type = 'text/javascript'
                    elif file_path.endswith('.png') or file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
                        content_type = 'image/png' if file_path.endswith('.png') else 'image/jpeg'
                    elif file_path.endswith('.ico'):
                        content_type = 'image/x-icon'
                    else:
                        content_type = 'application/octet-stream'
                    
                    print(f"DEBUG: Content type: {content_type}")  # Debug log
                    
                    self.send_response(200)
                    self.send_header('Content-type', content_type)
                    self.end_headers()
                    
                    # Read and serve the file
                    with open(full_path, 'rb') as f:
                        self.wfile.write(f.read())
                        
                    print(f"DEBUG: File served successfully")  # Debug log
                else:
                    # File not found
                    print(f"DEBUG: File not found or not a file")  # Debug log
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(f'Static file not found: {file_path}'.encode())
                    
            except Exception as e:
                # Error handling
                print(f"DEBUG: Error serving static file: {str(e)}")  # Debug log
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Error serving static file: {str(e)}'.encode())
            
        else:
            # Default response for other paths
            print(f"DEBUG: Unknown path, serving default response")  # Debug log
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Hello from Vercel!'.encode())
        return

    def do_POST(self):
        # Handle login form submission
        path = self.path
        
        if path == "/login":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            success_html = """
            <!DOCTYPE html>
            <html>
            <head><title>Login Success</title></head>
            <body>
                <h2>Login Successful!</h2>
                <p>Welcome to PuppyPlanner!</p>
                <p><a href="/login">Back to login</a></p>
            </body>
            </html>
            """
            self.wfile.write(success_html.encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('POST request received'.encode())
        return
