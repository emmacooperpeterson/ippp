## Thursday TA sessions will be 4:30-6:00 from now on!

#### 1. Relationship between things
* Atom <-> Word
* Terminal <-> Explorer/Finder
* Python/Bash <-> French
* Git <-> Canvas

#### 2. Process
* cd to folder you want it in (maybe mkdir to make a new directory)
* git clone
* cd into the directory you just cloned “01-welcome”
* atom “name_of_file”
* run (./salaries.sh in the terminal)
* add/commit/push (commit often & w good messages)
* for submission: fill in solutions file manually and push

#### 3. Homework Q8: How many of them are detectives?

echo "(8) DETECTIVES"

cat $f | sed 's/\$//' | sed "s/, / /" | grep ',POLICE,' | grep DETECTIVE | wc -l

echo

**echo** is a print statement

**cat** to view file

**sed** “stream editor” - allows you to filter and transform text

following **sed** is a **regular expression** that removes dollar signs

* s/ —> SEARCH (as opposed to find/replace)
* \$ escape character before $ because $ has meaning
* //

***use single quotes***

**grep** is used to search text for a match, in this case ‘,POLICE,’ and then DETECTIVE *(DETECTIVE doesn't need quotes because it begins and ends with a normal letter)*

**wc** is word count
*-l option print the number of lines in a file*

**pipe** | forwards the output to the next command

*****

### Installation issues (Mac geos problem) - Jamie's notes below

1. We did need geos.  Do this first.

* ruby -e "$(curl -fsSL
https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

* brew install geos

2. Turns out not to work in the main environment.  (WTF)
3. We tried installing Anaconda 3.4 and creating environments for 3.4 and 3.6.  **The one for 3.6 worked, with just "conda install -c conda-forge geopandas")**
4. I then reverted to Anaconda 3.6, which didn't work.  But creating an additional python=3.6 environment off of it did.
5. So I thought maybe all the extra Anaconda gunk was messing us up, and switched to Miniconda, but the default 3.6 didn't work.
6. But the env off of that did.  

*****

**conda create -n py36 python=3.6**

**source activate p36**

**conda install -c conda-forge geopandas**

**conda install --channel=conda-forge nb_conda_kernels**

**source deactivate**

7. Since I did this from Miniconda, I'm not sure if this part is necessary, but ...
8. We need to be able to switch jupyter notebook kernels as conda environments, instead of just python versions.  This was no longer working, and it sounds like it may not be shipping anymore as a conda default.
9. Anyway, the way to fix it is --

**conda install nb_conda**

**conda install ipython**

**conda install -c conda-forge nb_conda_kernels**
