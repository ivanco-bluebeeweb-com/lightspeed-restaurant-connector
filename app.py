"""Extension declaration, capabilities, health check for Lightspeed Restaurant Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "lightspeed-restaurant-connector",
    version="0.1.0",
    display_name="Lightspeed Restaurant",
    icon="icon.svg",
    capabilities=["lightspeed_restaurant:manage"],
    description="Official Imperal connector for Lightspeed Restaurant (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("lightspeed_restaurant_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Lightspeed Restaurant connection(s) configured." if count else "Not connected yet."
    }
