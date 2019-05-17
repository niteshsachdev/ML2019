"""
GIT Commands
"""
# Why git and what git can do
# Install git locally and Goto Github and create an account
# Create a new empty remote repo on Github with ForskLabs, which should be Public and click create repository
# copy the HTTPS URL of repo ( https://github.com/neuerung/ForskLabs.git  )
# Goto terminal or Command Prompt and change directory to the desktop 
# git clone https://github.com/neuerung/ForskLabs.git as to clone as a local repo 
# Change directory to FoskLabs
# create a test.py file on desktop/ForskLabs
# git config user.email "sylvester@neuerung.co.in"
# git config user.name "Dr. Sylvester Fernandes"

# Example to understand the concept 
# git add test.py 
# git commit -m "Added new file"
# git status #whether it is nothing to commit
# git push
# Goto github.com and refresh your page to see the test.py


# Onetime Workflow for old files
# Add all the files in the new folder
# git add --all
# git commit -m "Adding all files"
# git status
# git push
# Goto github.com and refresh your page to see all the files


# Everyday Workflow for new files
# git add <filename>
# git commit -m "Added new file"
# git status #whether it is nothing to commit
# git push
# Goto github.com and refresh your page to see all the new file added


# How to ignore files in git
# https://github.com/github/gitignore/blob/master/Python.gitignore

# Download the file from the above link and store in the project directory 
# Rename the file to .gitignore



18. Goto Github, edit and commit changes
19. git pull
20. Edit locally and git add test.py and git commit -m "Did some changes"
21. git push


22. Goto Github, edit and commit changes 
23. Edit locally and git add test.py and git commit -m "Did some more changes"
24. git pull
25. Merge Conflicts needs to be solved
26. Open Locally and edit, remove all <<<<<, ====== and >>>>>> and solve the error
27. git add <filename>
28. git commit -m "Fix Merge Conflict"
29. git push

30. git log ( history of commit )
31. git reset --hard <commit>   ( to have a copy of the commit number )
32. git reset --hard origin/master ( to have a fresh copy as you started )  


33. Messed working but NOT staged git checkout HEAD path/to/file
34. Messed working (but staged) git reset HEAD path/to/file and then git checkout HEAD path/to/file
35. Messed working (staged and commit)  git checkout HEAD^ path/to/file


36. git reflog ... # http://ohshitgit.com/
