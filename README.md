portfolio/ ├── README.md ├── .gitignore ├── docs/ │   ├── markdown/           # Human-polished Markdown docs │   ├── diagrams/           # Mermaid source files (.mmd) │   ├── images/             # Branded screenshots and logo ├── dita/ │   ├── topics/             # DITA XML topic files │   ├── maps/               # DITA map for Flare publishing ├── chatbot/ │   ├── internal-snippets.md │   ├── customer-snippets.md │   ├── onboarding-flow.md

---

## 📄 Documentation Highlights

### Markdown Portfolio (`/docs/markdown`)
- API authentication guide
- Mobile app transfer walkthrough
- Ops Console architecture overview
- Loan Portal release notes
- Onboarder provisioning runbook
- Docs-as-code deployment workflow
- Annotated rewrite sample

### DITA XML Portfolio (`/dita/topics`)
- Modular topic files for MadCap Flare
- Conditional publishing support (`audience="internal"` / `"customer"`)
- Branded diagrams embedded as SVGs

### Diagrams (`/docs/diagrams`)
- Mermaid-authored diagrams exported to SVG
- Includes token flow, user journeys, CI/CD pipelines, and system architecture

### Chatbot Content (`/chatbot`)
- Internal support bot snippets (Slack/Teams)
- Customer-facing assistant flows (mobile/web)
- Full onboarding simulation

---

## 🚀 Deployment Options

### GitHub Pages (Markdown)
To preview the Markdown docs as a live site:
1. Install [MkDocs](https://www.mkdocs.org/)
2. Add a `mkdocs.yml` file
3. Deploy via GitHub Actions or GitHub Pages

### MadCap Flare (DITA)
Import `/dita/` into Flare and configure outputs for:
- Responsive HTML5
- Print-ready PDFs
- Chatbot content filtering via conditional attributes

---

## 🧰 Tools Used

- Markdown + Mermaid.js  
- DITA XML + MadCap Flare  
- GitHub Actions  
- MkDocs (optional for live preview)  
- VS Code for editing and previewing

---

## 👤 Author

**John Stonecypher**  
Senior Technical Writer & AI Specialist  
Northglenn, CO  
[LinkedIn] | [Portfolio Site] | [Email]

---

## 📎 License

This portfolio is for demonstration purposes only. All content is fictional and created for illustrative use.


