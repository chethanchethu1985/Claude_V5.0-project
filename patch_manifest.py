# Adds the permissions and the text-to-speech lookup this app needs to the generated Android manifest.
import re
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
perms = (
    '    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />\n'
    '    <uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE" />\n'
    '    <uses-permission android:name="android.permission.VIBRATE" />\n'
)
if "MANAGE_EXTERNAL_STORAGE" not in s:
    assert "<application" in s
    s = s.replace("<application", perms + "    <application", 1)
# Android 11+ only lets an app see the voice engine if the manifest says so.
if "android.intent.action.TTS_SERVICE" not in s:
    queries = (
        "\n    <queries>\n"
        "        <intent>\n"
        '            <action android:name="android.intent.action.TTS_SERVICE" />\n'
        "        </intent>\n"
        "    </queries>\n"
    )
    s, n = re.subn(r"(<manifest[^>]*>)", lambda m: m.group(1) + queries, s, count=1)
    assert n == 1
open(p, "w", encoding="utf-8").write(s)
print("Manifest patched")
