# Network Speed Monitor - NVDA Add-on

## Description

An NVDA add-on that allows you to quickly check current download and upload speeds for all network interfaces.

## Features

- Real-time monitoring of download and upload speeds
- Automatic speed formatting (kbps for values below 1024 kbps, Mbps for higher values)
- Monitors traffic across all network interfaces simultaneously
- Simple keyboard shortcuts for quick speed checking
- Alternative display in bytes per second (KB/s, MB/s)

## Requirements

- NVDA version 2019.3 or newer
- Python (built into NVDA)
- `psutil` library (installation instructions below)

## Installation

### Step 1: Installing the psutil library

The add-on requires the `psutil` library to monitor network statistics. To install it:

1. Open the NVDA Python console:
   - Press NVDA+Control+Z (opens Python console)

2. In the console, enter the following commands:
   ```python
   import os
   import subprocess
   import sys

   # Get NVDA's Python path
   python_exe = sys.executable

   # Install psutil
   subprocess.check_call([python_exe, "-m", "pip", "install", "psutil"])
   ```

### Step 2: Installing the add-on

1. Run the `.nvda-addon` file - NVDA will automatically install the add-on
2. Restart NVDA

## Usage

After installing the add-on, you can use the following default keyboard shortcuts:

- **NVDA+Shift+N** - Announces current download and upload speed in kbps/Mbps (bits - network standard)
- **NVDA+Shift+Control+N** - Announces current download and upload speed in KB/s/MB/s (bytes - file download format)

### Changing keyboard shortcuts

You can change the default keyboard shortcuts in NVDA settings:

1. Open the NVDA menu (NVDA+N)
2. Select "Preferences" > "Input Gestures"
3. Find "Network Speed Monitor"
4. Select the function you want to change
5. Press "Add" or "Remove" to customize your keyboard shortcuts

### Example announcements:

- "Download: 125.5 kbps, Upload: 45.2 kbps"
- "Download: 5.23 Mbps, Upload: 1.15 Mbps"
- "Download: 1.31 MB/s, Upload: 287.5 KB/s"

## Technical notes

- The add-on monitors traffic across all active network interfaces (Ethernet, Wi-Fi, VPN, etc.)
- Speed measurement is calculated as the difference in transmitted/received bytes between consecutive invocations
- On first invocation after NVDA starts, there may be a brief delay during measurement initialization

## License

GPL v2

## Author

Michał Dziwisz

## Version History

### Version 1.0.0
- Initial release
- Basic download and upload speed monitoring
- Automatic kbps/Mbps and KB/s/MB/s formatting
- Keyboard shortcuts: NVDA+Shift+N and NVDA+Shift+Control+N
