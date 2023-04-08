# How to Contribute to this project

## Getting started
Anyone can contribute to this project despite your python skill level(Beginner, Intermediate or Expert)

If you are a newbie to open source, you can learn  [ how to contribute to projects](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)

## Opening an issue
- If you have suggestions on scripts feel free to open an issue. 
Please search for your issue or question briefly in our issues before opening a new one to help us avoid duplicates.
- If you are experiencing any bug in any of the scripts, feel free to open an issue.

## Fixing an Issue
Please indicate in a comment if you wish to resolve an existing issue. This is to abstain from having more than one person working on a particular issue.

## Creating Pull request
1. Fork this repo, then clone it
```
$ git clone https://github.com/FaithKovi/Automation-with-python.git
$ cd Automation-with-python
$ git remote add upstream https://github.com/FaithKovi/Automation-with-python.git
```
2. Create a new branch
```
$ git checkout -b my-new-branch
```
3. Make your changes

4. Commit your changes. Use a descriptive commit message
```
$ git add .
$ git commit -s -m "commit message"
$ git push -u origin my-new-branch
```
5. Submit a pull request

Once we have a chance to review your PR, it can either be marked as "needs review" and specific feedback will be provided or we can complete the pull request.

## Syncing with the repository
Keep in mind to regularly synchronize your fork with the main branch. To do this: Ensure you are in the root folder of the project and the branch should be main branch and type
```
$ git remote add upstream https://github.com/FaithKovi/Automation-with-python.git
```
Now that your upstream is set up on your local machine, whenever you need to create a new branch to make changes, make sure your main branch is in sync with the main repository by typing:
```
$ git pull upstream master
$ git push origin master
```

## Resources
- [What is Open Source](https://opensource.com/resources/what-open-source)
- [How to contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [How to write a good commit message](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)


