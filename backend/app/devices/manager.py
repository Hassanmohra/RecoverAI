from typing import Dict, List

class DeviceManager:
    """Manage devices discovered during the current RecoverAI session."""
    def __init__(self) -> None:
        self.devices: List[Dict] = []
    def list_devices(self) -> List[Dict]:
        return self.devices
    def add_device(self, device_id: str, device_type: str, name: str = "Unknown Device") -> Dict:
        device = {"device_id": device_id, "type": device_type, "name": name, "status": "connected"}
        self.devices.append(device)
        return device
    def clear_devices(self) -> None:
        self.devices.clear()

device_manager = DeviceManager()
