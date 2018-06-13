# SublimeText3

<!-- MarkdownTOC autolink="true" autoanchor="true" markdown_preview="github" -->

- [Overview](#overview)
- [Command Line Alias](#command-line-alias)
- [Setting up](#setting-up)
- [Unofficial Documentation](#unofficial-documentation)
- [Zeb's Settings](#zebs-settings)
    - [Recommended Packages for Climate Science](#recommended-packages-for-climate-science)
    - [Preferences --> Settings --> User](#preferences----settings----user)
        - [Makefile Preferences --> Settings --> Syntax Specific](#makefile-preferences----settings----syntax-specific)
    - [Preferences --> Key Bindings](#preferences----key-bindings)
    - [Snippets](#snippets)
- [Snippets](#snippets-1)
    - [Medium Guide to SublimeText Snippets](#medium-guide-to-sublimetext-snippets)
- [Package Guide](#package-guide)
    - [MarkdownPreview](#markdownpreview)
    - [SublimeLinter-pylint](#sublimelinter-pylint)
        - [Installation](#installation)

<!-- /MarkdownTOC -->

<a id="overview"></a>
## Overview

A bunch of tips and tricks about how to use Sublime Text 3.

<a id="command-line-alias"></a>
## Command Line Alias

Add alias in `~/.bashrc`

```
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
```

<a id="setting-up"></a>
## Setting up

Open up Sublime Text

- install package control
	- `cmd` + `shift` + `p`, `install package control`

<a id="unofficial-documentation"></a>
## Unofficial Documentation

- available [online](http://sublime-text-unofficial-documentation.readthedocs.io/en/latest/reference/commands.html)
- free
- ease of use: unknown (haven't read)
- recommendation: unknown (haven't read)

<a id="zebs-settings"></a>
## Zeb's Settings

<a id="recommended-packages-for-climate-science"></a>
### Recommended Packages for Climate Science

- `Fortran`
- `git`
- `GitGutter`
- `MarkdownTOC`
- `MarkdownPreview`
- `SublimeLinter-pylint`
- `WordCount`

<a id="preferences----settings----user"></a>
### Preferences --> Settings --> User

```java
{
	// Font stuff
    "font_face": "menlo regular",
    "font_size": 13,

    // Ignore the Vintage package as editing with vi keys
    // is of no interest
    "ignored_packages":
    [
        "Vintage"
    ],

    // Hide overview thing on right by default as it just takes up space
    // You'll probably have to toggle it once manually too
     "show_minimap": false,

    // These help to avoid thinking that you've made changes
    // when all that has changed is a random space or a newline
    // at the end of the file
	"trim_trailing_white_space_on_save": true,
	"ensure_newline_at_eof_on_save": true,

	// Rulers which are enabled by default. These help with
	// line length considerations
    "rulers":
    [
        80,
        100,
        132,
    ],

    // Default word wrap when Sublime is opened, can be changed
    // as is useful
    "word_wrap": true,
    "wrap_width": 80,

    // This ensures that you don't lose your work because you
    // forgot to save and clicked on something else
    "save_on_focus_lost": true,

    // PEP8 for Python and can be overridden for specific syntax
    // as required
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
}
```

<a id="makefile-preferences----settings----syntax-specific"></a>
#### Makefile Preferences --> Settings --> Syntax Specific

```java
{
	"translate_tabs_to_spaces": false,
}
```

<a id="preferences----key-bindings"></a>
### Preferences --> Key Bindings

```java
[
	// Duplicate a file
	{ "keys": ["super+shift+d"], "command": "clone_file"},

	// Same as defaults but worth highlighting
	// This moves your focus/cursor to the first window in your view
	// (e.g. first column or first row)
	{ "keys": ["ctrl+1"], "command": "focus_group", "args": { "group": 0 } },
	// This moves your focus to the second window (etc. etc. for third, fourth...)
	{ "keys": ["ctrl+2"], "command": "focus_group", "args": { "group": 1 } },
	// This moves your current tab to the first window
	{
		"keys": ["ctrl+shift+1"],
		"command": "move_to_group",
		"args": { "group": 0 }
	},
	// This moves your current tab to the second window (etc. etc. for third, fourth...)
	{
		"keys": ["ctrl+shift+2"],
		"command": "move_to_group",
		"args": { "group": 1 }
	},

	// Toggle word wrap on and off. Here you have to press "ctrl+k", then keep
	// holding "ctrl" but let go of "k", then press "r"
    {
        "keys": ["ctrl+k","ctrl+r"],
        "command": "toggle_setting",
        "args": { "setting": "word_wrap" }
    },

    // Set word wrap to 72 characters
    {
        "keys": ["ctrl+k","ctrl+1"],
        "command": "set_setting",
        "args": { "setting": "wrap_width", "value": 72 }
    },
    // Set word wrap to 80 characters
    {
        "keys": ["ctrl+k","ctrl+2"],
        "command": "set_setting",
        "args": { "setting": "wrap_width", "value": 80 }
    },
    // Set word wrap to 132 characters
    {
        "keys": ["ctrl+k","ctrl+3"],
        "command": "set_setting",
        "args": { "setting": "wrap_width", "value": 132 }
    },

    // Same as defaults but worth highlighting how this works
    // Set screen layout to a single screen
    {
		"keys": ["super+alt+1"],
		"command": "set_layout",
		"args":
		{
			// This defines where you want your column lines to be
			// The units are fractions of the screen width from the left so
			// 0.0 is the left edge, 1.0 is the right edge, 0.5 is in the
			// middle, 0.25 is a quarter of the way across from the left
			"cols": [0.0, 1.0],
			// This defines where you want your row lines to be
			// The units are fractions of the screen width from the top so
			// 0.0 is the top, 1.0 is the bottom, 0.5 is in the
			// middle, 0.25 is a quarter of the way down the screen
			"rows": [0.0, 1.0],
			// This defiens where you want the top-left and bottom-right
			// corners of each cell to be. The values refer to indexes
			// of the "cols" and "rows" lists we defined above. Hence the
			// overall cell syntax is
			// [top-left column index, top-left row index,
			//	bottom-right column index, bottom-right row index]
			// For easier use, I generally try and set the cells list out how I
			// expect the final screen to look (see more examples below)
			"cells":
			[
				[0, 0, 1, 1]
			]
			// This produces a single cell. Its top-left corner is located at
			// (cols[0], rows[0]) and its bottom-right corner is located at
			// (cols[1], rows[1]) which in this case means it takes up the
			// entire screen
		}
	},

	// Same as defaults
    // Set screen layout to two columns
    // (See single screen key binding for explanation)
    {
		"keys": ["super+alt+2"],
		"command": "set_layout",
		"args":
		{
			"cols": [0.0, 0.5, 1.0],
			"rows": [0.0, 1.0],
			"cells":
			[
				[0, 0, 1, 1], [1, 0, 2, 1]
			]
		}
	},

	// Same as defaults
    // Set screen layout to three columns
    // (See single screen key binding for explanation)
    {
		"keys": ["super+alt+3"],
		"command": "set_layout",
		"args":
		{
			"cols": [0.0, 0.33, 0.67, 1.0],
			"rows": [0.0, 1.0],
			"cells":
			[
				[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]
			]
		}
	},

	// Same as defaults
    // Set screen layout to four columns
    // (See single screen key binding for explanation)
    {
		"keys": ["super+alt+4"],
		"command": "set_layout",
		"args":
		{
			"cols": [0.0, 0.25, 0.5, 0.75, 1.0],
			"rows": [0.0, 1.0],
			"cells":
			[
				[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1], [3, 0, 4, 1]
			]
		}
	},

	// Same as defaults
    // Set screen layout to a 2 x 2 grid
    // (See single screen key binding for explanation)
    {
		"keys": ["super+alt+5"],
		"command": "set_layout",
		"args":
		{
			"cols": [0.0, 0.5, 1.0],
			"rows": [0.0, 0.5, 1.0],
			"cells":
			[
				[0, 0, 1, 1], [1, 0, 2, 1],
				[0, 1, 1, 2], [1, 1, 2, 2]
			]
		}
	},

    // Set screen layout to 2 columns with
    // 1 row in the left column, 2 rows in the right column
    {
        "keys": ["alt+super+6"],
        "command": "set_layout",
        "args":
        {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells":
            [
                [0, 0, 1, 2], [1, 0, 2, 1],
                			  [1, 1, 2, 2]
            ]
        }
    },

    // Set screen layout to 2 columns with
    // 2 rows in the left column, 1 row in the right column
    {
        "keys": ["alt+super+7"],
        "command": "set_layout",
        "args":
        {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells":
            [
                [0, 0, 1, 1], [1, 0, 2, 2],
                [0, 1, 1, 2]
            ]
        }
    },

    // Set screen layout to 3 rows
    {
        "keys": ["alt+super+8"],
        "command": "set_layout",
        "args":
        {
            "cols": [0.0, 1.0],
            "rows": [0.0, 0.33, 0.67, 1.0],
            "cells":
            [
                [0, 0, 1, 1],
                [0, 1, 1, 2],
                [0, 2, 1, 3],
            ]
        }
    },

    // Set screen layout to 2 rows
    {
        "keys": ["alt+super+9"],
        "command": "set_layout",
        "args":
        {
            "cols": [0.0, 1.0],
            "rows": [0.0, 0.5, 1.0],
            "cells":
            [
                [0, 0, 1, 1],
                [0, 1, 1, 2],
            ]
        }
    },
]
```

<a id="snippets"></a>
### Snippets

`Makefile_var.sublime-snippet`

```xml
<snippet>
    <content><![CDATA[
${1:VARIABLE}=${2:value}
$0@echo ${1:VARIABLE}: $(${1:VARIABLE})
]]></content>
    <tabTrigger>var</tabTrigger>
    <scope>source.makefile</scope>
    <description>Variable definition. Autogenerates code for `make variables` rule.</description>
</snippet>

```

<a id="snippets-1"></a>
## Snippets

<a id="medium-guide-to-sublimetext-snippets"></a>
### Medium Guide to SublimeText Snippets

- available [online](https://medium.freecodecamp.org/a-guide-to-preserving-your-wrists-with-sublime-text-snippets-7541662a53f2)
- free
- ease of use: high
- recommendation: high
- length: (short < 10 minutes)

<a id="package-guide"></a>
## Package Guide

<a id="markdownpreview"></a>
### MarkdownPreview

Super useful package to let you preview markdown documents as you write. There's heaps to read about this at [https://facelessuser.github.io/MarkdownPreview/usage/]() I'd be super interested if anyone has found a plugin which does live preview (rather than just preview on demand).

<a id="sublimelinter-pylint"></a>
### SublimeLinter-pylint

<a id="installation"></a>
#### Installation

- Follow [online instructions](https://github.com/SublimeLinter/SublimeLinter-pylint) to install the `pylint` python package (either python2 or python3) with `pip`
- then do `package control: install package` --> `SublimeLinter`
- then do `package control: install package` --> `SublimeLinter-pylint`
- then fix the path settings for this package, `SublimeText` --> `Preferences` --> `Package Settings` (follow this http://www.sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable)
    - e.g.

```
{
	"paths": {
	    "linux": [],
	    "osx": [
	        "/usr/local/bin/pylint"
	    ],
	    "windows": []
	}
}
```
