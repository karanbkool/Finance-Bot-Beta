"""Emit should_post=true/false to GITHUB_OUTPUT depending on whether it's
currently ~6:30 AM America/New_York.

GitHub Actions cron runs in UTC and doesn't shift for daylight saving, so the
workflow schedules two cron triggers (one for EDT, one for EST) and this
script lets only the one that actually lands at 6:30 AM local time post.

This always exits 0: skipping is expected, routine behavior for the cron
entry that doesn't match local time on a given day, not a failure, so it
must never fail the job (a nonzero exit here would mark the run "failed"
and trigger a GitHub failure-notification email for a no-op skip).
"""
import os
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("America/New_York"))
should_post = now.hour == 6 and 25 <= now.minute <= 35

print(f"Current America/New_York time is {now.strftime('%H:%M')}. should_post={should_post}")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"should_post={'true' if should_post else 'false'}\n")
