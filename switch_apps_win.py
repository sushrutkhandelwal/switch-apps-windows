import sys
import win32gui
import win32com.client as cli
wsh= cli.Dispatch("WScript.Shell")
import win32api,time,ctypes

def callback(hwnd, strings):
    if win32gui.IsWindowVisible(hwnd):
        window_title = win32gui.GetWindowText(hwnd)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        if window_title and right-left and bottom-top:
            strings.append('0x{:08x}: "{}"'.format(hwnd, window_title).encode("utf-8"))
    return True

#list of open applications/softwares
def getList():
    win_list = []  # list of strings containing win handles and window titles
    win32gui.EnumWindows(callback, win_list)  # populate list

    return win_list

boo=True
i=0
while(boo):
	x,y=win32api.GetCursorPos()
	if x==1279 and y==719:		
		win_list=getList()
		for item in win_list:
			print(item)
		i=i+1
		if i==len(win_list)-1:
			i=0
		print(str(win_list[i].decode("utf-8"))[13:])
		wsh.AppActivate(str(win_list[i].decode("utf-8")[13:len(win_list)-2]))
		#coordinates of bottom right corner
		while x==1279 and y==719:
			x,y=win32api.GetCursorPos()
	#close the program by bringing the cursor to top left corner
	if x==0 and y==0:
		boo=False