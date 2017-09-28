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
following SED is a regular expression that removes dollar signs

* s/ —> SEARCH (as opposed to find/replace)
* \$ escape character before $ because $ has meaning
* //

**use single quotes**

**grep** is used to search text for a match, in this case ‘,POLICE,’ and then DETECTIVE *(DETECTIVE doesn't need quotes because it begins and ends with a normal letter)*

**wc** is word count
*-l option print the number of lines in a file*

**pipe** | forwards the output to the next command
