import os

WS_HOST = os.getenv('WEB_SERVICE', 'localhost')
WS_PORT = os.getenv('WEB_SERVICE_PORT', 8001)
URL = f"http://{WS_HOST}:{WS_PORT}"
