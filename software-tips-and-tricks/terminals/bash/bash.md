# bash

<!-- MarkdownTOC autolink="true" autoanchor="true" markdown_preview="github" -->

- [Overview](#overview)
- [`bash_profile` vs `bashrc`](#bash_profile-vs-bashrc)

<!-- /MarkdownTOC -->

<a id="overview"></a>
## Overview

A bunch of tips and tricks about how to use the bash shell. 

<a id="bash_profile-vs-bashrc"></a>
## `bash_profile` vs `bashrc`

Read this which explains how things are a bit weird: [https://apple.stackexchange.com/questions/12993/why-doesnt-bashrc-run-automatically?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa]()

Basically, `bash` does not use `~/.bashrc` for login shells, only for non-interactive shells. Hence why it's standard advice to put 

```
if [ -s ~/.bashrc ]; then
    source ~/.bashrc;
fi
```

in `~/.bash_profile`.