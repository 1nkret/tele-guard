import psutil


def battery_status():
    battery = psutil.sensors_battery()
    result = str()

    if battery:
        result += f"\nBattery: {battery.percent}%  "

        if battery.power_plugged:
            result += "🔌⚡"
        else:
            result += "🔋"

    return result
