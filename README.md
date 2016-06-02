# Py4Eng

A Python programming course for Matlab users.

I'm Yoav Ram I develop and give [Python training](http://python.yoavram.com) for engineers, scientists, and everyone else.

This is the course website source code.

# Setup an Environment

Download Anaconda. The course uses Python 3.5 but will work with Python 3.4, too. 
You can create a new environment:

```sh
conda update -y -n conda
conda create -y -n Py4Eng python=3.5 ipykernel
activate Py4Eng
```

If you created an environment then you should setup it up as an IPython kernel:

```sh
python -m ipkernel install --name Py4Eng
```

Now, install required packages.
If you didn't create a dedicated environment, start with:

```sh
conda update -y -q conda
```

and add the [conda-forge](https://conda-forge.github.io/) channel:

```sh
conda config --add channels conda-forge
```

Now install the packages:

```sh
conda install -y -q requests jupyter notebook ipywidgets numpy scipy matplotlib pandas seaborn scikit-learn scikit-image sympy flask=0.10 click
conda install -y -q basemap 
conda update -y -q pip
pip install sdeint ipdb
```

Troubleshoot: 
- there is no conda support for Basemap with Python 3 on Windows, so you should download a wheel file from [Gohlke's site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#basemap) and install with `pip install basemap-1.0.8-cp35-none-win_amd64.whl`.

# Start an interactive session

Open a terminal window (`cmd.exe` in Windows), find the folder in which you put the course material.
If you created a dedicated conda environment, activate it with `activate Py4Eng`. 
Then start the notebook server with `jupyter notebook`. The sessions will be inside the `sessions` folder.

# License

`LICENSE.md` for everything unless otherwise mentioned.
