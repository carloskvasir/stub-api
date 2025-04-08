# Stub API

A simple FastAPI-based stub API that provides test endpoints. This project serves as a template or testing tool for API-dependent applications.

## Features

- Simple test endpoints for development and testing
- Health check endpoint for monitoring
- Docker-ready configuration for easy deployment
- Configurable via environment variables
- OpenAPI documentation (Swagger and ReDoc) included
- Minimal dependencies for easy maintenance

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn

## Installation

### Local Development

1. Clone this repository:
   ```bash
   git clone git@github.com:carloskvasir/stub-api.git stub_api
   cd stub_api
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```
   The API will be available at http://localhost:8000

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t stub-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 stub-api
   ```

To use a different port:
   ```bash
   docker run -p 8080:8080 -e PORT=8080 stub-api
   ```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/test` | GET | Generic test endpoint |
| `/check` | GET | Health check endpoint |
| `/message` | GET | Returns a test message |
| `/v1/logs` | POST | Logs the received token and JSON payload |
| `/docs` | GET | OpenAPI Swagger documentation |
| `/redoc` | GET | OpenAPI ReDoc documentation |

## Example Requests

### Using curl

```bash
# Test endpoint
curl http://localhost:8000/v1/test

# Health check
curl http://localhost:8000/check

# Get message
curl http://localhost:8000/message

# Log data (with token and JSON payload)
curl -X POST http://localhost:8000/v1/logs \
  -H "Authorization: Bearer your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"key": "value", "example": "data"}'
```

### Expected Responses

```json
// /v1/test
{
  "message": "Generic test endpoint working"
}

// /check
{
  "status": "ok"
}

// /message
{
  "message": "This is a test message from the API"
}

// /v1/logs
{
  "status": "success",
  "message": "Data received and logged successfully"
}
```

## API Documentation

After starting the application, visit:
- http://localhost:8000/docs - Swagger UI documentation
- http://localhost:8000/redoc - ReDoc documentation

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Port to run the application | 8000 |
| LOG_LEVEL | Logging level (DEBUG, INFO, WARNING, ERROR) | INFO |

## Development

### Project Structure
```
stub_api/
├── app.py            # Main application file
├── Dockerfile        # Docker configuration
├── requirements.txt  # Python dependencies
└── README.md         # This documentation
```

## License

This project is licensed under the [Mozilla Public License 2.0](LICENSE) - see the LICENSE file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [Uvicorn](https://www.uvicorn.org/) for the ASGI server

## Author

Copyright (c) 2025 Carlos Kvasir (https://kvasir.dev) | https://mozilla.org/MPL/2.0/