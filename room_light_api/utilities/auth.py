import httpx
import logging
from configuration.constants import ip_address
from configuration.constants import port_number

logger = logging.getLogger(__name__)

async def generate_auth_token() -> str:
    async with httpx.AsyncClient() as client:
        url = f"http://{ip_address}:{port_number}/api/v1/new"
        try:
            response = await client.post(url)
            return response.json().get("auth_token", "")
        except Exception as e:
            logger.error(f"Error generating auth token: {e}")
            return ""
