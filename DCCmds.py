import sublime
import sublime_plugin
import os

USER_PREFERENCES = 'Preferences.sublime-settings'
USER_WIDGET_SETTINGS = 'Widget - DC_3.sublime-settings'
COLOR_SCHEME_KEY = 'color_scheme'
COLOR_SCHEME_VALUE = "Packages/Theme - DC/{0}"

WIDGET_DD_KEY = 'dc_use_widget_darkdark'
WIDGET_DG_KEY = 'dc_use_widget_darkgray' 
WIDGET_DL_KEY = 'dc_use_widget_darklight'
WIDGET_GD_KEY = 'dc_use_widget_graydark'

WIDGET_DD_FILE = 'Widget_DarkDark.stTheme'
WIDGET_DG_FILE = 'Widget_DarkGray.stTheme'
WIDGET_DL_FILE = 'Widget_DarkLight.stTheme'
WIDGET_GD_FILE = 'Widget_GrayDark.stTheme'

WIDGET_DD_NAME = 'DarkDark'
WIDGET_DG_NAME = 'DarkGray'
WIDGET_DL_NAME = 'DarkLight'
WIDGET_GD_NAME = 'GrayDark'

class WidgetType(object):
    # Shared variables here.
    def __init__(self, name, settingKey, settingFilename):
        # Instance variables here.
        self.Name = name
        self.SettingKey = settingKey
        self.SettingFilename = settingFilename



class SetWidget(sublime_plugin.WindowCommand):
    WidgetTypes = {
            WIDGET_DD_NAME : WidgetType(WIDGET_DD_NAME, WIDGET_DD_KEY, WIDGET_DD_FILE),
            WIDGET_DG_NAME : WidgetType(WIDGET_DG_NAME, WIDGET_DG_KEY, WIDGET_DG_FILE),
            WIDGET_DL_NAME : WidgetType(WIDGET_DL_NAME, WIDGET_DL_KEY, WIDGET_DL_FILE),
            WIDGET_GD_NAME : WidgetType(WIDGET_GD_NAME, WIDGET_GD_KEY, WIDGET_GD_FILE)
        }

    def run(self, widgetName): 
        # Retrieve widgetType
        widget = WidgetTypes.get(widgetName)
        if widget == None:
            print('[SetDCWidget] Unknown widgetName: ' + widgetName) 
            return

        # Load preferences
        pref = sublime.load_settings(USER_PREFERENCES)
        
        # Remove existing widget keys
        for key, value in WidgetTypes.items():
            pref.erase(value.SettingKey)
        
        # Set Widget key
        pref.set(widget.SettingKey, True)
        #sublime.save_settings(USER_PREFERENCES)

        # /////////////////////////////////////////////
        # Change setting in Widget - DC.sublime-settings
        widgetSettings = sublime.load_settings(USER_WIDGET_SETTINGS)
        widgetSettings.set(COLOR_SCHEME_KEY, COLOR_SCHEME_VALUE.format(widget.SettingFilename))
        #sublime.save_settings(USER_WIDGET_SETTINGS)


class SaveWidgetSettings(sublime_plugin.WindowCommand):
    def run(self):
        sublime.save_settings(USER_PREFERENCES)
        sublime.save_settings(USER_WIDGET_SETTINGS)