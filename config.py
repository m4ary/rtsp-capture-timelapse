# Telegram notifications
telegram_enabled = False  # master switch — set to True to enable Telegram notifications

telegram_bot_token = "your_bot_token"
telegram_chat_id = "your_chat_id"

telegram_notify_on_capture = True   # notify when a frame is captured successfully
telegram_notify_on_timelapse = True  # notify when a timelapse is created successfully

# Sunrise capture (uses the free Open-Meteo API — no API key needed)
sunrise_city = "Riyadh"            # city name used to look up sunrise time
sunrise_country_code = "SA"        # optional ISO country code to disambiguate the city ("" to ignore)
sunrise_capture_offset_minutes = 30  # minutes after sunrise to capture (negative = before sunrise)
sunrise_max_late_minutes = 10        # skip the day's capture if it would be more than this late (e.g. after a power cut)

# List of cameras with their credentials
# Each camera should have: name, ip_address, username, password
cameras = [
    {
        "name": "backyard",
        "ip_address": "192.168.1.10",
        "username": "admin",
        "password": "your_password",
        "rtsp_path": "/Streaming/Channels/101"  # The path after the IP address
    },
    {
        "name": "sideyard",
        "ip_address": "192.168.1.11",
        "username": "admin",
        "password": "your_password",
        "rtsp_path": "/Streaming/Channels/101"
    },
    {
        "name": "middleyard",
        "ip_address": "192.168.1.12",
        "username": "admin",
        "password": "your_password",
        "rtsp_path": "/h264Preview_01_main"
    }
]
