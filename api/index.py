import os
from streamlit.web.bootstrap import run
from streamlit import config as _config

def handler(request):
    # Tell streamlit to run app.py
    sys.argv = ["streamlit", "run", "app.py", "--server.port", os.environ.get("PORT", "8501"), "--server.address", "0.0.0.0"]
    _config.set_option("server.headless", True)
    run("app.py", "", [], [])
    return {"statusCode": 200}