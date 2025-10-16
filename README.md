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

**Note:** The psutil library is included with this add-on - no additional installation required!

## Installation

1. Download the `.nvda-addon` file from the [releases page](https://github.com/michaldziwisz/networkSpeed/releases)
2. Run the file - NVDA will automatically install the add-on
3. Restart NVDA

## Usage

After installing the add-on, you can use the following default keyboard shortcuts:

- **NVDA+Shift+N** - Announces current download and upload speed in kbps/Mbps (bits - network standard)
  - Press twice quickly to copy the speed to clipboard
- **NVDA+Shift+Control+N** - Announces current download and upload speed in KB/s/MB/s (bytes - file download format)
  - Press twice quickly to copy the speed to clipboard

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
- Each measurement takes exactly 1 second - the add-on measures the actual speed at that moment by taking two measurements 1 second apart
- When you press the keyboard shortcut, there will be a 1-second delay while measuring

## License

GPL v2

This add-on includes the psutil library (BSD 3-Clause License). See LICENSE.txt for full license information.

## Author

Michał Dziwisz

## Version History

### Version 1.3.0
- **Added double-press feature** - press any shortcut twice quickly (within 0.5 seconds) to copy the speed to clipboard
- Double-press copies the last measurement instantly and announces the copied value
- Enhanced usability for sharing network speed information

### Version 1.2.0
- **psutil library now included** - no additional installation required!
- Simplified installation process
- Added LICENSE.txt with full license information for included libraries
- Removed psutil installation instructions from documentation

### Version 1.1.0
- Fixed speed measurement to be accurate - now measures actual current speed
- Each measurement takes exactly 1 second (two measurements 1 second apart)
- Removed unreliable "time since last measurement" method

### Version 1.0.0
- Initial release
- Basic download and upload speed monitoring
- Automatic kbps/Mbps and KB/s/MB/s formatting
- Keyboard shortcuts: NVDA+Shift+N and NVDA+Shift+Control+N
