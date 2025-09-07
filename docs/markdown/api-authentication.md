# Qbank API Gateway – Authentication Guide

Qbank’s API Gateway uses OAuth 2.0 for secure access. Clients must obtain an access token via the `/auth/token` endpoint.

---

## 🔐 Request Format

```http
POST /auth/token
Content-Type: application/json
{
  "client_id": "qbank-client-001",
  "client_secret": "s3cr3t-v@lu3"
}
```

---

## 🧾 Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 3600
}
```

---

## ⚠️ Rate Limits

- 1000 requests/hour  
- Exceeding returns `429 Too Many Requests`

---

## 📊 Diagram

![Token Flow](../diagrams/token-flow.svg)