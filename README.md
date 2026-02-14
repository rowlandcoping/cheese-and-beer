# Cheese and Beer

![image](media/images/general/cheese-quote.jpg)

Cheese and Beer is intended to become the UK's premier marketplace for purchasing cheese on the internet.  It will be reasonably priced (unlike the majority of other similar providers), and the website itself focussed on brilliant UI which not only makes it easy for users to find what they want, but that helps them find something they perhaps didn't even know they wanted in the first place. It's the Apple approach to cheese. The brand plays on the unheralded but actually excellent combination of beer and cheese, and the platform itself will not only reward the true cheese enthusiasts but actively encourages gifting from casual cheese purchasers - as such the platform will be accessible to all and free from any impenetrable cheese terminology or jargon.

## Contents:

### UX Design

[UX Design - Strategy](#ux---strategy)\
[UX Design - Scope](#ux---scope)\
[UX Design - Structure](#ux---structure)\
[UX Design - Skeleton](#ux---skeleton)\
[UX Design - Surface](#ux---surface)

### The MVP

[Specification Changes](#specification-changes)\
[MVP Data Structure](#mvp-data-structure)\
[Feature List](#feature-list)

### Testing and Deployment

[Testing Documentation](#testing-documentation)\
[Deployment](#deployment)

### Credits and Technical

[Credits](#credits)\
[Technical Information](#technical-information)

## UX - Strategy 
([back to top](#contents))

### 1) Research

You don't have to look far to find the best online retailers.  Amazon is the benchmark for everyone, majestically filtering a product range which includes pretty much everything and enabling users to one-click purchase whatever is on their mind and deliver it the very next day.  There is a reason they are number one and I think every online retailer draws inspiration from them.

This website is for a specialist retailer though, so I have looked for examples in that area as well.  Paxton and Whitfield's website, for example, is exhaustive in content and slick in design, and provides a good benchmark for the sort of range a decent cheese retailer needs to be carrying.  I have also found guides on how to pair cheese with beer which I think will be very useful when making suggestions to the user.

One thing that strikes me about Amazon in particular but also the cheese retailer is the sheer number of menus, sub-menus and options.  Paxton and Whitfields has no fewer than nine options in their main navigation bar, which open admittedly very nice sub-pages when you mouse-over.  Amazon... well Amazon is just ridiculous (it gets even more ridiculous when you try and navigate AWS but that's another matter).  I think Amazon assumes a certain familiarity from the user, and gets away with a lot of bad UI as a result.  Most people know where to find what they need on there.  I pretty much never click on any of the navigation links though, aside from the 'my account' options.  What would a new user make of it?  When you search for products and scroll down the page you get a heading saying more products, then the same heading again with even more products... then you finally get pagination! I think for a specialist site aimed at more casual users, you just can't get away with most of this - people will get lost and give up.  The simpler the navigation the better.  Of course, there is a huge caveat to this.  For the exact same reason it would be foolish not to emulate Amazon's site layout to some degree, so that the majority of users will feel comfortable and instantly be able to find where everything is.

When it comes to positioning and branding Paxton and Whitfield seems to be at the upper end of the market. It assumes a certain level of knowledge about the products, as I'd imagine most visitors will have.  At the other end of the market is the supermarket, and whilst you can purchase a similar quantity of pretty decent cheese and get change from ten pounds, it does lack a certain sense of occasion.  There is room then, in the middle ground.  The cheese and beer branding should sit perfectly in this area - craft ales rather than fine wines, and enough sense of occasion to feel like you're doing something special without being unconfortable about the amount of money you're spending on it.  A site that isn't just for enthusiasts, but is for everyone.

### 2) Project Goal

Cheese and Beer is about the democratisation of cheese. To enjoy the product you don't have to buy artisan cheese made only in a small shed somewhere in Wales, and you shouldn't be made to feel like you have to. The website will be focussed on casual browsing and making that easy for the user, with a search facility for those who know exactly what they want.  Suggestions and tools to help users plan and budget their purchases will encourage engagement and upsell, and intuative and simple account and address management tools will make checking out and making purchases as gifts incredibly simple.  Whilst the gifting market will be strongly in mind, there will also be visitors who are just love cheese and beer and want to treat themselves or their families without breaking the bank, and the website will cater for them too.

### 3) Developer Goals

- Simplify the MVP:  Having learned hard lessons from the initial over-ambition of previous projects, and keeping in mind the modular nature of Django, I am aiming for an extremely lean MVP which I can then build upon.  The way the user stories and feature list are structured will provide absolute clarity on the work that needs to be done, work that could be done if there is time, and work that won't even be considered as part of this project submission.
- Take advantage of Django: Learning how to customise Django will be my biggest challenge, as I intend to take advantage of Django Forms, Allauth and crispy forms (not to mention Stripe which is compulsary!).
- Deliver a Real World project:  This is always my ultimate goal, but in this case it's particularly relevant.  This should be a project that could conceivably be switched on to take real customer orders once the MVP has been submitted.

### 4) Site Owner - User Stories

- Site Identity: The landing page needs to make people feel at home and get across the core values of the site.
- Simple, familiar design:  There is no need to re-invent the wheel with this site, in terms of how products are presented, and there are plenty of excellent benchmarks out there.
- Uncluttered UI: I think it's important that users aren't overwhelmed with menu options, especially on mobile.  There is no need to overcomplicte a website about cheese (and beer).
- Clear Pathway:  As soon as the user lands on the site their pathway should be clear and the options they are presented with need to take them towards the site goal (ie sales) as quickly as possible.
- Engaging sales pathways: Although many features in this area may not form part of the MVP (see developed goals concerning keeping it simple) having novel and simple to use means of engagement, such as (for example) a cheeseboard generator, is key.
- Regulatory Compliance and Security: As I want this to be a real world application, no features will be implemented that are not compliant with best practice, such as PCI DSS regulations.  If implemented, things like storing user payment details should be done through Stripe (which presumably takes care of most of this).

### 5) Site Visitor - User Stories

The site is positioned, for want of a better description, to appeal to the cheese and beer layman.  For the end user, accessibility is key.

- A homepage like home: Users need to feel comfortable when they land on the site.  Not like they are being overly sold to, or that the site 'isn't for them'.  Homepage promotions should be informative first.
- Clear pathways: Once the user has landed on the homepage, they need a clear and obvious path to locate what it is they visited the site for in the first place.
- Recommendations: For users uninitiated in the world of cheese, it is important to have recommendations and suggestions, especially when it comes to pairing.
- Easy checkout: The user doesn't want to have to jump through a lot of hoops to do anything online, especially on mobile. They want to buy what they want and get gone.
- Seperate billing and delivery addresses: If a user is purchasing a gift it should be easy to add, select and save multiple delivery addresses.
- Retain key details:  People are used to one click shopping with Amazon's buy it now, for example.  Equally they also want to feel their data is protected.  This is a fine line.
- Review order history:  Customers would like to be able to review and track their orders, especially if everything doesn't go to plan. They want this re-assurance.

## UX - Scope
([back to top](#contents))

### Technology

The technology used will be HTML/CSS and JavaScript, and Python with the Django framework and a SQL-based relational database to store data, most likely using Django's built-in models.

I am lucky in that I have developed strong skills with vanilla Javascript and CSS Flexbox which means there is little to gain from using a heavy library like Bootstrap.  It's just as quick for me to hand-code my own media queries and in some ways quicker since Bootstrap needs a degree of customisation in any case.  I am also wary from a previous project of how awkward it can sometimes be to customise Bootstrap-based code.  Furthermore I don't want to slow my code down with multiple imports, where the majority of the code is actually unnecessary.  

One issue in dispensing with Bootstrap is the integration of Bootstrap JQuery libraries into the course material, and some of the custom methods that were used in the checkout process which I'm not sure how to replicate as yet. Whilst I can see the benefit of the shorthand, going forward I would rather invest time in learning something like React and REST APIs.  With the time limitations involved in this project, it is much easier for me to use the vanilla JavaScript I'm already familiar with - hopefully it will be pretty straighforward to build the vanilla JS code to emulate these methods, using fetch().

This all said, it is clear to me that some of the dependencies from the learning I have done (notably Stripe, Django, and AllAuth forms) benefit from using Crispy Forms and the templates that come with such libraries. I think there would be a very high development overhead in doing all this customisation myself (more so than building the forms from scratch). As such I have been looking at other CSS libraries that integrate with Crispy Forms, and have decided to attempt to use Tailwind. It seems to be the most popular and easy to use framework out there, and from my research seems to come without a lot of the bloat associated with Bootstrap, relying as it does on a range of helper classes. Ideally, I want the best of both worlds - instantly formatted forms that are easy to customise where necessary. Speaking frankly it may even prove to be easier to style the whole website in the manner of the forms than the other way around!

### Structure

 - Home Page: Logo, menu and search in the main navigation for immediate browsing.  The main area of the page will feature two callouts - one linking to special offers and the other to the create your own cheeseboard feature (if included).  It will also feature a brief site mission statement.
 - Search/Filter:  Once a user either searches or filters the page via one of the menus, a familiar looking results screen will appear with basic product information which the user can browse.
 - Product view: When clicking on a product the page provides more detailed information plus the opportunity to add the item to the cart or purchase immediately, and a 'recommended' section which will focus on product pairing (cheese to beer, and beer to cheese (or sundries should they be integrated into the project.)).
 - Cart page:  If the user has filled a cart with items, they can review and update these items.
 - Checkout page:  Here the user selects/inputs their billing and delivery address, specifies whether the item is a gift (and if they want it wrapped) and enters their payment details, and which details they wish to retain (ie register as a user)
 - Confirmation page: This is where users will be provided with confirmation of their purchase.
 - Product update page:  The site is not envisaged as an amazon style marketplace, so the only users who will have access to this are designated administrators of the platform.  Here new products can be added and removed.
 - Order history (with varying permissions):  Users can view their own order history, customer services can view any of them, and managers/admins have update tools.  Not all of this will be in the lean MVP as it's not clear on the levels of permissions built into allauth, but obviously superuser isn't suitable in all cases.
 - Manage account:  User can change billing/delivery addresses, other personal details, or payment options (if included).  They can access their order history from here. Users which are not signed in will have the option to search for their order by order number to track it.

### Features

I have organised the feature list into multiple categories based on user stories, with a very strict MVP list, an expanded list which ought to be viable in the time allowed once the MVP has been completed (with hard work and good luck), and a nice-to-have list which I view as highly unlikely to be implemented as things stand.

#### Site Template (features accessible anywhere)

MVP FEATURES

 - Users can search the products on the site
 - Users can access their account information (including order history)
 - Users can access their shopping cart.
 - Users can process direct to checkout for anything in their cart.
 - Users can browse cheese products
 - Users can browse beer products

STRETCH FEATURES:

- Users can filter and browse sundry products (jams/chutneys/accessories/meats).
- Users can filter and browse special offers.
- Users can access BYO / randomized cheeseboard features.

#### Landing Page

MVP FEATURES:

 - Site description (clarity)
 - Site Logo (branding)
 - Site callout for specific products (immediate call to action)

STRETCH FEATURES:

 - Site callout/navigation for cheeseboard builder
 - Site callout/navigation for cheeseboard randomizer
 - Site callout/navigation for special offers

#### Search Results page

MVP FEATURES:

 - Users can browse a list of products
 - Users can click to view individual products
 - Users can filter results by category by clicking on a product's category

STRETCH FEATURES:

 - Users can add x amount of the item to cart or checkout an item directly from search results.
 - Users can see paginated results.
 - Users can view associated recommendations by clicking on a link in the product's listing.

BLUE SKY FEATURES:

 - Users can share a product to social direct from the search results.
 - Users can select the number of results they want to see per page.
 - Users can enable infinite scrolling for results.

#### View Product Page

MVP FEATURES:

 - Users can view full product info
 - Users can click any product category to open another filtered list of results.
 - Users are presented recommendations for pairings with the product on this page(beer or cheese)
 - Users can add x amount of the item to the cart or checkout an item directly

STRETCH FEATURES

 - Add to cheeseboard feature (for BYO cheeseboard)

BLUE SKY FEATURES

 - Share product on social
 - Users can add product to a wishlist

#### Shopping Cart Page

MVP FEATURES:

 - Users can add or remove items from the cart
 - Users can increment or decrement the amount/quantity of an item they wish to purchase
 - Users can proceed to checkout
 - Users can easily return to what they were doing / the homepage

#### Checkout Page

MVP FEATURES:

 - Registered users can access saved addresses
 - Unregistered users can checkout
 - Unregistered users offered option to register prior to checkout
 - Users enter card details into secure checkout process
 - Registered users can opt to store addresses
 - Users can see order summary

STRETCH FEATURES:

 - Users can store card details for next time (this depends on stripe functionality - if it's not a Stripe feature this goes straight to Blue Sky as it would require a lot of reading)

BLUE SKY FEATURES:

 - Users can register as they checkout if they enter a password (NB this would require a custom authorisation system rather than using AllAuth)

#### Order Confirmation Page

MVP FEATURES:

 - Users see an order summary.
 - Users are provided with an order number referencing their order.
 - Users are provided a route back to the site.

BLUE SKY FEATURES:

 - users have option to share their purchase on social.

#### Account Page

MVP FEATURES:

 - Users can edit and update addresses
 - Users can view order history
 - Order history page allows drilling down into individual orders

STRETCH FEATURES:

 - Users can update payment options

BLUE SKY FEATURES:

 - When viewing past orders users can raise a ticket (This is probably un-necessary in a test iteration of the site but will be essential if it ever goes into production, along with some kind of CRM for issue handling, including amending orders and processing refunds.)

#### Admin Features

MVP FEATURES:

 - Admin user can access 'add products' page
 - Admin user can add products
 - Admin user can delete products
 - Admin user can edit products

BLUE SKY FEATURES:

 - Admin user can view sales volumes
 - Admin user has access to stock control algorithms to help stock purchasing or promotional decision making

## UX - Structure
([back to top](#contents))

As with the Scope, it is important to make clear the structure outlined here is the one envisaged at the beginning of the project, and that there was always anticipated to be an evolutionary process in producing an MVP.  For a full overview of specification changes in the completed MVP, please click [HERE](#specification-changes).

The data structure for the submitted MVP can be found [HERE](#mvp-data-structure).

### Site pages and elements

#### Main Template and Navigation

The homepage navigation will emulate to a degree the way Amazon is arranged, with a small logo, prominent search and key navigation arranged horizontally across the top of the screen.  On mobile this stacks to arrange the navigation filters below the search and account links.  For logged in users the can access their account details at the top right of the page, as is convention.

Although I generally try to avoid drop-down menus, I believe they will be necessary to allow users to filter without multiple clicks, but I do not wish menus to go more than 1 deep.  Javascript will be effective on desktop, and allow users to filter all by category with one click whilst using mouseover to reveal other options.  For mobile this will require 2 taps but I think users will be used to this.

#### Results Page

Basic product details will be shown on results pages, with an initial 4-8 items shown and the option to view more (as with Amazon).  I would like to include pagination if I have time, but on such a niche site the small number of products available should mean it's not an essential (and it would require learning from scratch to do it with Django although I'd imageine the principle is the same as with anything else!).  I'm also keen to have instant checkout options here (everywhere in fact) as somtimes people just know what they want and the shopping cart mean unnecessary extra clicks.

#### Item Page

This will contain full product information, more order options and a recommendation section, which will pair beer with cheese.  This will be pretty straighforward process and the pairings will be set on product creation as part of the data modelling.

#### Shopping Basket Page

The concept involves allowing users to edit their basket and also add giftwrap/convert to cheeseboard (if included) options on the page.  These are nice to have options but they should be straightforward to include and I think are close to essential on a site which will lean heavily towards gifting.  If I include as planned and instant checkout option then these options will also need to be available on the checkout page, as well as the option for a user to change their mind.  It's important in these sorts of cases the user doesn't have to go hunting to achieve what they want to achieve.

#### Checkout Page

I intend to give users a choice of saved addresses, and the option to designate a seperate billing / delivery address using Javascript to show/hide and autofill fields if boxes are checked or unchecked.  I think the convenience of this is a key part of what makes Amazon so successful.  I would also like to do the same for payment details, but that will be time-restricted as there are a lot of extra considerations when it comes to storing sensitive financial data which I think are beyond the scope of this project.  The theory remains the same however, minimal user input to acheive the end result, creating a seamless experience.

#### Confirmation Page

This will be straightforward so I haven't wireframed it, but I also want to provide unique order references so that users can track their order without logging in.  This is very important for unregistered users.

#### Add / Edit Product Page

I've considered a number of complex iterations of this, but in the end it will be very simple case of choosing to add beer or cheese and then having near identical forms to fill out in the style of the wireframe. It could be condensed to a single page and the form presented and controlled using Javascript and a drop-down, but it makes little sense to spend time on this when it is only for site-affiliated admin users, which in practice will only ever be me.  That said, although this website is not intended to be a storefront, it will be formatted so that other admin users find it a pleasure to use. It will also have proper image handling so that images are uploaded and stored in the proper size and format rather than this being incumbent on the user. Searching for products will also provide admin users the chance to edit products (but they can only be deleted from the edit item page, I'm keen not to make that too easy).  I also think it will make sense that for any product which has been involved in an order to have a for a hide option rather than a delete, which hides them from the user using an availability toggle - items may often be temporarily unavailable and if something has been sold in the past it's important to retain that link to the order history.

#### Account Section

This will be a simple menu offering order history, manage addresses or update personal details.  Order history will be a simple list of orders that can be expanded when clicked on.

### Core Data Structure

Please note that this section represents the initial design phase for the database schema, and may well be subject to change.

Having used MongoDB in my previous project, I'm glad that a relational database will be used in this one - it means that data can be broken down into chunks and their relationships with each other can be tracked and indexed very easily and my Python code should be a lot simpler (theoretically).

My main decisions when modelling the data for this project are whether I need sub-models for the various classes of product.  In the end I have decided that the bulk of the information for each product will be defined by the type (cheese or beer) and then category selected from a drop-down dependent on the type.  This will be extremely handy when it comes to making recommendations on the item page and will make product creation a simple matter of adding a name, image, price and quantity, then selecting the appropriate category from a drop-down.  Each product will be sub-class of the selected type and category (eg Camembert) and inherit its characteristics, likewise for beer.  I belive this functionality is built in to Django Models so should be easy to implement. It ought to make creating products very easy, as the user can opt to either keep the general category description or edit it to their own.  

Apart from that everything will be very straightforward, except that addresses will have their own data model linked to the user by a foreign key so that users can save multiple addresses.  It will also make it easy to track which addresses have been used in the order history, should users subsequently change their address.

I am keen that users log in with their e-mail.  It is rare pepole are able to remember their username, especially as often the one they are most likely to use is already taken.  Personally, there is little more frustrating.  Because the e-mail address is a unique piece of data, I don't know why anyone would do it any other way unless they are safeguarding against very weak passwords, which will be taken care of in this case when they are created.

#### Schema Diagram

![image](media/data-model/db-schema.png)

#### Users Model

This will include basic user authentication data, for the most part created by AllAuth.  

#### Addresses Model

This is the model for user addresses, which also logs the associated user ID and whether it is a billing or shipping address.  For shipping addresses there will also be the option to add a shipping name, which will default to the user's name for billing addresses.

#### Cheese Category Model

Will include details of generic cheese types, from Goat's Cheese to Gruyere, along with their characteristics and pairing recommendations.

#### Beer Category Model

Will include details of generic beer types, along with their characteristics and pairing recommendations.

#### Products Model

A unique product which will include type, name, description, images, price, and will relate to an order history.  Related to the selected category model.

#### Orders Model

Each table entry will be for a seperate order, logging who ordered it, when, the total order value, additional options selected, plus the billing and shipping address foreign keys.

#### Order Items Model

A record of each individual item ordered, linked to an order by foreign key as well as the product.

![image](static/images/data-model/diary.png)

## UX - Skeleton
([back to top](#contents))


### Design Choices

 - I've kept the site layout as simple and familiar as possible, looking to emulate the layout of similar sites that users will be familiar with.
 - The intention is that users are able to to make a purchasing decision from pretty much anywhere and with minimal clicks (as with most online retailers)
 - The navigation is designed to stack on mobile but users will still have access to navigation icons.  I do not want users having to negotiate multiple clicks to find what they want on smaller screens.  Neither do I want mobile users to lose any core functionality or visual clarity.
 - When products are displayed the balance is to show the information the user needs without overloading the page.  As such initial search results are limited and the user can opt to view more if they want to.  Again this is a concept borrowed from Amazon.
 - Entering new products is designed to be as fast and simple as possible with nominal information required and a lot of core info stored in the item category section.  The categories will require some work to get right.
 - When checking out the strategy is to only show information the user needs on the screen.  For example if the user checks the box to ship to the billing address, or if they have default billing and shipping addresses the want to use, then they don't need to see an address form.  

### Wireframes

Please find the wireframes [HERE](WIREFRAMES.md).

## UX - Surface
([back to top](#contents))

The main site inspiration when it comes to much of the layout is Amazon, mainly because I know that all potential users will be highly familiar with it. What I have focussed on is reducing clutter and maximising reponsiveness but still providing the user with plenty of elements to interact with and keep them engaged.  The green and gold scheme is evocotive of quality, and also of cheese.  The color scheme background is intended to provide a slight contrast for item elements across the product and purchase pages. The grey border and dividing lines break up the page without being as obtrusive as a horizontal rule, although I have used these for hard dividing lines, for example in the checkout section. For all forms and indeed any page without a lot of complex content (for example the whole admin site) I have used an image background to provide some depth to the page.

### Color Palate

HELPER CLASSES

rgb(3, 126, 3): green-text\
rgb(255, 0, 0): red-text\
rgb(95, 0, 0): dark-red-text\
rgb(1, 70, 1): forest-green-text\
rgb(0, 51, 0): dark-green-text\
rgb(63, 63, 63): grey-text\

SITE THEME

rgb(1, 70, 1): background for top section of site containing navigation and search, also used for form buttons and links, and a border on focussed form elements.\
rgb(0, 51, 0): background for checkout buttons and the main site logo. Generally used to accent the main green theme, also used for links.\
rgb(0, 15, 0) : dark green border used in title banner, also used to accent form fields.\
rgb(255, 255, 140): text color for titles and navigation, also inverted with the forest green for mouseover effect. Also used on mousover for checkout and basket buttons.\
rgb(255, 255, 255): white is used as the immediate background for across the listing and purchases sections of the site.  It provides a contrast with the light yellow used for page backgrounds on these pages.\
rgb(247, 241, 213): the off-yellow base background for the listing and product pages.  Also forms the text background on form pages, the header and footer background on alerts, and the background for basket alerts.\
grey (50 shades of): used for border helper classes, and generally any borders or boundaries anywhere across the site.
rgb(107, 107, 107): the grey used for the box shadow effect site-wide.\
rgb(129, 153, 124): used for the hover state for most form buttons.\

PURCHASE BUTTONS

rgb(139, 67, 0): the color for the add to basket button, universally.\
(245, 183, 126): hover state for add to basket button.\
rgb(16, 95, 0): the color for the buy now button, site-wide.\
rgb(129, 153, 124): hover state for the buy now button.\

MESSAGES AND ALERTS

rgb(245, 26, 26) - used as border for error messages.\
rgb(16, 95, 0) - used as border for success messages.\
rgb(245, 150, 26) - used as border for warning messages.\
rgb(0, 32, 0) - background for the yes button.\
rgb(50, 90, 50) - hover background for yes button.\
rgb(49, 0, 0) - background for no button.\
rgb(94, 42, 42) - hover background for no button.

### Fonts

Title: FallIsComingRegular-Mx9B (Fontspace)\
Content: RobotoFlex (google fonts)

### Images

The only static image is the background used on form pages, which comes from unsplash.

### Navigation

The navigation is drop-down on desktop to limit the number of clicks between a user and their destination. The idea is that by simply having a drop-down category selector a user can immediately navigate to the content they want.  This is a two tap process on mobile but the principle remains the same.  The navigation is very much in keeping with the site theme, and to some degree actually sets the site theme.

Buttons are clearly styled according to their purpose, so without even reading them a user can know what they are expected to do.  So the outsize green buttons to make purchases clearly indicate a major action, whilst the buy now and add buttons are consistently styled and retain an icon to make their purpose clear.

Results from searches are clearly indicated, and in the search listings I have underlined key links either immediately, or in the case of listing titles, on hover to make the action which the user needs to take as clear as possible. When a user adds a product to their basket there is a clear message on the page, indicating the specific product, and the user is taken back to the view that they were in so they retain their search results.

Across the user account section, all pages have a link back to the user's most likely point of origin, which I think really helps the flow of the site.

Of course user experience is key, but the focus of this site is driving people to make purchases.  As such most calls to action are focussed around pointing people in this direction, including buy now buttons on every product listing (even 'buy again' on the order view page) which take the user directly to checkout.  THere are multiple purchase buttons on the checkout page itself, which on desktop are prominently located at the top right of the page.

### Alerts

The alert system on Cheese and Beer is key to the user experience.  If a user adds or updates a product to their basket from any screen, they see an alert detailing the specific product next to the checkout button, which fades to avoid obscuring the navigation.  I have learned a lot from Amazon's Buy Now process, which is confusing and inconsistent. By providing the user with a 'buy now' alert if they click buy now with products already in their basket, it provides the user with a clear pathway to checkout. In this case they are asked if they want to clear other products in their basket or retain them, before the new product is added and they are taken to the checkout screen.  This is aimed at making the process as clear and seamless as possible.  

Additionally users are warned if they are about to delete an address from their addresses page, although the same doesn't apply to items in the wishlist or basket as they can easily be re-added.

On the admin site the same alerts provide clear feedback for user actions.
  
### Responsiveness

The site has been built for desktop, but designed throughout to easily scale for mobile and with that in mind.  The exceptions in my mind are the order list and messages view pages, which had to display a lot of information in a tabular format to be effective. This caused difficulties in scaling them to mobile to the point where I had to remove the 'products ordered' section from the orders list view for smaller screens.  Although I believe they are responsive in their current form, should the site go into live production I would like to re-design them.  Because the admin site is largely for employees and only ever likely to be used in desktop environments, I have not implemented features like auto-resizing of form textboxes to content, for example, but all admin site pages are still perfectly responsive and look good on mobile.

I built the site's responsiveness using the following break-points:

max-width: 359px (for very very very small phones)\
max width: 450px (the main break point for converting to smaller mobile format)\
max-width: 650px (the main break point for converting to a mobile format)\
max width: 940px (for large tablets or people viewing in smaller windows)\
max width: 1200px (to accommodate smaller laptop screens)\
max width: 1650px (to accommodate laptop screens)

## The MVP

### Specification Changes
([back to top](#contents))

As Donald Rumsfeld (RIP) memorably said:

"There are known knowns. These are things we know that we know. There are known unknowns. That is to say, there are things that we know we don't know. But there are also unknown unknowns. There are things we don't know we don't know."

The final feature list for the MVP contains everything from the initial outline, with additional features documented here including the wishlist and contact form.  Focus has been on providing an enhanced experience for logged-in users.  Overall, whilst I only wireframed a handful of pages there are now 32 pages on the site.  However most of them follow one or other of the templates outlined at the outset; product search, product view, order/basket list and forms.

IMPLEMENTATION

My intitial intention was to use crispy forms with templates from Tailwind, having had my fingers burned with Bootstrap on a previous project.  When I first installed Tailwind it immediately implemented its own quite opinionated styling site-wide.  It also seemed a lot more complex than a simple CDN to deploy.  Given how unfamiliar I am with it, I opted to dispense with CSS libraries and style the site myself.  In the event, I found the forms in Django by far the easiest things to style.  In fact the challenge wasn't so much technical aspects as the volume of pages involved. I have definitely learned lessons on this project about improving the re-usability of my code, through thinking about my designs and how I will re-use them rather than just jumping in and attaching styles to elements. There is still room for improvement though. I also think these lessons will help me a lot when I do finally decide to use a CSS library again.

USER SIGNUP

Although I haven't added additional roles as I would like to in the future, I have set all logins and validation to be done via e-mail.  The Allauth login no longer requires a username, because I have built a signal to set the username to equal the user's e-mail address pre-save.  I have also disabled e-mail verification for signup. This makes for a far better user experience and a very slick sign-in process to ensure no potential customer is lost at checkout.

ADDRESS OPTIONS

I decided to dispense with billing address options because it was not required by Stripe to facilitate payments.  Indeed I discovered all Stripe needs for an extra layer of security is an e-mail address, so that is all I passed to the payment intent.  Instead I focussed on usability - users can now add a new shipping address or select from existing addresses directly in the checkout screen.  Instead of seeing a form they are hidden by Javascript and the existing default address is displayed. An additional feature is the 'selected address'.  Users can select a different shipping address for an order without changing their default address, which is stored as a session variable.

USER ACCOUNT PAGE

The user account page now has multiple additional options, adding wishlist and contact options to the existing manage address and order fields. The orders and view order pages now provide direct access to the contact form with pre-populated details.  In fact as the site designer I highly recommend logging in before you use it because it provides so much more functionality.

WISHLIST

Logged-in users can now add items to or remove them from their wishlist from any product page.  THey can also view their wishlist and purchase items from it via their account page or the menu.  This was a simple to implement custom model added at a fairly late stage, but I believe it enhances user experience and makes the site 'stickier'.

CONTACT FORM

I have created a contact form so that users can make queries regarding their orders.  If a user is logged in their data auto-populates, and if they click though from an order this carries over as well. The messages received are currently displayed in the admin site in a very basic view, but for a live payments site this could become a full-blown ticketing system without too much additional work.

ADMIN SITE

Although Products is a single model I created two seperate forms to add either cheese or beer. This is all then processed in the same view. Editing products is all accessed now via the admin site, and includes its own search facility.  Deleting a product is only available if none have been sold. Note that when it comes to categories in the context of this site I consider them close to immutable objects so I haven't included any means to delete them from the front end at all.  This is at least partly because I was worried I might do it by accident!

LOGGED OUT USERS

Even if a user is not registered they can still access their orders if they provide multiple exact details, and can still contact the customer services team (ie me).

### MVP Data Structure
([back to top](#contents))

As anticipated, the final data structure is significantly more complex than the basic structure outlined at the outset of the project.  I have detailed significant changes below:

CHEESE AND BEER CATEGORY MODELS

All custom fields were moved to the products model, and their many to many relationship is represented in a seperate table to reflect how it is handled by Django.

PRODUCTS MODEL

Many fields have been added as the project has progressed.  Most notably the model now tracks units sold, and all the custom cheese or beer fields that were originally in the category models have found a home in the product model.

ORDERS MODEL

This now contains an estimated delivery date for every order.  This will reflect the date that is passed to the view when users are making their purchases.

CONTACT FORM MODEL

I have created a contact form model so that users can make queries regarding their orders.  this simply contains a message and an e-mail address at the bare minimum.  It also has order and user foreign keys, if a user is logged in or provides an order number.

WISHLIST MODEL

This simply contains two foreign keys, one linking the user and one linking the product they added to their wishlist.

#### Schema Diagram

![image](media/data-model/schemaupdated.svg)


### Feature List
([back to top](#contents))

I have outlined here how the site meets the requirements of the MVP feature list, and also demonstrated some of the additional features I have been able to implement to improve user engagement.

#### Site Template

_"Users can search the products on the site."_

![image](media/testing/feature-list/site-template/search.png)

![image](media/testing/feature-list/site-template/filter.png)

_"Users can access their account information (including order history)."_

![image](media/testing/feature-list/site-template/account.png)

_"Users can access their shopping cart."_

![image](media/testing/feature-list/site-template/basket.png)

_"Users can process direct to checkout for anything in their cart."_

![image](media/testing/feature-list/site-template/checkout.png)

_"Users can browse cheese products"_

![image](media/testing/feature-list/site-template/cheese.png)

_"Users can browse beer products."_

![image](media/testing/feature-list/site-template/beer.png)

#### Landing Page

_"Site description (clarity)."_

![image](media/testing/feature-list/landing-page/description.png)

_"Site Logo (branding)."_

![image](media/testing/feature-list/landing-page/logo.png)

_"Site callout for specific products (immediate call to action)"_

![image](media/testing/feature-list/landing-page/products.png)

#### Search results page

_"Users can browse a list of products."_

![image](media/testing/feature-list/results-page/click-to-view.png)

_"Users can click to view individual products."_

![image](media/testing/feature-list/results-page/browse-list.png)

_"Users can filter results by category by clicking on a product's category."_

![image](media/testing/feature-list/results-page/filter-category.png)

_"Users can add x amount of the item to cart or checkout an item directly from search results."_ (Stretch Feature)

![image](media/testing/feature-list/results-page/add-buy.png)

#### View Product Page

_"Users can view full product info."_

![image](media/testing/feature-list/view-product/full-ingo.png)

_"Users can click any product category to open another filtered list of results."_\
NB: whilst this is available for pairings I chose not to make it available for the product itself.  In line with other sites, once a user has drilled down into a product they want you really want them purchasing it rather than navigating away.

![image](media/testing/feature-list/view-product/click-category.png)

_"Users are presented recommendations for pairings with the product on this page(beer or cheese)."_

![image](media/testing/feature-list/view-product/pairings.png)

_"Users can add x amount of the item to the cart or checkout an item directly."_

![image](media/testing/feature-list/view-product/buy-now.png)

_"Users can add product to a wishlist."_ (Blue Sky Feature)

![image](media/testing/feature-list/view-product/wishlist.png)


#### Shopping Cart Page (Basket)

_"Users can add or remove items from the cart."_\
NB: I'm not sure how they'd add them from this view, presumably this means increment.

![image](media/testing/feature-list/shopping-cart/add-remove.png)

_"Users can increment or decrement the amount/quantity of an item they wish to purchase."_

![image](media/testing/feature-list/shopping-cart/inc-dec.png)

_"Users can proceed to checkout."_

![image](media/testing/feature-list/shopping-cart/go-checkout.png)

_"Users can easily return to what they were doing / the homepage."_\
NB: there is no other exit link other than site navigation or checkout on this page by design. Once a user is at their basket you really don't want them going anywhere else until they've bought something!

![image](media/testing/feature-list/shopping-cart/navigation.png)

#### Checkout

_"Registered users can access saved addresses."_

![image](media/testing/feature-list/checkout/saved-addresses.png)

_"Unregistered users can checkout."_

![image](media/testing/feature-list/checkout/unregistered.png)

_"Unregistered users offered option to register prior to checkout."_

![image](media/testing/feature-list/checkout/reg-option.png)

_"Users enter card details into secure checkout process."_

![image](media/testing/feature-list/checkout/stripe.png)

_"Registered users can opt to store addresses."_

![image](media/testing/feature-list/checkout/add-address.png)

_"Users can see order summary."_

![image](media/testing/feature-list/checkout/summary.png)

#### Order Confirmation Page

_"Users see an order summary."_\
NB:Rather than showing a complete order summary on checkout, I kept the page simple opting to share the order number and a link to a summary of the order instead.

![image](media/testing/feature-list/confirmation/summary-link.png)

_"users are provided with an order number referencing their order."_

![image](media/testing/feature-list/confirmation/order-number.png)

_"users are provided a route back to the site."_\
NB: apart from viewing their order, there is always the site navigation.

![image](media/testing/feature-list/confirmation/nav.png)

#### Account Page


_"Users can edit and update addresses."_

![image](media/testing/feature-list/account/addresses-link.png)

![image](media/testing/feature-list/account/addresses.png)

_"Users can view order history."_

![image](media/testing/feature-list/account/orders-link.png)

![image](media/testing/feature-list/account/orders.png)

_"Order history page allows drilling down into individual orders."_

![image](media/testing/feature-list/account/link-order.png)

![image](media/testing/feature-list/account/order-link.png)

_"When viewing past orders users can raise a ticket."_(Blue Sky Feature)
NB: not a ticket as such but the model has a lot of room for expansion

![image](media/testing/feature-list/account/contact.png)

#### Admin Features

_"Admin user can access 'add products' page."_\
NB: admin users don't exist as such, the only option at present is superuser.  Updating the user model was not part of the scope for this MVP.  Presumably this feature means the admin console, hence the screengrab.

![image](media/testing/feature-list/admin/admin-console.png)

_"Admin user can add products"_

![image](media/testing/feature-list/admin/add.png)

_"Admin user can delete products"_

![image](media/testing/feature-list/admin/delete.png)

_"Admin user can edit products"_

![image](media/testing/feature-list/admin/edit.png)

## Testing Documentation
([back to top](#contents))

Please find all testing documentation [HERE](TESTING.md).
  
## Deployment
([back to top](#contents))

### Initial Deployment

Please note the long term home for Cheese and Beer is now [HERE](https://cheesebeer.cookery-corner.co.uk/).  It was a very straightforward process and the entire site worked immediately with only changes to the DATABASE setup and related .env settings. I used the first part of [this guide](https://umar-yusuf.blogspot.com/2020/04/setting-up-django-project-and-app-on.html) to get it set up.

Rather than create a new app, I emptied the folder and [imported](https://www.namecheap.com/support/knowledgebase/article.aspx/10113/2210/how-to-use-git-version-control-cpanel-plugin/) the files from GitHub, before installing everything in requirements.txt using the command on the cpanel terminal: (pip install -r requirements.txt).  It was then a simple matter of adding and updating the .env file.

The main issue was with the export of the ElephantSQL database.  It was zipped using a file format only accesssible via Linux, and then I had to manually go through the export file removing all extensions and changing the name of the default user to that of the new database in every instance (about 250 of them).  This was easy, but only once I had worked it out!

Cheese and Beer was initially deployed via Heroku [HERE] (https://cheese-and-beer-896aa5a35920.herokuapp.com/), following the steps below:

Preparing for Deployment:

- For the site to function, I needed to add a Procfile to the repo containing the command to start the app (web: python app.py).
- I already had an up-to-date requirements.txt file in my repository which I updated as I installed new dependencies.  This was a product of developing my project using a virtual environment in VS Code.
- In order to serve my static files I decided to use WhiteNoise, in order to avoid dependence on AWS or incurring charges. Because my media files are all stored in Cloudinary simply serving static files as efficiently as possible is my priority.
- I added a runtime.txt file to the repo containing the Python version used for this project (python-3.10.12). I upgraded this version on Heroku to 3.10.14 to implement a security upgrade.  Interestingly my Linux Distro (Mint) still serves 3.10.12 as the latest version as of when I began work on this project.

Deploying with WhiteNoise:

In order to deploy with WhiteNoise I did the following:

- Install WhiteNoise
- Add WhiteNoise to the MIDDLEWARE list in settings.py
- Add 'STATICFILES_STORAGE' value: STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

With STATICFILES_STORAGE this differes from the recommended setting in the WhiteNoise documentation, which broke the website.

Creating the App and connecting to Github:

- I logged into my Heroku account.
- From my Dashboard, I selected 'new' then 'Create new app'.
- I selected an available name appropriate to the website - in this case I chose cheese-and-beer, before selecting my region (Europe) and clicking the 'create app' button.
- Heroku immediately took me to the 'Deploy' page.  From this page I went straight to 'Deployment Method' and clicked on Github.
- Once my Github account was connected, I selected the Cheese and Beer repository and clicked 'connect'.
- Once connected I enabled automatic deploys, which means the deployed site automatically updates when it detects a new commit to the linked repository.

Setting up the deployment:

For the site to function I also needed to add the correct environment variables.

- I first went to the settings tab and selected 'Reveal Config Vars' from the 'Config Vars' menu.  
- I then proceeded to add all of my environment variables to this section and save them in turn.
- The final step prior to submission was to ensure the 'DEBUG' environment variable was set to 'False'.

### Deploying this Project

If you wish to deploy a version of this website for yourself, here is how to go about it.

#### Create a Version of the repository:

 - Log in to or create your own Github account [HERE](https://github.com/).
 - Go to the Cheese and Beer repository [HERE](https://github.com/rowlandcoping/cheese-and-beer) and select 'Fork' to create your own snapshot of the repository.

#### Creating your own Heroku Account:

 - Sign in to Heroku [HERE](https://www.heroku.com/).  Keep in mind you will need two-factor authentication to use this website.
 - To use Heroku, unless you have access by some other means, you will need to purchase some platform credits.  For a basic deployment, this won't cost you more than $5/month.

#### Creating the database:

This project uses PostgreSQL to store all data, therefore you will need to create a version of the database to deploy it for yourself.

 - You can sign up to ElephantSQL here [HERE](https://www.elephantsql.com/), this is what I used initially.  A caveat to this is ElephantSQL is at end of life and will be decommissioned in January of 2025, so if you want to work on the project longer term I recommend a more permanent solution.
 - Click 'Create New Instance' to create a new database. Mine is called cheese_beer.  If you click your newly-created database in ElephantSQL it provides all the settings you need to connect it to your Django project.
 - Be sure to migrate the database models to your database from your development platform before you attempt to run the site. This will set all your models up on your database, ready to go!
    - python3 manage.py makemigrations
    - python3 manage.py migrate

#### Creating a Cloudinary Account:

This project hosts all images on Cloudinary.  In order to do the same you will need a Cloudinary account.

 - Sign up to Cloudinary [HERE](https://cloudinary.com/).

Creating an email for the password reset functionality and confirmation e-mails:

For this project you can use gmail to set up an account through which all password reset e-mails and notifications are sent.

 - Set up a gmail account [HERE](https://gmail.com)
 - Once in gmail you can set up a specific app password so that the app can connect to it via SMTP.  Find details of this [HERE](https://support.google.com/mail/answer/185833?hl=en-GB).  Keep in mind this app password resets if you change the password of the gmail account!
 - Keep in mind you can do similar for any email provider.  For this project I have been using Zoho mail (you can set up an account [HERE](https://www.zoho.com/)).  The advantage is they tend to provide fewer hoops for you to jump through than google!
 - I set the non-secure e-mail settings in my settings.py file which you will be able to find in the repo. Keep in mind these settings may vary depending on the provider you are using.

#### Creating a STRIPE Account:

 - In order to process payments (even in a test environment) you will need to set up stripe. I will provide basic instructions here. For local testing you can also install the Stripe CLI which can be useful in tracking down errors in your webhook handlers.
 - sign up to stripe [HERE](https://stripe.com)
 - click 'developers' from the top menu, then select API keys.  You can find the environment variables you need here.

#### Deploy to Heroku

 - Once all of this is set up, you are ready to deploy - first use the instructions I outlined in the [Initial Deployment](#initial-deployment) section.
 - When it comes to setting up the config vars, you will need to set them up according the details of your own database/cloudinary/email accounts.  I have included below a list of all the [environment variables](#cheese-and-beer-environment-variables) that need to be set up on Heroku, and indeed in any local deployment via a .env file.

### Continuing the Project

Once the deployment steps have been completed, as above, you will be in a great position to continue the project.  All you will need to do is set up the [environment variables](#cheese-and-beer-environment-variables) in your chosen development environment.

Using VS Code on Linux:

Using VS Code to continue the project is actually a simple matter because you already have the requirements.txt. I have used it throughout and I have found it straightforward to set it up on a second machine using a venv and the requirements.txt file.

Setting up:

- Install Linux on your machine. You can either dual-boot like I do, or even install a virtual version in Windows.  Either approach is much more straightforward than trying to use VS Code native in Windows, for a number of reasons.  [HERE](https://itsfoss.com/guide-install-linux-mint-16-dual-boot-windows/) is a guide to setting up a dual boot install.
- Install VS Code [HERE](https://code.visualstudio.com/download)
- Click Extensions and search for 'github'.  You want to install 'GitHub Pull Requests and Issues'.
- You should see a github icon you can now use to log in to Github.  Restart VS Code at this point.
- Press CTRL-shift-P to open the command palette and then type 'git:clone'.
- Select this, then click 'clone from github' before selecting your forked repository of Hopes and Dreams.
- Create a folder in an appropriate location.  I save all my repos in a folder called 'repos'.
- You will now be set up and connected to the appropriate repo and the files should all be available in VS CODE, including requirements.txt

Making it work:

- Create an .env file and a .gitignore file.  Add .env to your .gitignore file to ensure you don't upload sensitive data to the public repository!
- Ensure you have python3-venv installed ($sudo apt get update, then $sudo apt-get install python3-venv).
- Press CTRL-shift-P again, then type in python: Create Environment.
- Select Venv, then select the recommended settings to create a new virtual environment. It will install all the dependencies outlined in the requirements.txt file.  Keep in mind that whilst this worked perfectly for me when I used the method with Flask, I haven't yet tried setting up a new development environment in this way for Django. There may be extra steps you need to take.

Setting up your local environment:

With Django I've discovered that using .env is a lot more convenient than an env.py file.  The main advantage is that zero modification is required between development and production servers, aside from the environment variables themselves of course!

- Add the [environment variables](#hopes-and-dreams-environment-variables) to your .env file. Be sure to update your HOST variable to reflect the port you are using locally as opposed to any deployment on Heroku.  For me the HOST is 127.0.0.1.
- Be sure to migrate the database models to your database before you attempt to run the site. This will set all your models up on your database, ready to go!
    - python3 manage.py makemigrations
    - python3 manage.py migrate
- If you type python3 manage.py runserver in your new virtual environment in VS Code, you should see the site working in your if you open the port. You can now continue to develop the project.

### Cheese and Beer Environment Variables

CLOUDINARY:

All the details for your Cloudinary account are provided on your Cloudinary Dashboard when you log in.

CLOUD_NAME=xxxxxxxxxxxxxxx\
    _as found on your Cloudinary dashboard_\
API_KEY=xxxxxxxxxxxxxxx\
    _as found on your Cloudinary dashboard_\
API_SECRET=xxxxxxxxxxxxxxxxxx\
    _as found on your Cloudinary dashboard_\    

EMAIL PROVIDER:

development:\
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend  (this is for development, relays email to your console)\
production:\
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend\
EMAIL_HOST_PASSWORD=xxxxxxxxxx\
EMAIL_HOST_USER=emailaddress@email.com\
    _the e-mail address you've set up_

DATABASE:

DATABASE_URL=postgres://ehsgxqzh:xxxxxxxxxxxxxxxxxxxxxxxxx@flora.db.elephantsql.com/xxxxxx\
_the first set of xs is your password and database, and the last is the database.  All these settings are easily found in the ElephantSQL control panel_

STRIPE SETTINGS:

STRIPE_PUBLIC_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
STRIPE_SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
STRIPE_WH_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\

DJANGO SETTINGS:

CLOUDINARY_BASE=https://res.cloudinary.com/xxxxxxx/image/upload/xxxxxxxxxx/cheese-and-beer/\
_this is the base URL for your media images - in this case we are using cloudinary. please note the first 'xxxxxxx' portion is the same as your cloud name.  If you view an image in the cloudinary explored and check the 'original url' you will be able to find the second part._\
SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
DEBUG=True/False\
_this sets the site into debug or production mode. You should never deploy a live production site with debug set to True.  Keep in mind with debug set to false in the local environment this will cause problems collecting static files.  To run your site locally in this instance, type python3 manage.py runserver --insecure_\
DEVELOPMENT=True/False\
_this should always be set to True on your local host, or False on the live site, otherwise it won't work at all._\
HOST=cheese-and-beer-896aa5a35920.herokuapp.com\
_the host is the base for all urls.  On the deployed site this will be the base of the URL you have deployed to, in a local environment this will be your local host (in my case 127.0.0.1)._

## Credits
([back to top](#contents))

### Layout and Inspiration

AMAZON:

Amazon has been a constant reference point for me in terms of how they manage the customer journey and lay out their site.  They do a lot of things wrong, but they also get a lot right.

PLYMOUTH ARGYLE:

As a fan and former season ticket holder, I can't help but thing my site design has been influenced by their magnificent [home strip](https://www.argylesuperstore.co.uk/kits/home-kit/adults/2507_2324-home-shirt-womens.html) for this season.  It's a real shame the players aren't of the same standard as the shirts.

CHEESE AND BEER:

The following websites have been instumental in furnishing me the the in-depth knowledge I needed to create this website:

https://www.cheesesexdeath.com/the-5-cheese-types\
https://www.pigbeer.com/post/top-5-popular-types-of-beer-found-in-the-uk-and-how-best-to-drink-them

### Fonts

[Fall Is Coming](https://www.fontspace.com/fall-is-coming-font-f30492)\
[Roboto Flex](https://fonts.google.com/specimen/Roboto+Flex)

### Images and Icons

IMAGES:

All product images (barring one or two) are sourced from wikimedia commons.
The background page for forms and the homepage was found on Unsplash.
The favicon was created using GIMP and a free icon I found on a google image search.
The homepage cheese and beer banners were created using Bing image creator.

As such I am free to use them all for the purposes of this site.

ICONS:

Icons are from Font Awesome.

### Content

© 2023 John Hall.

### Code

BOUTIQUE ADO:

The Code Institue project Boutique Ado is what I used to learn Django, and has been a constant reference point.  Notably there are some sections of code, mentioned in the project itself, where I have leaned heavily on it:

- webhook and webhook handling
- The basket app
- Order and OrderItems models
- Stripe payment confirmation
- sort filter and search on product view page

When it comes to the Javascript processing a stripe payment, I have used the Boutique Ado code as a base but made significant adjustments. I do not make a server request (this is covered in detail in the bugs section of [TESTING.md](TESTING.md)). Additionally all the JQuery is converted to JavaScript. I also make sure the form is validated with Javascript prior to processing the payment intent.

HOPES AND DREAMS:

I have used some substantial chunks of code from my last project, including the image handling functionality and how Cloudinary is managed within the project. I have also used the JavaScript for the category selector in Hopes and Dreams in order to pair cheese with beers in my views for editing categories, which I felt was much easier than a series of drop-downs and actually easier to implement because the codebase already existed.

THE INTERNET:

I have opened so many tabs during the cours of the last 8 weeks and found a lot of great solutions, however for my basket alert messages I borrowed substantially from geeksforgeeks.org in order to add the fade effect:

 https://www.geeksforgeeks.org/how-to-add-fade-out-effect-using-pure-javascript/


### Acknowledgments

HELP AND ASSISTANCE:

Thank you again to Mitko for your honest and constructive feedback and indeed thoughout this course.  You have made me a better developer. Enormous credit has to go to family, friends and co-workers who have had to put up with me in a highly distracted and stressed out state, waking up in the mornings with database models forming in my head.  In particular my girlfriend Ffion who has been patient and kind and supportive throughout in spite of me deserving much less.  Once again, in spite of my caution at the outset, this project has ended up being a lot more work than I anticipated!

## Technical Information
([back to top](#contents))

Version Control: Git and Github.\
JavaScript validation: JSHint.\
Python validation: CI Python Linter.\
Framework: Django.\
Image Hosting: Cloudinary.\
DBMS: PostgreSQL via Django.\
SMTP Mail Server: gmail.\
Languages: HTML, CSS, JavaScript, Python.\
Development Environment: VS Code on Linux.\
Wireframes: Balsamiq.\
Database Modelling: dbdiagram.io\
Image Creation: Bing Image Creator & Inkscape.\
Image Editing: GIMP.\
Screen Capture: Kazam.

([back to top](#contents))