z## Known issues during development </a>

[Click here to go to the Readme file ](https://github.com/ccarabine/junior-dev-talent/blob/main/readme.md#known-issues)

### During development, the following issues were identified by user feedback and corrected
# EXAMPLE
 - **Issue 1:** 
 
    *In production, summernote wysiwyg not displaying icons*

-	**Corrective Action:** 
    *Add header link and js and uploaded fonts to css*
    
    https://stackoverflow.com/questions/36034892/icons-not-showing-with-summernote-rails
    
    *Added configuration to cors in s3 bucket"*

<details>
<summary>Click here to view image </summary>

![screenshot of issue1](docs/images/testing/development/issue_1.png)
</details>

___



---

## Known issues during testing <a name="known-issues"></a>

### HTML vaildation issues 

#### **Forum**

<details>
<summary>Click here to view image </summary>

![screenshot of forum issues](../images/testing/html_testing/issues/forum_issues.png)
</details>

- **Issue 1,2,3 :** 

    *An img element must have an alt attribute*


- **Corrective Action:** 

    Add alt attribute alt="{{topic.name}} image">

#### **Subscription**

<details>
<summary>Click here to view image </summary>

![screenshot of subscription issues](../images/testing/html_testing/issues/subscription_issues.png)
</details>

- **Issue 1 :** 

    *Bad value button for attribute type on element*


- **Corrective Action:** 

    Remove type

#### **Product**

<details>
<summary>Click here to view image </summary>

![screenshot of product issues](../images/testing/html_testing/issues/product_issues.png)
</details>

- **Issue 1 & 2:** 

    *The type attribute is unnecessary for JavaScript resources.*


- **Corrective Action:** 

    Remove type

#### **Product detail**

<details>
<summary>Click here to view image </summary>

![screenshot of product detail issues](../images/testing/html_testing/issues/product_detail_issues.png)

</details>

- **Issue 1:** 

    *No p element in scope but a p end tag seen*


- **Corrective Action:** 

    Remove close p tag


- **Issue 2:** 

    *The type attribute is unnecessary for JavaScript resources.*


- **Corrective Action:** 

    Remove type

#### **Basket**

<details>
<summary>Click here to view image </summary>

![screenshot of product issues](../images/testing/html_testing/issues/basket_issues.png)
</details>

- **Issue 1 & 2:** 

    *The type attribute is unnecessary for JavaScript resources.*


- **Corrective Action:** 

    Remove type

___


## Wave accessibility vaildation issues 

#### **Index**

<details>
<summary>Click here to view image </summary>

![screenshot of CSS issues](../images/testing/wave_testing/issues/index_issues.png)

</details>

- **Issue 1 & 2:** 

    Missing form labels
    

- **Corrective Action:** 

    Add aria label


#### **Product**

<details>
<summary>Click here to view image </summary>

![screenshot of product issues](../images/testing/wave_testing/issues/product_issues.png)

</details>

- **Issue 1 & 2:** 

    low contract errors on pagination numbers
    

- **Corrective Action:** 

    Change to text black

#### **Product detail**

<details>
<summary>Click here to view image </summary>

![screenshot of product detail issues](../images/testing/wave_testing/issues/product_detail_issues.png)

</details>

- **Issue 1:** 

    1. 1x mising form label
    2. 2 x empty button
    

- **Corrective Action:** 

   1. Add aria label
   2. Add aria labels

___
   
## PEP8 validation issues 
#### **apps.py**

<details>
<summary>Click here to view image </summary>

![screenshot of apps.py issues](../images/testing/pep8_testing/issues/apps.png)

</details>

- **Issue 1 :** 

    expect 2 lines
    

- **Corrective Action:** 

   Added a line

___



## Lighthouse validation issues 
#### **Accessibility home page mobile**

<details>
<summary>Click here to view image </summary>

![screenshot of accessibility_mobile_1 issues](docs/images/testing/lighthouse_testing/issues/accessibility_mobile_home_1.png)

</details>

- **Issue 1 :** 
    Aria attributes do not match their roles
    
- **Corrective Action:** 
    Added aria label to mobile-search

___

#### **SCO -home page mobile**

<details>
<summary>Click here to view image </summary>

![screenshot of seo_mobile_1 issues](docs/images/testing/lighthouse_testing/issues/seo_mobile_home_1.png)

</details>

- **Issue 1 :** 
    interactive elements - privacy policy link does not have enough space around them
    

- **Corrective Action:** 
    Added margin bottom to the links

___


___

## Known issues during user story testing

- **Issue 1 :** 

    Mobile - on home page
    On the account dropdown, "change password" doesn't show on drop down menu

<details>
<summary>Click here to view image </summary>

![screenshot of issue](docs/images/testing/features/issues/test_1_4.png)

</details>

<br>

- **Corrective Action:** 

    Added code to mobile-top-header
___
