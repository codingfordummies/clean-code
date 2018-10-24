# Python environment management

**Zeb's tips**

The easiest way to manage environments with conda [add link] and pip. Whilst these two aren't completely compatible, I've never found a case where they've failed me.

This is how I set up my environments.

Firstly, install conda [add instructions].

Then make sure that you never ever install anything into your base conda environment, that is a recipe for disaster and confusion.

Next, make an environment with the following command

```
conda create --name [env-name] pip
```

This tells conda to create an environment called `[env-name]` and to install pip in that environment. Next activate the environment with `conda activate [env-name]` (in old versions of conda it has to be `source activate [env-name]`) If you now do

```
which pip
```

it should give you a path like `/Users/username/miniconda3/envs/env-name/bin/pip` which allows you to confirm that your environment is also using a version of pip which is specific to that environment. This helps you to manage your packages and avoid clashes. If you get an output like `/Users/username/miniconda3/bin/pip` then you are still using your base environment's version of pip and the setup hasn't worked. If this is the case, don't proceed, try and work out what is wrong (reinstall conda, remake your environment, reactivate it, try again).

Now you can install all the Python packages you need. In general, I conda install everything I can, falling back to pip only where the package isn't available via conda (or conda-forge [add conda-force use explanation]) or the package installed via conda is broken (one example I've seen is Matplotlib on windows).
