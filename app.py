import os
from dotenv import load_dotenv
from flask import Flask, jsonify

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Read configuration from environment variables
APP_NAME = os.getenv("APP_NAME", "Cloud Config Manager")
APP_ENV = os.getenv("APP_ENV", "Development")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
SERVER_MESSAGE = os.getenv(
    "SERVER_MESSAGE",
    "Application is running using environment variables!"
)


@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>{APP_NAME}</title>
    </head>
    <body style="font-family: Arial; margin: 50px;">
        <h1>{APP_NAME}</h1>
        <h3>Cloud Server Environment Configuration</h3>
        <p><b>Environment:</b> {APP_ENV}</p>
        <p><b>Version:</b> {APP_VERSION}</p>
        <p><b>Message:</b> {SERVER_MESSAGE}</p>
        <p>Configuration loaded from environment variables.</p>
    </body>
    </html>
    """


@app.route("/config")
def config():
    return jsonify({
        "app_name": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION,
        "message": SERVER_MESSAGE
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
