import httpx
import logging
from configuration.constants import BASE_URL

logger = logging.getLogger(__name__)

async def set_light_state(state: bool) -> httpx.Response | None:
    try:
        async with httpx.AsyncClient() as client:
            url = f"{BASE_URL}/state"
            json_data = {"on": {"value": state}}
            response = await client.put(url, json=json_data)
            return response
    except httpx.HTTPError as exc:
        logger.error(f"HTTP error occurred: {exc}")
        return None
    except Exception as exc:
        logger.error(f"An error occurred: {exc}")
        return None


async def get_light_state() -> str | None:
    try:
        async with httpx.AsyncClient() as client:
            url = f"{BASE_URL}/state/on"
            response = await client.get(url)
            return response.json().get("value", None)
    except httpx.HTTPError as exc:
        logger.error(f"HTTP error occurred: {exc}")
        return None
    except Exception as exc:
        logger.error(f"An error occurred: {exc}")
        return None
