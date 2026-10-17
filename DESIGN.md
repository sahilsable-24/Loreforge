# LOREFORGE DESIGN (filled Week 1 design days, then keep short)

Status: Sections 0-6 filled (Days 1-3). Tokens confirmed, contrast verified Day 3. UI code starts Day 8.
Visual reference: Claude design canvas "Loreforge: D&D Beyond x Stripe Press direction" + "Loreforge: final look preview" (hub + session).

## 0. Brand
- Name: Loreforge
- Wordmark: one word, capital L only, sturdy serif (Source Serif 4, 600), ember dot after the word in the logo only. No logo mark until Week 8.
- Idea: lore is written (ink, paper), forge is made (iron, heat). Palette is ink-dark, paper-light, ember for action, brass for trim.

## 1. Product feel
- 3 adjectives: Inked (text-first, high contrast), Sturdy (clear structure, solid borders), Candlelit (warm, low-glare, dark-first)
- Direction: DARK-FIRST and art-led like D&D Beyond; paper-colored editorial bands for reading, like Stripe Press.
- References:
  - D&D Beyond: dark moody page, black top bar, big art cards with small-caps eyebrow + huge serif title, brass outline buttons, arched portrait frame with name plate, ability score tiles, tan name chips. Avoid: heavy red branding, upsell clutter, ornate frames.
  - Stripe Press: editorial serif, comfortable reading width, a real 3D rulebook you can drag to rotate. Avoid: sparse gallery layout (we need app density).
  - Linear: quiet dense lists and tables, restrained accent. Avoid: cold blue-grey mood.
- Art sourcing (free): users upload their own portraits and campaign covers; default art = public-domain paintings (Met Open Access, CC0) darkened under a scrim. No stock dragons, no clip-art.

## 2. Color (dark-first; light = "paper")
| Role | Dark (ink, default) | Light (paper) |
|---|---|---|
| bg | #16130F | #F6F1E7 |
| top bar | #0D0B08 | #0D0B08 |
| surface | #1F1B16 | #FFFDF8 |
| border | #3A332A | #D9CFBC |
| text | #EDE6D8 | #1F1B16 |
| text-muted | #A99F8E | #6B6254 |
| primary (ember, actions) | #E0763A | #B5471B |
| brass (trim: frames, outline buttons) | #C9A24B | #85641B |
| success | #7DB377 | #3F6B3A |
| warning | #E0A537 | #8F5F10 |
| danger | #E5675F | #B3322B |
- Rules: ember = actions and status accents; brass = frames and borders only, never body text; status always has icon + label, never color alone. Text on ember: ink on dark mode, paper on light mode.
- Contrast: all pairs verified Day 3 (text 4.5:1+, borders/shapes 3:1+). Only change: light success #4F7F4A -> #3F6B3A (was 4.18, now 5.53).
- Why: warm neutrals keep it Candlelit; ember and brass are the only loud colors, each with one job.

## 3. Typography
- Fonts (2): Source Serif 4 (headings, display, eyebrows, editorial text, AI game master replies), IBM Plex Sans (UI, body, tables). tabular-nums on for stats.
- Scale (px): 12 / 14 / 16 / 18 / 20 / 24 / 32 / 40 / 48 / 64. Base 16. Editorial serif text 18.
- Eyebrow: serif 600, 13px, uppercase, letter-spacing .08em.
- Weights: 400 body, 500 labels and buttons, 600 serif only. Nothing heavier.

## 4. Tokens (confirmed Day 3)
- Spacing: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64
- Radius: 4 chips, 6 buttons and panels, 8 cards, arch (half-width top radius) for character portraits only
- Shadows: none, except a soft contact shadow under the 3D book and the focus ring
- Borders: 1px default, brass 2px on the portrait arch
- Focus ring: 2px ember, 2px offset, on every interactive element
- Motion: the lore library rulebook is a 3D book (CSS 3D): slow idle spin, drag to rotate, off with reduced motion. No other decorative animation.

## 5. Key screens (wireframes done Day 3)
Shared patterns: any list = dense Linear-style row list; any hero = art card. Every screen: skeleton while loading, "Couldn't load X. Retry" on error, empty = invitation + one ember button.
- [x] Login: wordmark, email, password, ember Sign in, register link. Error under form (icon + text). Mobile: card fills width.
- [x] Guild / campaign hub: top bar, eyebrow + serif title, art cards grid, arch portrait + name plate, ember New campaign. Empty: "Start your first campaign". Mobile: one column.
- [x] Session screen: chat with AI GM (serif replies, citation chips, dice result), party panel (HP bar + status icon/label), approval-pending notice, input row. Empty: "Say what your character does". Mobile: party becomes bottom drawer.
- [x] Character sheet: arch portrait, name/class/HP, 6 ability tiles, inventory + quests with ember section rules. Empty: "No characters yet". Mobile: tiles 2 per row.
- [x] DM approval queue: rows with action, risk label, Approve (ember) / Reject; row opens what the AI wants and why. Empty: "Nothing waiting for you". Mobile: buttons below row.
- [x] Lore and rulebook library: 3D book, upload area, shelf rows (file, status icon + label, pages), citations view. Empty: "Upload your first rulebook". Mobile: book hidden, list only.
- [x] Admin analytics + audit log: 3 stat tiles, usage per campaign chart, audit rows (time, actor, AI decision, trace link). Empty: "No usage yet". Mobile: stats stack, table scrolls sideways.
- [x] Settings: tabs (Profile, Guild, Members, Theme), form fields, members list with roles, Save changes. Mobile: tabs become a dropdown.

## 6. Anti "AI-look" checklist
- [x] No default purple-blue gradients
- [x] No generic glassmorphism
- [x] No emoji as icons (one icon set: Lucide)
- [x] Fantasy theme is restrained: no clip-art, readable body font, brass frames thin and only on portraits and key panels
- [ ] shadcn/Tailwind defaults customized (Day 8)
- [x] Real copy, no lorem ipsum or "future of X" slogans
- [ ] Loading, empty, error states on every screen (designed, verify in code)
- [ ] Mobile-responsive (designed, verify in code)