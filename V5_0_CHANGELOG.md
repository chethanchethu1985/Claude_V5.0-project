# Version 5.0 (upgrade from 4.2.1)
versionName 5.0, versionCode 8. Same app ID and the same signing key as 4.2 and 4.2.1, so it installs over them and keeps your data.

## Bugs fixed
1. Top "Start" button opened breathing instead of the warm-up. Cause: the plan began with the "before the workout" breathing item. The plan order is now warm-up first, then the "before" breathing, then the main workout, stretching, "after" breathing and cardio. Plans already saved on the phone are re-ordered automatically. (Sundays have no warm-up, so Start there still begins with breathing, as in the PDF.)
2. Voice cues played only as ticks. Cause: Android's web view often has no speech engine. The app now uses the phone's own text-to-speech through a small native plugin, with the browser voice and then ticks as fall-backs. More > Voice > Test voice shows what is used. Needs a rebuild (native code changed).

## Workout Library
- Every category is visible at once (All, Chest, Back, Shoulders, Legs, Arms, Core, Yoga, Cardio, Stretching, Breathing) instead of a hidden sideways list.
- "Mine" removed from the filters.
- Delete any workout (Delete button when a workout is expanded). Built-in workouts are hidden from the library only, the 8-week plan keeps them; Show > Deleted lists them and Restore brings them back. Your own workouts are removed completely.

## Redesign for less scrolling
- Bottom navigation: Today, Calendar, Library, Progress, More. Plan, Yoga, Cardio and Health live under More (tiles) with a "< More" back link.
- Segmented tabs inside long screens: Plan (Edit, Add, Saved, Bulk plan), Yoga/Cardio (Run, Add, Edit), Progress (Summary, History, Health), Health (Add, Trends, Records), Calendar (Day, Weeks).
- Plan editor: exercises are compact rows grouped by section; tap a row to edit it.
- Today: slimmer dashboard with one Start workout button and Move / swap.
- Calendar: a short day summary (with an "All exercises" fold-out) instead of a 30-row table.
- More: tools plus folded sections (Voice, Backup, Programme guide, Workout timing, Other apps).
- Colours, splash screen and icon are unchanged.

## Planning after the programme
- Plan > Bulk plan: choose a start date and number of weeks (1 to 52), then repeat the 8-week programme (from any week), copy one programme week, or build your own weekly pattern from saved plans. A preview shows how many sessions will be added; days that already have a plan are kept unless you tick "Replace". "Remove bulk-planned days" undoes it. History is never touched.
- When the programme ends, Today offers "Plan your next weeks"; the dashboard looks up to 400 days ahead for the next workout.

## Version label
V5.0 chip on the "My Workouts" line, "Version 5.0" on the splash, versionName 5.0.
