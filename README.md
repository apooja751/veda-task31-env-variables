# Task 31: Configure Environment Variables on a Cloud Server

## Project Overview

This project demonstrates how to configure environment variables for a Python Flask application deployed on an AWS EC2 Ubuntu server.

Instead of hardcoding application configuration inside the source code, the application reads its settings from a `.env` file using `python-dotenv`.

## Objectives

- Understand environment variables in Linux.
- Configure application settings using a `.env` file.
- Read environment variables in Python using `os.getenv()`.
- Load configuration using `python-dotenv`.
- Protect sensitive configuration using `.gitignore` and Linux file permissions.
- Deploy and test a Flask application on AWS EC2.

## Technologies Used

- AWS EC2
- Ubuntu 24.04 LTS
- Python 3.12
- Flask 3.1.3
- python-dotenv 1.2.4
- Linux Shell
- Git and GitHub

## Project Structure

```text
veda-task31-env-variables/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env                 # Not uploaded to GitHub
└── venv/                # Not uploaded to GitHub
```

## Application Features

- Displays application name and environment.
- Reads configuration from environment variables.
- Supports Development, Staging and Production configurations.
- Provides a JSON configuration endpoint at `/config`.
- Separates application code from configuration.

## Environment Variables

The application uses the following variables:

| Variable | Description |
|---|---|
| APP_NAME | Application name |
| APP_ENV | Application environment |
| APP_VERSION | Application version |
| SERVER_MESSAGE | Application message |
| SECRET_KEY | Secret configuration value |

Example configuration (using a placeholder secret):

```env
APP_NAME="Cloud Config Manager"
APP_ENV="Production"
APP_VERSION="1.0.0"
SERVER_MESSAGE="Environment variables are working on AWS!"
SECRET_KEY="your-own-secret-value"
```

**Security:** The actual `.env` file is excluded from GitHub using `.gitignore`.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/apooja751/veda-task31-env-variables.git
cd veda-task31-env-variables
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the environment file

```bash
nano .env
```

Add your own configuration values using the example above.

### 5. Start the Flask application

```bash
python app.py
```

The application runs on port 5000.

## Testing

### Main application

```text
/
```

Displays the application configuration.

### JSON configuration endpoint

```text
/config
```

Returns the application configuration in JSON format.

## Security Practices

- Sensitive environment files are excluded using `.gitignore`.
- `.env` permissions are restricted using `chmod 600 .env`.
- Virtual environment directories are excluded from version control.
- Actual secret values must never be committed to GitHub.

## Verification Results

- Python virtual environment created.
- Flask application configured successfully.
- Environment variables loaded using `python-dotenv`.
- Application tested on AWS EC2.
- Production configuration verified.
- Staging configuration verified after restarting the Flask application.
- JSON endpoint tested successfully.

## Learning Outcome

This task demonstrates practical environment variable management, configuration separation, Linux file permissions, and basic secret-handling practices for cloud-hosted Python applications.

