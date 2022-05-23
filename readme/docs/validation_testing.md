# Code Validators and Website Analysis

[Click here to go to the Readme file ](https://github.com/ccarabine/junior-dev-talent/blob/main/readme.md#validation-testing)

The website's pages was tested against the following validators:

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                       |0 errors | [Results](../images/testing/html_testing/index.png)
forum - forum.html               |0 errors | [Results](../images/testing/html_testing/forum.png)
profiles- subscription.html      |0 errors | [Results](../images/testing/html_testing/subscription.png)
products- products.html          |0 errors | [Results](../images/testing/html_testing/products.png)
products- product_detail.html    |0 errors | [Results](../images/testing/html_testing/product_detail.png)
checkout- checkout.html          |0 errors | [Results](../images/testing/html_testing/checkout.png)
checkout -checkout_success.html  |0 errors | [Results](../images/testing/html_testing/checkout_success.png)
checkout- basket.html          |0 errors | [Results](../images/testing/html_testing/basket.png)


<br>

## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

all css files
Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
basestatic/css/style.css | Passed, No errors found | [Results](../images/testing/css_testing/main_css.png) 
checkoutstatic/css/style.css | Passed, No errors found | [Results](../images/testing/css_testing/checkout_css.png)
forumstatic/css/style.css | Passed, No errors found | [Results](../images/testing/css_testing/forum_css.png) 
profilestatic/css/style.css | Passed, No errors found | [Results](../images/testing/css_testing/profile_css.png) 
<br>

## Wave Accessibility
- Wave accessibility(https://wave.webaim.org/) was used to test the websites accessibility

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                       |0 errors | [Results](../images/testing/wave_testing/index.png)
forum - forum.html               |0 errors | [Results](../images/testing/wave_testing/forum.png)
products- product.html          |0 errors | [Results](../images/testing/wave_testing/product.png)
products- product_detail.html    |0 errors | [Results](../images/testing/wave_testing/product_detail.png)
checkout- checkout.html          |0 errors | [Results](../images/testing/wave_testing/checkout.png)
checkout -checkout_success.html  |0 errors | [Results](../images/testing/wave_testing/checkout_success.png)
checkout- basket.html          |0 errors | [Results](../images/testing/wave_testing/basket.png)



___

## JSHint
- JSHint(https://jshint.com/) was used to analyse the Javascript files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
1.base.html | 0 errors and 2 warning | [Results](../images/testing/jshint_testing/base.png)
2.basket/basket.html | 0 errors and 0 warning | [Results](../images/testing/jshint_testing/basket_basket.png)
3.checkout/js/stripe_elementsjs.js 1/2| 0 errors and 0 warning | [Results](../images/testing/jshint_testing/checkout_stripe_elementsjs_1.png)
4.checkout/js/stripe_elementsjs.js 2/2| 0 errors and 0 warning | [Results](../images/testing/jshint_testing/checkout_stripe_elementsjs_2.png)
5.product/add_product | 0 errors and 0 warning | [Results](../images/testing/jshint_testing/product_add_product.png)
6.product_update_product.html | 0 errors and 0 warning | [Results](../images/testing/jshint_testing/product_update_product.png)
7.products/includes/quantity_input_script.html | 0 errors and 0 warning | [Results](../images/testing/jshint_testing/products_includes_quantity_input_script.png)
8.products/products.html | 0 errors and 0 warning | [Results](../images/testing/jshint_testing/products_products.png)
9.products/products.html | 0 errors and 0 warning | [Results](../images/testing/jshint_testing/profiles_countryfield_js.png)

1. Three underfined variables - fnames, ftypes,jQuery. Two warnings The array notation[] is preferable

<br>


## PEP8online
- PEP8online was used to analyse the Python files (https://pep8online.com/)

Page | Errors|Results
------------ | -------------  | ------------- 
Forum
forum/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/for_admin.png)
forum/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_apps.png)
forum/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_forms.png)
forum/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_models.png)
forum/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_urls.png)
forum/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_views.png)
forum/widgets.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_widgets.png)
forum/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_test_models.png)
forum/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/for_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
products/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/pdt_admin.png)
products/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_apps.png)
products/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_forms.png)
products/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_models.png)
products/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_urls.png)
products/widgets.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_widgets.png)
products/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_test_models.png)
products/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/pdt_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
basket/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_apps.png)
basket/contexts.py | No errors/warnings| [Results](../images/testing/pep8_testing/bkt_contexts.png)
basket/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_urls.png)
basket/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_views.png)
basket/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/bkt_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
checkout/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/ch_admin.png)
checkout/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_apps.png)
checkout/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_forms.png)
checkout/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_models.png)
checkout/signals.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_signals.png)
checkout/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_urls.png)
checkout/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_views.png)
checkout/webhook_handler.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_webhook_handler.png)
checkout/webhooks.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_webhooks.png)
checkout/test_forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_test_forms.png)
checkout/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_test_models.png)
checkout/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/ch_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
home/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_apps.png)
home/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_urls.png)
home/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_views.png)
home/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/hom_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
profiles/admin.py | No errors/warnings| [Results](../images/testing/pep8_testing/pr_admin.png)
profiles/apps.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_apps.png)
profiles/forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_forms.png)
profiles/models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_models.png)
profiles/signals.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_signals.png)
profiles/urls.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_urls.png)
profiles/views.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_views.png)
profiles/widgets.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_widgets.png)
profiles/test_forms.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_test_forms.png)
profiles/test_models.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_test_models.png)
profiles/test_views.py | No errors/warnings | [Results](../images/testing/pep8_testing/pr_test_views.png)

Page | Errors|Results
------------ | -------------  | ------------- 
custom_storages.py | No errors/warnings| [Results](../images/testing/pep8_testing/custom_storages.png)
util.py | No errors/warnings| [Results](../images/testing/pep8_testing/util.png)
settings.py | No errors/warnings| [Results](../images/testing/pep8_testing/settings.png)
project_urls.py | No errors/warnings| [Results](../images/testing/pep8_testing/project_url.png)


___

## a11y Color Contrast Accessibility Validator

- Color accessibility(https://color.a11y.com/) was used to test the websites accessibility

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
index.html                       |0 automated color contrast issues | [Results](../images/testing/a11y/index.png)
forum - forum.html               |0 automated color contrast issues | [Results](../images/testing/a11y/forum.png)
profiles- subscription.html      |0 automated color contrast issues| [Results](../images/testing/a11y/subscription.png)
products- products.html          |0 automated color contrast issues | [Results](../images/testing/a11y/products.png)
products- product_detail.html    |0 automated color contrast issues | [Results](../images/testing/a11y/product_detail.png)
checkout- checkout.html          |0 automated color contrast issues | [Results](../images/testing/a11y/checkout.png)
checkout -checkout_success.html  |0 automated color contrast issues | [Results](../images/testing/a11y/checkout_success.png)
checkout- basket.html          |0 automated color contrast issues | [Results](../images/testing/a11y/basket.png)
