# SublimeText3

<!-- MarkdownTOC autolink="true" autoanchor="true" markdown_preview="github" -->

- [Overview](#overview)
- [Command Line Alias](#command-line-alias)
- [Setting up](#setting-up)
- [Zeb's Settings](#zebs-settings)
	- [Recommended Packages for Climate Science](#recommended-packages-for-climate-science)
	- [Preferences --> Settings --> User](#preferences----settings----user)
	- [Preferences --> Key Bindings](#preferences----key-bindings)
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
	"font_size": 13,
	"ignored_packages":
	[
		"Vintage"
	],

	"trim_trailing_white_space_on_save": true,
	"ensure_newline_at_eof_on_save": false,
}
```

<a id="preferences----key-bindings"></a>
### Preferences --> Key Bindings

```java
[
	// Duplicate a file
	{ "keys": ["super+shift+d"], "command": "clone_file"}
]
```

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