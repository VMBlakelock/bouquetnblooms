

# Bouquet'N'Blooms

*Amazing fresh Bouquet'N'Blooms for many an occasion*


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

Fresh flowers undoubtedly show love and provide that all important meaning. 
Bouquet'N'Blooms will ensure fresh flowers will make the perfect addition to any occasion.

<hr>

### Aim

To create a full stack website that allows users to purchase a product or service.

Technologies to be used in the project are HTML/CSS/Javascript/Python3 and Django - v3.1.4.


### Purpose

Bouquet'N'Blooms is a floristry website in which users can order fresh bouquets of flowers delivered directly to them.

All users to the site will see the websites products on offer. However only registered users can order.


<hr>


## UX

## User stories

There are three types of users for this website, 'User Stories' for each user are discussed below:

### Guest User

As a guest user I want to:
 - navigate around the site easily.
 - find a navigation bar that links to other pages when clicked. 
 - understand the sites purpose upon landing.
 - be able to view the sites offerings.
 - be able to click social media icons to link out to other Bouquet'N'Blooms pages.
 - have the option to register to the site to be able to interact with the site, see more and make a purchase.

### Registered Account

As a registered user I want to:
 - see all site content.
 - log into the site easily.
 - log out successfully.
 - have buttons to click to login, log out and submit data.
 - be able to add products to my basket.
 - review the products in my basket before purchasing.
 - safe and secure area where I can add confidential data and payment details.
 - receive an email when I’ve purchased something.
 - be able to cancel an order if I change my mind.
 - be notified of all my interactive actions.
 - Have the option to subscribe to the site and have a product delivered monthly.

### Admin User

As an admin user I want to:
- have full access to the site to ensure all content is viable.
- have access to be able to add more products and offers to the site.
- edit any content posted by me.


### Website Owner

The website owner would like users of the website to:
-  Interact with the site.
-  Enjoy the site.
-  Find the site easy to register to and purchase products.

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

- Bouquet'N'Blooms is an e commerce website. It allows users to purchase flowers. 
- The site features one required payment by the user, the product is then dispensed by the retailer.
- Initially the site was to have a main feature of a 'subscription' page where users could register for a monthly subscription
  thus having fresh flowers delivered monthly after a one-time payment.
- The site features the 3 core languages of web development HTML, CSS and Javascript, as well as Python and uses Django. 
- The project uses an 'sqlite' database initially, and it was hoped a postgress database via heroku. 
- There is a clear brand to the site that draws users and entices further interaction.
- Users who discover Bouquet'N'Blooms, love flowers and are excited to use the site and order.
- Bouquet'N'Blooms has the potential to become an excellent revenue generating business site. 
- Adding additional features (blog, client reviews  - for example) and marketing the site well could mean Bouquet'N'Blooms could generate even more revenues.
- During research there were other sites found that had the same concept, most offering a full inventory of products and subscriptions, where as Bouquet'N'Blooms offers only purchases currently. 


### Scope 

- The site was developed with the intention of allowing users to purchase Bouquet'N'Blooms products in any of the categories.
- Its main feature was to have a subscription page where users could register and subscribe to the site thus have flowers delivered to them on a monthly basis.
  The subscription was to be available to registered users after a one-time payment.
- The database of choice to build with was 'sqllite' in the initial instance then onto Postgress via Heroku.
- The project was scoped to provide ease of use.
- It was to have minimal pages, however it must house a home page, registration page, log in page, log out page, various category pages and a shopping bag page.
- Have various app installed that allowed users to manipulate the data and to eventually purchase from the site.
- Be responsive on all devices.
- Be visually appealing that incorporated the beauty of flowers and blooms in the front-end design.


### Structure

- Bouquet'N'Blooms site structure was created from the UX user stories - therefore developed with pages that were required to enable users to sign up and add data.
  Unfortunately during development not all user stories where met.
- The Home page, All Flowers, Flower Type, Occasion Flowers, Special Offer and Shopping Bag pages are designed identically each with the navbar, basket and account icons. 
  This is so the user is clear as to where they are on the site. The developer cannot advise on the structure of other pages that should be within the project as
  time constraints these where not implemented.
- The site's main nav header has bold text that introduces the site and easily shows its features, also a 'banner' that advises of an offer that currenty is ongoing. 
- The Shopping bag page shows users what is in thier bag - this feature is not fully functional at present.

