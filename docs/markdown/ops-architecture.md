# Qbank Ops Console Architecture Overview

This document outlines the system architecture of Qbank’s internal Ops Console, used by support and IT teams to monitor and manage platform operations.

---

## 🧩 Architecture Components

- **Frontend:** React  
- **Backend:** Node.js  
- **Event Streaming:** Kafka  
- **Database:** MongoDB  
- **Authentication:** Qbank SSO  
- **Alerting:** Slack + PagerDuty

---

## 🧠 Design Principles

- Modular microservices  
- Real-time event processing  
- Role-based access control  
- Scalable logging and alerting

---

## 📊 Diagram

![System Architecture](../diagrams/system-architecture.svg)