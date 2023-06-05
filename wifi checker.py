import psutil


def is_wifi_connected():
    interfaces = psutil.net_if_stats()
    for interface, stats in interfaces.items():
        if stats.isup and "wireless" in interface.lower():
            return True
    return False


if is_wifi_connected():
    print("Device is connected through Wi-Fi.")
else:
    print("Device is not connected through Wi-Fi.")
