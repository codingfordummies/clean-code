.. _scientific-computing:

Scientific computing
====================

Zeb's list of important tools
-----------------------------

.. _zeb-development-tools:

Development tools
+++++++++++++++++

This list of development tools is what Zeb relies on to develop scientific software reliably and reproducibly.
Links are included with each of these tools to useful starting points.

- Version control: `Git <http://swcarpentry.github.io/git-novice/>`_
- Automating repetitive tasks: `Make <https://swcarpentry.github.io/make-novice/>`_
- Virtual environments: `Conda virtual environments <https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c>`_

    - note the common gotcha that ``source activate`` has now changed to ``conda activate``
    - we use conda instead of pure pip environments because they help us deal with more complicated dependencies: if you want to learn more about pip and pip virtual environments, check out:

        - `this introduction <https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/>`_
        - `this longer piece <https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/>`_ which explains the details

- Tests: many available frameworks, here's `a link to testing intro that Zeb likes <https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest>`_

    - most of the time, a blend of `pytest <https://docs.pytest.org/en/latest/>`_ and the inbuilt Python testing capabilities works

- `Continuous integration (CI) <https://docs.travis-ci.com/user/for-beginners/>`_

    - `Travis CI <https://travis-ci.com/>`_ is a good choice but there are a number of good providers

- `Jupyter Notebooks <https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46>`_

    - simply installing ``jupyter`` (``conda install jupyter``) in your virtual environment is as good a way as any

- `Sphinx <http://www.sphinx-doc.org/en/master/>`_


Other tools
+++++++++++

Other tools also exist which are useful but not necessarily essential and not necessarily related to development.
Here we provide a list of these along with useful resources.

.. _regular-expressions:

- `Regular expressions <https://www.oreilly.com/ideas/an-introduction-to-regular-expressions>`_

    - `regex101.com <regex101.com>`_ to helps write and check regular expressions, make sure the language is set to Python to make your life easy!
