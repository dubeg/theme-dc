# DC Theme

Dark and Cyan (DC) theme for Sublime Text 3.

Based on Soda Theme by Ian Hill [(buymeasoda.com)](http://buymeasoda.com/), and inspired by many others.

Project site: [github.com/dubeg/theme-dc](https://github.com/dubeg/theme-dc).

## Images

![Screenshot](http://i.imgur.com/VWfm2Xv.png)

## Installation

DC theme is designed to work with the latest development builds of Sublime Text 3.

### Using Sublime Package Control

If you are using Will Bond's [Sublime Package Control](http://wbond.net/sublime_packages/package_control), 
you will be able to install DC Theme via the `Package Control: Install Package` menu item. 
The DC Theme package will be listed as `Theme - DC` in the packages list.

I'll try to add it to wbond's package control relatively soon.

### Using Git

Alternatively, if you are a git user, you can install the theme and 
keep up to date by cloning the repo directly into your `Packages` directory 
in the Sublime Text application settings area.

You can locate your Sublime Text `Packages` directory by using the menu item `Preferences -> Browse Packages...`.

While inside the `Packages` directory, clone the theme repository using the command below:

    git clone https://github.com/dubeg/theme-dc/ "Theme - DC"

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Theme - DC`
* Find your `Packages` directory using the menu item  `Preferences -> Browse Packages...`
* Copy the folder into your Sublime Text `Packages` directory

## Activating the theme

To configure Sublime Text to use the theme, follow the instructions below.


### Sublime Text 3

* Open your User Settings Preferences file `Sublime Text -> Preferences -> Settings - User`.
* Add (or update) your theme entry to be `"theme": "DC.sublime-theme"`.

**Example User Settings**

    {
        "theme": "DC.sublime-theme"
    }

## Additional Features


### Settings - User


Here are the settings you can use to customize the theme to your liking:

**Example User Settings**

    // Hide Close Button in tabs.
    "dc_hide_btn_close_tab": true,

    // Hide group arrows in the sidebar.
    "dc_hide_arrows": true,

    // Hide folder and file icons in the sidebar.
    "dc_hide_folders": true,

    // Hide only file icons in the sidebar.
    "dc_hide_fileicons": true,

    // Bold folder labels in the sidebar.
    "bold_folder_labels": true,

    // Always show the minimap viewport.
    "always_show_minimap_viewport": true,


### Resolution Support

Unfortunately, I've been too lazy to test the DC Theme on high DPI displays (over 1080p).
However, I'll probably add the support if requested, or when I start using devices with such displays.

## Bonus

### Syntax Highlighting Colour Schemes (to modify)

The DC Theme screenshot uses a modified version of Monokai.

If you'd like to use the syntax highlighting schemes shown in the screenshots:

* Download [colour-schemes.zip](http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip)
* Unzip and place the extracted `tmtheme` files in the Sublime Text `Packages/User` folder
* Enable the colour scheme via `Preferences -> Color Scheme -> User`


## License (to modify)

DC Theme is licensed under the [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). You are free to share and remix the theme, however please abide by the license terms when doing so.

The following details apply to the Creative Commons license "author specified" components:

* Attribution example: Based on DC Theme.

* Naming guidelines: If you create and distribute a derivative theme, please give your theme a unique and original name that does not directly include "Soda Theme" (or a close variant) in the main project title, repo name or Package Control name.
