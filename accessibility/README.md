Tasks
0. make the "works" card focus visible
#advanced
Start with this 00-styles.css file:

Click to expand/hide file contents
You can use it with this 00-index.html file:
````

````
As you can see, the contrast is not good. The easy fix is simply to remove the body styles in the embed <style>. Do this in your fix-a11y/01-index.html file. In a real case, you could use the Contrast Ratio section of the Color Picker.

Check with Axe to ensure the issue is fixed.

Rendering the page should display something like this



Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/01-index.html
3. Documents must have <title> element to aid in navigation
#advanced
Taking your code from the previous task, in your fix-a11y/02-index.html file

Add a title: Homepage - A fake website

Check with Axe to ensure the issue is fixed



Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/02-index.html
4. <html> element must have a lang attribute
#advanced
Taking your code from the previous task, in your fix-a11y/03-index.html file

On the html tag, add the attribute lang with the en value.

Check with Axe to ensure the issue is fixed.

Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/03-index.html
5. Images must have alternate text
#advanced
Taking your code from the previous task, in your fix-a11y/04-index.html file

Locate the img that points to the logo.png
Add an alt attribute with the text Name of the logo
Locate the img that points to the hero-img.png
Add an empty alt (decorative image)
Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/04-index.html
6. Form elements must have labels
#advanced
Taking your code from the previous task, in your fix-a11y/05-index.html file, locate the form

Add a label just before the input
Class: visually-hidden
For: email
On the input
Add an id: email
Axe tells use that the issue is solved. But actually, some elements should be fixed for better accessibility and usability.

We can change the type from text to email
Add the attribute autocomplete with the value email
Add the required attribute and the aria-required="true"
Change the a to be a button
We can remove the placeholder as it doesn’t add any value
We don’t have any error handling in our example, that should exist on the front-end / back-end side.

Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/05-index.html
7. Links must have discernible text
#advanced
In your fix-a11y/06-index.html file

Locate thefacebook-icon and add an aria-label on the a with the text Facebook
Locate the twitter-icon and add an aria-label on the a with the text Twitter
Links should never be empty, in our case, we are using a font (like Font Awesome) to generate icons.

Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/06-index.html
8. Zooming and scaling must not be disabled
#advanced
In your fix-a11y/07-index.html file

Locate the meta viewport and remove user-scalable=no

Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/07-index.html
9. Heading levels should only increase by one and all page content must be contained by landmarks
#advanced
You can install the headingsMap extension to have a visual representation of your headings.

Taking your code from the previous task, in your fix-a11y/08-index.html file

Like our Techium project, we are going to create an h1 just after the <div class="header"> closing tag. (The h1 will be sibling to the <div class="header"> div)
Text: Homepage
Change <h6>This is me</h6> to be <h2>This is me</h2>
Change <h1>Philip Gilbert</h1> to be <span>Philip Gilbert</span>
Change <h6>About Me</h6> to be <h2>About Me</h2>
Change <h1>Personal Details</h1> to be <span>Personal Details</span>
Change <h1>My Offered Services</h1> to be <h2>My Offered Services</h2>
Change <h4>Web Design</h4> to be <h3>Web Design</h3>
Change <h4>Web Development</h4> to be <h3>Web Development</h3>
Change <h1 class="counter">2536</h1> to be <span class="counter">2536</span>
Change <h1 class="counter">6784</h1> to be <span class="counter">6784</span>
Change <h1>Client's Feedback About Me</h1> to be <h2>Client's Feedback About Me</h2>
Change <h4>Harriet Maxwell</h4> to be <span>Harriet Maxwell</span>
Change <h1>Choose Your Plan</h1> to be <h2>Choose Your Plan</h2>
Change <h1>01</h1> to be <h3>01</h3>
Change <h1>$199.00</h1> to be <span>$199.00</span>
Change <h4>About Me</h4> to be <span>About Me</span>
Change <h4>Newsletter</h4> to be <span>Newsletter</span>
Change <h4>Follow Me</h4> to be <span>Follow Me</span>
Fixing wrong headings is not an easy task. Headings represent the outline of your content. Like the table of contents in a book, headings should help to understand what is inside your page.

Always ask yourself if that word or sentence would make sense for anybody visiting your website.

Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/08-index.html
10. Document must have one main landmark
#advanced
You can install the Landmarks extension to visually locate the landmarks on your pages.

Taking your code from the previous task, in your fix-a11y/09-index.html file

Locate the header class and convert that <div> into a <header> tag (only change the tag, no need to change or remove other attributes in the tag)
Convert the <div class='nav'> into a <nav> element (only change the tag, no need to change or remove other attributes in the tag)
Wrap everything from the <h1>Homepage</h1> to before the <div class="footer"> in a <main> tag.
Locate the footer class and transform the div to a <footer> (only change the tag, no need to change or remove other attributes in the tag)
Locate all divs with the section class, and update divs to be <section> (only change the tag, no need to change or remove other attributes in the tag). Except the one with the Projects Completed text. Sections should have headings, we don’t have one anymore.
If you open the landmarks extension, you should see the landmarks showing.

Tip

Remember that header, section, footer etc contain a default role (=landmarks).

All automated issues are now solved! You fixed around 50% of accessibility issues. The rest are manual issues, tested using screen-reading tools or just reading the code.

Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/09-index.html
11. More than 2 elements become list
#advanced
Automated tools can’t always alert about elements that should exist as a list.

Taking your code from the previous task, in your fix-a11y/10-index.html file

Locate the nav
Transform the <div> in a <ul> and every <p> in an li
Locate the div with package-list class
Transform the children in an ul with the 3 spans being each an li
Repo:

GitHub repository: alx-frontend-for-fun
Directory: accessibility
File: fix-a11y/10-index.html
Copyright © 2024 ALX, All rights reserved.
