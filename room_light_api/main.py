from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from utilities.light_status import set_light_state
from utilities.light_status import get_light_state


app = FastAPI()


@app.post("/lights/{command}", operation_id="change_light_state")
async def change_light_state(command: str):
    if command.lower() not in ["on", "off"]:
        return {"error": "Invalid state. Use 'on' or 'off'."}
    # Here you would add code to actually control the lights
    if command.lower() == "on" and (await get_light_state()) is False:
        await set_light_state(True)
    elif command.lower() == "off" and (await get_light_state()) is True:
        await set_light_state(False)
    else:
        return {"message": f"Lights are already {command.lower()}"}
    return {"message": f"Lights turned {command.lower()}"}


if __name__ == "__main__":
    mcp = FastApiMCP(app, include_operations=["change_light_state"])
    mcp.mount()
