# API Documentation

This document provides a reference for all endpoints available in the Stub API.

## Base URL

All endpoints are relative to the base URL: `http://localhost:8000`

## Endpoints

### GET `/v1/test`

Generic test endpoint.

**Response**:
```json
{
  "message": "Generic test endpoint working"
}
```

### GET `/check`

Health check endpoint.

**Response**:
```json
{
  "status": "ok"
}
```

### GET `/message`

Returns a test message.

**Response**:
```json
{
  "message": "This is a test message from the API"
}
```

### POST `/v1/logs`

Logs the received token and JSON payload.

**Headers**:
- `Authorization`: Bearer token (required)
- `Content-Type`: application/json

**Request Body**:
```json
{
  // Any JSON data
}
```

**Response**:
```json
{
  "status": "success",
  "message": "Data received and logged successfully"
}
```