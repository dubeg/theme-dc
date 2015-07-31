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
class DCUtils:
    # Private
    __widgetTypes = None
    # Public
    USER_PREFERENCES = 'Preferences.sublime-settings'
    USER_WIDGET_SETTINGS = 'Widget - DC_3.sublime-settings'
    COLOR_SCHEME_KEY = 'color_scheme'
    COLOR_SCHEME_VALUE = "Packages/Theme - DC/{0}"
    IS_DEV = True

    WIDGET_KEY_PREFIX  = 'dc_use_widget_'
    WIDGET_FILE_PREFIX = 'Widget_'
    WIDGET_FILE_EXT_DEV  = '.tmTheme'
    WIDGET_FILE_EXT_PROD = '.stTheme'
    WIDGET_TYPENAMES = [
        "DarkDark",
        "DarkGray",
        "DarkLight",
        "GrayDark"
        ]

    @staticmethod
    def __initTypes():
        types = dict()
        for i,typeName in enumerate(DCUtils.WIDGET_TYPENAMES):
            types[typeName] = WidgetType(
                typeName, 
                DCUtils.WIDGET_KEY_PREFIX, 
                DCUtils.WIDGET_FILE_PREFIX, 
                DCUtils.getWidgetExt()
                )
        return types

    @staticmethod
    def getWidgetExt():
        if DCUtils.IS_DEV:
            return DCUtils.WIDGET_FILE_EXT_DEV
        else:
            return DCUtils.WIDGET_FILE_EXT_PROD

    @staticmethod
    def getWidgetTypes():
        if DCUtils.__widgetTypes == None:
            DCUtils.__widgetTypes = DCUtils.__initTypes()        
        return DCUtils.__widgetTypes;

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Set Widget Theme
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    def setWidgetTheme(widgetName):
        widgetTypes = DCUtils.getWidgetTypes()

        # Retrieve WidgetType
        widget = widgetTypes.get(widgetName)
        if widget == None:
            print('[SetDCWidget] Unknown widgetName: ' + widgetName) 
            return

        # Load preferences
        pref = sublime.load_settings(DCUtils.USER_PREFERENCES)
        
        # Remove existing widget keys
        for key, value in widgetTypes.items():
            pref.erase(value.SettingKey)
        
        # Set Widget key
        pref.set(widget.SettingKey, True)

        # Change setting in Widget - DC.sublime-settings
        widgetSettings = sublime.load_settings(DCUtils.USER_WIDGET_SETTINGS)
        widgetSettings.set(
            DCUtils.COLOR_SCHEME_KEY, 
            DCUtils.COLOR_SCHEME_VALUE.format(widget.SettingFilename)
            )

        return None

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Save Widget Settings
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    def saveWidgetSettings():
        sublime.save_settings(DCUtils.USER_PREFERENCES)
        sublime.save_settings(DCUtils.USER_WIDGET_SETTINGS)        

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Toggle Widget Development env. & settings
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    def toggleWidgetDev():
        hintON = "ON"
        hintOFF = "OFF"
        pluginDir = os.path.dirname(os.path.realpath(__file__))
        renameCount = 0

        # Get infos related to current status
        currentExt = DCUtils.getWidgetExt()
        # Toggle
        DCUtils.IS_DEV = not DCUtils.IS_DEV
        # Get infos related to new status
        newExt = DCUtils.getWidgetExt()
        statusHint = hintON if DCUtils.IS_DEV else hintOFF
        # Rename widget files if necessary
        for filename in os.listdir( pluginDir ):
            (name, ext) = os.path.splitext(filename)  

            if ext == currentExt:  
                newFilename = name + newExt
                os.rename( 
                    os.path.join(pluginDir, filename), 
                    os.path.join(pluginDir, newFilename)
                    )    
                renameCount += 1 
        
        # TODO: write to Widget - DC3.sublime-settings
        # - User
        # - Package

        # Display cmd status
        sublime.status_message("DEV is " + statusHint + ", Renamed: " + str(renameCount))

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Is this Plugin Packaged/zipped
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~        
    def isPluginPackaged():
        packageFileExt = ".sublime-package"
        isPackaged = (packageFileExt in __file__)
        return isPackaged

# ===================================================================
# Section: Plugin Window Commands
# ===================================================================
class SetWidget(sublime_plugin.WindowCommand):
    def run(self, widgetName):
        DCUtils.setWidgetTheme(widgetName)
        return None


class SaveWidgetSettings(sublime_plugin.WindowCommand):
    def run(self):
        DCUtils.saveWidgetSettings()
        return None


class ToggleWidgetDev(sublime_plugin.WindowCommand):
    def run(self):
        DCUtils.toggleWidgetDev()
        return None

    # Is Enabled:
    # Returns true if the command is able to be run at this time. 
    # The default implementation simply always returns True.
    def is_enabled(self):
        canBeRun = not DCUtils.isPluginPackaged()
        return canBeRun
