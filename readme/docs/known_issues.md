## Known issues during development </a>

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

#### **Postlist**

<details>
<summary>Click here to view image </summary>

![screenshot of image21](docs/images/testing/html_testing/issues/postlist_issues.png)

</details>

- **Issue 1 :** 

    *Misuse of aria label*


- **Corrective Action:** 

    Removed aria-label



___

## CSS vaildation issues 

<details>
<summary>Click here to view image </summary>

![screenshot of CSS issues](docs/images/testing/css_testing/issues/css_issues.png)

</details>

- **Issue 1 :** 

    *Value Error : background-color Parse Error var(-color-rich-black-fogra-29)*


- **Corrective Action:** 

    Remove background-color: var(-color-rich-black-fogra-29);



## Wave accessibility vaildation issues 

#### **Post form**

<details>
<summary>Click here to view image </summary>

![screenshot of CSS issues](docs/images/testing/wave_testing/issues/postform.png)

</details>

- **Issue 1 :** 

    missing or uninformative page
    language missing or invalid
    

- **Corrective Action:** 

    They are included in the base.html
    `<html lang="en">`
    `<title>Corona Virus Forum</title>`
    
    The error may occur from not being signed in

___

___
   
## PEP8 validation issues 
#### **apps.py**

<details>
<summary>Click here to view image </summary>

![screenshot of apps.py issues](docs/images/testing/pep8_testing/issues/apps.png)

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
