# COMP0034 Lab 1: Starting coursework 1

## Accept the GitHub Classroom assignment

Assignment links are in the Assessment section on Moodle only to maintain them in a single location.

Students working on the coursework as an individual assignment should accept the GitHub Classroom assignment for
coursework 1.

Students working on the coursework as a group assignment:

- _One group member only_: accept the GitHub Classroom assignment for coursework 1 and create a group name. The group
  name must match the group name on Moodle.
- _All other group members_: accept the GitHub Classroom assignment for coursework 1 and select the same group name that
  the person above just created.

## Set up the repository in your IDE

Each person should do this.

1. Clone the repository you created above in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in
   your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
   or [Cloning a repository in VS Code](https://code.visualstudio.com/docs/editor/github#_cloning-a-repository)
2. Add a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [use python in your shell.](https://pip.pypa.io/en/latest/user_guide/#requirements-files)
4. Edit .gitignore to add any config files and folders for your IDE. PyCharm, VisualStudio Code, Xcode and NetBeans have
   already been added.
5. Copy the prepared data set from COMP0035 coursework to this repository. You may need to use 'git add' to add the file
   to be tracked by git.
6. Commit and push the data set to GitHub. This is your first commit for coursework 1. Remember to use source code
   control throughout the coursework.

## Check that you can run a Dash app

`dash_app.py` has been included to allow you to test that your project set up is sufficient to run Dash. Once you are
happy that you have set up the project then you should delete the contents of app.py and replace with your coursework
code.

- To run the dash app from the terminal or shell, make sure you are in directory of your repository and type and
  run `python dash_app.py`
- To run the dash app from PyCharm, right-click on the file name `dash_app.py` in the Project pane and
  select `Run dash_app`. Or open `dash_app.py` and click on the green run arrow near line 29.
- To run the dash app from VS Code, use the Run option from the left pane.

By default, the dash app should launch on port 8050 of your localhost with the IP address 127.0.0.1:8050. Open the URL
in a browser [http://127.0.0.1:8050](http://127.0.0.1:8050/).

Note: If you get an error like this:

```text
OSError: [Errno 48] Address already in use
``` 

then another application is already using the default port (this will also happen if you forget to stop a previous Dash
app and try to start another!). You can try another port by modifying the line of code that runs the Dash app to specify
a different port number e.g.

```python
app.run_server(debug=True, port=1337)
```

## Start the coursework

1. Read the coursework specification on Moodle.
2. Copy your target audience description e.g., persona(s), from COMP0035 coursework 1 into your coursework repository
   into a suitable directory.
3. Copy the questions you intend to answer from COMP0035 coursework 1 into your repository (e.g. copy and paste them to
   the COMP0034 coursework 1 markdown).
4. Select one question from your list.
5. Review the chart types and consider which might be suitable for the audience and question.

    - [The Data Visualisation Catalogue](https://datavizcatalogue.com/index.html)
    - [Interactive Chart Chooser](https://depictdatastudio.com/charts/)

6. If you have read the week 1 materials, consider the design (layout, colours, titles, use of whitespace etc.) for your
   chart.