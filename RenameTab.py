# $language = "Python3"
# $interface = "1.0"

# Title: RenameTab
# Author: Josh Lowe (josh.lowe@ontariotechu.ca)
# Last Updated: Oct 20, 2026
# Description: This script will quickly rename the current tab in SecureCRT
#              to match the hostname of the device you are connected to. It
#              works by reading the current CLI prompt and extracting the
#              hostname from it.
# Inputs: None
# Outputs: None
# Instructions: Run this script from within
#               SecureCRT (Script>Run) or assign it to
#               a button on the button bar

import re


def main():
    tab = crt.GetScriptTab()
    screen = tab.Screen

    if not tab.Session.Connected:
        crt.Dialog.MessageBox("No active connection.")
        return

    # Read the current CLI prompt from the screen
    row = screen.CurrentRow
    prompt = screen.Get(row, 1, row, screen.Columns).strip()

    # Match Cisco-style prompts:
    # SW-CORE-01#
    # SW-CORE-01>
    # SW-CORE-01(config)#
    match = re.search(r"([A-Za-z0-9_.-]+)(?:\([^)]+\))?[#>]\s*$", prompt)

    if match:
        hostname = match.group(1)
        tab.Caption = hostname
    else:
        crt.Dialog.MessageBox("Could not detect hostname from:\n" + prompt)


main()
