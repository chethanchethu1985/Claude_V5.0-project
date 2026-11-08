# Version 5.0 test report
Desktop browser (headless Chromium) only. No APK built, nothing run on a phone. Native Android code (voice, folder picker) was only syntax-checked against stand-in classes; the manifest patch was run on a sample manifest.
| Area | Status | Evidence |
|---|---|---|
| Top Start opens the warm-up; plans re-ordered; old saved order repaired | PASS (browser) | first item is a warm-up on all 48 training days; reorder test |
| Voice: native plugin used, fall-back when plugin missing, voice off, no engine, no start-up crash | PASS (mock plugin) | calls observed; start-up with an Android-like page has no errors |
| Voice actually audible on a phone | NOT TESTED | needs the rebuilt app |
| Library: all 10 categories visible, no Mine, delete built-in and custom, deleted list, restore, plan keeps exercise, backup keeps deleted list | PASS (browser) | |
| Bulk planner: repeat, copy, own pattern, preview counts, apply, remove, replace option | PASS (browser) | 14 sessions added and removed; pattern preview |
| Bottom navigation, More tiles, back link, segmented tabs, accordions | PASS (browser) | |
| Plan editor grouped rows, tap to edit, stays open while editing | PASS (browser) | |
| Calendar day summary and weeks tab | PASS (browser) | |
| Earlier features: dates, migration, superset rests, Excel optional columns, health, projected HbA1c, YouTube preview, move/swap, backup/restore, folder flows (mock), back/redo, splash | PASS (browser) | re-run on 5.0 |
| No sideways scrolling at 360, 412, 768 px on every screen and tab (320 px on Plan) | PASS (browser) | |
| App name, icon, install over 4.2.1, native voice, folder picker | NOT TESTED | needs the GitHub build and install |
