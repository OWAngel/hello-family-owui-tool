# hello-family-owui-tool

Minimal FastAPI OpenAPI tool for Family AI Open WebUI GitHub self-install smoke tests.

## Layout
- `server.py` — FastAPI app with `echo_message`
- `openapi.json` — OpenAPI 3 spec
- `requirements.txt` — Python deps

## Run
```bash
pip install -r requirements.txt
TOOL_PORT=28901 python server.py
```
