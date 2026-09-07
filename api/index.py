from streamlit.web import cli as stcli
import sys
import os

def handler(request):
    # This tells Vercel "I am a handler"
    sys.argv = [
        "streamlit", 
        "run", 
        "app.py", 
        "--server.port", os.environ.get("PORT", "8501"), 
        "--server.address", "0.0.0.0", 
        "--server.headless", "true"
    ]
    stcli.main()
    return {"statusCode": 200, "body": "OK"}