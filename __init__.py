bl_info = {
    "name": "Floating Windows",
    "author": "Jonathan Kron",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Pie Menu",
    "description": "Open floating windows",
    "warning": "",
    "wiki_url": "",
    "category": "Windows",
}
import bpy
import os
from bpy.types import Menu
from bpy.types import Operator
import webbrowser
import ctypes
from ctypes import wintypes
import time











#----------------------Inputs-------------------------

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# List of all codes for keys:
# # msdn.microsoft.com/en-us/library/dd375731
UP = 0x26
DOWN = 0x28
A = 0x41

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


#----------------------Inputs-------------------------













#directory
script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)

#Scripts:
class new_current_FWindow(Operator):
    """open current window as float"""
    bl_idname = "menu.add_current"
    bl_label = "Open CURRENT"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)

        return {'FINISHED'}



class new_FWindow_VIEW_3D(Operator):
    """open new window"""
    bl_idname = "menu.add_view3d"
    bl_label = "Open VIEW_3D"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'VIEW_3D'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)

        return {'FINISHED'}

class new_FWindow_IMAGE_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_imageeditor"
    bl_label = "Open IMAGE_EDITOR"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'IMAGE_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
            
        return {'FINISHED'}
    
class new_FWindow_NODE_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_nodeeditor"
    bl_label = "Open NODE_EDITOR"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'NODE_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_SEQUENCE_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_sequenceeditor"
    bl_label = "Open SEQUENCE_EDITOR"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'SEQUENCE_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_CLIP_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_clipeditor"
    bl_label = "Open CLIP_EDITOR"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'CLIP_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}

class new_FWindow_DOPESHEET_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_dopesheeteditor"
    bl_label = "Open DOPESHEET_EDITOR"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'DOPESHEET_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_GRAPH_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_grapheditor"
    bl_label = "Open GRAPH_EDITOR"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'GRAPH_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_NLA_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_nlaeditor"
    bl_label = "Open TIMELINE"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'NLA_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_TEXT_EDITOR(Operator):
    """open new window"""
    bl_idname = "menu.add_texteditor"
    bl_label = "Open TEXT_EDITOR"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'TEXT_EDITOR'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}

class new_FWindow_CONSOLE(Operator):
    """open new window"""
    bl_idname = "menu.add_console"
    bl_label = "Open CONSOLE"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'CONSOLE'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_INFO(Operator):
    """open new window"""
    bl_idname = "menu.add_info"
    bl_label = "Open INFO"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'INFO'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_OUTLINER(Operator):
    """open new window"""
    bl_idname = "menu.add_outliner"
    bl_label = "Open OUTLINER"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'OUTLINER'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_PROPERTIES(Operator):
    """open new window"""
    bl_idname = "menu.add_properties"
    bl_label = "Open PROPERTIES"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'PROPERTIES'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}
    
class new_FWindow_FILE_BROWSER(Operator):
    """open new window"""
    bl_idname = "menu.add_filebrowser"
    bl_label = "Open FILE_BROWSER"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'FILE_BROWSER'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}

class new_FWindow_PREFERENCES(Operator):
    """open new window"""
    bl_idname = "menu.add_preferences"
    bl_label = "Open PREFERENCES"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        area = bpy.context.area
        t = area.type
        area.type = 'PREFERENCES'
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        area.type = t
        
        if alwaysOnTopAlwaysOn == True:
            PressKey(0x11)
            PressKey(0x20)
            time.sleep(0.5)
            ReleaseKey(0x11)
            ReleaseKey(0x20)
        return {'FINISHED'}





#openAlwaysOnTop
class open_always_on_top(Operator):
    """open always on top exe"""
    bl_idname = "file.openalwaysontop"
    bl_label = "Open always on top"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        
        
        #diritems = os.listdir(directory.replace(bpy.path.basename(bpy.data.filepath), "")) #in .blend
        diritems = os.listdir(directory) #in addon
        if "always-on-top.exe" in diritems:
            ShowMessageBoxForConfirmation("Execute always-on-top.exe.", "Execute always-on-top.exe", 'ERROR')
        else:
            ShowMessageBoxForDownload("To use this feature you will have to download the always-on-top.exe and copy the file into the root-folder of this addon.", "Installing always-on-top.exe", 'ERROR')
            #webbrowser.open_new_tab('https://www.labnol.org/software/tutorials/keep-window-always-on-top/5213/')
        return {'FINISHED'}

  
  
