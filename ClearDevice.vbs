#$language = "VBScript"
#$interface = "1.0"

'##################################################
'#                                                #
'# Title: ClearDevice                             #
'# Author: Josh Lowe (josh.lowe@ontariotechu.ca)  #
'# Last Updated: Sept 26, 2023                    #
'# Description: This script will quickly erase    #
'# 		and reload a device (router or switch)    #
'#		including deleting vlan.dat               #
'#                                                #
'# Inputs: None                                   #
'# Outputs: None		                          #
'# Instructions: Run this script from within      #
'#		SecureCRT (Script>Run) or assign it to    #
'#      a button on the button bar                #
'#                                                #
'##################################################

crt.Screen.Synchronous = True

Sub Main
	' Send Ctrl-C to ensure not in config mode
	crt.Screen.Send chr(13)
	crt.Screen.Send chr(3)

	' Delete vlan.dat, erase start, and reload
	crt.Screen.Send chr(13)
	If (crt.Screen.WaitForString ("#", 3)) Then
		' Delete vlan.dat file
		crt.Screen.Send "delete flash:/vlan.dat" & chr(13)
		crt.Screen.Send chr(13)
		crt.Screen.Send chr(13)

		' Erase the startup config
		crt.Screen.Send chr(26)
		crt.Screen.Send "write erase" & chr(13)

		crt.Screen.WaitForString "Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]"
		crt.Screen.Send chr(13)
		If (crt.Screen.WaitForString ("complete", 13)) Then
			crt.Screen.Send "Reload" & chr(13)
			' If config has changed, say "no" to prompt to save
			If (crt.Screen.WaitForString ("Save? [yes/no]:", 5)) Then
				crt.Screen.Send "n" & chr(13)
				crt.Screen.Send chr(13)
				crt.Screen.Send chr(13)
			Else
				crt.Screen.Send chr(13)
				crt.Screen.Send chr(13)			
			End If
			' Wait for the Syslog message to confirm that the reload has actually been accepted before exiting
			If (crt.Screen.WaitForString ("%SYS-5-RELOAD")) Then
				Exit Sub
			Else
				' If we don't see the reload message right away, it may be waiting for confirmation, so send a few more CRLFs
				crt.Screen.Send chr(13)
				crt.Screen.Send chr(13)
				If (crt.Screen.WaitForString ("%SYS-5-RELOAD")) Then
					Exit Sub
				Else
					' If we STILL haven't seen the reload message, something terrible has happened
					MsgBox "This router isn't reloading"
					Exit sub
				End If
			End If
		Else
			' If we don't get a "complete" message when erasing the configs, something terrible has happened
			MsgBox "There was a problem erasing the configs"
			Exit sub
		End If	
	End If
	
End Sub