### Skeleton

- Four wireframes where created - the three main pages of the site and a subscription page. As it was initially planned
  that there would be a 'Home', Register and Login page as well as a 'subscription' page as a main feature. This supscription feature wasnt implemented and due to time contraints the 
  developer dint get to add in the register or log in page.
- It was found during development that by following the code institute example project there would be multiple pages of products.
  These pages where not created in wireframe as they where similar to the home page.
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
 - It is anticipated that the user would feel happy and positive on landing on the site and feel they wanted to purchase something even if that wasn't their intention.

The typography colours and fonts where important to promote a calming effect but with a tempting feel good reaction that made the want to fulfil the sites output fully.
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

**Forms:** Code from Bootstrap. The Search Bar uses a form and requires the user to input data, this form is self explanatory.
        
**Icons:** Font Awesome icons are used throughout the site, account, basket and form fields to provide image instructions aswell as for design, the font awesome kit is used in the code. 

**Images:** Vibrant images are used in the design. Selected images provide an idea of the product on offer if you buy a subscription.

**Search Bar:** Have a 'Search' bar, so users can search for specific items using key words.


### Future Features

Bouquet'N'Blooms - Future features could include:

- A footer was an initial requirement to provide a clear indication of the end of the page and house the location of HQ.
- Social Media Links - Bouquet'N'Blooms would have various Social Media accounts in the real world therefore icons for these site need to be found in the footer that will direct to the social sites.
- Copyright logo - hosts the website owners own work this was not added to the site.
- Having a larger database of products.
- Have the intended subscription page to provide packages for registered users to view and purchase.
- The subscriptions could be monthly, weekly or seasonal.
- All subscriptions as per the products have packages with different price points.
- User profile to be created. There is an icon for my account however this is not currently active.
- Have a logo, that adds to the Bouquet'N'Blooms text into something more memorable.
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

