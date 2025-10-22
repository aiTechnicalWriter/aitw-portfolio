---
title: Error Messaging Guidelines
topic-type: concept
audience: technical writers, UX designers, developers
last-updated: 2025-09-29
related-topics:
  - style-guide/ui-terminology.md
  - style-guide/voice-and-tone.md
  - style-guide/code-syntax-guide.md
---

# Error Messaging Guidelines

Clear, actionable error messages help users recover quickly and build trust in the product. This guide defines best practices for writing effective error messages across UI, API, and CLI contexts.

## What Is an Error Message?

An error message communicates that something has gone wrong and guides the user toward resolution. It may appear in a dialog, toast, inline field, or log output.

## Principles of Effective Error Messaging

!include "includes/error-principles.md"

## Structure Template

```text
[What happened] + [Why it happened] + [What to do next]

### Example
Upload failed. The file exceeds the 10MB limit. Please compress the file or choose a smaller one.
```

## Common Patterns

!include "includes/error-patterns-validation.md"
!include "includes/error-patterns-auth.md"
!include "includes/error-patterns-connectivity.md"
!include "includes/error-patterns-upload.md"
!include "includes/error-patterns-system.md"

## Localization & Accessibility

!include "includes/error-localization-accessibility.md"

## Do & Don’t Table

!include "includes/error-do-dont.md"

## Reuse Strategy & Platform Notes

To ensure consistency across platforms and reduce duplication, reuse modular error messaging components wherever possible. Reference shared terminology, patterns, and principles from the includes folder.

!include "includes/error-patterns-reuse-strategy.md"
!include "includes/error-platform-notes.md"
