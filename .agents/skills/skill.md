---
name: bakerydemo-theme-qa
description: Run repeatable Bakerydemo UI QA checks for theme toggle behavior, localStorage persistence, mobile breakpoints, desktop zoom, RTL and multilingual smoke checks, and generate concise PR-ready QA notes. Use for UI/theme/layout PRs.
---

Use this checklist to run Bakerydemo UI QA for theme-related changes and produce a PR-ready summary.

# Bakerydemo QA Checklist

## Theme
- [ ] Toggle Light <-> Dark works.
- [ ] Theme persists after reload.
- [ ] Hero/card text remains readable in both modes.

## Responsive + Zoom
- [ ] 320px: no clipped critical text/buttons.
- [ ] 375px: nav/search/toggle usable.
- [ ] 768px: layout stable.
- [ ] Desktop: normal layout.
- [ ] Desktop zoom 125%: no major overflow/wrap bugs.
- [ ] Desktop zoom 150%: no clipped text in nav/header/search.

## i18n + RTL
- [ ] One translated page loads correctly.
- [ ] One RTL page loads correctly.
- [ ] No major alignment/overflow breakage in RTL.

## Core Routes
- [ ] `/` returns expected page.
- [ ] `/blog/` returns expected page.
- [ ] `/search/` works with a basic query.
- [ ] Unknown URL returns expected 404 page.

## PR Note Template
- Scope:
- Checks run:
- Pass/Fail:
- Screenshots/Video:
- Known limitations: