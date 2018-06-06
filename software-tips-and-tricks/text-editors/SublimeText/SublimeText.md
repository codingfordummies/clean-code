# SublimeText3

<!-- MarkdownTOC autolink="true" autoanchor="true" markdown_preview="github" -->

- [Overview](#overview)
- [Command Line Alias](#command-line-alias)
- [Setting up](#setting-up)
- [Zeb's Recommended Packages for Climate Science](#zebs-recommended-packages-for-climate-science)
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

<a id="zebs-recommended-packages-for-climate-science"></a>
## Zeb's Recommended Packages for Climate Science

- `Fortran`
- `git`
- `GitGutter`
- `MarkdownTOC`
- `MarkdownPreview`
- `SublimeLinter-pylint`
- `WordCount`


<a id="package-guide"></a>
## Package Guide

<a id="markdownpreview"></a>
### MarkdownPreview

Super useful package to let you preview markdown documents as you right. There's heaps to read about this at [https://facelessuser.github.io/MarkdownPreview/usage/]() I'd be super interested if anyone has found a plugin which does live preview (rather than just preview on demand).

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