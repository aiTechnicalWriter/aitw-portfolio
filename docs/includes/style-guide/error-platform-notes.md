## Platform-Specific Error Messaging Notes

While reuse is ideal, some error messages must be tailored to the platform’s interaction model and user expectations.

- **Web UI**: Prioritize clarity and brevity. Inline errors should be scannable and avoid technical jargon.
- **Mobile**: Use concise language and avoid multi-step instructions. Consider limited screen space and touch interaction.
- **CLI**: Provide detailed context and actionable steps. Include error codes and log references when appropriate.
- **API**: Structure messages for machine readability. Include status codes, error types, and resolution hints in the response body.

> Tip: When customizing for a platform, retain core terminology and structure to preserve consistency across surfaces.
