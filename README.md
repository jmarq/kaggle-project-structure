# Experimenting with Kaggle directory setup

my experience with Kaggle so far has me: 
- trying out some pandas/numpy/etc code in the console to manipulate and get a feel for the data
- writing helper scripts for transforming the data
- writing model scripts that use trasnformed data to train/run ML models
- getting kind of sloppy as I copy and paste files and comment/uncomment code to try out different features/models

I was ending up with a big flat folder full of scripts that were getting out of control. I am now wondering how I might reign in some of this emerging mess. Are there some conventions I can follow to ease some of my cognitive burden? maybe make better use of python modules?

as a simple start, I created a project module folder (`titanic`, here) with submodules for feature engineering and model creation, a main.py file that imports from it, and a ipynb notebook file for interactive exploratory work (accessible by running `jupyter notebook` from the root directory of the project)

This is still probably too simplistic and naive. As I continue to work on kaggle problems, perhaps this directory structure convention project will adopt some of my learnings.

(as of now, this does not contain any real project data/features/models. just placeholders)

currently working on a cookiecutter branch that would allow using this template via cookiecutter cli
`cookiecutter git+ssh://git@github.com/jmarq/kaggle-project-structure --checkout cookiecutter`