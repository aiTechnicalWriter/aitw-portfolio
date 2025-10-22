---
title: Localization & Accessibility Guidelines for Error Messaging
topic-type: reference
audience: technical writers, UX designers, developers
last-updated: 2025-09-29
---

## Localization & Accessibility

Design error messages to be inclusive, translatable, and accessible to all users.

### Localization Tips

- Use plain language that can be easily translated.
- Avoid idioms, cultural references, or humor that may not localize well.
- Keep sentence structure simple and consistent.

### Accessibility Tips

- Ensure screen readers can access error messages.
- Use semantic HTML elements (e.g., `aria-live`, `role="alert"`).
- Don’t rely on color alone to convey meaning—use icons, text, or patterns.
- Place error messages near the relevant input field or action.

### Example

```html
<div role="alert" aria-live="assertive">
  Upload failed. The file exceeds the 10MB limit.
</div>
```