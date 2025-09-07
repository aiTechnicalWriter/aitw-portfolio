# Chatbot Onboarding Flow – Qbank Loan Assistant

This flow guides new users through the onboarding process via the Qbank chatbot, designed for mobile and desktop experiences.

---

## 👋 Welcome Message

**Trigger:** `start`  
**Bot Response:**  
> Welcome to Qbank! I’ll help you get started with your loan application. Ready to begin?

---

## 🧾 Collect Basic Info

**Trigger:** `begin`  
**Bot Response:**  
> Great. What’s your full name and email address?

---

## 🏠 Ask for Location

**Trigger:** `location`  
**Bot Response:**  
> Got it. What ZIP code are you applying from?

---

## 💰 Income Details

**Trigger:** `income`  
**Bot Response:**  
> Thanks. What’s your monthly income before taxes?

---

## 📎 Upload Documents

**Trigger:** `upload`  
**Bot Response:**  
> You can upload your documents here: [secure.qbank.com/upload](https://secure.qbank.com/upload)

---

## ✅ Confirmation

**Trigger:** `done`  
**Bot Response:**  
> You’re all set! Your application is now in review. I’ll notify you when there’s an update.

---

## 📎 Notes

- Flow is stored in `chatbot/onboarding-flow.md`  
- Bot uses session memory to track progress  
- All responses are optimized for mobile chat widgets