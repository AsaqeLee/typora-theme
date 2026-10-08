# Typora Theme

A clean light and dark theme for the [Typora](https://typora.io/) Markdown editor.

## Overview

This repository provides two CSS themes optimized for long-form writing and technical notes:

| Theme file | Appearance |
|------------|------------|
| `theme/my-theme.css` | Light |
| `theme/my-theme-dark.css` | Dark |

Supporting assets include code-highlight styles under `theme/` and preview images under `img/`.

## Features

- Readable typography for prose and headings
- Coordinated light and dark color palettes
- Code-block highlighting support
- Styling for common Markdown elements (tables, quotes, lists)
- Support for math formulas and other Typora-rendered constructs

## Requirements

- Typora (desktop)

## Installation

1. Clone or download this repository.
2. Open Typora → **Preferences** (Windows/Linux: **File → Preferences**; macOS: **Typora → Preferences**).
3. Open **Appearance → Open Theme Folder**.
4. Copy the contents of `theme/` (CSS files and any font folders) into the Typora theme folder.
5. Restart Typora.
6. Choose **my-theme** or **my-theme-dark** from the **Themes** menu.

## Preview

### Light

![Light theme preview](img/light-preview.png)

### Dark

![Dark theme preview](img/dark-preview.png)

## Customization

Edit the CSS files directly. Color and font variables are defined in the `:root` section of each theme file.

## Project layout

```text
typora-theme/
├── theme/
│   ├── my-theme.css
│   ├── my-theme-dark.css
│   └── code-highlight.css
├── img/                 # Preview screenshots
├── example.md           # Sample Markdown for visual checks
└── generate_preview.py  # Optional preview helper
```

## Status / limitations

Personal theme; visual details may differ slightly across Typora versions and operating systems.

## Example

See [`example.md`](example.md) for a sample document that exercises common Markdown elements under this theme.

## License

MIT. See [LICENSE](LICENSE).
