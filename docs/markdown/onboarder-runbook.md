# Qbank Onboarder – Provisioning Runbook

This runbook outlines the steps for provisioning new employees using Qbank Onboarder, the internal HR automation tool.

---

## 🧭 Provisioning Workflow

1. Log into the Qbank Admin Console  
2. Navigate to **Onboarder > New Hire**  
3. Enter employee details: name, role, department, manager  
4. Select provisioning profile (e.g., Developer, Support, Contractor)  
5. Review auto-assigned resources:
   - Email account
   - Slack invite
   - Jira, Confluence, GitHub access
   - VPN credentials

6. Click **Provision Now**

---

## 🧩 Manual Overrides

Use manual provisioning for:
- Contractors
- Interns
- Temporary access requests

---

## 📊 Diagram

![Provisioning Flow](../diagrams/provisioning.svg)

---

## 🧠 Notes

- Provisioning triggers are logged in the audit trail  
- Failed provisioning attempts generate alerts in Slack  
- Profiles can be customized via the Admin Console