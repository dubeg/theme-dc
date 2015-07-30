import sublime
import sublime_plugin
import os


class DCUtils:
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
    def getWidgetExt():
        if IS_DEV:
            return WIDGET_FILE_EXT_DEV
        else:
            return WIDGET_FILE_EXT_PROD


class WidgetType(object):
    def __init__(self, typeName, keyPrefix, filePrefix, fileExt):
        self.Name = typeName
        self.SettingKey = keyPrefix + typeName.lower()
        self.SettingFilename = filePrefix + typeName + fileExt


class SetWidget(sublime_plugin.WindowCommand):
    WidgetTypes = None

    def __initTypes(self):
        types = dict()
        for i,typeName in enumerate(DCUtils.WIDGET_TYPENAMES):
            types[typeName] = WidgetType(
                typeName, 
                DCUtils.WIDGET_KEY_PREFIX, 
                DCUtils.WIDGET_FILE_PREFIX, 
                DCUtils.getWidgetExt()
                )
        return types

    def run(self, widgetName):
        if SetWidget.WidgetTypes == None:
            SetWidget.WidgetTypes = self.__initTypes()

        # Retrieve widgetType
        widget = SetWidget.WidgetTypes.get(widgetName)
        if widget == None:
            print('[SetDCWidget] Unknown widgetName: ' + widgetName) 
            return

        # Load preferences
        pref = sublime.load_settings(USER_PREFERENCES)
        
        # Remove existing widget keys
        for key, value in SetWidget.WidgetTypes.items():
            pref.erase(value.SettingKey)
        
        # Set Widget key
        pref.set(widget.SettingKey, True)

        # Change setting in Widget - DC.sublime-settings
        widgetSettings = sublime.load_settings(USER_WIDGET_SETTINGS)
        widgetSettings.set(COLOR_SCHEME_KEY, COLOR_SCHEME_VALUE.format(widget.SettingFilename))


class SaveWidgetSettings(sublime_plugin.WindowCommand):
    def run(self):
        sublime.save_settings(DCUtils.USER_PREFERENCES)
        sublime.save_settings(DCUtils.USER_WIDGET_SETTINGS)


class ToggleWidgetDev(sublime_plugin.WindowCommand):
    def run(self):
        hintON = "ON"
        hintOFF = "OFF"

        # Toggle
        DCUtils.IS_DEV = not DCUtils.IS_DEV
        fileExt = DCUtils.getWidgetExt()
        currentHint = hintON if DCUtils.IS_DEV else hintOFF
            
        #for filename in os.listdir("."):
        #     if filename.startswith("cheese_"):    
        #         os.rename(filename, filename[7:])     

        sublime.status_message("DEV is " + currentHint)

    def is_enabled(self):
        packageFileExt = ".sublime-package"

        # Do not run if plugin is packaged/zipped.
        ok_to_run = False
        if packageFileExt not in __file__:
            ok_to_run = True

        return ok_to_run
        # Returns true if the command is able to be run at this time. 
        # The default implementation simply always returns True.

    def is_visible(self):
        return True
        # Returns true if the command should be shown in the menu at this time. 
        # The default implementation always returns True.

    def description(self):
        # hintON = "[ON]"
        # hintOFF = "[OFF]"
        # currentHint = hintON if IS_DEV else hintOFF 
        return None
        # Returns a description of the command with the given arguments. 
        # Used in the menu, if no caption is provided. 
        # Return None to get the default description.
