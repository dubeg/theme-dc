# Theme - DC

Dark and Cyan (DC) theme for Sublime Text 2/3.

Project site - [github.com/dubeg/theme-dc](https://github.com/dubeg/theme-dc)


**Table of Contents**

- [Theme - DC](#theme---dc)
	- [Screenshots](#screenshots)
		* [Main window](#main-window)
	 	* [Alternate widget colors](#alternate-widget-colors)
		* [Alternate folder icons](#alternate-folder-icons)
		* [Alternate group icons](#alternate-group-icons)
		* [Alternate search icons](#alternate-search-icons)
	- [Installation](#installation)
		- [Using Sublime Package Control](#using-sublime-package-control)
		- [Download Manually](#download-manually)
	- [Activation](#activation)
	- [Configuration](#configuration)
	- [Resolution Support](#resolution-support)
	- [Bonus](#bonus)
		- [Color Scheme](#color-scheme)
		- [Filetype icons](#filetype-icons)
		- [Similar themes](#similar-themes)
	- [Credits](#credits)
	- [License](#license)



## Screenshots

### Main window

![Main window](http://i.imgur.com/AvyhY2z.png)

### Alternate widget colors

![DC_3](http://i.imgur.com/71HGEdo.png)

![DC_3_LW](http://i.imgur.com/eYR07Sy.png)

![DC_3_GW](http://i.imgur.com/vA1VzVT.png)

### Alternate folder icons

![Compare](http://i.imgur.com/pMJkIs5.png)

### Alternate group icons

![Compare](http://i.imgur.com/0Si2xIC.png)

### Alternate search icons

![CTRL + F](http://i.imgur.com/URLemr8.png)

### New file icons

![File icons](http://i.imgur.com/57G0GMJ.png)


## Installation

### Using Sublime Package Control

Using Will Bond's [Sublime Package Control](http://wbond.net/sublime_packages/package_control),

- Open the Command Palette `Tools -> Command Palette...`.
- Type `Package Control: Install Package`.
- Search for `Theme - DC` in the packages list.

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Theme - DC`
* Find your `Packages` directory using the menu item  `Preferences -> Browse Packages...`
* Copy the folder into your Sublime Text `Packages` directory

## Activation

To configure Sublime Text to use the theme, follow the instructions below.

* Open your User Settings Preferences file `Sublime Text -> Preferences -> Settings - User`.
* Add (or update) your theme entry according to your version of Sublime text.

**ST3**

    // Theme with dark widget colors
    "theme": "DC_3.sublime-theme"

    // Theme with dark widget backgrounds and white input fields
    "theme": "DC_3_LW.sublime-theme"

    // Theme with gray/dark widget colors
    "theme": "DC_3_GW.sublime-theme"


**ST2**

    "theme": "DC_2.sublime-theme"


## Configuration

You can use the settings below to customize the theme to your liking.

**Example User Settings**

    "dc_hide_file_icons" : false,
    "dc_hide_folders" : false,
    "dc_hide_group_icons" : false,
    "dc_hide_scrollbars" : false,
    "dc_hide_btn_close_tab" : false,

    "dc_use_group_icon1" : true,
    "dc_use_group_icon2" : false,
    "dc_use_group_icon3" : false,
    "dc_use_group_icon4" : false,

    "dc_use_folder_icon1" : true,
    "dc_use_folder_icon2" : false,
    "dc_use_folder_icon3" : false,

    "dc_use_soda_search_icons" : false,
    
    "dc_autohide_scrollbar" : false,
    "dc_use_white_puck" : false,
    "dc_always_show_minimap_viewport" : true,
    "dc_bold_folder_labels" : true,
    "dc_mouse_wheel_switches_tabs" : true,
    "dc_highlight_active_sidebar_row" : true
    

## Resolution Support

Unfortunately, I've been too lazy to test the DC Theme on high DPI displays.
However, I'll probably add the support if requested, or when I start using devices with such displays.

## Bonus

### Color Scheme

The color scheme seen in the screenshot is a modified version of Monokai, called `Monokai Soda`.

It is made available by buymeasoda. Here's how to get it:

* Download [colour-schemes.zip](http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip)
* Unzip and place the extracted `tmtheme` files in the Sublime Text `Packages/User` folder
* Enable the colour scheme via `Preferences -> Color Scheme -> User`

### Filetype icons

The file icons seen in the screenshot are assets collected from the [Seti_ST3 repository](https://github.com/ctf0/Seti_ST3).

I modified and added a few of my own however.


### Similar themes

- [Seti_ST3](https://github.com/ctf0/Seti_ST3)
- [Cobalt2](https://github.com/wesbos/cobalt2)


## Credits

Based on Soda Theme by Ian Hill [(buymeasoda.com)](http://buymeasoda.com/), and inspired by many others.

Some assets used in this theme are from (or modified from):

- the Soda theme project (search icons and a few others)
- the Numix project (alternate folder icons)
- Visual Studio 2013 (alternate folder icons, and a few filetype icons)
- the Seti_UI project (most of the filetype icons)



## License

DC Theme is licensed under the [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). You are free to share and remix the theme, however please abide by the license terms when doing so.

The following details apply to the Creative Commons license "author specified" components:

* Attribution example: Based on DC Theme.

* Naming guidelines: If you create and distribute a derivative theme, please give your theme a unique and original name that does not directly include "DC Theme" (or a close variant) in the main project title, repo name or Package Control name.
