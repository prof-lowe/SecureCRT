# $language = "Python3"
# $interface = "1.0"

# Title: RenameTab
# Author: Josh Lowe (josh.lowe@ontariotechu.ca)
# Last Updated: Oct 20, 2026
# Description: Rename the current SecureCRT tab using the hostname in the
#              current Cisco or Linux CLI prompt.
# Instructions: Run within SecureCRT (Script > Run), or assign to a button.

import re


def hostname_from_prompt(prompt):
    # Remove ANSI color sequences if they appear in the captured text.
    prompt = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", prompt).strip()

    # Login prompts, such as PC-C login:
    match = re.fullmatch(r"([A-Za-z0-9_.-]+)\s+login:\s*", prompt)
    if match:
        return match.group(1)

    # Common Linux/Unix prompts (check before the Cisco pattern):
    # user@server:~$
    # root@server:/etc#
    # [user@server ~]$
    # user@server ~ %
    match = re.search(
        r"(?:^|\s|\[)([A-Za-z0-9_.-]+)@([A-Za-z0-9_.-]+)"
        r"(?=[:\s\]$#%>])"
        r"[^\r\n]*[$#%>]\s*$",
        prompt,
    )
    if match:
        return match.group(2)

    # Linux prompts without a username: PC-B:~$ or PC-B:/etc#
    match = re.fullmatch(
        r"([A-Za-z0-9_.-]+):(?:~|/)[^\r\n]*[$#%>]\s*", prompt
    )
    if match:
        return match.group(1)

    # Cisco-style prompts:
    # SW-CORE-01#
    # SW-CORE-01>
    # SW-CORE-01(config)#
    match = re.fullmatch(
        r"([A-Za-z0-9_.-]+)(?:\([^)]+\))?[#>]\s*", prompt
    )
    if match:
        return match.group(1)

    return None


def main():
    tab = crt.GetScriptTab()
    screen = tab.Screen

    if not tab.Session.Connected:
        crt.Dialog.MessageBox("No active connection.")
        return

    # Read the current CLI prompt from the screen.
    row = screen.CurrentRow
    prompt = screen.Get(row, 1, row, screen.Columns).strip()
    hostname = hostname_from_prompt(prompt)

    if hostname:
        tab.Caption = hostname
    else:
        crt.Dialog.MessageBox(
            "Could not detect hostname from:\n" + prompt
            + "\n\nRun this script at an empty command prompt. "
            "The prompt must include the hostname."
        )


main()
