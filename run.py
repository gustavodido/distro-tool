from app import app
from os import getenv

port = int(getenv("PORT", 8080))
app.run(host='0.0.0.0', port=port, debug=True)