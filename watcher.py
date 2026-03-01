# AI Employee Vault Watcher
# Monitors the Inbox\ folder every 30 seconds for new .md files.
# When found, moves them to Needs_Action\ and logs the event to watcher.log.

import os
import shutil
import time
from datetime import datetime

VAULT_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_DIR = os.path.join(VAULT_DIR, "Inbox")
NEEDS_ACTION_DIR = os.path.join(VAULT_DIR, "Needs_Action")
LOG_FILE = os.path.join(VAULT_DIR, "watcher.log")
SCAN_INTERVAL = 30  # seconds


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def scan_inbox():
    try:
        files = [f for f in os.listdir(INBOX_DIR) if f.endswith(".md")]
    except OSError as e:
        print(f"[WATCHER] ERROR reading Inbox: {e}")
        log(f"ERROR reading Inbox: {e}")
        return

    if not files:
        print("[WATCHER] Scanning Inbox... nothing new")
        return

    for filename in files:
        src = os.path.join(INBOX_DIR, filename)
        dst = os.path.join(NEEDS_ACTION_DIR, filename)
        try:
            print(f"[WATCHER] New file detected: {filename}")
            shutil.move(src, dst)
            print(f"[WATCHER] Moved {filename} to Needs_Action\\")
            log(f"Moved {filename} from Inbox to Needs_Action")
        except OSError as e:
            print(f"[WATCHER] ERROR moving {filename}: {e}")
            log(f"ERROR moving {filename}: {e}")


def main():
    print(f"[WATCHER] Starting. Vault: {VAULT_DIR}")
    print(f"[WATCHER] Scanning every {SCAN_INTERVAL} seconds. Press Ctrl+C to stop.\n")
    log("Watcher started.")

    while True:
        scan_inbox()
        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[WATCHER] Stopped by user.")
        log("Watcher stopped by user.")
