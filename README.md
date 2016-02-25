# Py4Eng

A Python programming course for Matlab users.

This is the course website source.

The website is currently hosted by github pages at <http://amat.yoavram.com>.

I'm Yoav Ram I develop and give [Python training](http://python.yoavram.com) in Academia and Industry.

# Setup an Environment

Download Anaconda. The course assumes Python 3.5 (will work with Python 3.4, too). 
You can create a new environment:

```
conda update -y -n conda
conda create -y -n Py4Eng python=3.5
activate Py4Eng
```

If you created an environment then you should setup it up as an IPython kernel:

```
ipython kernel install --name Py4Eng
```

Now, install required packages.
If you didn't create a dedicated environment, start with:

```
conda update -y -q conda
```

Now install the packages:

```
conda install -y -q requests jupyter notebook ipywidgets numpy scipy matplotlib pandas seaborn scikit-learn scikit-image sympy 
conda install -y -q basemap 
conda update -y -q pip
pip install sdeint ipdb
```

Troubleshoot: 
- if you get 404 for some package, try installing with `-c anaconda`
- there is no conda support for basemap with for python 3 on Windows, so you should download wheel from [Gohlke's site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#basemap) and install with `pip install basemap-1.0.8-cp35-none-win_amd64.whl`.

# Start an Interactive Session

Open a terminal window (`cmd.exe` in Windows), find the folder in which you put the course material.
If you created a dedicated conda environment, activate it with `activate Py4Eng`. 
Then start the notebook server with `jupyter notebook`. The sessions will be inside the `sessions` folder.

# License

`LICENSE.md` for everything unless otherwise mentioned.