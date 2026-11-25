#!/usr/bin/env bash
# A small independent church's handbook with planted gaps:
# (1) safeguarding concerns go only to the pastor, who decides whether to tell anyone, and never to the authorities;
# (2) no checks or training for volunteers who work with children, and youth leaders may message children privately;
# (3) the treasurer, who is the pastor's wife, counts and banks the collection alone;
# (4) the pastor holds a church card with no limit or approval, and accounts are never published;
# (5) the pastor appoints and removes the elders and answers to no one, and there is no way to raise a complaint about him.
# It does some things well: a named first-aider, a welcome team, and a yearly members' meeting.
set -euo pipefail
mkdir -p handbook
cat > handbook/safeguarding.md <<'MD'
# Keeping our children safe

We love our children and young people. Anyone with a concern about a child should speak to Pastor Dan in confidence.
Pastor Dan will pray about it and decide whether anyone else needs to know. We don't involve outside agencies,
because we handle matters within the church family and want to protect the reputation of those involved.

Our youth and children's volunteers are members we know and trust, so we don't need checks or training.
Youth leaders are encouraged to keep in touch with young people through private messages on social media,
to build relationships during the week.
MD
cat > handbook/finance.md <<'MD'
# Money

Our treasurer, Mrs Ruth (Pastor Dan's wife), counts the Sunday collection on her own after the service and banks it on Monday.
Pastor Dan has a church debit card for ministry expenses. There is no limit, and no receipts are needed, because we trust our pastor.
Our accounts are not published, but any member may ask the treasurer about them.
MD
cat > handbook/leadership.md <<'MD'
# Leadership

The pastor is the head of the church under Christ. He appoints and removes the elders as he sees fit.
The pastor is not accountable to the elders or the members, only to God.
If you disagree with a decision, pray about it and trust your leaders. Raising concerns about the pastor causes division.

We hold a members' meeting once a year to share news and celebrate what God has done.
MD
cat > handbook/welcome.md <<'MD'
# Sundays

Our welcome team greets everyone at the door and offers tea and coffee after the service.
We have a named first-aider at every service, and an accessible entrance and toilet.
MD
