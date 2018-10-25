SublimeText3
============

Overview
--------

A bunch of tips and tricks about how to use Sublime Text 3.


Command line alias
------------------

Mac
~~~

Add alias in `~/.bashrc`

``alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"``


Setting up
----------

Open up Sublime Text

- install package control
    - `cmd` + ``shift`` + ``p``, ``install package control``


Zeb's recommended packages for climate science
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Fortran
- Git
- GitGutter
- SublimeLinter-pylint
- OmniMarkupPreview


Package guide
-------------

MarkdownPreview
~~~~~~~~~~~~~~~

Super useful package to let you preview markdown documents as you right.
There's heaps to read about this at `<https://facelessuser.github.io/MarkdownPreview/usage/>`_.
I'd be super interested if anyone has found a plugin which does live preview well (rather than just preview on demand).

SublimeLinter-pylint
~~~~~~~~~~~~~~~~~~~~

Installation
++++++++++++

- follow the `online instructions <https://github.com/SublimeLinter/SublimeLinter-pylint>`_ to install the `Pylint <https://github.com/PyCQA/pylint>`_ python package (either python2 or python3) with `pip` [add link to pip guide]
- then do ``package control: install package`` --> ``SublimeLinter``
- then do ``package control: install package`` --> ``SublimeLinter-pylint``
- then fix the path settings for this package, ``SublimeText`` --> ``Preferences`` --> ``Package Settings`` (follow `this guide <http://www.sublimelinter.com/en/latest/troubleshooting.html#finding-a-linter-executable>`_ )

    - for example

        ::

            {"paths": {
                "linux": [],
                "osx": [
                    "/usr/local/bin/pylint"
                ],
                "windows": []
            }}
