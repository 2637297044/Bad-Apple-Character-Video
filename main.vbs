Set wshShell = CreateObject("WScript.Shell")
Function Check(filespec)
Dim fso
Set fso = CreateObject("Scripting.FileSystemObject")
If Not (fso.FileExists(filespec)) Then
wshShell.Run "py ""Bad Apple.py"" ", 1, 1
End If
End Function
Check("video_data.py")
strCmd1 = "python main.py"
strCmd2 = "py play_bgm.py"
wshShell.Exec(strCmd1)
wshShell.Exec(strCmd2)