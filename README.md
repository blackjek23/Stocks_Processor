# Stock EMA Cross Alert System

This project is a Python-based system that monitors stock price movements in relation to the 150 EMA (Exponential Moving Average). The system logs cross-up and cross-down alerts and provides a simple Flask web interface for viewing the results. Docker is used to containerize the application, ensuring a smooth deployment process.

## Features

- **Stock Monitoring**: Detects when stock prices cross the 150 EMA.
- **Alert Logging**: Alerts for cross-ups and cross-downs are logged in `alerts.txt`.
- **Docker Support**: The application can be easily deployed using Docker.
- **Flask Web Interface**: Displays alerts in a web page. (pending)

## Project Structure

```plaintext
.
├── alerts.txt           # Logs of EMA cross alerts
├── app/                 # Flask app directory
│   ├── templates/       # HTML templates for the web interface
│   └── app.py           # Main Flask application file
├── downloader/      # Docker implementation for downloading stock data
├── prosses/         # Docker implementation for processing stock data
|── shreder/         # Docker implementation for shredding unnecessary data
├── Jenkinsfile          # Jenkins pipeline for CI/CD
├── S3_Start.tf          # Terraform file for S3 bucket setup
```
## CI/CD Pipeline

The project includes a Jenkins pipeline (`Jenkinsfile`) for automating the integration and deployment process. Configure Jenkins to use the pipeline for continuous integration and delivery.

---

Let me know if you'd like any further adjustments!