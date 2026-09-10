from fastapi import APIRouter

from app.devices.manager import device_manager

router = APIRouter(
    prefix="/api/devices",
    tags=["Devices"],
)


@router.get("/")
async def list_devices():
    return {
        "status": "success",
        "devices": device_manager.list_devices(),
    }
