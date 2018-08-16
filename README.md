# Behave-Selenium-Python test framework overview.

## I. Parts of the framework:
        1. Java (programming language)
        2. TestNG (testing framework)
        3. Maven (build automation tool)
        4. Selenium Webdriver (webui)
        5. unirest (API HTTP requests)
        6. <3 Selenoid & Selenoid-UI (selenium HUB & UI)
        7. Appium. Mobile tests.
    
        x. Allure Framework (reports)
        y. Jenkins (CI Server)
        z. Git (version control)

## II. Git intro:
        1. What is GIT? / Git workflow - https://backlog.com/git-tutorial/git-workflow/
        2. Repo init, git remote add origin git@github.com:f1r3ok/skywind-git-workshop.git, pull, fetch (https://github.com/f1r3ok/skywind-git-workshop)
        3. New file (untracked, Work Tree), add (Staged, new, Index), commit (Committed) , push (tracked, Repository)
        4. Modify (Modified), 
            remove local, 
            remove from remote (rm --cached), 
            uncommit (reset HEAD^, https://stackoverflow.com/a/2846154/2417397), 
            revert (uncommit if pushed), 
            branch (link to a commit) / checkout (https://learngitbranching.js.org/), 
        5. Git in IDEA / rebase vs merge - Merge ONLY!
        6. Git stash. (Not a shelf)
        7. .gitignore (!)
        8. Git bash / config / alias / color
        z. Questions? Further actions.

        $ pip install allure-behave
        $ behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
        $ allure serve %allure_result_folder%

## III. BackOffice demo:
        1. Test-case overview
        2. Demo, reports
        3. Conclusion, questions, tea =)

## IV. Links:
        https://bitbucket.skywindgroup.com/projects/SQA/repos/sqa-autotests/browse
        http://ndpsoftware.com/git-cheatsheet.html
        https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf
        https://backlog.com/git-tutorial/git-workflow/
        https://learngitbranching.js.org/
        https://github.com/jlord/git-it-electron/releases/tag/4.3.3