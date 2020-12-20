

<img src="static/images/mock-up-responsive.jpg">

# BouquetnBlooms

*Subscribe to have fresh BouquetnBlooms everyday*

*Deployed to [Heroku](https://flask-saute-and-skewers.herokuapp.com/) and stored in [Github](https://github.com/)*

<hr>

## Contents

- [Introduction](#introduction)
- [Aim](#aim)
- [Purpose](#purpose)
- [UX](#ux)
- [Planes](#planes)
- [Features](#features)
- [Technologies](#technologies)
- [Testing](#testing)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

<hr>

## Introduction

................................................

<hr>

### Aim

To create a full stack website that allows users to purchase a product or service.

Technologies to be used in the project are HTML/CSS/Javascript/Python3 and Django - v3.1.4.


### Purpose

BouquetnBlooms is a floristry website in which users can subscribe to have fresh bouquets of flowers delivered to them monthly.

All users to the site will see the websites services. However only registered users can subscribe and order.


<hr>


## UX

## User stories

There are three types of users for this website, 'User Stories' for each user are discussed below:

### Guest User

As a guest user I want to:
 - navigate around the site easily.
 - find a navigation bar that links to other pages when clicked. 
 - understand the sites purpose upon landing.
 - be able to view the sites basic offerings.
 - be able to click social media icons to link out to other BouquetnBlooms pages.
 - have the option to register to the site to be able to interact with the site, see more and make a purchase.

### Registered Account

As a registered user I want to:
 - see all site content.
 - log into the site easily.
 - log out successfully.
 - have buttons to click to login, log out and submit data.
 - be able to add services to my basket.
 - review the services in my basket before purchasing.
 - safe and secure area where I can add confidential data and payment details.
 - recieve and email when i've purchased something.
 - be able to cancel a subsription if I change my mind.
 - be notified of all my interactive actions.

### Admin User

As an admin user I want to:
- have full access to the site to ensure all content is viable.
- have access to be able to add more subscription offers to the site.
- edit any content posted by me.


### Website Owner

The website owner would like users of the website to:
-  Interact with the site.
-  Enjoy the site.
-  Find the site easy to register to and purchase a subscription.

The website owner would like the website design to: 
- be clean and crisp with visuals that are minimal and of soft colours yet with a striking bold balance.
- have professional images that creates an instant attraction to the site.
- have whitespace to create flow.
- be easy to navigate.
- have a footer containing social media icon links.
- show the sites headquarters address.

<hr>

## The 5 Planes of content strategy

### Strategy

- BouquetnBlooms is an e commerce website. It allows users to purchase a subscription. 
- The subscription is a one time payment and the subscription is then dispensed by the retailer.
- The site features the 3 core languages of web development HTML, CSS and Javascript, as well as Python and uses Django. 
- The project uses a ...................... database. 
- There is a clear brand to the site that draws users and entices further interaction.
- Users who discover BouquetnBlooms, love flowers and are excited to use the service.
- BouquetnBlooms has the potential to become an excellent revenue generating business site. 
- Adding additional features (blog, client reviews for example) and marketing the site well could mean BouquetnBlooms could generate even more revenues.
- During research there were other sites found that had the same 'subscription' concept, most offering a full inventory of products where as BouquetnBlooms overs just subscriptions. 


### Scope 

- The site was developed with the intention of allowing users to subscribe and purchase a monthly BouquetnBloom in any of the catergories.
- The database of choice to build with was ...............
- It was scoped to provide ease of use.
- It has minimal pages, however must it must house a home page, registration page, log in page, log out page and various category pages.
- Have and app that allowed users to purchase from the site.
- Be responsive on all devices.
- Be visually appealing that incorporated the beauty of flowers and blooms in the front-end design.


### Structure

- BouquetnBlooms site structure was created from the UX user stories - therefore developed with pages that were required to enable users to sign up and add data.
- All pages are designed identically each with the navbar, basket and account............
- The Home page has a banner that advises of an offer and bold text that introduces the site. 

- The Register page has a basic registration form with a button and a link to login if already registered.
- The Login page has a basic login form with a button and a link to register if not already a member. 
- Once logged in the Login page opens a Profile page, this shows a 'Welcome Back' text, a few enticing words and a links to the 'Add Recipe' 'Highlights' 'Recipes' Pages.
- If logged in, a user can see all .............. supscriptions on offer, with functionality to 'edit' or 'delete'.............

- Finally the Log Out page displays, a 'You have been logged out message' and the returns to the Log In page view.

### Skeleton

- Four wireframes where created - the three main pages of the site and a subscription page.....
- These Desktop and Mobile wireframes demonstrate the basic design and structure of the site and the required elements each page needed. 
- All wireframes were created using [Balsamiq](https://balsamiq.com/wireframes/).

Desktop:

[Home](wireframes/base-desktop.png)
[Register](wireframes/register-desktop.png)
[Login](wireframes/login-desktop.png)
[Subscription](wireframes/subscription-desktop.png)

Mobile:

[Home](wireframes/base-mobile.png)
[Register](wireframes/register-mobile.png)
[Login](wireframes/login-mobile.png)
[Subscription](wireframes/subscription-mobile.png)

### Surface 

Front-end visuals where based on:
 - A great brand design.
 - Soft pastel colours in wallpapers.
 - Vibrant and professional flower and bouquet images.
 - Enticing and positive text.
 - It is anticipated that the user would feel happy and positive on landing on the site and feel they wanted to purchase something even if that wasnt their intention.

The typography colours and fonts where important to promote a calming effect but with a tempting feel good reaction that made the want to fullfil the sites output fully.
With vibrant flower images in all colours the sites aim was to incorporate the many different seasonal blooms on offer into its design. 

BouquetnBlooms chose a simplistic design with whitespace so to not overpower the user.

 - colour: the text is - #555;  - from Colorcodehex 
 - font: developer chose - 'Lato' - from Google Fonts

<hr>

## Features 

### Existing Features

**Multiple pages:** The site has multiple responsive pages, using the mobile first approach. 

**User friendly:** Each page has its own purpose and uses a simple mouse movement on desktop and scroll movement on mobiles and tablets to provide easy navigation. 

**Fonts and Colours:** Simplistic design incorporating pastel colours with a striking navbar and minimal text.

**Navbar:** A Bootstrap fixed Navbar at the top on desktop on mobiles and tablets. The navbar links to the site pages, this changes dependent on the users status: Logged in, Logged out.

**Button:** Chosen from Bootstrap the buttons when clicked do something and confirm user actions. Buttons are big and small an of different colours and provide 'word' instruction. 

**Forms:** Code from Bootstrap. The Search Bar, Register and Log In pages all use forms and require the user to input data, these forms are self explanatory.
        
These forms have input fields and textareas that are set with min-length and max-length classes.......

**Icons:** Font Awesome icons are used throughout the site, account, basket and form fields to provide image instructions aswell as for design, the font awesome kit is used in the code. 

**Images:** Vibrant images are used in the design. Selected images provide an idea of the product on offer if you buy a subscription.

**Search Bar:** Have a 'Search' bar, so users can search for specific items using key words.


########################################

**Flash Messages:** Flash messages provide feedback to users. Users that have an unsuccessful login will receive the message "Incorrect Username and/or Password".
The 'Registered users' will see, "Welcome, USERNAME" on login and on logging out user will receive the message "You have successfully logged out".
Flash messages are also used for confirming a recipe has been added, edited and deleted.

**Favourites Toggle:** A Favourites Toggle for the user to highlight if a recipe is a user favourite.

**Hyperlinks:** There is a hyperlink on the 'Register page', 'Login page' to redirect users to an alternative area dependent on their next wanted action.

**Footer:** The footer provides a clear indication of the end of the page.

**Social Media Links:** BouquetnBlooms has various Social Media accounts therefore icons for these are found in the footer that will direct to the social site.


############################################

**Copyright:** Copyright logo - hosts the website owners own work.



############################################

### Future Features

BouquetnBlooms - Future features could include:

- Having a larger database of subscription packages for guest users to view and purchase.
- The subscriptions could be seasonal or weekly, have products with different price points.
- User profile to be created.......
- Have a logo, that adds to the BouquetnBlooms text into something more memorable.
- Add a favicon so the sites logo is displayed in the browser tab for ease of navigation.
- A review score of the subscriptions.
- Feedback section to provide users with feedback on the sites product and services.
- Forgotten password feature, so passwords can be reset.
- A blog that gives advise on how to care for your product and offer lessons on floristry.
- A messenger area where registered users can chat to a company employee live on the site.
- Expand the e commerce shop where users could order one time products and merchandise.

<hr>

## Technologies and Frameworks 


#### Technologies
- [HTML](https://www.w3schools.com/whatis/whatis_html.asp)
- [CSS](https://www.w3schools.com/css/css_intro.asp)
- [Javascript](https://www.w3schools.com/whatis/whatis_js.asp)
- [Python](https://www.python.org/doc/essays/blurb/)
- JSON

#### Frameworks
- [Django](https://www.djangoproject.com/)
    - The web application framework used in the project to allow fast and easy development of sites.

- [Werkzeug](https://palletsprojects.com/p/werkzeug/)
    - A web application library in Flask that was used to for secure authentication using password hashing.

- [Bootstrap](https://getbootstrap.com/)
    - A web based front-end framework that assists in responsiveness and styling that was used throughout the project.

- [JQuery](https://jquery.com/)
    - The JavaScript library used within the Materialize framework.

#### Database
- [........](https://www................../)
    - A document based database and the type of database used when developing this project

#### Text Editor
- [Gitpod](https://gitpod.io/)
    - A cloud based IDE, that uses prebuilt workspaces.

#### Version Control
- [Git](https://git-scm.com/)
    - Version control system that works within the Gitpod terminal. Used to commit and push recent code to GitHub.

#### Hosting Platform
- [Heroku](https://https://dashboard.heroku.com/)
    - The application platform used for the live deployed site.

- [Github](https://github.com/)
    - A repository store, used to house the sites repository.

#### Developer Tools
- [Google Dev Tools](https://developers.google.com/web/tools/chrome-devtools)

#### Colorcodehex
- [Colorcode](https://www.colorcodehex.com/022072.html)

#### Font Awesome
- [Font Awesome](https://fontawesome.com/)
    - Used for UX icons and getting 'kit' code.

#### RandomKeygen
- [RandomKeygen](https://www.randomKeygen.com/)
  - Site to select a secure SECRET_KEY password.

#### Validation sites
- [W3C Markup Validation](https://validator.w3.org/)
- [Jshint](https://jshint.com/)
- [PEP8](http://pep8online.com/)

<hr>

### Testing

Manual Testing was undertaken during the creation of this site. 
Testing included tests on various devices for responsiveness and UX aswell as testing code for bugs.
Code was validated for best practice.

 - Validation sites used:
   - W3C Markup Validator
   - Jshint
   - Pep8 Compliance

Below highlights the main issues, bugs and validation errors found during the development and how if possible the issues were rectified.
Some errors where not rectified, this was due to either lack of developer knowledge or due to time constraints for further reading of validation documentation and/or testing.


#### Issue 1

Issues with errors occurred when working on py files. I had to clear the errors Gitpod advised on. 
Most errors due to the 2 line spacing rule and using the tab key instead of spaces and also not entering to a new line.
Other errors included -*'lines being to long'* and *'Doctype must be declared'*.  
In previous module for using Flask it was advised that it is acceptable for the *'Doctype must be declared'* to be left uncleared as this was 
due to the linter Gitpod uses not understanding the template language Jinja. 

*When you save the file you might see a warning on the first line, 'Doctype must be declared first'. We can ignore this as the linter doesn't know how to properly read templating languages like Jinja*
Video: Flask Mini-Project 20 | 01 - Putting The Basics In Place (1e - Template Inheritance) 
[Code Institute](https://codeinstitute.net/)

Most errors where fixed except those of which the developer did not understand fully for example - 'imported but unused'.

#### Issue 2

SECRET KEY - During development the SECRET_KEY was accidently pushed to GitHub. The developer did not realise Django automatically
creates this and therefore pushed the code. On receiving the GitGuardian email the error was realized and a new env.py file was created
and a new Django SECRET_KEY added. 
....................However in the git commit history there is no confirmation code was pushed here as the next commit states *'index.html block content code added'*
Something for the developer to note for future 'all major changes and bug fixes to be commited and pushed for reference'.

#### Issue 3

When it came to adding datasets for the project it was advised to use [Kaggle](https://www.kaggle.com/).
However when researching and trying to download there was an error on the site *too many requests*. Reading through the documentation and forums it seems this is a 
known error. The developer requested advise from Code Institute on this matter to assist in moving forward with getting a dataset for the project.

#### Issue 4

During development the Gitpod terminal offered a warning. Advising that it was working with pip v20.2.4 and there was a new version and recommends and upgrade.
The developer followed the on terminal instructions and upgraded to v20.3.3.


#### Issue 5

At one point during development Python advised to install [Pillow](https://pillow.readthedocs.io/en/stable/). The developer did not have any knowledge of this imaging library.
The documentation was reviewed and the library was installed in the project.

#### Issue 6

It was found during development that the site definitely needed more pages adding. The initial four created an inception and wireframing wasn't going to be enough. 
This was to allow for guest users to see more than just the home page and register pages. It was realised the guest user needed to be enticed more. Therefore the Highlights page was created.
Furthermore the registered user required a profile page for when they logged in, and an add recipe, edit recipe and logout page. All additional pages have been created and are suitable for its purpose. 

### Validation sites

- When validating the code for HTML and CSS using [W3C Markup Validation](https://validator.w3.org/), errors where found and some were rectified, rectified errors included simple code errors and typos.
  However there were some errors the developer was unable to fix. Below shows a few examples.
  
  base.html
  - x errors found
  
  Error: xxx.
    At line x, column x   


- [Jshint](https://jshint.com/) for JS validation found error warnings, however many was of the same error. Unfortunately a fix wasn't implemented due to lack of understanding on how to resolve them and to time constraints. 
  Here are the errors for highlight.html
  - 4 errors found.

  Expected a string and instead saw %.
  Expected ':' and instead saw 'extends'.
  Expected '}' and instead saw '%'.
  Unrecoverable syntax error. (1% scanned).

- [PEP8](http://pep8online.com/) was used for testing Python errors.
  There were many errors on most pages, mostly referencing tabs and indentation. Again due to time constraints these errors were not rectified.
  Below are some common examples
    - missing whitespace around operator
    - trailing whitespace
    - indentation contains tabs


### Browsers tested

- Chrome: Using Google Developer Tools - Chrome was used for testing on Laptop, Tablet and Android devices.

- Safari: Safari wasn't used for testing on an I phone or Mac, due to not having physical access to these type of devices. However they were viewed on Google Dev Tools.

### Devices tested

On the final testing session the below devices where used to check if responsive, here are the outcomes.

Mobile:
- Android - Samsung Galaxy A40 - Outcome: All is responsive.
- Android - Samsung Galaxy A20 - Outcome: All is responsive.
- Android - Samsung Galaxy S10 - Outcome: All is responsive.

Laptop:
- Toshiba Satellite C850 - Outcome: All is responsive.
- HP Model I5 - Outcome: All is responsive.

The only responsive bug the developer found was on the [Techsini](https://techsini.com/multi-mockup/) - Responsive Mock up.
On the mock up it shows on I pad that the footer is half way up the page, however in Google Dev Tools this is not the case.
However due to not having an Apple Ipad to physically, it cannot be concluded the site is not responsive.   

<hr>

## Evaluation

- Overall the design and development of this site is suitable for its intended purpose.
- It has all the basic requirements of a functional website and meets CRUD functionality of the project criteria.
- Due to do external commitments additional features have been left out. The developer is aware of aspects that don't function as intended or are not yet could be added.        
- Most of the user stories where met, with the exception of editing user content as an Admin User. In the future this can be looked into and implemented along with the option to delete or block user if required.
- Images on the site are not all suitable for the sites look. It was found to be an issue to find a good selection of free stock professional images of Greek Cuisine.
  This is something that can be changed so it gives the site a better visual. For now some Mediterranean images were used. 
- Many future features could be added to provide more interactive activity, functionality and imagery.
- Branch testing - No branch testing was undertaken, something that the developer was intending to do - however was just overlooked.
- Manual Testing was undertaken and this was found to be successful. It is noted that there are many validation errors that needs to be looked into by the developer at a later date.
- [Werkzeug](https://palletsprojects.com/p/werkzeug/) was used in this project for authentication and secure passwords. This was new to the developer and was found to be interesting and a great tool to be aware of for future projects.
- Some front-end design changes were made during the build due to varying factors:
    - Materialize image carousel, looked good and fitted the sites initial idea but didnt load well. Also the developer found it difficult to change the prebuilt images and the image links kept breaking.
    - The site was to have 4 pages initially but it was discovered early in development that more pages would be required.

<hr>


## Deployment

#### Heroku:

The project is deployed to Heroku. It uses the automatic deployment method via Github, using your Github repository.
Below shows the steps to deploy on Heroku:

1. Heroku requires certain dependencies and applications to run our application. There we need to tell it what is required. 
   In the terminal type 
   - $ pip3 freeze --local > requirements.txt
   - $ echo web: python app.py > Procfile
2. Register on the Heroku website - [Heroku](https://www.heroku.com/) or Log in for existing users.
3. From the dashboard click 'New' and 'Create new app'.
4. Enter your unique 'App name' (Heroku practice is for it to be lowercase and to use hyphen (-) instead of spaces).
5. Select your region, then click 'Create App'.
6. Create app directs to Heroku's 'Deploy' tab, select the deployment method of 'GitHub'.
7. Your Github profile should be displayed, enter your repository name here and click 'Search'. (Idealy your Heroku app name and your repository name should be the same).
8. Your repository should display here and a 'Connect' button appears to connect to your app.
9. Before you click 'Connect', head over to 'Settings' tab and scroll down to the 'Config Vars' section. As we have contained our Environment Variables
   in our env.py file we need to tell Heroku these in a secure manner.
   Add your variables to the below Key/Value pairs:
    - IP
    - PORT
    - SECRET_KEY
    - MONGO_URI
    - MONGO_DBNAME

10. Final step before we connect to Heroku is to push our new files 'requirements.txt' and 'Procfile' to the repository.
    Back in the terminal have a check of the workspace status, type: git status. this will show your new pending files.
    Continue in the terminal and type:
    - $ git add requirements.txt
    - $ git commit -m "Added requirements.txt"
 
   - $ git add Procfile
   - $ git commit -m "Added Procfile"

   - $ git push

11. Go back to Heroku 'Deploy' tab, click 'Enable Automatic Deploys' in the section Automatic Deploys. Finally under Manual Deploy section click 'Deploy Branch'.
    Heroku will now receive the code from GitHub and start building the app using the required packages.
    Once built you will receive the message 'Your app was successfully deployed' then can click 'View' to launch your new app.

12. Your deployed app is now available and should update automatically everytime you push to the Github repository.



#### Github:

In [GitHub](https://github.com/) we can view the repository. 

Should you want to 'Fork' or 'Clone' this repository to use as a base template for your own projects you can do so.
 - To 'Fork':
1. Head to the repository, on the top right click 'fork' button.
   You now have your own copy of the forked repository in your Github account.

If you want to run this project locally, we must clone the project.
- To 'Clone':
1. Under the repository name, click the 'Code' button on the right.
2. A dropdown 'Clone with HTTPs' section appears, here copy the clone URL for the repository.
3. In your local IDE open Git Bash.
4. Change the current working directory to the location where you want the cloned directory to be made.
6. Type 'git clone' and paste the URL you copied.

- Example: git clone  = https://github.com/VMBlakelock/saute-and-skewers-greekfood

6. Press Enter. Your local clone is now created.


<hr>


## Credits

Personal credits go out to the following people:

Tutor Support
- Igor from tutor support who clarified issues regarding Secret key errors.
- Scott for totor support for assisting in follow up questions to Igor, also pointing me in the direction of Gitpod variable section.

<hr>


#### Websites reviewed

Websites reviewed and used during the creation of this project.

- [Balsamiq](https://balsamiq.com/)
  - Used for creating the wireframe mocks.
  
- [Bootstrap](https://getbootstrap.com/)
  - Researching carousel functionality, although wasn't used in the project.

- [Codeacademy](https://www.codecademy.com/catalog/language/python)
  - Article referring to Python programming language.

- [Diffchecker](https://www.codecademy.com/catalog/language/python)
  - Site for checking differences in code.

- [Google Fonts](https://www.fonts.google.com/basic-syntax/)
  - Used for choosing the site font.

- [Jsonformatter](https://jsonformatter.org/)
  - Reviewed whilst following the module videos.

- [Jshint](https://jshint.com/)
  - Validation testing of Javascript.

- [Kaggle](https://www.kaggle.com/)
  - Reviewed for data set examples.

- [Markdownguide](https://www.markdownguide.org/basic-syntax/)
  - This website was used to refresh knowledge on how to write Markdown.

- [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/)
  - This website was used to generate the new SECRET_KEY.

- [Pexels](https://www.pexels.com/)
  - Website flower images were selected from this source.

- [Pillow](https://pillow.readthedocs.io/en/stable/)
  - Reviewed site documentation due to python advising of installing it.

- [Python](https://www.python.org/doc/essays/blurb/)
  - Reviewed for gaining additional understanding of the language.

- [RandomKeygen](https://www.randomKeygen.com/)
  - Used for Fort Knox password.

- [StackOverflow](https://stackoverflow.com/)
  - Various research and questions throughout.

- [Techsini](https://techsini.com/multi-mockup/)
  - Used for Mock Up Images.

- [TraversyMedia](https://youtu.be/e1IyzVyrLSU)
    - A You Tube tutorial video to gain greater understanding of Django.
    
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)
    - Used to gain knowledge in authentication and secure passwords.

- [W3Schools](https://www.w3schools.com/basic-syntax/)
  - Reviewed and used frequently throughout the design of this project.

- [W3C Markup Validation](https://validator.w3.org/)
  - Validation testing of HTML and CSS.

<hr>


## Acknowledgements

[Slack](https://slack.com/intl/en-gb/), the entire community of students past and present for their motivation and concern in this last submission and pushing to 
ensure something was submitted.

[Code Institute](https://codeinstitute.net/) Tutor Support for assistance when facing difficulties.


The developer's abilities where tested during the development of this project.
2020 has been a strange and tough year, the developer tried hard to stay on track with study and all project submissions as 
well as working full time, over and above the normal working days throughout the year. Unfortunatley time and health tookover.
Therefore the ms4 project was created with minimum time left before submission date and the developers subscription ended.
Unfortunately no additional extentions were allowed.

The developer can only apologies for the basic and unfunished BouquetnBlooms project submission, however it was decided to submit something rather than nothing.

The developer has tried to incorporate as much of the project criteria as possible in the time left to create, to show there is an understanding there of the requirements of full stack implementation.
For quickness and ease to have something for submission the sites design is directly copied from the Boutique_Ado mini project from [Code Institute](https://codeinstitute.net/), 
however there are a few style tweaks and differences to try to make the site more individual and of course the product and subscription is completley different to that of Boutique_Ado.

Finally and again for quickenss the Readme was created initially by copy an pasting in one of the developers previous readme files and editing it for this project. 
This can be seen in the commit history. 


*Created for education purposes only*
