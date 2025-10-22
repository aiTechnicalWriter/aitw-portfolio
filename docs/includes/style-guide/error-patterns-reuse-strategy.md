## Error Messaging Reuse Strategy

Modular error messages improve consistency, reduce duplication, and simplify localization. Use shared patterns and terminology across platforms and contexts.

- **Centralize reusable fragments** in the `includes` folder for common error types (e.g., validation, connectivity).
- **Reference terminology** from `ui-terminology.md` to align with platform standards.
- **Avoid hardcoding** platform-specific details unless necessary; use conditional phrasing when reuse is intended.
- **Document rationale** for reuse decisions in the style guide to support onboarding and governance.

> Example: Instead of writing “Your mobile app session expired,” use “Your session expired” and let the UI context clarify the platform.
