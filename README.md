## Instructions
### Setup
To get started, you need to:
1. Clone this GitHub repository to your local machine
2. Run `make html` in the project's parent directory, which will the website using the `.md` files. If this works, you're all set! If this does not, continue to the next step.
3. Run `pip install sphinx`, then run `pip install recommonmark`, and finally run `pip install sphinx-rtd-theme`. Try running `make html` again. If this fails, ask a previous crash course developer to help you troubleshoot.


### Development
To create a new lesson you need to perform the following steps:
1. Create a new `.md` file under the `source` directory. You should name it something like `#_LessonName.md`.
2. Open `index.rst` and add the name of the `.md` file you created to the existing list. You should keep `About This Course` as the last entry in the list. Keep in mind that indentation matters!
3. Create your lesson in the `.md` file. When you want to view your changes, run `make html` in the project's parent directory (above `source`) 
4. Push your changes to GitHub. The web server will automatically register the changes and rebuild. (This might take a few minutes.)

Please do not change the `About This Course` page without consulting <a href="https://sabeelmansuri.com/" target="_blank">Sabeel</a>!
