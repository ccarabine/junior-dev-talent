## User story testing
[Click here to go to the Readme file ](https://github.com/ccarabine/junior-dev-talent/blob/main/readme.md#user-stories-testing)

**All tests have been tested on google chrome inspect tools with small, medium and large devices**

## Testing of Feature 1 - Navigation 
User stories

- 1.1 As a site user I can intuitively navigate the site so that the layout of the site is consistent
- 1.2 As a site user I can click on the navigation bar so that I can select pages to view

___

**Action** 
1.	Navigate to https://junior-dev-talent.herokuapp.com/
2.	Navigate and click on menu icon (on SM/MD devices only)
3.	Navigate and click on Search icon (on SM/MD devices only)
4.	Navigate and click on the account icon
5.	Navigate and click on the basket
6.	Navigate and click on the Junior Dev Talent icon (on large devices only)
7.  Navigate and click on Forum
8.  Navigate and click on Growth Hub
9.  Navigate and click on Talent center


This action was tested on a logged in user, not logged user and admin
</br>

## Small/Medium screen devices

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Navigation bar is displayed at the top of the page|[SM/MD](../images/testing/user_story/test1_1.png)|Passed|
||**From left to right**|
||Menu icon is displayed|see "SM/MD" link above|Passed|
||Search icon with "Search" beneath is displayed|see "SM/MD" link above|Passed|
||Profile icon with "Account"/name beneath is displayed|see "SM/MD" link above|Passed|
||Shopping Basket icon with amount in GBP beneath is displayed|see "SM/MD" link above|Passed|
|2|Dropdown menu displayed with the following links“Home”, “Forum”, “Growth Hub” ,“Talent Center” |[SM/MD](../images/testing/user_story/test1_2.png)|Passed|
|3|Search bar displayed "Search our growth hub store is the placeholder within the search bar" |[SM/MD](../images/testing/user_story/test1_3.png)|Passed|
|4|Dropdown menu displayed with the following links"Register", "Login" |[SM/MD](../images/testing/user_story/test1_4.png)|Passed|
|5|Redirected to basket template |[SM/MD](../images/testing/user_story/test1_5.png)|Passed|
|7|Redirected to forum template, navigation is consistent |[SM/MD](../images/testing/user_story/test1_7.png)|Passed|
|8|Redirected to growth hub template, navigation is consistent |[SM/MD](../images/testing/user_story/test1_8.png)|Passed|
|9|Redirected to Talent center template, navigation is consistent |[SM/MD](../images/testing/user_story/test1_9.png)|Passed|

</br>

## Large screen devices
Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Navigation bar is displayed at the top of the page|[LG](../images/testing/user_story/test1_1_1.png)|Passed|
||**From left to right**|
||Junior Dev Talent icon is displayed with "Junior Dev Talent" beneath|see "LG" link above|Passed|
||Search bar with "Search our growth hub store" is the placeholder within the search bar|see "LG" link above|Passed|
||Profile icon with "Account"/name beneath is displayed|see "SM/MD" link above|Passed|
||Shopping Basket icon with amount in GBP beneath is displayed|see "SM/MD" link above|Passed|
|4|Dropdown menu displayed with the following links"Register", "Login" |[LG](../images/testing/user_story/test_1_4_1.png)|Passed|
|5|Redirected to basket template |[LG](../images/testing/user_story/test1_5_1.png)|Passed|
|6|Redirected to home template |[LG](../images/testing/user_story/test1_6.png)|Passed|
|7|Redirected to forum template, navigation is consistent |[LG](../images/testing/user_story/test1_7_1.png)|Passed|
|8|Redirected to growth hub template, navigation is consistent |[LG](../images/testing/user_story/test1_8_1.png)|Passed|
|9|Redirected to Talent center template, navigation is consistent |[LG](../images/testing/user_story/test1_9_1.png)|Passed|

___


## Testing of Feature 2 - Footer 
- 1.3 As a site user I can see a link in the footer to the site’s Facebook Business Page, so that I can follow the company on Facebook
- 1.4 As a site user I can subscribe to get the newsletter, so that I can keep up to date with the company
- 1.5 As a site user I can view the sites privacy policy, so that i can read more about the sites policy
- 1.6 As a site user I can view the sites Terms of use policy, so that i can read more about the terms of use

___

**Action** 
1.	Navigate to footer
2.	Navigate to subscribe to our newsletter, enter email address and click join
3.	Navigate and click on Follow us on facebook
4.	Navigate and click on Privacy policy
5.	Navigate and click on Terms of use


This action was tested on a logged in user, not logged user and admin

## Small/Medium/Large screen devices

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Navigation bar is displayed at the top of the page|[SM/MD/LG](../images/testing/user_story/test2_1.png)|Passed|
||**From top to bottom**|
||There are two colums with |see "SM/MD" link above|Passed|
||1. Newsletter icon, subscribe to our newsletter beneath and a input field with placeholder text "Enter your email" followed by a Join button |see "SM/MD/LG" link above|Passed|
||2. Facebook icon, Keep upto date with all our latest offers, a link to the facebook site "follow us on facebook" |see "SM/MD/LG" link above|Passed|
||Privacy Policy and Terms of use links are displayed|see "SM/MD/LG" link above|Passed|
||Copyright information is displayed|see "SM/MD/LG" link above|Passed|
|2|Redirected to subscription confirmation |[SM/MD/LG](../images/testing/user_story/test2_2.png)|Passed|
|3|Redirected to facebook business page |[SM/MD/LG](../images/testing/user_story/test2_3.png)|Passed|
|4|Privacy policy modal is displayed |[SM/MD/LG](../images/testing/user_story/test2_4.png)|Passed|
|5|Terms of use modal is displayed|[SM/MD/LG](../images/testing/user_story/test2_5.png)|Passed|

## X-Small screen devices

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Navigation bar is displayed at the top of the page|[XS](../images/testing/user_story/test2_1.png)|Passed|
||**From top to bottom**|
||1. Newsletter icon, subscribe to our newsletter beneath and a input field with placeholder text "Enter your email" followed by a Join button |see "XS" link above|Passed|
||2. Facebook icon, Keep upto date with all our latest offers, a link to the facebook site "follow us on facebook" |see "XS" link above|Passed|
||Privacy Policy and Terms of use links are displayed|see "XS" link above|Passed|
||Copyright information is displayed|see "XS" link above|Passed|
|2|Redirected to subscription confirmation |[XS](../images/testing/user_story/test2_2.png)|Passed|
|3|Redirected to facebook business page |[XS](../images/testing/user_story/test2_3.png)|Passed|
|4|Privacy policy modal is displayed |[XS](../images/testing/user_story/test2_4_1.png)|Passed|
|5|Terms of use modal is displayed|[XS](../images/testing/user_story/test2_5_1.png)|Passed|


## Testing of Feature 3 - Home page

2.1 As a site user I can view the home page so that I can learn more about the website and its purpose
2.2 As a site user I can click on get hired so that I can learn more about the site and update my profile
2.2 As a site user I can click on forum card so that I can learn more about the service chosen and goto the forum
2.3 As a site user I can click on Growth hub so that I can learn more about the service chosen and go to the shop
2.4 As a site user I can click on the talent center so that I can learn more about the service chosen and register

___

**Action** 
1.	Navigate to Home page
2.	Navigate to click on get hired card </br>
2.1 Click start now
3. Navigate and click forum card </br>
3.1 Click chat now
4.	Navigate and click on growth hub card </br>
4.1 Click shop now
5.	Navigate and click on talent center card </br>
5.1 Click start now

This action was tested on a logged in user, not logged user and admin

## Small screen devices

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Hero image with a junior developer working at their computer|[SM](../images/testing/user_story/test3_1.png)|Passed|
||4 cards stacked in one column explaining each of the services of the site|||
||Get hired, Forum, Growth Hub and Talent Center|||
||Hero image with a hiring manager shaking the hand of a candidate through a laptop|||
|2|Get hired modal displayed with a title, 3 cards stacked in one column and a call to action button "Start now"|[SM](../images/testing/user_story/test3_2_1.png)|Passed|
|2.1|Logged in users - Update profile template is displayed|[SM](../images/testing/user_story/test3_2_2.png)|Passed|
||Non-Logged in users - Sign-in template is displayed|[SM](../images/testing/user_story/test3_2_3.png)|Passed|
|3|Forum modal displayed with a title, 4 cards stacked in one column and a call to action button "Chat now"|[SM](../images/testing/user_story/test3_3.png)|Passed|
|3.1|Redirect to forum|[SM](../images/testing/user_story/test3_3_1.png)|Passed|
|4|Growth hub modal displayed with a title, 4 cards stacked in one column and a call to action button "Shop now"|[SM](../images/testing/user_story/test3_4.png)|Passed|
|4.1|Redirect to Growth hub|[SM](../images/testing/user_story/test3_4_1.png)|Passed|
|5|Talent modal displayed with a title, 3 cards stacked in one column and a call to action button "Start now"|[SM](../images/testing/user_story/test3_5.png)|Passed|
|5.1|Non-Logged in user - Redirect to talent center benefits page(subscription)|[SM](../images/testing/user_story/test3_5_1_1.png)|Passed|
||Logged in user and is_ hiring_manager is false -Redirect to talent center benefits page(subscription)|[SM](../images/testing/user_story/test3_5_1_2.png)|Passed|
||Logged in user and is_ hiring_manager is true - talent center template displayed|[SM](../images/testing/user_story/test3_5_1_3.png)|Passed|

## Medium screen devices
Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Hero image with a junior developer working at their computer|[MD](../images/testing/user_story/test3_1a.png)|Passed|
||4 cards stacked in two column and two rows explaining each of the services of the site|||
||Get hired, Forum, Growth Hub and Talent Center|||
||Hero image with a hiring manager shaking the hand of a candidate through a laptop|||
|2|Get hired modal displayed with a title, 3 cards stacked in one row and a call to action button "Start now"|[MD](../images/testing/user_story/test3_2_1a.png)|Passed|
|2.1|Logged in users - Update profile template is displayed|[MD](../images/testing/user_story/test3_2_2a.png)|Passed|
||Non-Logged in users - Sign-in template is displayed|[MD](../images/testing/user_story/test3_2_3a.png)|Passed|
|3|Forum modal displayed with a title, 4 cards stacked in two columns and two rows and a call to action button "Chat now"|[MD](../images/testing/user_story/test3_3a.png)|Passed|
|3.1|Redirect to forum|[MD](../images/testing/user_story/test3_3_1a.png)|Passed|
|4|Growth hub modal displayed with a title, 4 cards stacked in two columns and two rows and a call to action button "Shop now"|[MD](../images/testing/user_story/test3_4a.png)|Passed|
|4.1|Redirect to Growth hub|[MD](../images/testing/user_story/test3_4_1a.png)|Passed|
|5|Talent modal displayed with a title, 3 cards stacked in one row and a call to action button "Start now"|[MD](../images/testing/user_story/test3_5a.png)|Passed|
|5.1|Non-Logged in user - Redirect to talent center benefits page(subscription)|[SM](../images/testing/user_story/test3_5_1_1a.png)|Passed|
||Logged in user and is_ hiring_manager is false -Redirect to talent center benefits page(subscription)|[SM](../images/testing/user_story/test3_5_1_2a.png)|Passed|
||Logged in user and is_ hiring_manager is true - talent center template displayed|[SM](../images/testing/user_story/test3_5_1_3a.png)|Passed|

## Large  screen devices
Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Hero image with a junior developer working at their computer|[LG](../images/testing/user_story/test3_1b.png)|Passed|
||4 cards stacked in one rows explaining each of the services of the site|||
||Get hired, Forum, Growth Hub and Talent Center|||
||Hero image with a hiring manager shaking the hand of a candidate through a laptop|||
|2|Get hired modal displayed with a title, 3 cards stacked in one row and a call to action button "Start now"|[LG](../images/testing/user_story/test3_2_1b.png)|Passed|
|2.1|Logged in users - Update profile template is displayed|[LG](../images/testing/user_story/test3_2_2b.png)|Passed|
||Non-Logged in users - Sign-in template is displayed|[LG](../images/testing/user_story/test3_2_3b.png)|Passed|
|3|Forum modal displayed with a title, 4 cards stacked in one row and a call to action button "Chat now"|[LG](../images/testing/user_story/test3_3b.png)|Passed|
|3.1|Redirect to forum|[LG](../images/testing/user_story/test3_3_1b.png)|Passed|
|4|Growth hub modal displayed with a title, 4 cards stacked in one row and a call to action button "Shop now"|[LG](../images/testing/user_story/test3_4b.png)|Passed|
|4.1|Redirect to Growth hub|[LG](../images/testing/user_story/test3_4_1b.png)|Passed|
|5|Talent modal displayed with a title, 3 cards stacked in one row and a call to action button "Start now"|[LG](../images/testing/user_story/test3_5b.png)|Passed|
|5.1|Non-Logged in user - Redirect to talent center benefits page(subscription)|[LG](../images/testing/user_story/test3_5_1_1b.png)|Passed|
||Logged in user and is_ hiring_manager is false -Redirect to talent center benefits page(subscription)|[LG](../images/testing/user_story/test3_5_1_2b.png)|Passed|
||Logged in user and is_ hiring_manager is true - talent center template displayed|[LG](../images/testing/user_story/test3_5_1_3b.png)|Passed|

## Testing of Feature 4 - Forum topics
- 4.1 As a site user I can view the room topics so I can select a room of interest
- 9.1. As a site admin I can create a room topic so that I can manage the site content
- 9.2. As a site admin I can update a room topic so that I can manage the site content
- 9.3. As a site admin I can delete a room topic so that I can manage the site content

___

**Action** 
1.	Navigate to forum ( not logged in user) </br>
1.1 Log in as a normal user </br>
2. Log in as superuser, navigate to the forum</br>
2.1 Click on Create Topic</br>
2.1.1 Click on back</br>
2.1.2 Click submit</br>
2.1.3 Enter name and click submit</br>
2.1.4 Select image and click submit</br>
3. Log in as superuser, navigate to the forum</br>
3.1 Click on update Topic</br>
3.1.1 Click on back</br>
3.1.2 Click submit</br>
3.1.3 Click on update , change name to Coding challenges, select image and change, click submit </br>
3.1.4 Click on update , select remove,click submit </br>
3.1.5 Click on update , select image, and change to a word document,click submit </br>
4. Log in as superuser, navigate to the forum</br>
4.1 Click on delete</br>
4.1.1 Click on back</br>
4.1.2 Click confirm</br>

This action was tested on a logged in user, not logged user and admin


Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1 & 1.1|Display Forum title and a description followed by a sub heading room topics|||
||Room topics are displayed using cards stacked in one column|[SM](../images/testing/user_story/test4_1.png)|Passed|
||Room topics are displayed using cards stacked two columns|[MD/LG](../images/testing/user_story/test4_1.png)|Passed|
||Room icon and the name of the topic is displayed in each card|see above links|Passed|
|||||
|2|Logged in as superuser|[SM/MD/LG](../images/testing/user_story/test4_1_2.png)|Passed|
||+Add topic links will be displayed under the Room topic section divider to allow admin users to add a topic|see above links|Passed|
||Edit and delete link will be displayed in each card about room discussion to allow admin users to edit/delete a topic|see above links|Passed|
|2.1|Create topic template displayed|[SM/MD/LG](../images/testing/user_story/test4_2_1.png)|Passed|
|2.1.1|Redirect to forum displaying the topics|[SM/MD/LG](../images/testing/user_story/test4_2_1_1.png)|Passed|
|2.1.2|Validation error message" Please fill this field - referring to topic name |[SM/MD/LG](../images/testing/user_story/test4_2_1_2.png)|Passed|
|2.1.3|Validation error message" Please fill this field - referring to image |[SM/MD/LG](../images/testing/user_story/test4_2_1_3.png)|Passed|
|2.1.4|Redirect to forum displaying the topics |[SM/MD/LG](../images/testing/user_story/test4_2_1_4.png)|Passed|
||Success message displayed “Topic was added successfully” |[SM/MD/LG](../images/testing/user_story/test4_2_1_4a.png)|Passed|
|||||
|3.1|Update topic template displayed with the details displayed|[SM/MD/LG](../images/testing/user_story/test4_3_1.png)|Passed|
|3.1.1|Redirect to forum displaying the topics|[SM/MD/LG](../images/testing/user_story/test4_3_1_1.png)|Passed|
|3.1.2|Success message displayed “Topic was updated successfully” |[SM/MD/LG](../images/testing/user_story/test4_3_1_2.png)|Passed|
|3.1.3|Success message displayed “Topic was updated successfully” |[SM/MD/LG](../images/testing/user_story/test4_3_1_3.png)|Passed|
|3.1.4|No image displayed |[SM/MD/LG](../images/testing/user_story/test4_3_1_4.png)|Passed|
|3.1.5|No image uploaded |[SM/MD/LG](../images/testing/user_story/test4_3_1_5.png)|Passed|
|||||
|4|Delete topic template displayed with the details displayed|[SM/MD/LG](../images/testing/user_story/test4_4.png)|Passed|
|4.1|Redirect to forum displaying the topics|[SM/MD/LG](../images/testing/user_story/test4_4_1.png)|Passed|
|4.2|Success message displayed “Topic was deleted successfully” |[SM/MD/LG](../images/testing/user_story/test4_4_2.png)|Passed|



## Testing of Feature 5 - forum posts
- 4.2 As a logged-in site user I can view a list of posts by room so that I can select a post that interests me and view user comments
- 4.3 As a logged-in site user I can view a paginated list of posts so that my screen doesn't get overpopulated with posts
- 4.4 As a logged-in site user I can click on a post so that I can read the full article and related comments
- 4.5 As a logged-in site user I can create a new post so that I can post content on the site for other users to view
- 4.6 As a logged in site user (owner of post) I can edit a post (subject header /text body) so that I can change the content if required
- 4.7 As a logged-in site user (owner of post) I can delete a post that I have posted so that I can take content off the website
- 9.5. As a site admin I can Manage posts in the django admin area so that I can manage the site content
- 10.2. As a site admin i want non-logged users not to have access to forum( only access to logged in users)

___

**Action** 
1.	Log in, navigate to forum, click on a room topic  </br>
2.	Navigate to forum, click on a room topic, click on number 2 on the pagination bar  </br>
3.  Navigate to forum, click on a room topic, Click on a post </br>
3.1.  Click on back to forum link
4.  Navigate to forum, click on a room topic, Click on a -> Start a new post within this topic </br>
4.1. Click on back to forum link</br>
4.2. Click submit</br>
4.3  Type a post name (required field) and click submit post</br>
4.4 Navigate to forum, click on a room topic, Click on a -> Start a new post within this topic , enter a post title, description and upload an image, click submit</br>
5.  Navigate to forum, click on a room topic, Click on a post that was just created</br>
5.1. Click on edit
5.2. Change name, description, and image and click submit
6.  Navigate to forum, click on a room topic, Click on a post that was just created</br>
6.1. Click on delete</br>
6.2. Click on cancel</br>
6.3. Click on delete post</br>
7. Log in to django admin, click on posts and the post title to edit, update a field, click save, navigate to post on the site


This action was tested on a not logged user and logged in user 

Action|Expected result| Actual result| Status|
------------ | ------------ | ------------ |------------ |
|1|Room topic display, Post list displayed with number of comments and the time it was created from today |[SM/MD/LG](../images/testing/user_story/test5_1.png)|Passed|
|2|list of posts displayed on second page |[SM/MD/LG](../images/testing/user_story/test5_2.png)|Passed|
|3|Post displayed displayed with user who created the post , number of comments and the time it was created from today and related comments displayed with who created the comment the time it was created from today  stacked in one column|[SM](../images/testing/user_story/test5-3.png)|Passed|
||Post displayed and related comments  stacked in two column|[MD/LG](../images/testing/user_story/test5_3_1.png)|Passed|
|3.1|redirected to forum |[SM/MD/LG](../images/testing/user_story/test5_3_1_1.png)|Passed|
|4|redirected to add new post template |[SM/MD/LG](../images/testing/user_story/test5_4.png)|Passed|
|4.1|redirected to forum |[SM/MD/LG](../images/testing/user_story/test5_4_1.png)|Passed|
|4.2|Validation error message" Please fill this field - referring to post name |[SM/MD/LG](../images/testing/user_story/test5_4_2.png)|Passed|
|4.3|Success message displayed “Post submitted” |[SM/MD/LG](../images/testing/user_story/test5_4_3.png)|Passed|
|4.4|Success message displayed “Post submitted” |[SM/MD/LG](../images/testing/user_story/test5_4_4.png)|Passed|
||Redirected to post with images and fields displayed |||
|5|Post displayed with Update and delete link under the post |[SM/MD/LG](../images/testing/user_story/test5_4.png)|Passed|
|5.1|Redirected to update post template displayed with fields data |[SM/MD/LG](../images/testing/user_story/test5_4_1.png)|Passed|
|5.2|Success message displayed “Post updated” |[SM/MD/LG](../images/testing/user_story/test5_5_2.png)|Passed|
||Redirected to post template with updated data displayed  |[SM/MD/LG](../images/testing/user_story/test5_5_2a.png)|Passed|
|6|Redirected to delete post template with post name displayed |[SM/MD/LG](../images/testing/user_story/test5_6.png)|Passed|
|6.1|Redirected to update post template displayed with fields data |[SM/MD/LG](../images/testing/user_story/test5_6_1.png)|Passed|
|6.2|Redirected to post |[SM/MD/LG](../images/testing/user_story/test5_6_2.png)|Passed|
|6.3|Success message displayed “Post deleted” |[SM/MD/LG](../images/testing/user_story/test5_6_3.png)|Passed|
||Redirected to forum |[SM/MD/LG](../images/testing/user_story/test5_6_4.png)|Passed|
|7|Fields updated on post |[SM/MD/LG](../images/testing/user_story/test5_7.png)|Passed|





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
