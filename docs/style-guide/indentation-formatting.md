## Indentation & Formatting

Markdown ignores leading spaces in regular paragraphs. To simulate indentation or control spacing, use HTML elements or non-breaking spaces.

✅ Techniques:

- Use `&nbsp;` (non-breaking space) for manual indentation.  
- Use inline HTML for styled indentation when semantic spacing is needed.

✅ Example:

```html
<p style="text-indent: 2em;">This paragraph is indented using HTML styling.</p>
```

💡 Tip: Avoid using tabs or multiple spaces for layout—they may be collapsed or ignored by Markdown renderers. Use HTML only when semantic spacing is required and supported by your theme.