class SimpleConfirmOperatorForDownload(bpy.types.Operator):
    #"""Really?"""
    bl_idname = "my_category.custom_confirm_dialog"
    bl_label = "Go to the download-page"
    bl_options = {'REGISTER', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        webbrowser.open_new_tab('https://www.labnol.org/software/tutorials/keep-window-always-on-top/5213/')
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

def ShowMessageBoxForDownload(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        layout = self.layout
        self.layout.label(text = message)
        layout.operator(SimpleConfirmOperatorForDownload.bl_idname)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)





class SimpleConfirmOperatorForConfirmation(bpy.types.Operator):
    #"""Really?"""
    bl_idname = "my_category.custom_confirm_dialog_execution"
    bl_label = "Execute"
    bl_options = {'REGISTER', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        #newdir = directory.replace(bpy.path.basename(bpy.data.filepath), "") + "always-on-top.exe" #in .blend
        newdir = directory + "//always-on-top.exe" #in addon
        
        os.startfile(newdir)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

def ShowMessageBoxForConfirmation(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        layout = self.layout
        #self.layout.label(text = message)
        layout.operator(SimpleConfirmOperatorForConfirmation.bl_idname)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)












alwaysOnTopAlwaysOn = False

class setAlwaysOnTopAlwaysOn_class(Operator):
    """Always open always-on-top.exe"""
    bl_idname = "file.alwaysopenalwaysontop"
    bl_label = "Always open new windows on top(OFF)"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        global alwaysOnTopAlwaysOn
        if alwaysOnTopAlwaysOn == False:
            alwaysOnTopAlwaysOn = True
        
        return {'FINISHED'}
    
class setAlwaysOffOnTopAlwaysOn_class(Operator):
    """Never open always-on-top.exe"""
    bl_idname = "file.neversopenalwaysontop"
    bl_label = "Always open new windows on top(ON)"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        global alwaysOnTopAlwaysOn
        if alwaysOnTopAlwaysOn == True:
            alwaysOnTopAlwaysOn = False
        
        return {'FINISHED'}



class ctrlspace_class(Operator):
    """Make window on top"""
    bl_idname = "window.makewindowontop"
    bl_label = "Make window on top"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):

        PressKey(0x11)
        PressKey(0x20)
        time.sleep(0.5)
        ReleaseKey(0x11)
        ReleaseKey(0x20)
        return {'FINISHED'}


#PieMenu
class VIEW3D_MT_PIE_MENU(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Floating Windows"
    bl_idname = "pie.add_fwindows"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()

        gap = pie.column()
        
        menu = gap.box()
        menu.scale_x = 1.2
        menu.scale_y = 1.5
        
        menu.operator("menu.add_current")
        
        menu.separator()
        menu.separator()
        
        menu.operator("menu.add_view3d")
        menu.operator("menu.add_nodeeditor")
        menu.operator("menu.add_texteditor")
        menu.operator("menu.add_outliner")
        menu.operator("menu.add_properties")
        menu.operator("menu.add_filebrowser")
        menu.operator("menu.add_imageeditor")
        menu.operator("menu.add_sequenceeditor")
        
        menu.operator("menu.add_clipeditor")
        menu.operator("menu.add_dopesheeteditor")
        menu.operator("menu.add_grapheditor")
        menu.operator("menu.add_nlaeditor")
        menu.operator("menu.add_console")
        menu.operator("menu.add_info")
        menu.operator("menu.add_preferences")
        
        menu.separator()
        menu.separator()
        
        
        menu.operator("file.openalwaysontop")
        menu.operator("window.makewindowontop")
        
        if alwaysOnTopAlwaysOn == True:
            menu.operator("file.neversopenalwaysontop")
        else:
            menu.operator("file.alwaysopenalwaysontop")

        
        
        
#Keymap
# store keymaps here to access after registration
addon_keymaps = []  
        
        

# Registration
classes = (
    VIEW3D_MT_PIE_MENU,
    
    new_current_FWindow,
    
    new_FWindow_VIEW_3D,
    new_FWindow_IMAGE_EDITOR,
    new_FWindow_NODE_EDITOR,
    new_FWindow_SEQUENCE_EDITOR,
    new_FWindow_CLIP_EDITOR,
    new_FWindow_DOPESHEET_EDITOR,
    new_FWindow_GRAPH_EDITOR,
    new_FWindow_NLA_EDITOR,
    new_FWindow_TEXT_EDITOR,
    new_FWindow_CONSOLE,
    new_FWindow_INFO,
    new_FWindow_OUTLINER,
    new_FWindow_PROPERTIES,
    new_FWindow_FILE_BROWSER,
    new_FWindow_PREFERENCES,
    
    open_always_on_top,
    
    SimpleConfirmOperatorForDownload,
    SimpleConfirmOperatorForConfirmation,
    
    setAlwaysOnTopAlwaysOn_class,
    setAlwaysOffOnTopAlwaysOn_class,
    
    ctrlspace_class,
    
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
        
        
    # handle the keymap
    wm = bpy.context.window_manager
    kc = bpy.context.window_manager.keyconfigs.addon
    if wm.keyconfigs.addon:
        
        km = wm.keyconfigs.addon.keymaps.new(name = "Window",space_type='EMPTY', region_type='WINDOW')
 
        kmi = km.keymap_items.new('wm.call_menu_pie', 'F', 'PRESS' ,alt=True,ctrl=True)
        kmi.properties.name = "pie.add_fwindows"
        addon_keymaps.append((km,kmi))


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
        
        
    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()


    
if __name__ == "__main__":
    register()



    #bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_PIE_template")
