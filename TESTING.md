# Testing Documentation

([return to README](README.md))

## Contents

### Audit and Validation

[HTML Validation](#html-validation)\
[CSS Validation](#css-validation)\
[JavaScript Validation](#javascript-validation)\
[Python Validation](#python-validation)

### User Story Validation

[Site Owner User Stories](#site-owner-user-stories)\
[Site Visitor User Stories](#site-visitor-user-stories)

### Testing

[Automated Testing](#automated-testing)\
[Manual Testing](#manual-testing)\
[Bugs and Issues](#bugs-and-issues)

## Code Validation

### HTML Validation
([back to top](#testing-documentation))

I have validated the html code by copying and pasting the source code from each page into the w3c validator [HERE](https://validator.w3.org/).  When formatting the code I have decided to format the Jinja2 templating without indents to preserve the integrity of the HTML.

Please note I have not validated (or styled) the admin only pages as they are not intended to be user facing.\
Only myself and the user created for assessment purposes will have admin access for this iteration of the site.

Page validated: Landing Page\
URL: https://hopes-and-dreams-15b83f2d1383.herokuapp.com/ \
Repaired Issues: Missing image alt tags.\
Outstanding Issues: None.

Page validated: Signup Page\
URL: https://hopes-and-dreams-15b83f2d1383.herokuapp.com/dare-to-dream \
Repaired Issues: H2 tag not closed, missing image alts, stray closing tag for div.\
Outstanding Issues: None.

### CSS Validation
([back to top](#testing-documentation))

File Validated: style.css\
URL: https://hopes-and-dreams-15b83f2d1383.herokuapp.com/ \
Repaired Issues: 4 errors total - invalid font-style and ineligable margin values (due to typo).\
Outstanding Issues: None.

![image](static/images/testing/css-validation.png)

### JavaScript Validation
([back to top](#testing-documentation))

I have validated my JavaScript file using [JSHint](https://jshint.com/)

Repaired Issues: There were a number of missing semicolons and some undeclared variables, but no major issues.\
Outstanding Issues: None.

![image](static/images/testing/jshint-validation.png)

### Python Validation
([back to top](#testing-documentation))

I have used the [CI Python Linter](https://pep8ci.herokuapp.com/#) to ensure my python files are PEP 8 compliant:

App: addresses\
Files Linted: forms.py, models.py, urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.\

App: admin_console\
Files Linted: urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.\

App: basket\
Files Linted: contexts.py, urls.py, views.py, order_calculator.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.\

App: checkout\
Files Linted: forms.py, models.py, urls.py, views.py, webhook_handler.py, webhooks.py\
Repaired Issues: whitespace, spaces around operators and line length.  Line length issues meant I had to refactor code with variables and functions assigned shorted names and swap some fstrings for regularly constructed ones.
Outstanding Issues: None.\

App: cheese_beer\
Files Linted: settings.py, urls.py\
Repaired Issues: whitespace, spaces around operators, issue using '==' operator to test for boolean False (changed to 'is')
Outstanding Issues: None.\

App: home\
Files Linted: urls.py, views.py\
Repaired Issues: whitespace
Outstanding Issues: None.\

App: product_views\
Files Linted: urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length, also cannot use bare except so i had to look up the error
I was testing for and add it to the code.
Outstanding Issues: None.\

App: products\
Files Linted: contexts.py, signals.py, forms.py, models.py, urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.\

App: user_account\
Files Linted: forms.py, models.py, urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.\

## User Stories
([back to top](#testing-documentation))

### Site Owner User Stories

([back to top](#testing-documentation))

### Site Visitor User Stories
([back to top](#testing-documentation))

_"Users need to feel ... that they have control over comments and content they see."_\
Users may delete any comments on their own dreams they find unacceptable, or if they prefer disable comments entirely.

![image](static/images/user-stories/disabled.png)

## Testing
([back to top](#testing-documentation))

### Automated Testing
([back to top](#testing-documentation))


### Manual Testing
([back to top](#testing-documentation))

#### Manually Testing Page Functionality

For me the most sensible way of approaching this is to systematically check the functionality on every page to ensure that everything appears as intended when an action is taken on the site and that the database is updated accoringly.  As such I've created a table for each of the pages on the site and tested all of the features therein.

DREAMSCAPE PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |

PERSONAL PROFILE PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |


MANAGE CATEGORIES


| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |


MANAGE USERS


| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |


MANAGE DREAMS

On deleting a dream:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |


#### Issues found during manual testing

The manual testing process uncovered a number of issues.  The issues around dream cretion and editing in particular required significant remedial work.

 - The sign up section in the 404 page did not work correctly.
 - The dream string used to create the slug was not being created as intended, which I fixed by reversing the order or the string creation logic.  I'm not sure at which point this stopped working!
 - On editing a dream the code did not check if the dream name already existed for the user.  I created the appropriate logic and a re-direct to stop the code executing further.
 - On editing a dream if the name and dream slug was updated the page would not return the new url for the dream.  This was achieved via a redirect with the updated data on update.
 - On submitting a duplicate comment on the view dream page the page was not redirected back to the same dream.
 - edit comment code on view dream page did not check for duplicate comments.  It now does!
 - view dream page was not refocussing on comments after likes/dislikes, but now is.  Also the logged in version of the page was not properly validated (I had previously validated the logged out version!)
- edit comment code on dreamscape page did not check for duplicate comments.  It now does!
- editing categories did not update the category in user and dream category arrays, which needed a fix.

#### Responsiveness Testing

I have tested at (in descending order) 3072px, 1920px (default), 1200px, 920px, 650px, 450px, 360px, 320px.  This is reflective of the major break points.

As well as using google developer tools in responsive mode, this has been tested in the real world on Chrome and Firefox in Windows on a 1920 x 1080 HD monitor, and on a Samsung Galaxy S8 (at c.360px width).

| Page tested | Screen width tested | Result |
| ------------- | ------------------|-------------- |
| landing page | 3072px | Success |
| landing page | 1920px | Success |
| landing page | 1200px | Success |
| landing page | 920px | Success |
| landing page | 650px | Success |
| landing page | 450px | Success |
| landing page | 360px | Success |
| landing page | 320px | Success |
| sign-up page | 3072px | Success |
| sign-up page | 1920px | Success |
| sign-up page | 1200px | Success |
| sign-up page | 920px | Success |
| sign-up page | 650px | Success |
| sign-up page | 450px | Success |
| sign-up page | 360px | Success |
| sign-up page | 320px | Success |
| welcome page | 3072px | Success |
| welcome page | 1920px | Success |
| welcome page | 1200px | Success |
| welcome page | 920px | Success |
| welcome page | 650px | Success |
| welcome page | 450px | Success |
| welcome page | 360px | Success |
| welcome page | 320px | Success |
| password reset page | 3072px | Success |
| password reset page | 1920px | Success |
| password reset page | 1200px | Success |
| password reset page | 920px | Success |
| password reset page | 650px | Success |
| password reset page | 450px | Success |
| password reset page | 360px | Success |
| password reset page | 320px | Success ||
| password reset page (dream) | 3072px | Success |
| password reset page (dream) | 1920px | Success |
| password reset page (dream) | 1200px | Success |
| password reset page (dream) | 920px | Success |
| password reset page (dream) | 650px | Success |
| password reset page (dream) | 450px | Success |
| password reset page (dream) | 360px | Success |
| password reset page (dream) | 320px | Success |
| reset password | 3072px | Success |
| reset password | 1920px | Success |
| reset password | 1200px | Success |
| reset password | 920px | Success |
| reset password | 650px | Success |
| reset password | 450px | Success |
| reset password | 360px | Success |
| reset password | 320px | Success |
| lost bunnies (404 page) | 3072px | Success |
| lost bunnies (404 page) | 1920px | Success |
| lost bunnies (404 page) | 1200px | Success |
| lost bunnies (404 page) | 920px | Success |
| lost bunnies (404 page) | 650px | Success |
| lost bunnies (404 page) | 450px | Success |
| lost bunnies (404 page) | 360px | Success |
| lost bunnies (404 page) | 320px | Success |
| dreams page | 3072px | Success |
| dreams page | 1920px | Success |
| dreams page | 1200px | Success |
| dreams page | 920px | Success |
| dreams page | 650px | Success |
| dreams page | 450px | Success |
| dreams page | 360px | Success |
| dreams page | 320px | Success |
| create dream page | 3072px | Success |
| create dream page | 1920px | Success |
| create dream page | 1200px | Success |
| create dream page | 920px | Success |
| create dream page | 650px | Success |
| create dream page | 450px | Success |
| create dream page | 360px | Success |
| create dream page | 320px | Success |
| image upload page | 3072px | Success |
| image upload page | 1920px | Success |
| image upload page | 1200px | Success |
| image upload page | 920px | Success |
| image upload page | 650px | Success |
| image upload page | 450px | Success |
| image upload page | 360px | Success |
| image upload page | 320px | Success |
| edit dream page | 3072px | Success |
| edit dream page | 1920px | Success |
| edit dream page | 1200px | Success |
| edit dream page | 920px | Success |
| edit dream page | 650px | Success |
| edit dream page | 450px | Success |
| edit dream page | 360px | Success |
| edit dream page | 320px | Success |
| view dream page | 3072px | Success |
| view dream page | 1920px | Success |
| view dream page | 1200px | Success |
| view dream page | 920px | Success |
| view dream page | 650px | Success |
| view dream page | 450px | Success |
| view dream page | 360px | Success |
| view dream page | 320px | Success |
| dreamscape page | 3072px | Success |
| dreamscape page | 1920px | Success |
| dreamscape page | 1200px | Success |
| dreamscape page | 920px | Success |
| dreamscape page | 650px | Success |
| dreamscape page | 450px | Success |
| dreamscape page | 360px | Success |
| dreamscape page | 320px | Success |
| profile page | 3072px | Success |
| profile page | 1920px | Success |
| profile page | 1200px | Success |
| profile page | 920px | Success |
| profile page | 650px | Success |
| profile page | 450px | Success |
| profile page | 360px | Success |
| profile page | 320px | Success |

### Bugs and Issues
([back to top](#testing-documentation))

FRONT-END ISSUES


DEFAULT ADDRESS FORMATTING ISSUES:

I initially used dispaly: inline-block to display the address boxed on the 'manage addresses' page, and flexbox to arrange the content of the boxes.  I soon discovered that if I used templating logic (in this case to display which address was selected as default) it affected the layout of the page, offsetting the box containing the text injected by the template.  Equally bafflingly, if I removed the template logic and simply entered the text the problem went away.

Clues as to the solution became apparent when I noticed that changing the flex code within the first container (ie the add address container) similarly broke the flow of the page (the other boxes were all part of a for loop).  I struggled with this for a long while before eventually re-discovering the ability to wrap content within a flex container (which I haven't used for a couple of projects!) and switching the entire layout to flexbox.  I still have no clue what was causing these issues which seemed to be caused somehow by the code for the templating logic.  I think it might be whitespace-related as I gathered from my research that inline-block elements are susceptible to this, however as the code works perfectly with flexbox I have paid it no further attention.  It seems using inline-block to wrap elements is not best practice in any case.

jQuery .post / Javascript fetch() request, client_secret and the checkout_cache view:

For multiple reasons I decided very early on to dispense with jQuery in my code - for one thing there wasn't enough of it to warrant the inclusion of all the overhead, in many cases where it was used it Boutique Ado it was also mixed and matched with vanilla Javascript and by and large used deprecated methods (eg extensive use of var for declaring variables).  

As such I decided to write the code which posted to the checkout_cache view using the fetch() API instead.  I managed to do this successfully, but soon observed a number of issues.

The main bug was that when using no-cors mode in the fetch request, it prevented the  view from accessing the CSRF Token, which was throwing an error in the running Python terminal.  However, if I switched the mode to same-site, then it prevented the STRIPE javascript from functioning correctly, which was throwing an error in the console (although it still worked as intended).  This problem seemed to me to be intractable, however it was soon solved.

On further observation, I noted that the checkout_cache view was entirely redundant, rendering use of any fetch() or .post request pointless.  Because the code already passed the client_secret from the stripe payment intent to a hidden form field in the template, there was no need to fetch anything from a view on the server side. I didn't need to update the payment intent there either, because I had already decided that I was going to save the client_secret in the server session.  I had already done this because I noticed that every time a user re-visited or refreshed the checkout page it created a new payment intent in the Boutique Ado code. I thought this strange and on checking the STRIPE documentation found that indeed this is not best practice, therefore I made sure the the checkout view retrieved the payment intent from the session and updated it whenever the checkout page was loaded, if a session already existed, as well as passing the value into the hidden form field.  This way there aren't a multitude of open payment intents.

Given all this was the case, I was able to remove the fetch request entirely with zero detriment to the functionality of the code.  I believe I could do exactly the same with the Boutique Ado code should I wish.  I think the reason for the redundancy is also found in the STRIPE documentation - The best practice for handling the client_secret is to store it on the server side, and avoid passing it to the client side at all (in fact storing it as a value in a hidden form field seems like a terrible idea, since it is fully visible on the client side).  I believe that when the Boutique Ado project was written that the checkout_cache view was intented to retrieve the client_secret key from the session on the server side with fetch() or .post and return it to STRIPE in order to process the payment.  At some point this entire section of code must have broken or become deprecated (possibly due to the bug I encountered with the fetch API, indeed this may explain the mish-mash of JQuery and JavaScript).  I suspect it remains largely for demonstration purposes, although it has now been given repurposed to add metadata to the payment intent (although it doesn't seem to actually retrieve anything from the server).

Although I have been assured that for assessment purposes the current method will be adequate, given more time to complete this project I would definitely want to remove the hidden form field in the template which provides the client_secret to STRIPE and replace it with a proper fetch() request.  Indeed in a live production environment this would be a must. Although I would like to attempt it if I can I don't belive I will have time at this stage, which is why I have documented it here.


Form submission without server-side validation

The way I chose to submit the checkout form initially proved problematic.  In order to have multile checkout buttons on the page, rather than include a button (even a fake one) within the form, I chose to include elements outside of the form that were entirely dependent on JavaScript to function.  I soon discovered that if a user without a saved address submitted their card details, the payment would process without any of their delivery or personal details being saved - because the button was not within the form the validation wasn't taking any effect. 

I decided to resolve this by adding a hidden button withing the form which was triggered by the javascript buttons outside the form.  This worked, however if the default effects of the button were disabled this also disabled form validation - it meant either the form was submitted without the payment, or again it wasn't validated.  I solved the first part of this by adding a further event listener on the form itself to prevent it from submitting, yet still enable the button was to trigger field validation.  However even thoguh the html was now showing the correct messages to the user, the form was still submitting regardless of whether or not it was filled out if the card payment details were valid.

In the end I wrote a javascript loop to ensure the required fields are filled out, returning true if they were and triggering the STRIPE payment.  I'm still not 100% clear on why this was happening, but I suspect it is linked to the choice of JavaScript event that I used.  However with the code now working in a jury-rigged type of way, my thoughts turned to what this should look like in a production environment.
I subsequently needed to eliminate HTML validation altogether as on testing (actually when I was writing the CSS) I noticed that the javascript was throwing errors in the console due to empty required fields existing on form submit button click, so I have validated the form using Javascript instead.  I also moved the loop immediately prior to form submission and stripe payment validation to make it clearer.

In fact this bug raised another issue with the code in general - that the STRIPE payment is submitted prior to the order being processed on the server side.  This means that for unregistered users form validation on the client side is practically impossible, which is quite a big security risk.  Although this problem stems from the course material, there is a relatively simple solution which is very similar to what I have already implemented for users with saved addresses.  In these cases the saved or selected address and e-mail (which has already been validated client side) pre-populates the form that is passed to the order model for processing.  The solution for either logged-in users without a saved address or for unregistered users is to add an additonal screen which either saves or validates the contact details in the database or caches them in a session cookie.  They can then be used to pre-populate the order form in the checkout view.  This way I could ensure all data is properly validated on the server side prior to submitting the stripe payment confirmation. Whilst this change would be essential for a live production environment (indeed it is clear that this is the process for the majority of online retailers for unregistered members) it is unlikely I will be able to implement it prior to submission of the MVP due to time constraints.


CALCULATING ORDER TOTALS IN THE MODEL

I decided to calculate order totals in the view rather than in the model on checkout, to ensure consistency between the amounts being submitted by the view to the order model and those submitted by to STRIPE via the STRIPE payment intent.   It means a common source for the number, ie the cached basket of goods which is passed to the payment intent when the checkout page is loaded.  Although there are no guarantees of issues if the amount was calculated in the view, I wanted to avoid any inconsistencies.

ALLAUTH USERNAME ISSUE

Whilst allauth does great things, it also insists on users providing a username.  Whilst this used to be good pratice in reality few sites these days require this, and most signin activity requires a username.  I was able to set up Django so that allauth used the e-mail address to login, but when I tested the signup process without a required username it started throwing errors.  I tried various combinations of settings before I realised I would have no choice but to customise the user model.  The solution I found, alongside various settings, was to set up a reciever in my user account model which, presave, would set the username to the same value as the e-mail address. That way the field would easily be populated with a unique value.  I feel sure a neater solution must exist (although this is about the neatest solution I've seen so far) but nothing that makes for such a seamless user experience.

UNUPLOADED FILES PERSIST ON PAGE REFRESH

When uploading an image with Django, I have been able to use javascrip to preview files in the form and a cancel button to remove any such files and prevent the image uploading. However, if the page is refreshed the file previously selected seems to persist in the cache (this was also a problem with Boutique Ado).  It could lead to a user unwittingly updating a file. I have searched a lot for answers of doing this in the view - in the end I simply set Javascript to clear the field on page reload.






([back to top](#contents))