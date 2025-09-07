# Annotated Rewrite – API Authentication Guide

This document presents a side-by-side comparison of the original API authentication guide and its rewritten version, with annotations explaining editorial decisions.

---

## 📝 Original Version

> Qbank uses OAuth 2.0. To get a token, post to `/auth/token` with your client ID and secret. You’ll get a token back. Rate limit is 1000/hour.

---

## ✍️ Rewritten Version

Qbank’s API Gateway uses OAuth 2.0 for secure access. Clients must obtain an access token via the `/auth/token` endpoint.

### 🔐 Request Format

```http
POST /auth/token
Content-Type: application/json
{
  "client_id": "qbank-client-001",
  "client_secret": "s3cr3t-v@lu3"
}
```

### 🧾 Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 3600
}
```

### ⚠️ Rate Limits

- 1000 requests/hour  
- Exceeding returns `429 Too Many Requests`

---

## 🧠 Editorial Annotations

| Change | Rationale |
|-------|-----------|
| Expanded intro | Adds clarity and context for new users |
| Structured request/response | Improves readability and copy/paste usability |
| Added headings and icons | Enhances visual scanning and accessibility |
| Formal tone | Aligns with enterprise documentation standards |
| Explicit rate limit behavior | Reduces ambiguity and support tickets |

---

## 📎 Notes

This rewrite reflects Qbank’s editorial standards for clarity, consistency, and user empowerment. It demonstrates how small changes in tone and structure can dramatically improve usability.