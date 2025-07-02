import subprocess

try:
    print("🔰 Starting PRIMARY tracker...")
    subprocess.run(["python", "tracker_primary.py"], check=True)
except Exception as e:
    print("⚠️ PRIMARY tracker failed:", e)
    print("🔁 Switching to FALLBACK tracker...")
    subprocess.run(["python", "tracker_fallback.py"])