# -*- coding: utf-8 -*-
# Network Speed Monitor - NVDA Add-on
# Author: Michał Dziwisz
# Displays current network download and upload speeds

import globalPluginHandler
import ui
import scriptHandler
import time
import api
try:
	import psutil
except ImportError:
	psutil = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	"""Global plugin for monitoring network speed"""

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.lastMessage = None
		self.lastMessageBytes = None
		self.lastCallTime = 0
		self.lastCallTimeBytes = 0

	def formatSpeed(self, bytesPerSecond):
		"""Formats speed from bytes per second to kbps or Mbps"""
		if bytesPerSecond is None:
			return "0 kbps"

		# Convert from bytes/s to kiloBITS/s
		kbps = (bytesPerSecond * 8) / 1024

		if kbps < 1024:
			# Less than 1 Mbps - show in kbps
			return "{:.1f} kbps".format(kbps)
		else:
			# 1 Mbps or more - show in Mbps
			mbps = kbps / 1024
			return "{:.2f} Mbps".format(mbps)

	def formatSpeedBytes(self, bytesPerSecond):
		"""Formats speed from bytes per second to KB/s or MB/s"""
		if bytesPerSecond is None:
			return "0 KB/s"

		# Bytes per second to kiloBytes/s
		kbytes = bytesPerSecond / 1024

		if kbytes < 1024:
			# Less than 1 MB/s - show in KB/s
			return "{:.1f} KB/s".format(kbytes)
		else:
			# 1 MB/s or more - show in MB/s
			mbytes = kbytes / 1024
			return "{:.2f} MB/s".format(mbytes)

	def getNetworkSpeed(self):
		"""Calculates current download and upload speed by measuring over 1 second"""
		try:
			# First measurement
			firstNetIO = psutil.net_io_counters()

			# Wait exactly 1 second
			time.sleep(1.0)

			# Second measurement
			secondNetIO = psutil.net_io_counters()

			# Calculate speeds (bytes per second)
			downloadSpeed = secondNetIO.bytes_recv - firstNetIO.bytes_recv
			uploadSpeed = secondNetIO.bytes_sent - firstNetIO.bytes_sent

			return downloadSpeed, uploadSpeed

		except Exception as e:
			ui.message("Error retrieving network statistics: {}".format(str(e)))
			return None, None

	@scriptHandler.script(
		description="Announces current download and upload speed. Press twice to copy to clipboard.",
		gesture="kb:NVDA+shift+n",
		speakOnDemand=True
	)
	def script_announceNetworkSpeed(self, gesture):
		"""Script invoked by keyboard shortcut"""
		# Check if this is a double-press (called within 0.5 seconds of last call END time)
		currentTime = time.time()
		timeSinceLastCall = currentTime - self.lastCallTime

		if timeSinceLastCall < 0.5 and self.lastMessage:
			# Double press - copy last message to clipboard
			api.copyToClip(self.lastMessage)
			ui.message("Copied to clipboard: {}".format(self.lastMessage))
			# Don't update lastCallTime so triple-press won't trigger again
			return

		# Single press - measure speed over 1 second
		downloadSpeed, uploadSpeed = self.getNetworkSpeed()

		if downloadSpeed is None or uploadSpeed is None:
			ui.message("Unable to measure speed.")
			return

		# Format and announce result
		downloadStr = self.formatSpeed(downloadSpeed)
		uploadStr = self.formatSpeed(uploadSpeed)

		message = "Download: {}, Upload: {}".format(downloadStr, uploadStr)
		self.lastMessage = message
		ui.message(message)

		# Update last call time AFTER measurement completes
		self.lastCallTime = time.time()

	@scriptHandler.script(
		description="Announces current download and upload speed in bytes. Press twice to copy to clipboard.",
		gesture="kb:NVDA+shift+control+n",
		speakOnDemand=True
	)
	def script_announceNetworkSpeedBytes(self, gesture):
		"""Script invoked by keyboard shortcut - bytes version"""
		# Check if this is a double-press (called within 0.5 seconds of last call END time)
		currentTime = time.time()
		timeSinceLastCall = currentTime - self.lastCallTimeBytes

		if timeSinceLastCall < 0.5 and self.lastMessageBytes:
			# Double press - copy last message to clipboard
			api.copyToClip(self.lastMessageBytes)
			ui.message("Copied to clipboard: {}".format(self.lastMessageBytes))
			# Don't update lastCallTimeBytes so triple-press won't trigger again
			return

		# Single press - measure speed over 1 second
		downloadSpeed, uploadSpeed = self.getNetworkSpeed()

		if downloadSpeed is None or uploadSpeed is None:
			ui.message("Unable to measure speed.")
			return

		# Format and announce result in bytes
		downloadStr = self.formatSpeedBytes(downloadSpeed)
		uploadStr = self.formatSpeedBytes(uploadSpeed)

		message = "Download: {}, Upload: {}".format(downloadStr, uploadStr)
		self.lastMessageBytes = message
		ui.message(message)

		# Update last call time AFTER measurement completes
		self.lastCallTimeBytes = time.time()
