## User story testing
[Click here to go to the Readme file ](https://github.com/ccarabine/junior-dev-talent/blob/main/readme.md#user-stories-testing)

**All tests have been tested on google chrome inspect tools with small, medium and large devices**

## Testing of Feature 1 - Navigation 
User stories

1.1 As a site user I can intuitively navigate the site so that the layout of the site is consistent
1.2 As a site user I can click on the navigation bar so that I can select pages to view
1.3 As a site user I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook

## Testing of Feature 2 - Footer 
1.4 As a site user I can subscribe to get the newsletter, so that I can keep up to date with the company
1.5 As a site user I can view the sites privacy policy, so that i can read more about the sites policy
1.6 As a site user I can view the sites Terms of use policy, so that i can read more about the terms of use

## Testing of Feature 3 - Home page

2.1 As a site user I can view the home page so that I can learn more about the website and its purpose
2.2 As a site user I can click on get hired so that I can learn more about the site and update my profile
2.2 As a site user I can click on forum card so that I can learn more about the service chosen and goto the forum
2.3 As a site user I can click on Growth hub so that I can learn more about the service chosen and go to the shop
2.4 As a site user I can click on the talent center so that I can learn more about the service chosen and register

## Testing of Feature 4 - forum topics
4.1 As a site user I can view the room topics so I can select a room of interest
9.1. As a site admin I can create a room topic so that I can manage the site content
9.2. As a site admin I can update a room topic so that I can manage the site content
9.3. As a site admin I can delete a room topic so that I can manage the site content

## Testing of Feature 5 - forum posts
4.2 As a logged-in site user I can view a list of posts by room so that I can select a post that interests me and view user comments
4.3 As a logged-in site user I can view a paginated list of posts so that my screen doesn't get overpopulated with posts
4.4 As a logged-in site user I can click on a post so that I can read the full article and related comments
4.5 As a logged-in site user I can create a new post so that I can post content on the site for other users to view
4.6 As a logged in site user (owner of post) I can edit a post (subject header /text body) so that I can change the content if required
4.7 As a logged-in site user (owner of post) I can delete a post that I have posted so that I can take content off the website
9.5. As a site admin I can Manage posts in the django admin area so that I can manage the site content
10.2. As a site admin i want non-logged users not to have access to forum( only access to logged in users)

## Testing of Feature 6 - forum comments
4.8 As a logged-in site user I can leave comments on a post so that I can take an active role in the forum (be involved in the conversation/express my opinion)
4.9 As a logged in site user(owner of comment) I can edit a comment so that I can change the content if required
4.10 As a logged-in site user(owner of comment) I can delete a comment that I have posted so that I can take content off the website
4.11 As a logged-in site User(owner of comment), I can view a paginated list of comments so that my screen doesn't get overpopulated with comments
4.12. As a site user who is directed to a non-existent page or resource, I can redirected to the relevant error page
9.6. As a site admin I can Manage comments in the django admin area so that I can manage the site content 

## Testing of Feature 7 - talent center
8.1. As a site user, I can register so that i can access the talent center to view candidate profiles
8.2. As a employer site user I can click on talent center so I can view profiles that interest me
8.3. As a employer site user I can search profiles by skill so I can view junior developers
8.4. As a employer site user I can view candidates by date joined so that i can quickly junior developers by new and old
8.5. As a employer site user I can view candidates linkedin /github so that see more information about them
8.6. As a employer site user I can download a developers CV so that read their experience
8.7. As a employer site user I can Contact a developer directly so that i can contact them about a job

## Testing of Feature 8 - Ecommerce Store
5.1. As a site user I can click on categories to view so that i can view products by courses, mentor programmes and events
5.2. As a site user I can click on a product so I can view learn more about the product
5.3. As a site user I can add the product to my basket so that i can make a purchase
5.4. As a site user I can search products by name so I can view products that interest me
5.5. As a site user I can paginate search products so I can view a paginated list of products so they don’t over populate the page
5.6. As a site user I can sort the products list by category, alphabetically so that i can quickly find the product I seek
5.7. As a site user who is directed to a non-existent page or resource, I can redirected to the relevant error page
9.7. As a site admin I can create a product so that I can manage the site content
9.8. As a site admin I can update a product so that I can manage the site content
9.9. As a site admin I can delete a product so that I can manage the site content

## Testing of Feature 9 - Ecommerce Store - Basket
6.1. As a site user I can always see the total price of my basket in the navigation bar, so that I know what the total cost will be when on the products page
6.2. As a site user i can adjust the quantity of the product chosen after adding it to the shopping basket
6.3. As a site user I can view the products added to my basket by clicking the basket icon or by adding an item to the basket
6.4. As a site user I can click on Proceed to Checkout, so that I can purchase the items in my basket
6.5. As a site user who is directed to a non-existent page or resource, I can redirected to the relevant error page

## Testing of Feature 10 - Ecommerce Store - checkout
7.1. As a site user i can review my basket before i pay , so that i can change my mind or proceed with order
7.2. As a logged in site user i can complete my billing details so my records are correct
7.3. As a logged-in site user i can update and save my billing details so for future purchases they are completed
7.4. As a logged-in site user i can enter my card details on the checkout page, so that I can make the desired purchase
7.5. As a logged-in site user I am informed of whether my purchase was successful or not via the Order Successful page, as well as via an email sent upon order confirmation
7.6. As a site user who is directed to a non-existent page or resource, I can redirected to the relevant error page

## Testing of Feature 11 - My profile

3.8: As a logged-in site user I can view my profile and see clearly what fields i haven't completed so i have a greater chance for hiring managers to view all my information about myself
3.9. As a logged-in site user I can update my profile so that i can change information about myself
3.10. As a logged-in site user I can delete my account so that my account is deleted and no longer have access to the functionality

3.14: As a logged-in site user I can view my Default billing information: Full name, Street Address 1, Street Address 2, Town or City, County, Postal Code, Country, phone number and email address
3.15: As a logged-in site user I can view my order history(Order Number, Date, Items and Order Total)
3.16: As a logged-in site user I can click on an order number to view the order information

3.19. As a site user who is directed to a non-existent page or resource, I can redirected to the relevant error page

9.10. As a site admin I can Manage Profiles in the django admin area so that I can manage the site content
10.3. As a site admin i want users only access their profile with products brought
## Testing of Feature 12 - Candidate skills
3.11. As a logged-in site user I can add a skill so that i can add a skill to my profile
3.12. As a logged-in site user I can update a skill so that i can update the name of the skill on my profile
3.13. As a logged-in site user I can delete a skill so that i can delete the name of the skill on my profile
9.11. As a site admin I can Manage skills in the django admin area so that I can manage the site content
## Testing of Feature 13 - Account management
3.1. As a site user I can sign up so that I have a role-based login and community functionality
3.2 As a site user I can receive a welcome email so that I know that I have signed up correctly and feel like a valued user
3.3 As a site user I can login with my username and password so that I can access the sites full functionality
3.4 As a logged in site user I can change my password so that I can stay secure
3.5 As a site user I can reset my password so that I can stay secure
3.6 As a logged-in site user I can log out of my account so that other users cannot access my account
3.7 As a site user I can see the current logged-in state so that I know if I can access logged in functionality

## Testing of Feature 14 - Privacy policy
## Testing of Feature 15 - Terms of use
## Testing of Feature 16 - Sign up to newsletter
## Testing of Feature 17 - Error handling

10.1. As a site user who is directed to a non-existent page or resource, I can redirected to the relevant error page




**Action** 
1.	Navigate to https://coronavirusforum.herokuapp.com/
2.	Navigate and click on menu icon
3.	Navigate and click on the account icon
4.	Navigate and click on account icon, sign in, enter credentials
5.	Navigate and click on the account icon
6.	Navigate and click on Search icon

This action was tested on a logged in user, not logged user and admin

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|**Small screen devices**|[Small](docs/images/testing/features/test1_1.png)|Passed|
||Navigation bar is displayed at the top of the page|see "small" link|Passed|
||**On the Left**|
||Menu icon is displayed|see "small" link|Passed|
|2|Navigation links are displayed “Home”, “Topics”, “Latest Statistics” ,“About Us”|[Dropdown menu](docs/images/testing/features/test1_2.png)|Passed|
||**Center**|||
||**Not logged in user**|||
||Account icon is displayed|see small link above|Passed|
|| “Sign in” link is displayed|see small link above|Passed|
|3.| “Sign up” or “Sign in” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_3.png)|Passed|
||**Logged in user**|||
||Account icon is displayed|see small link above|Passed|
|4.|“Welcome (username)” e.g. “Welcome Admin” displayed under icon|see small link above|Passed|
|5.|“Change password” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_4.png)|Passed|
|| “Logout” is displayed in the drop down menu|see dropdown menu link above|Passed|
||**Right**|||
||Search icon is displayed|see small link above|Passed|
|6. |Search bar and submit button is displayed under the navigation menu|[Search bar](docs/images/testing/features/test1_5.png)|Passed|

<br>

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|**Medium and large screen devices**|[Medium ](docs/images/testing/features/test1_6.png)[large](docs/images/testing/features/test1_7.png)|Passed|
||**On the Left**||
||A coronavirus icon is displayed|see medium/large links above|Passed|
||**Center**||
||Search bar and submit button is displayed|see medium/large links above|Passed|
||Navigation links are displayed -“Home”, “Topics”, “Latest Statistics” ,“About Us”|see medium/large links above|Passed|
||**Right**||
||**Not logged in user**|||
||Account icon is displayed|see medium/large links above|Passed|
||Under icon, “Sign in” is displayed
|3.| “Sign up” or “Sign in” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_8.png)|Passed|
||**Logged in user**|||
||Account icon|see medium/large links above|Passed|
|4.|Under icon  - “Welcome (username)” e.g. “Welcome Admin”|[Dropdown menu](docs/images/testing/features/test1_8a.png)|Passed|
|5.|“Change password” is displayed in the drop down menu|[Dropdown menu](docs/images/testing/features/test1_9.png)|Passed|
|| “Logout” is displayed in the drop down menu |see dropdown menu link above|Passed|

___
