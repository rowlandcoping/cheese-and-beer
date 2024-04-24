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


UNIVERSAL PAGES

Page validated: Home\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/ \
Repaired Issues: stray tags\
Outstanding Issues: None.

Page validated: Find Order\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/my-account/find-order/ \
Repaired Issues: label for attributes remained from a different form\
Outstanding Issues: None.

Page validated: 404 page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/typeanthinghere/ \
Repaired Issues: missing image alt\
Outstanding Issues: None.

Page validated: Products list page and search\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/view-products/?query= \
Repaired Issues: missing image alt, illegal query from where I was using category name, changed to id, some nesting issues. superfluous duplicate ids.\
Outstanding Issues: None.

Page validated: View Product Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/view-products/product-detail/xxxx/ \
Repaired Issues: missing image alts, illegal query from spaces in variety names (Added variety_slug field, populated database, added variety GET query). Some nesting issues. superfluous duplicate ids.\
Outstanding Issues: None.

Page validated: Checkout Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/checkout/ \
Repaired Issues: missing image alts, stray tags, placeholders in hidden fields. Issue where there are two address forms on page populated from the same django model. Solved by removing id attributes from the form that isn't submitted via checkout.\
Outstanding Issues: None.

Page validated: Checkout Confirmation Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/checkout/confirmation/xxxx \
Repaired Issues: missing closing tags\
Outstanding Issues: None.

Page validated: Basket Review Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/basket/ \
Repaired Issues: missing image alts, some superflous duplicate ids, one for styling reasons solved using specificity instead
Outstanding Issues: None.

ALLAUTH PAGES

Page validated: Login Page\
URL: http://127.0.0.1:8000/accounts/login/ \
Repaired Issues: Allauth ariadescribedby attribute in password field didn't have companion field.  Solved by pasting the source code instead and deleting it.\
Outstanding Issues: None.

Page validated: Signup Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/accounts/signup/ \
Repaired Issues: Allauth ariadescribedby attribute in password field didn't have companion field.  Solved by pasting the source code instead and deleting it.\
Outstanding Issues: None.

Page validated: Password Reset Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/accounts/password/reset/ \
Repaired Issues: None. \
Outstanding Issues: None.

Page validated: Password Reset Done\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/accounts/password/reset/done/ \
Repaired Issues: Unclosed elements. \
Outstanding Issues: None.

Page validated: Password Reset From Key\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/accounts/password/reset/key/done/ \
Repaired Issues: Unclosed Elements. \
Outstanding Issues: None.

USER ACCOUNT PAGES

Page validated: My Account\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/my-account/ \
Repaired Issues: None. \
Outstanding Issues: None.

Page validated: Manage Addresses\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/addresses/ \
Repaired Issues: None. \
Outstanding Issues: None.

Page validated: Add an Address\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/addresses/xxxx/ \
Repaired Issues: None. \
Outstanding Issues: None.

Page validated: Edit an Address\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/addresses/edit-address/xxxx/ \
Repaired Issues: None. \
Outstanding Issues: None.

Page validated: Orders Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/my-account/orders/ \
Repaired Issues: Stray tags, nesting issues. \
Outstanding Issues: None.

Page validated: View Order Info\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/my-account/order-info/xxxx/ \
Repaired Issues: missing image alts, duplicate id in undisplayed element. Solved this by removing id as it was superfluous. \
Outstanding Issues: None.

Page validated: View Wishlist\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/my-account/wishlist/ \
Repaired Issues: missing image alts, duplicate superfluous ids. Also duplicate ids which meant creating a container div. \
Outstanding Issues: None.

Page validated: Contact Us\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/my-account/contact/ \
Repaired Issues: duplicate stray ids in input elements. \
Outstanding Issues: None.

ADMINISTRATOR ONLY PAGES

Page validated: Admin Console\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/admin-console/ \
Repaired Issues: nesting issue with button inside an anchor.  converted to and styled a span. \
Outstanding Issues: None.

Page validated: Add Cheese Category\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/add-cheese-category/ \
Repaired Issues: issue with empty src element in hidden element used to preview images.  struggled to add holding image until I realised the load static tag doesn't carry over from base.html, and had to be loaded in the template.  \
Outstanding Issues: None.

Page validated: Add Beer Category\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/add-beer-category/ \
Repaired Issues: empty src attribute. \
Outstanding Issues: None.

