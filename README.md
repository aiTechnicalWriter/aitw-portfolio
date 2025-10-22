# aiTechnicalWriter Portfolio

Welcome to my modular documentation portfolio, built with MkDocs and structured for reuse, clarity, and scalability. This site showcases my expertise in technical writing, content architecture, and Docs-as-Code workflows.

## 🔧 What’s Inside

- **Style Guide**: Modular standards for voice, terminology, error messaging, and content types.
- **API Docs**: Conceptual guides and quickstarts for developer onboarding.
- **User Guide**: Tutorials and reference topics for end users.
- **Strategy**: Roadmaps, metrics, and excerpts that reflect documentation maturity.
- **Projects**: Real-world examples like Fraud Detection AI, showing applied writing and UX empathy.
- **Architecture**: C4 model diagrams and structural thinking.

## 🧩 Modular Authoring

This portfolio uses `!include` syntax to embed reusable fragments from the `includes/` folder. Topics are structured for DITA-style reuse and wired into `mkdocs.yml` for clean navigation.

## 🚀 Goals

- Demonstrate customer-centric, scalable documentation practices.
- Showcase structured authoring and modular reuse.
- Align with roles like Technical Writer, Content Architect, or UX Documentation Lead.

> Built with ❤️ using MkDocs, GitHub, and a passion for clarity.


# More

## 📘 Portfolio Overview: Modular Docs-as-Code with DITA-Inspired Structure

This portfolio demonstrates a modern, maintainable Docs-as-Code workflow built with MkDocs and Python macros. It showcases modular content architecture, semantic front matter, and reusable Markdown includes — all inspired by DITA principles and adapted for Markdown-based publishing.

### ✅ Key Features

- **Modular Topic Structure**  
  Each guide, concept, and reference is authored as a standalone Markdown file, following DITA-style granularity. This enables reuse, clarity, and future-proof scalability.

- **Reusable Includes via Macros**  
  Shared content (e.g., lifecycle explanations, error patterns, terminology) is stored in `docs/includes/` and injected dynamically using a custom `read_file()` macro powered by `mkdocs-macros-plugin`.

- **Semantic Metadata**  
  Each topic includes structured front matter (`title`, `topic-type`, `audience`, `last-updated`) to support filtering, transformation, and automated indexing.

- **Step-by-Step Validation Discipline**  
  Every modular refactor is validated incrementally to ensure rendering integrity and maintain authoring confidence. This mirrors the rigor of traditional DITA workflows.

- **Cross-Platform Compatibility**  
  The system is designed to support dual-use content strategies, enabling future export to DITA, Flare, or other structured formats if needed.

### 🧠 Why It Matters

This approach reflects industry best practices in technical communication:
- It aligns with modular authoring standards used in DITA, MadCap Flare, and Oxygen XML
- It supports single-source publishing and content reuse
- It demonstrates fluency in Docs-as-Code tooling, automation, and semantic structuring

Whether you're reviewing this portfolio as a hiring manager, peer, or collaborator, you'll find a system that’s not just functional — but thoughtfully engineered for clarity, maintainability, and scale.


# Summary:

This portfolio demonstrates a modern technical writing workflow using Docs-as-Code principles. It’s built with MkDocs and enhanced by a custom macro system that enables reusable content, semantic structuring, and modular authoring. Inspired by DITA best practices, each guide is broken into maintainable components that can be reused across documents. The system supports single-source publishing, step-by-step validation, and future scalability — all while staying readable, lightweight, and version-controlled. It reflects how experienced technical writers work today: modular, semantic, and automation-ready.


# QBank Documentation Style Guide

This repository contains a modular, reusable style guide for QBank documentation, authored using Docs-as-Code principles and structured authoring techniques inspired by DITA.

## Overview

The style guide is organized into standalone Markdown topics, each focused on a specific aspect of writing and formatting technical documentation. These topics are designed for reuse, clarity, and scalability across multiple documentation projects.

## Features

- ✅ Modular topic files for code, syntax, formatting, and best practices  
- ✅ Parent guide page with linked topics for easy navigation  
- ✅ Integrated into MkDocs site structure  
- ✅ Follows Docs-as-Code best practices  
- ✅ Ready for transclusion, reuse, and automation  
- ✅ Authored with structured authoring mindset (DITA-inspired)

## Navigation

The guide is accessible via the MkDocs sidebar under:

```
Style Guide > Code & Syntax Guide
```

Or directly via: [`docs/style-guide/code-syntax-guide.md`](docs/style-guide/code-syntax-guide.md)

## Technologies Used

- [MkDocs](https://www.mkdocs.org/) for static site generation  
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for enhanced styling and navigation  
- Markdown for modular topic authoring  
- GitHub for version control and collaboration

## Authoring Philosophy

This project reflects a shift from traditional documentation to modular, structured authoring. Each topic is scoped, reusable, and semantically clear—mirroring DITA’s topic-based architecture while remaining lightweight and Markdown-native.

## License

This project is open-source and available under the MIT License.