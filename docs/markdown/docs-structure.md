# Qbank Documentation Structure Overview

This document outlines the structure and organization of Qbank’s technical documentation suite, designed for multi-channel publishing and audience-specific delivery.

---

## 🧱 Content Channels

- **Markdown:** Developer guides, user-facing help, chatbot snippets  
- **DITA XML:** Modular topics for HTML5, PDF, and conditional publishing  
- **Chatbot:** Snippets and flows for internal and customer-facing bots

---

## 🗂️ Folder Layout

```
docs/
├── markdown/       # Human-readable guides
├── diagrams/       # Mermaid source files
├── images/         # Screenshots and branding

dita/
├── topics/         # DITA XML topic files
├── maps/           # DITA maps for publishing

chatbot/
├── internal-snippets.md
├── customer-snippets.md
├── onboarding-flow.md
```

---

## 🧠 Audience Targeting

Content is tagged and filtered based on audience:

- `audience="internal"` → Support, IT, DevOps  
- `audience="customer"` → End users, loan applicants

---

## 🧩 Publishing Outputs

- **HTML5:** Responsive help center  
- **PDF:** Print-ready onboarding packets  
- **Chatbot:** Slack, Teams, mobile widget integration

---

## 📊 Diagram

![Content Map](../diagrams/content-map.svg)