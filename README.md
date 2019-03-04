# ICS3U1d-2018-19
Repo for ICS3U1 Spring 2019 notes and examples.  This is not an assignment repository.  Please see specific assignment details for the proper repository to be creating/submitting your work.

[Getting Things Set Up](https://github.com/StRobertCHSCS/ICS4U1c-2018-19#getting-things-set-up)  
[Day to Day Procedures](https://github.com/StRobertCHSCS/ICS4U1c-2018-19#day-to-day-procedures)  
[Changing/Checking the Git User](https://github.com/StRobertCHSCS/ICS4U1c-2018-19#changing-the-git-user-name)  
[Settings Things Up at Home](https://github.com/StRobertCHSCS/ICS4U1c-2018-19#settings-things-up-at-home)  
 

## Getting Things Set Up

### 1) Fork this repository
* From the upstream(parent) repository (StRobertCHSCS/ICS4U1c-2018-19), click on *Fork* at the top right of your screen.
* Choose your account to fork to.

### 2) Clone your Fork
* From *your* fork [your_account]/ICS4U1c-2018-19, click on the **Clone or Download** button (the green one on the right) and copy the URL
* In Pycharm, go to VCS --> Checkout from Version Control --> Git or from the Pycharm Welcome screen just Checkout from Version Control --> Git
    * in the pop up that follows, paste in the URL and hit Clone
    
### 3) Set Up the `upstream` remote
Do this when there are updates to pull from the upstream(parent) repository StRobertCHSCS/ICS4U1c-2018-19 (not your fork)
* first you will need to add and upstream remote (you only need to do this once)
    * In Pycharm, VCS -> Remotes ... -> click + to add a remote
    * In the popup:
        * Name: *upstream*
        * URL: https://github.com/StRobertCHSCS/ICS3U1d-2018-19.git

## Day-to-Day Procedures

### 1) Beginning Your Session

* Pull your changes from github: VCS -> pull ... -> select *origin* -> pull
* Pull changes from the upstream: VCS -> pull ... -> select *upstream* (select to merge the *upstream/master*) -> pull

### 2) During your session
#### Commit Changes
* make the necessary changes to your code or other project files
* In the terminal (make sure you are in the directory of your project (type `pwd` on the terminal to verify your current directory):
* add files for tracking: VCS -> add -> choose files that you will be editing
* commit changes: VCS -> commit ... > choose the files to commit, enter a short meaningful message in present tense about your changes`


### 3) At the end of your session
* Do a final commit (see above)
* Push your changes to github: VCS -> Push ... -> select origin --> Push



## Other Things
### Changing the git user name
Before you make any changes when working on the school laptops (class chromebooks),  it's a good idea to check that you are the current git user.
* To check the current git user: `git config user.name`
* To change the current git user:
```text
git config user.name "your_git_username"
git config user.email "your_git_account_email"

```

### Settings Things Up at Home
1) Install git and make necessary settings/preferences changes in Pycharm (see instructions posted in class)
2) Follow the steps above starting from **2) Clone Your Fork**
3) Day-to-day procedures are the same as above
