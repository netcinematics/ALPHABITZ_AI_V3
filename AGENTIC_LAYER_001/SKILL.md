## SKILL

Teach agents to use scripts. Custom tools - core four.
CONTEXT | MODEL | PROMPT | TOOLS.


Start the app - Stop the app.

### tools

- tools/start.py - start the app
- tools/stop.py - stop the app
- tools/restart.py - restart the app
- tools/reload.py - reload the app

### usage

```bash
# start
uv run .claude/skills/start/tools/start.py

# stop
uv run .claude/skills/stop/tools/stop.py

# restart
uv run .claude/skills/restart/tools/restart.py

# reload
uv run .claude/skills/reload/tools/reload.py
```