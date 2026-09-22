"""Exit non-zero unless it's currently ~6:30 AM America/New_York.

GitHub Actions cron runs in UTC and doesn't shift for daylight saving, so the
workflow schedules two cron triggers (one for EDT, one for EST) and this
guard lets only the one that actually lands at 6:30 AM local time proceed.
"""
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("America/New_York"))
if now.hour == 6 and 25 <= now.minute <= 35:
    sys.exit(0)

print(f"Skipping: current America/New_York time is {now.strftime('%H:%M')}, not ~6:30 AM.")
sys.exit(1)
