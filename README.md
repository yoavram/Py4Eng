# Py4Eng

A Python programming course for MATLAB® users.

I'm Yoav Ram I develop and give [Python training](http://python.yoavram.com) for engineers, scientists, and everyone else.

This is the course website source code.

[Contact me](mailto:yoav@yoavram.com) if you are interested in Python workshops anywhere in the world!

# Setup an Environment

Download Anaconda. The course uses Python 3.6 but will work with Python 3.4/3.5, too. 

You can create a new environment:

```sh
conda config --add channels conda-forge
conda update conda pip
conda env create -n Py4Eng -f environment.yml
```

# Start an interactive session

Open a terminal window (`cmd.exe` in Windows), find the folder in which you put the course material.
If you created a dedicated conda environment, activate it with `activate Py4Eng` (prepend with `source` if on Mac/Linux).
Then start the notebook server with `jupyter notebook`. The sessions will be inside the `sessions` folder.

# License

`LICENSE.md` for everything unless otherwise mentioned.
