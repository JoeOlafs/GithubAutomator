<h1>GithubAutomator</h1> 

This program simplifies and speeds up process of creating new projects.

This program is setup for Windows and meant to be used through CMD

<h2><b>How it works?</b></h2>

Type into CMD: 

<code class="docutils literal"><span class="pre">Project projectName fileEnding</span></code>

In order for this to work you need to add your personalised Github Token and a directory of your chosing to Environments.

In order to create a local project, simply add 'local' to the end of your command and the project will not be uploaded to Github: 

<code class="docutils literal"><span class="pre">Project projectName fileEnding local</span></code>

Additionally, if you do not have the Github API installed already.
Run in CMD: 

<code class="docutils literal"><span class="pre">pip install pygithub</span></code>



This is not my idea and some of the code is taken from the original project. However I have changed some parts in order to get the function as I wanted it to be. 
This program from Kalle Hallden and I used it to learn more about programming and command line. 
In addition I added in the function of creating a 'main' file for the programming language you 
Link to original project: https://github.com/KalleHallden/ProjectInitializationAutomation