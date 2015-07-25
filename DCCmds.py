import sublime
import sublime_plugin
import os

USER_PREFERENCES = 'Preferences.sublime-settings'
USER_WIDGET_SETTINGS = 'Widget - DC_3.sublime-settings'
COLOR_SCHEME_KEY = 'color_scheme'
COLOR_SCHEME_VALUE = "Packages/Theme - DC/{0}"
IS_DEV = True

WIDGET_KEY_PREFIX  = 'dc_use_widget_'
WIDGET_FILE_PREFIX = 'Widget_'
WIDGET_FILE_EXT_DEV  = '.tmTheme'
WIDGET_FILE_EXT_PROD = '.stTheme'
WIDGET_FILE_EXT = WIDGET_FILE_EXT_DEV if IS_DEV else WIDGET_FILE_EXT_PROD
WIDGET_TYPENAMES = [
    "DarkDark",
    "DarkGray",
    "DarkLight",
    "GrayDark"
    ]


class WidgetType(object):
    def __init__(self, typeName, keyPrefix, filePrefix, fileExt):
        self.Name = typeName
        self.SettingKey = keyPrefix + typeName.lower()
        self.SettingFilename = filePrefix + typeName + fileExt


class SetWidget(sublime_plugin.WindowCommand):
    WidgetTypes = None

    def __initTypes(self):
        types = dict()
        for i,typeName in enumerate(WIDGET_TYPENAMES):
            types[typeName] = WidgetType(
                typeName, 
                WIDGET_KEY_PREFIX, 
                WIDGET_FILE_PREFIX, 
                WIDGET_FILE_EXT
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
        sublime.save_settings(USER_PREFERENCES)
        sublime.save_settings(USER_WIDGET_SETTINGS)

class ReloadWidgetTheme(sublime_plugin.WindowCommand):        
    def run(self):
        sublime.load_settings("Theme - DC/Widget_DC_3.sublime-settings")