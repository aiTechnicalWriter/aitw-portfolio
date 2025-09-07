# Internal Chatbot Snippets – Qbank Ops Bot

These snippets are used by Qbank’s internal Slack bot to assist support and IT teams with quick answers and automation triggers.

---

## 🔧 Reset VPN Credentials

**Trigger:** `reset vpn`  
**Bot Response:**  
> Sure. I’ve sent a reset link to your Qbank email. If you don’t see it in 2 minutes, type `vpn help`.

---

## 🧠 Check System Health

**Trigger:** `status check`  
**Bot Response:**  
> All systems are operational. Kafka latency is under 50ms. MongoDB replication is healthy.  
> Type `logs` to view recent alerts.

---

## 🛠️ Restart Microservice

**Trigger:** `restart service <name>`  
**Bot Response:**  
> Restarting `<name>` now. You’ll get a confirmation in Slack once it’s back online.

---

## 📎 Notes

- All snippets are stored in `chatbot/internal-snippets.md`  
- Bot uses regex matching and role-based access control  
- Responses are editable via the Admin Console