- [Bulma](https://bulma.io/)
    - This framework was used for enable Font Awesome icons to be consitant and centred throughout.

- [Bootstrap](https://getbootstrap.com/)
  - Researching carousel functionality, although wasn't used in the project.

- [JQuery](https://jquery.com/)
    - The JavaScript library used within the Materialize framework.

#### Database
- The project is created in Gitpod SQLLite due to not having time to deploy the project to Heroku.

#### Text Editor
- [Gitpod](https://gitpod.io/)
    - A cloud based IDE, that uses prebuilt workspaces.

#### Version Control
- [Git](https://git-scm.com/)
    - Version control system that works within the Gitpod terminal. Used to commit and push recent code to GitHub.

#### Hosting Platform
- [Heroku](https://https://dashboard.heroku.com/)
    - The application platform that was to be used for the live deployed site.

- [Github](https://github.com/)
    - A repository store, used to house the sites repository.

#### Developer Tools
- [Google Dev Tools](https://developers.google.com/web/tools/chrome-devtools)

#### Colorcodehex
- [Colorcode](https://www.colorcodehex.com/022072.html)

#### Font Awesome
- [Font Awesome](https://fontawesome.com/)
    - Used for UX icons and getting 'kit' code.

#### Validation sites
- [W3C Markup Validation](https://validator.w3.org/)
- [Jshint](https://jshint.com/)
- [PEP8](http://pep8online.com/)

<hr>

### Testing

Manual Testing was undertaken during the creation of this site. 
Testing included tests with in Django, on various devices for responsiveness and UX aswell as testing code for bugs.
Code was validated for best practice.

 - Validation sites used:
   - W3C Markup Validator
   - Jshint
   - Pep8 Compliance

Below shows some tests undertaken during development and the issues, bugs and validation errors found. Also how if possible the issues were rectified.
Some issues and errors were not rectified, due to either lack of developer knowledge or due to time constraints for additional study of documentation and/or more testing.

#### Test 1

The site was developed using Django. During creation various tests were used to ensure the site was built correctly.
- All Auth
    All Auth email account authentication was tested by using the word 'success' temporarily placed in the settings.py file.
    The code **LOGIN_REDIRECT_URL = '/success'** was used.

    Open project using **python3 manage.py runserver**
    This shows a 404 page not found error
    In browser type **/accounts/login** to the end of the gitpod url navigate to the email of a superuser we created previously
    Enter superuser credentials, sign in - this returns a page asking for email verification
    This confirms 'allauth' is working as emails are required to be confirmed in order to log in

    To test further some amendments were made to Django Admin, and the test was performed again 
    In browser type **/accounts/login** to the end of the gitpod url navigate to the email of a superuser we created previously
    Enter superuser credentials, sign in - this returns a page asking for email verification
    As expected we get a 404 page not found, however this time in the browser we are redirected to **/success** url this confirming 
    our All Auth login system redirects back to the login redirect url in **settings.py**
    Which confirms that All Auth authentication is working properly.
    


#### Issue 1

Issues with errors occurred when working on py files. The developer had to clear the errors Gitpod advised on. 

- Errors due to the 2 line spacing rule and using the tab key instead of spaces and also not entering to a new line.
- Errors from -*'lines being to long'* and *'Doctype must be declared'*.  
    In previous module for using Flask it was advised that it is acceptable for the *'Doctype must be declared'* to be left uncleared as this was 
    due to the linter Gitpod uses not understanding the template language Jinja. Therefore these error remain.

*When you save the file you might see a warning on the first line, 'Doctype must be declared first'. We can ignore this as the linter doesn't know how to properly read templating languages like Jinja*
Video: Flask Mini-Project 20 | 01 - Putting The Basics In Place (1e - Template Inheritance) 
[Code Institute](https://codeinstitute.net/)

- Errors with *'continuation line under-indented for visual indent'* was often showing up the developer had to review [Stackoverflow](https://stackoverflow.com/questions/15435811/what-is-pep8s-e128-continuation-line-under-indented-for-visual-indent/)
to rectify this. 

All other errors where fixed except those of which the developer did not understand fully or have time to investigate additionaldocumentation to fix, for example - *'imported but unused'* and *'Class 'Product' has no 'objects' member'*.

#### Issue 2

SECRET KEY - During development the SECRET_KEY was accidently pushed to GitHub. The developer did not realise Django automatically
creates this and therefore pushed the code. On receiving the GitGuardian email the error was realized and a new env.py file was created
and a new Django SECRET_KEY added. 
However in the git commit history (20th Dec) there is no confirmation code was pushed here as the next commit is on the 21st Dec.
Something for the developer to note for future *'all major changes and bug fixes to be commited and pushed for reference'*.

#### Issue 3

After adding base.html code it was realised the site pulled everything on the nav header to the left.
It was found a '</div>' hadnt not been removed on the 'header nav with title' section on the send line - with the row.


#### Issue 4

When it came to adding datasets for the project it was advised to use [Kaggle](https://www.kaggle.com/).
However when researching and trying to download there was an error on the site *too many requests*. Reading through the documentation and forums it seems this is a 
known error. The developer requested advise from Code Institute on this matter to assist in moving forward with getting a dataset for the project.
It was decided to build the dataset via the Django admin.

#### Issue 5

At one point during development at the stage of creating 'models', Python advised in the CLI to install 'Pillow'. The developer did not have any knowledge of this imaging library, however as it was advised by Gitpod/Python/Django the developer reviewed the documentation.
After reviewing Pillow-8.0.1 - the library was installed in the project. The issue was rectified.

It is noted and the developer is aware that there should have been more testing stages to the project however due to time constraints it wasnt possible to test further or document. 

### Validation sites

- When validating the code for HTML and CSS using [W3C Markup Validation](https://validator.w3.org/), errors where found and some were rectified, rectified errors included simple code errors and typos.
  However there were some errors the developer was unable to fix. 
  Please click on the validator website and copy/paste in the base.html file for examples of left errors.

- [Jshint](https://jshint.com/) for JS validation found error warnings, however the error was referring to <doctype!>. Unfortunately a fix wasn't implemented due to lack of understanding on how to resolve them and to time constraints. 
  Please click on the validator website and copy/paste in the base.html file for examples of left errors.

- [PEP8](http://pep8online.com/) was used for testing Python errors.
  There were a few errors in the code below are some common examples
    - missing whitespace around operator
    - trailing whitespace
    - indentation contains 
    
    Again due to time constraints it was found at the last moment errors- mostly referencing line length being to long. these errors were not rectified.
    Please click on the validator website and copy/paste in the settings.py file for examples of left errors.

### Browsers tested

- Chrome: Using Google Developer Tools - Chrome was used for testing on Laptop, Tablet and Android devices.
  All responsive - no issues.

- Safari: Safari wasn't used for testing on an I phone or Mac, due to not having physical access to these type of devices. However they were viewed on Google Dev Tools.

### Devices tested

On the final testing session the below devices was used to check if responsive, here is the outcome and notes.

Mobile:
- No actual mobile device was tested on as the project is not deployed to Heroku.

Laptop:
- Toshiba Satellite C850 - Outcome: All is responsive.
The site works well via Goolge Chrome on this device - No issues.


<hr>

## Evaluation

- Overall the design and development of this site is suitable for viewing and searching only.
- It has basic requirements of a functional website and meets only some the project criteria.
- Due to do external commitments and running out of time to continue to develop - many main features have been left out. The developer is aware of aspects that don't function as intended or are not added.        
- Most of the user stories where met, however the criteria of the project where not.
  In the future these can be looked into and implemented to allow for a fully functional backend site.
- Images on the site are not all suitable for use of selling a 'product'. Users want to receive what they see in the image on a site. In the future or in real life scenario the site would have
  professional photos of thier actual products. This is something that can be changed so it gives the site a better visual. For now some generic flower images were used. 
- Many future features could be added to provide more interactive activity, functionality and imagery.
- Branch testing - No branch testing was undertaken, something that the developer was intending to do - however due to time contraints just got on with creating as much of the site as possible.
- Minimal manual testing was undertaken and this was found to be successful. It is noted that there are still validation errors that would need to be looked into by the developer should there have been more time before submission.
- The site was to have 4 pages initially but it was discovered early in development that more pages would be required.

<hr>


## Deployment

#### Heroku:

The project should have been deployed to Heroku. It should use the automatic deployment method via Github, using your Github repository.

Note: The project is not deployed due to errors and no time to rectify before submission.
Error:
gitpod /workspace/bouquetnblooms $ heroku config:set DISABLE_COLLECT=1 --app django-bouquetnblooms
Setting DISABLE_COLLECT and restarting ⬢ django-bouquetnblooms... !
 ▸    Invalid credentials provided.

Therefore nt able to get past this part to continue.


*Deployed to [Heroku](https://django-bouquetnblooms.herokuapp.com/) and stored in [Github](https://github.com/)*

Below shows the steps the developer believes is required to deploy on Heroku:

1. Heroku requires certain dependencies and applications to run our application. There we need to tell it what is required. 
   In the terminal type - requirements.txt
   We also need to create a Procfile - in there add - web: gunicorn bouquetnblooms.wsgi:application
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
    - **database details** as the project did not get deployed the developer cannot comment on this requirement.
    - **database URL** as the project did not get deployed the developer cannot comment on this requirement.

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

- Example: git clone  = https://github.com/VMBlakelock/bouquetnblooms

6. Press Enter. Your local clone is now created.


<hr>


## Credits

Personal credits go out to the following people:

Tutor Support
- Igor from tutor support who clarified issues regarding Secret key errors.
- Scott from tutor support for assisting in follow up questions to Igor, also pointing me in the direction of Gitpod variable section.
- Samantha from tutor support for confirming the data set can be done manaually as I was having difficulties getting a data set from [Kaggle](https://www.kaggle.com/)
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
well as working full time, over and above the normal working days throughout the year. Unfortunately time and health tookover.
Therefore the ms4 Bouquet'N'Blooms project was created with minimum time left before submission date and the developers subscription ended.
A small extension was allowed for by code institute.

The developer can only apologies for the basic and unfinished Bouquet'N'Blooms project submission, however it was decided to submit something rather than nothing.

The developer has tried to incorporate as much of the project criteria as possible in the time left to create, to show there is an understanding there of the requirements of full stack implementation.
For quickness and ease to have something for submission the sites design is directly copied from the Boutique_Ado mini project from [Code Institute](https://codeinstitute.net/), 
however there are a few style tweaks and differences to try to make the site more individual and of course the products that are on offer.

Finally and again for quickness the Readme was created initially by copy an pasting in one of the developers previous readme files and editing it as the project was developed. 
This can be seen in the beginning of the commit history. 


*Created for education purposes only*
