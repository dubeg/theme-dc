# DC Theme

Dark and Cyan (DC) theme for Sublime Text 2/3.

Based on Soda Theme by Ian Hill [(buymeasoda.com)](http://buymeasoda.com/), and inspired by many others.

Uses assets made by:

- Ian Hill, from the Soda theme (search icons, and others)
- the Numix project (alternate folder icon)
- VisualStudio (alternate folder icon)
- the Seti_UI project (file icons)

And probably more than I remember right now..


Project site: [github.com/dubeg/theme-dc](https://github.com/dubeg/theme-dc).

## Images

![Main screen](http://i.imgur.com/AvyhY2z.png)

### Alternate folder icons

![Compare](http://i.imgur.com/pMJkIs5.png)

### Alternate group icons

![Compare](http://i.imgur.com/4apuFcD.png)

### Alternate search icons

![CTRL + F](http://i.imgur.com/xCG4hgg.png)

![CTRL + SHIFT + F](http://i.imgur.com/3z0LwIh.png)

![CTRL + H](http://i.imgur.com/kCBFkmW.png)

## Installation

### Using Sublime Package Control

Using Will Bond's [Sublime Package Control](http://wbond.net/sublime_packages/package_control),

- Open the mini quick panel.
- Type `Package Control: Install Package`.
- Search for `Theme - DC` in the packages list.

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Theme - DC`
* Find your `Packages` directory using the menu item  `Preferences -> Browse Packages...`
* Copy the folder into your Sublime Text `Packages` directory

## Activating the theme

To configure Sublime Text to use the theme, follow the instructions below.

* Open your User Settings Preferences file `Sublime Text -> Preferences -> Settings - User`.
* Add (or update) your theme entry according to your version of Sublime text.

**ST3**

    {
        "theme": "DC_3.sublime-theme"
    }


**ST2**

    {
        "theme": "DC_2.sublime-theme"
    }

## Additional Features


### User Settings

You can use the settings below to customize the theme to your liking.

**Example User Settings**

    "dc_hide_file_icons": false,
    "dc_hide_folders": false,
    "dc_hide_group_icons": false,
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
    "dc_bold_folder_labels": true,
    

### Resolution Support

Unfortunately, I've been too lazy to test the DC Theme on high DPI displays (over 1080p).
However, I'll probably add the support if requested, or when I start using devices with such displays.

## Bonus

### Color Scheme

The color scheme seen in the screenshot is a modified version of Monokai, called `Monokai Soda`.

It is made available by buymeasoda. Here's how to get it:

* Download [colour-schemes.zip](http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip)
* Unzip and place the extracted `tmtheme` files in the Sublime Text `Packages/User` folder
* Enable the colour scheme via `Preferences -> Color Scheme -> User`

### File icons

The file icons seen in the screenshot are assets collected from the [Seti_ST3 repository](https://github.com/ctf0/Seti_ST3).



## License

DC Theme is licensed under the [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). You are free to share and remix the theme, however please abide by the license terms when doing so.

The following details apply to the Creative Commons license "author specified" components:

* Attribution example: Based on DC Theme.

* Naming guidelines: If you create and distribute a derivative theme, please give your theme a unique and original name that does not directly include "Soda Theme" (or a close variant) in the main project title, repo name or Package Control name.
