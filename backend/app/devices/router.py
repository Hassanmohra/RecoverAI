from fastapi import APIRouter
from app.devices.android.adb import detect_android_devices
from app.devices.manager import device_manager

router = APIRouter(prefix="/api/devices", tags=["Devices"])

@router.get("")
async def list_devices():
    return {"status": "success", "devices": device_manager.list_devices()}

@router.get("/android")
async def list_android_devices():
    return {"status": "success", "devices": detect_android_devices()}
