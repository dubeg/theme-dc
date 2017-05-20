import sublime
import sublime_plugin
import os

# -------------------------------------------------------------------
# Metadata about a widget theme
# -------------------------------------------------------------------
class WidgetType:
    def __init__(self, typeName, keyPrefix, filePrefix, fileExt):
        self.Name = typeName
        self.SettingKey = keyPrefix + typeName.lower()
        self.SettingFilename = filePrefix + typeName + fileExt

# ------------------------------------------------------------------- 
# Utils: contains various methods manage widget themes.
# -------------------------------------------------------------------
class ThemeManager:
    # Public
    USER_PREFERENCES = 'Preferences.sublime-settings'
    USER_WIDGET_SETTINGS = 'Widget - DC_3.sublime-settings'

    LIGHTMODE_KEY = "dc_use_light";
    COLOR_SCHEME_KEY = 'color_scheme'
    COLOR_SCHEME_VALUE = "Packages/Theme - DC/{0}"

    WIDGET_KEY_PREFIX  = 'dc_use_widget_'
    WIDGET_FILE_PREFIX = 'Widget_'
    WIDGET_FILE_EXT_DEV  = '.tmTheme'
    WIDGET_FILE_EXT_PROD = '.stTheme'
    WIDGET_TYPENAMES = [
        "DarkDark",
        "DarkGray",
        "DarkLight",
        "GrayDark",
        "LightMode"
        ]


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def detect_is_dev(self):
        prodcount = 0
        devcount = 0
        pluginDir = os.path.dirname(os.path.realpath(__file__))
        for filename in os.listdir(pluginDir):
            (name, ext) = os.path.splitext(filename)  

            if name.startswith(ThemeManager.WIDGET_FILE_PREFIX):
                if ext.endswith(ThemeManager.WIDGET_FILE_EXT_DEV):
                    devcount += 1
                if ext.endswith(ThemeManager.WIDGET_FILE_EXT_PROD):
                    prodcount += 1
        return devcount > prodcount;


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def initWidgetTypes(self):
        types = dict()
        for i,typeName in enumerate(ThemeManager.WIDGET_TYPENAMES):
            types[typeName] = WidgetType(
                typeName, 
                ThemeManager.WIDGET_KEY_PREFIX, 
                ThemeManager.WIDGET_FILE_PREFIX, 
                self.getWidgetExt()
                )
        return types

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getWidgetExt(self):
        if self.is_dev:
            return ThemeManager.WIDGET_FILE_EXT_DEV
        else:
            return ThemeManager.WIDGET_FILE_EXT_PROD

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Constructor
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        self.is_dev = self.detect_is_dev()
        self.widget_types = self.initWidgetTypes()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Set Widget Theme
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    def setWidgetTheme(self, widgetName):
        widgetTypes = self.widget_types

        # Retrieve WidgetType
        widget = widgetTypes.get(widgetName)
        if widget == None:
            print('[SetDCWidget] Unknown widgetName: ' + widgetName) 
            return

        # Load preferences
        pref = sublime.load_settings(ThemeManager.USER_PREFERENCES)
        
        # Remove existing widget keys
        for key, value in widgetTypes.items():
            if pref.has(value.SettingKey):
                pref.erase(value.SettingKey)

        # Set Widget key
        pref.set(widget.SettingKey, True)

        # Change setting in Widget - DC.sublime-settings
        widgetSettings = sublime.load_settings(ThemeManager.USER_WIDGET_SETTINGS)
        
        widgetSettings.set(
            ThemeManager.COLOR_SCHEME_KEY, 
            ThemeManager.COLOR_SCHEME_VALUE.format(widget.SettingFilename)
            )

        return None


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Activate light mode
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    def setLightMode(self, enable):
        pref = sublime.load_settings(ThemeManager.USER_PREFERENCES)
        pref.set(ThemeManager.LIGHTMODE_KEY, enable)
        return None

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Save Widget Settings
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    def saveWidgetSettings(self):
        sublime.save_settings(ThemeManager.USER_PREFERENCES)
        sublime.save_settings(ThemeManager.USER_WIDGET_SETTINGS)        

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Toggle Widget Development env. & settings
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    def toggleWidgetDev(self):
        hintON = "ON"
        hintOFF = "OFF"
        pluginDir = os.path.dirname(os.path.realpath(__file__))
        renameCount = 0

        # --------------
        # Toggle dev
        # --------------
        currentExt = self.getWidgetExt()
        self.is_dev = not self.is_dev
        newExt = self.getWidgetExt()
        statusHint = hintON if self.is_dev else hintOFF

        # --------------
        # Rename widget files.
        # --------------
        for filename in os.listdir( pluginDir ):
            (name, ext) = os.path.splitext(filename)  

            if ext == currentExt:  
                newFilename = name + newExt
                os.rename( 
                    os.path.join(pluginDir, filename), 
                    os.path.join(pluginDir, newFilename)
                    )
                renameCount += 1 
        
        # --------------
        # Set schemes
        # --------------
        if renameCount > 0:
            widget_settings = sublime.load_settings(ThemeManager.USER_WIDGET_SETTINGS)
            current_widget_color_key = widget_settings.get("color_scheme")
            new_widget_color_key = current_widget_color_key.replace(currentExt, newExt)
            widget_settings.set("color_scheme", new_widget_color_key)
            sublime.save_settings(ThemeManager.USER_WIDGET_SETTINGS)

        # --------------
        # Display status
        # --------------
        sublime.status_message("DEV is " + statusHint + ", Renamed: " + str(renameCount))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Is this Plugin Packaged/zipped
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @staticmethod        
    def isPluginPackaged():
        packageFileExt = ".sublime-package"
        isPackaged = (packageFileExt in __file__)
        return isPackaged

# ===================================================================
# Section: Plugin Window Commands
# ===================================================================
class ActivateLightMode(sublime_plugin.WindowCommand):
    def run(self):
        mgr = ThemeManager()
        mgr.setWidgetTheme("LightMode")
        mgr.setLightMode(True)
        return None

class SetWidget(sublime_plugin.WindowCommand):
    def run(self, widgetName):
        mgr = ThemeManager()
        mgr.setWidgetTheme(widgetName)
        mgr.setLightMode(False)
        return None


class SaveWidgetSettings(sublime_plugin.WindowCommand):
    def run(self):
        mgr = ThemeManager()
        mgr.saveWidgetSettings()
        return None


class ToggleWidgetDev(sublime_plugin.WindowCommand):
    def run(self):
        mgr = ThemeManager()
        mgr.toggleWidgetDev()
        return None

    # Is Enabled:
    # Returns true if the command is able to be run at this time. 
    # The default implementation simply always returns True.
    def is_enabled(self):
        canBeRun = not ThemeManager.isPluginPackaged()
        return canBeRun
