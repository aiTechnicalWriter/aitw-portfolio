# Docs-as-Code Deployment Workflow – Qbank

This document outlines Qbank’s docs-as-code workflow for publishing technical documentation using GitHub, Markdown, and automated CI/CD pipelines.

---

## 🧰 Tools & Stack

- **Authoring:** Markdown + Mermaid.js  
- **Version Control:** Git + GitHub  
- **CI/CD:** GitHub Actions  
- **Preview:** MkDocs (local and GitHub Pages)

---

## 🔄 Workflow Steps

1. Author content in Markdown  
2. Save diagrams as `.mmd` and export to `.svg`  
3. Commit changes to GitHub repo  
4. GitHub Actions triggers build and deploy  
5. Docs are published to GitHub Pages

---

## 🧠 Editorial Practices

- Use semantic headings (`#`, `##`, `###`)  
- Keep line length under 80 characters for readability  
- Include diagrams and screenshots for clarity  
- Write commit messages that reflect content changes

---

## 📊 Diagram

![Docs-as-Code Pipeline](../diagrams/docs-pipeline.svg)

---

## 🧪 Testing

- Preview locally with `mkdocs serve`  
- Validate links and image paths  
- Confirm diagram rendering and layout

---

## 📎 Notes

- All content is versioned and traceable  
- Markdown files are human-readable and Git-friendly  
- Diagrams are stored as source + export for transparency