Page validated: Edit Categories\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/edit-catgories/ \
Repaired Issues: None. \
Outstanding Issues: None.

Page validated: Edit Cheese Category\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/edit-cheese-category/xxxx/ \
Repaired Issues: Unclosed elements. \
Outstanding Issues: None.

Page validated: Edit Beer Category\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/edit-beer-category/xxxx/ \
Repaired Issues: None (fixed prior to validation). \
Outstanding Issues: None.

Page validated: Add Beer\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/add-beer/ \
Repaired Issues: removed unnecessary label for django form radio input. \
Outstanding Issues: None.

Page validated: Add Cheese\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/add-cheese/ \
Repaired Issues: None. \
Outstanding Issues: None.

Page validated: Edit Existing Product\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/edit-product/ \
Repaired Issues: Stray tag, nesting issue. \
Outstanding Issues: None.

Page validated: Product Edit Page\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/products/product-edit/xxxx/ \
Repaired Issues: removed unnecessary label for django form radio input. \
Outstanding Issues: None.

Page validated: View Customer Messages\
URL: https://cheese-and-beer-896aa5a35920.herokuapp.com/admin-console/view-messages/ \
Repaired Issues: nesting issues, stray tags. 
Outstanding Issues: None.


### CSS Validation
([back to top](#testing-documentation))

File Validated: style.css\
URL: https://hopes-and-dreams-15b83f2d1383.herokuapp.com/ \
Repaired Issues: 2 issues found - 1 incorrect use of relative and 1 legacy negative padding value which was removed.  I also had a few warnings about two elements with borders the same color as their backgrounds, and a further 3 warnings about the CSS used to hide the native html used to adjust for an integer field. I have not fixed these warnings, in the first case because it is intentional behaviour (the border is set like this so that the elememt size is constant and it stands out on hover).  In the second case the CSS is purely cosmetic, so if for example a 95 year old is still for some reason using Internet Explorer and the field adjuster is not hidden it won't affect the functionality or layout of the site at all.\
Outstanding Issues: None.

![image](media/testing/css-validation.png)

### JavaScript Validation
([back to top](#testing-documentation))

I have validated my JavaScript file using [JSHint](https://jshint.com/)

Repaired Issues: I had to refactor some code due to the way I had set up a function, and I added a large number of semicolons.  I also found some undeclared variables which also required some refactoring.  The one outstanding error refers to Stripe, which JSHint sees as an undefined variable.  I believe this is unavoidable due to the way Stripe functions and the context in which JSHint lints the code - even in my editor it is flagged as undefined, however the Stripe functionality works perfectly which means I do not believe it is a problem.\
Outstanding Issues: Stripe flagged as undefined.

![image](media/testing/jshint-linted.png)

### Python Validation
([back to top](#testing-documentation))

I have used the [CI Python Linter](https://pep8ci.herokuapp.com/#) to ensure my python files are PEP 8 compliant:

App: addresses\
Files Linted: forms.py, models.py, urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.

App: admin_console\
Files Linted: urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.

App: basket\
Files Linted: contexts.py, urls.py, views.py, order_calculator.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.

App: checkout\
Files Linted: forms.py, models.py, urls.py, views.py, webhook_handler.py, webhooks.py\
Repaired Issues: whitespace, spaces around operators and line length.  Line length issues meant I had to refactor code with variables and functions assigned shorted names and swap some fstrings for regularly constructed ones.\
Outstanding Issues: None.

App: cheese_beer\
Files Linted: settings.py, urls.py\
Repaired Issues: whitespace, spaces around operators, issue using '==' operator to test for boolean False (changed to 'is')
Outstanding Issues: None.

App: home\
Files Linted: urls.py, views.py\
Repaired Issues: whitespace.\
Outstanding Issues: None.

App: product_views\
Files Linted: urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length, also cannot use bare except so i had to look up the error
I was testing for and add it to the code.\
Outstanding Issues: None.

App: products\
Files Linted: contexts.py, signals.py, forms.py, models.py, urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.

App: user_account\
Files Linted: forms.py, models.py, urls.py, views.py\
Repaired Issues: whitespace, spaces around operators and line length\
Outstanding Issues: None.

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

During the course of the Django module we were shown how to use the testing feature and assess testing coverage.  I would have loved to implement it for this project, however on account of the size of the project and the timescales involved applying automated testing across the site would have taken too much time and resource to do properly.

With this in mind and the fact I have a well established manual testing process which I have applied successfully to my last two projects, I have decided to stick to manual testing on this occasion, and look into automated testing once the MVP has been completed.

### Manual Testing
([back to top](#testing-documentation))

#### Manually Testing Page Functionality

Although there are a total of 32 pages across the site, manual testing is still practical because many of them are very similar, and none of them are extremely complicated. As such my apporach will be to systematically check the functionality of every page against expected outcomes to ensure the site is working as intended, rather than go through every line of code, which will only be necessary if I find a major bug.

BASE TEMPLATE NAVIGATION:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| Cheese menu | on mousover or onclick (for mobile) returns drop-down list of cheese categories | Success |
| Cheese menu | mouseover highlights menu options correctly  | Success |
| Cheese menu | on clicking out of the menu the menu hides (mobile)  | Success |
| Cheese menu | each category returns product view with products in that category | Success |
| Beer menu | on mousover returns or onclick (for mobile)  drop-down list of beer categories | Success |
| Beer menu | mouseover highlights menu options correctly  | Success |
| Beer menu | on clicking out of the menu the menu hides (mobile)  | Success |
| Beer menu | each category returns product view with products in that category | Success |
| Account menu | on mousover returns appropriate drop-down list to user status | Success |
| Account menu | mouseover highlights menu options correctly  | Success |
| Account menu | on clicking out of the menu the menu hides (mobile)  | Success |
| Account menu | all menu options return the correct page | Success |
| Main Search | mouseover or on-click effects on search button work correctly | Success |
| Main Search | on entering a search term the product view is returned with appropriate results | Success |
| Main Search | if no search term is entered the product view is returned with all products dispayed | Success |
| Logo banner | returns the user to the homepage | Success |
| Checkout button | only visible if the user has something in their basket | Success |
| Checkout button | mouseover/active effects work as intented | Success |
| Checkout button | on click takes user directly to checkout page | Success |
| Basket section | only visible if the user has something in their basket | Success |
| Basket section | mouseover/active effects work as intented | Success |
| Basket section | on click takes user directly their basket of goods | Success |

HOME PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| Buy cheese button | returns product list view of all cheeses | Success |
| Buy beer button | returns product list view of all beers | Success |

FIND ORDER:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| Input fields | highlight correctly when focussed | Success |
| Form element | form will not submit unless all fields correctly filled out | Success |
| Form element | accurately filled out form returns specific order items | Success |

404 PAGE

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| DOM |	page loads correctly whenever an invalid url is entered | Success |
| Life goals button | Returns product view with a list of all cheeses  | Success |

PRODUCTS LIST PAGE AND SEARCH

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| Initial Sorting |	Products initially sorted by most recently added |	Success |
| Search Text |	Correctly displays the search results |	Success |
| Sort by Price Filter (low-high) | Orders products from the cheapest by weight/volume to the most expensive |	Success |
| Sort by Price Filter (high-low) | Orders products from the most expensive by weight/volume to the cheapest |	Success |
| Sort by Most Popular | Orders products by the most units sold |	Success |
| Category Link | returns product list page with all products in category |	Success |
| Variety Link | link returns product list page with all products containing that variety |	Success |
| Product Image | clicking the product image returns the product detail view for that product | Success |
| Product Name | clicking the product name returns the product detail view for that product | Success |
| More information | clicking returns the product detail view for that product | Success |
| Add to wishlist | successfully adds the product to the wishlist for that user, re-loads with remove from wishlist button | Success |
| Remove from wishlist | successfully adds the product to the wishlist for that user, re-loads with add to wishlist button | Success |
| Add button | successfully adds product to basket, activates appropriate notification | Success |
| Buy button (no items in basket) | adds item to basket, returns user to checkout page, triggers appropriate notification | Success |
| Buy button (items in basket) | successfully triggers a buy now notification for the product if items are in basket | Success |
| Buy notification ('no') | returns user to checkout page with just that item in basket, returns appropriate notification | Success |
| Buy notification ('yes') | returns user to checkout page adding the item to the basket, returns appropriate notification | Success |
| Buy notification ('yes') | returns user to checkout page adding the item to the basket, returns appropriate notification | Success |

VIEW PRODUCT

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| Pairings sorted by Most Popular | Orders paired products by the most units sold |	Success |
| Pairing Category Link | returns product list page with all products in category |	Success |
| Pairing Variety Link | link returns product list page with all products containing that variety |	Success |
| Pairing Product Image | clicking the product image returns the product detail view for that product | Success |
| Pairing Product Name | clicking the product name returns the product detail view for that product | Success |
| Pairing More information | clicking returns the product detail view for that product | Success |
| Pairing Add to wishlist | successfully adds the product to the wishlist for that user, re-loads with remove from wishlist button | Success |
| Pairing Remove from wishlist | successfully adds the product to the wishlist for that user, re-loads with add to wishlist button | Success |
| Pairing Add button | successfully adds product to basket, activates appropriate notification | Success |
| Pairing Buy button (no items in basket) | adds item to basket, returns user to checkout page, triggers appropriate notification | Success |
| Pairing Buy button (items in basket) | successfully triggers a buy now notification for the product if items are in basket | Success |
| Pairing Buy notification ('no') | returns user to checkout page with just that item in basket, returns appropriate notification | Success |
| Pairing Buy notification ('yes') | returns user to checkout page adding the item to the basket, returns appropriate notification | Success |
| Product Add button | successfully adds product to basket with correct quantity, activates appropriate notification | Success |
| Product Buy button (no items in basket) | adds item to basket with correct quantity, returns user to checkout page, triggers appropriate notification | Success |
| Product Buy button (items in basket) | successfully triggers a buy now notification for the product if items are in basket | Success |
| Product Buy notification ('no') | returns user to checkout page with just that item in basket in correct quantity, returns appropriate notification | Success |
| Product Buy notification ('yes') | returns user to checkout page adding the item to the basket in correct quantity, returns appropriate notification | Success |
| Product Add to wishlist | successfully adds the product to the wishlist for that user, re-loads with remove from wishlist button | Success |
| Product Remove from wishlist | successfully adds the product to the wishlist for that user, re-loads with add to wishlist button | Success |
| Product Add to wishlist | successfully adds the product to the wishlist for that user, re-loads with remove from wishlist button | Success |
| Product Remove from wishlist | successfully adds the product to the wishlist for that user, re-loads with add to wishlist button | Success |
| Product Quantity Plus | Increments quantity counter by 1, updates total | Success |
| Product Quantity Plus | Will not advance beyond 200 units | Success |
| Product Quantity Minus | Decrements quantity counter by 1, updates total | Success |
| Product Quantity Minus | Will not decrease below 1 | Success |
| Product Quantity Box manual entry | updates total with appropriate value to number typed | Success |
| Product Remove from wishlist | successfully adds the product to the wishlist for that user, re-loads with add to wishlist button | Success |
| Product Quantity Limited | If a number is entered below 1 or above 200 buttons disapled and notification displayed | Success |
| Product Buttons re-enabled | If a number beyond the threshold is adjusted below it, buttons re-enabled | Success |

CHECKOUT

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| Address Form | displayed if user is not logged in along with sign-up / sign-in links | Success |
| Address Form Validation | JavaScript validation prevents form submission unless address correctly filled out | Success |
| Credit card validation | JavaScript validation prevents form submission unless stripe element correctly filled out | Success |
| Sign in link | returns user to sign-in page | Success |
| Sign up link | returns user to sign-up page | Success |
| Quantity plus | adds another unit of item to basket, returns appropriate notification | Success |
| Quantity minus | removes a unit item to basket unless there is only 1 unit remaining, returns appropriate notification | Success |
| Quantity minus disable | disables minus button when quantity is 1 | Success |
| Quantity minus re-enable | enables minus button when quantity climbs above | Success |
| Purchase Now | Submits form when all fields correctly filled out and returns user to confirmation page | Success |
| New user loggin in checkout | User with no addresses shown form to add new address | Success |
| New user address form | will not submit unless correctly filled out | Success |
| New user address form | on submission returns user to checkout with address listed in address section | Success |
| New user address form | on submission first address automatically set to default | Success |
| Address-prepopulation | the selected user address pre-populates the checkout address field | Success |
| Address options | display the correct options depending on the address status | Success |
| Use new address llink | displays address form for existing user to add a new address | Success |
| Address add cancel button | returns user to checkout | Success |
| Select another address link | opens address selector to select another address | Success |
| Address selector | correctly highlights selected address and adjusts if clicked on | Success |
| Address selector select button | selects current address for order, returns to checkout view with correct address populated | Success |
| Address selector cancel button | returns to checkout view with no changes to previously selected address | Success |
| Use Default link | changes selected address to default, re-loads checkout page | Success |
| Form submission | on correctly entering card details, form submits with selected address correctly populating order form and returns user to conformation page | Success |

CHECKOUT CONFIRMATION

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| Order Link | link redirects user to the order they have just submitted | Success |
| Order e-mail | the checkout page displays the correct e-mail address  | Success |
| e-mail confirmation | the user receives e-mail confirmation of their order  | Success |

BASKET REVIEW

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |
| Product Image | clicking the product image returns the product detail view for that product | Success |
| Product Name | clicking the product name returns the product detail view for that product | Success |
| Quantity plus | adds another unit of item to basket, returns appropriate notification | Success |
| Quantity minus | removes a unit item to basket unless there is only 1 unit remaining, returns appropriate notification | Success |
| Quantity minus disable | disables minus button when quantity is 1 | Success |
| Quantity minus re-enable | enables minus button when quantity climbs above | Success |
| remove link | removes item from basket, returning basket notification on same page if there are still produts remaining, or returning to homepage with message if the action empties the basket | Success |
| Go to Checkout buttons | both return user to checkout page | Success |

LOGIN

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

SIGNUP

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

PASSWORD RESET

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

PASSWORD RESET DONE

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

PASSWORD RESET FROM KEY

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

MY ACCOUNT

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

MANAGE ADDRESSES

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

ADD AN ADDRESS

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

EDIT AN ADDRESS

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

ORDERS PAGE

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

VIEW ORDER INFO

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

VIEW WISHLIST

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

CONTACT US

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

ADMIN CONSOLE

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

ADD CHEESE CATEGORY

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

ADD BEER CATEGORY

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

EDIT CATEGORIES

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

EDIT CHEESE CATEGORY

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

EDIT BEER CATEGORY


| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

ADD BEER

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

ADD CHEESE

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

EDIT EXISTING PRODUCT

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

PRODUCT EDIT PAGE

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

VIEW CUSTOMER MESSAGES

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| DOM |	all interactable elements change on hover and show pointer | Success |

#### Issues found during manual testing

The manual testing process uncovered a few issues, none of which were serious and all of which were easily fixed.

 - The majority of buttons site-wide did not display the pointer on mouse element, so I needed to add the appropriate helper class to them all.
 - The Account menu header was nested in a span rather than a div which meant it wasn't takig up all the space it was supposed to and proved hard to click on.  This was rectified by updating how the elements were nested.
 - found issue in checkout and basket pages where decremening the amount when it was on 1 unit still triggered a notification.  Wrote some javascript to disable the button on that amount.

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


CONSOLE WARNINGS:

The presence of Stripe leads to multiple warnings in the console.  Further reading revealed this was on account of how browsers are becoming stricter in terms of how they handle third party cookies. Reading the Stripe documentation this was acknowledged, however it was also made clear that none of these warnings affect the functionality of the API.  In terms of removing them, there is not much I can do for now other than to remove Stripe, which is obviously not a good idea since it is a compulsary component of this project.

SITE FLAGGED AS MALICIOUS:

When testing on my mobile, I noticed that Cheese and Beer was flagged as malicious; on entering my password it was suggested I change it anywhere I use it. Obviously this is not the case and my password is safe, but it does make me wonder what aspect of either Allauth, Stripe, my own custom code or Django in general is causing this, since it has not occurred on any of my other projects.  I have already mentioned a number of concerns I have about the way the site is structured, in particularly how Stripe client secret keys are handled, and wonder if it could be related to this. It may be where I have removed the JQuery.post API - un-necessary as it was in the context of the site perhaps that buffer served to re-assure the browser. If this were to be a production site with live payments and customers I would definitely need to address these concerns in the manner I have already outlined in this section. As things stand it is only an 8 week project and in the context of its current purpose and that timescale I'm not able to prioritise this at all for now.

QUANTITY BUG:

In our final meeting my mentor pointed out that if he purchased 7 million units of cheese from the product view it broke the site.  I added javascript to disable the add or buy now buttons for numbers outside of reasonable parameters to stop this becoming a problem.  I also updated the database fields so that a user may spend several googols on cheese if they wish.






([back to top](#contents))