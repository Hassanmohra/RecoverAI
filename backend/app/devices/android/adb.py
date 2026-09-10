import subprocess
from typing import Dict, List

def detect_android_devices() -> List[Dict]:
    """Detect Android devices through an authorized ADB connection."""
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=10, check=False)
    except FileNotFoundError:
        return [{"status": "error", "message": "ADB is not installed or not available."}]
    except subprocess.TimeoutExpired:
        return [{"status": "error", "message": "ADB command timed out."}]
    if result.returncode != 0:
        return [{"status": "error", "message": result.stderr.strip() or "ADB command failed."}]
    devices: List[Dict] = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line or line.startswith("List of devices"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            devices.append({"device_id": parts[0], "status": parts[1], "type": "android"})
    return devices
