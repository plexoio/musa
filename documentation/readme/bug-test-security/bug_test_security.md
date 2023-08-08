## [HOME | RETURN](https://github.com/plexoio/musa)

# Test, Bug and Security

## Test

We have discovered that using the `user story` as the `expected result` in manual testing is a valid approach. It ensures that the functionalities implemented align with the user's requirements or expectations as defined in the user story. By doing so, we're essentially validating that the developed feature or functionality meets the criteria described previously.

| Action | Expected Result | Issues Found & Resolved | Test |
|--------|-----------------|--------------|------|
|   Use header     |     As a user, I want a clean, user-friendly header at the top of the page so that I can easily navigate and access the key features of the system.            |     NA         |  PASS    |
|    Use of Campaign Section    |        As a user, I want to see a general campaign section displayed prominently under the header, providing a recent mix of 'official' and 'community' created campaigns so that I can quickly overview current campaigns.         |      NA        |   PASS   |
|        |        As a user, I want each card to display key information in the 'Campaign' section related to the event, so I understand what I'm clicking on.         |        NA      |   PASS   |
|        |        As a user, I want to see a 'see more' button under the 'Campaigns' section so that I can view more comprehensive results on a separate page.         |        NA      |   PASS   |
|    Use of Official Section    |        As a user, I want to see an 'Official' section beneath the 'Campaign' row, presenting single-related events so that I can preview events related to this category.         |        NA      |   PASS   |
|        |        As a user, I want each card to display key information in the 'Official' section related to the event, so I understand what I'm clicking on.         |        NA      |   PASS   |
|        |        As a user, I want to see a 'see more' button under the 'Official' section so that I can view more comprehensive results on a separate page.         |        NA      |   PASS   |
|    Use of Community Section    |        As a user, I want to see a 'Community' section beneath the 'Official' row, presenting single-related events so that I can preview events related to this category.         |        NA      |   PASS   |
|                 |        As a user, I want each card to display key information in the 'Community' section related to the event, so I understand what I'm clicking on.         |        NA      |   PASS   |
|                 |        As a user, I want to see a 'see more' button under the 'Community' section so that I can view more comprehensive results on a separate page.         |        NA      |   PASS   |
|        Use of Footer         |        As a user, I want to scroll to the end of the page to see the footer so that I have access to extra key information, useful links, and legal data         |        NA      |   PASS   |
|        Use of Sign in/up & Dashboard         |        As a user or admin, I want to click on the header 'sign in/sign up' and be able to validate my login details on a separate page so that I can access my dashboard.         |        NA      |   PASS   |
|                |        As a user or admin, I want to log in and signup so that I can find a useful dashboard with key stats & menu options, based on my role, to interact with the system securely and smoothly.         |        YES      |   PASS   |
|       Use of Voting Sytem         |        As a user or admin, I want to create voting events from my dashboard and make them visible on the homepage once I have been verified, to make use of the powerful voting system.         |        NA      |   PASS   |
|                |        As a user, I want to see voting events and participate, I can also click on 'Vote' to start the voting process on a separate page to have a more comprehensive section related to the event, seeing information not available on the homepage.         |        NA      |   PASS   |
|                |        As a user, I want to see a success alert or message after voting on an event as well as an update about the current stats, to have a better perception of the event situation and my contribution.         |        NA      |   PASS   |
|                |        As a user, I want to see a Vote Count & Progress Bar (time-related) on the homepage for each voting card and on the single page, to know how many people have participated and how much time is left for the event to end.         |        NA      |   PASS   |
|                |        As a user, visitor, or admin, I want to have a visual understanding of my privileges depending on my role, to grasp the full potential of the site.         |        NA      |   PASS   |
|       Use of See More page         |        As a user, I want to see a 'see more' button after each section on the homepage which will take me to another page where I can see all the active events.         |        NA      |   PASS   |
|       Use of premature KYC         |        As a user with a publisher role, I want to create events once verified, but still need approval from the admin side, for my voting event to be published.         |        NA      |   PASS   |
|       Use of contact form        |        As a user, I want a well-designed contact page to get in touch with the support team.         |        NA      |   PASS   |
|       Use of FAQ        |        As a user, I want to find a FAQ section on the support page, to see videos or articles for troubleshooting or other questions related to the voting system.         |        NA      |   PASS   |
|       Use of the full Voting Card        |        As a User I want to see displayed in a structured manner the winner, the challengers, and the vote numbers So that I have a transparent view of the event, especially for tied results.         |        NA      |   PASS   |

### 
###
###
###

## Bugs

Like any project, ours has had its share of bugs. Below are some of the challenges we've faced:

#### a) Website Performance
We endeavored to consolidate everything using Django, Bootstrap, JQuery, PostgreSQL database and other technologies, aiming for a robust web application that functions seamlessly across all devices. However, we cannot assure consistent performance on devices with limited memory or processing capabilities.

#### b) Cloudinary Error: KeyError 'etag'
We encountered an error that prevented us from submitting our project to the Code Institute on time. Despite many hours of debugging with tutor assistance, the only resolution was to create a 'custom_storage.py' file to circumvent the problem.

**Error breakdown:**

> During the execution of the `collectstatic` command, Django attempted to gather and process static files. The `cloudinary_storage` package managed some or all of these files. As part of its routine, `cloudinary_storage` checks for duplicate content on Cloudinary to avoid redundant uploads. It does this by verifying the ETAG header in Cloudinary's response. However, the ETAG header was absent, resulting in a KeyError.

#### c) Event Completion Status
Events marked as expired only transition to "complete" after a user attempts to vote. This behavior is intentional for performance reasons. In the future, we might programmatically update the status upon loading, similar to the vote count or progress bar.

#### d) Social Media Links
At the moment, social media buttons direct users to the primary pages, intended solely for demonstration.

#### e) Vote Events Deletion
Indeed, in this version, VoteCards are only marked as completed, preventing further voting. Only a superuser or the website owner can delete a VoteCard. Deleting a VoteCard will also remove associated elected persons and vote card records, effectively erasing all data linked to that event.

#### Other Potential Bugs
For other issues, we suggest refreshing the page or clearing cache files. If problems persist, it's likely not an issue with the Musa project but may pertain to third-party services or the specific settings and capabilities of your device.

## Security

Concise explanation of why Django, Bootstrap, and PostgreSQL are considered safe:

1. **Django**:
   - **Framework Design**: Django follows the "batteries-included" philosophy and provides built-in protection against many common security threats like SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).
   - **Secure Defaults**: By default, Django configurations are set to be secure, ensuring developers don't accidentally expose vulnerabilities.
   - **Regular Updates**: The Django team frequently releases updates and patches to address any identified security concerns.

2. **Bootstrap**:
   - **Sanitized Inputs**: Bootstrap's JavaScript plugins are designed to automatically sanitize inputs to protect against XSS attacks.
   - **Trusted Development**: Bootstrap is maintained by a dedicated team and has a large community that helps in identifying and fixing potential vulnerabilities.
   - **Consistent Updates**: The Bootstrap team provides regular updates to keep the library secure against new threats.

3. **PostgreSQL**:
   - **Robust Access Controls**: PostgreSQL offers fine-grained access controls, allowing administrators to define who can access the database and what actions they can perform.
   - **SQL Injection Prevention**: PostgreSQL has built-in measures to prevent SQL injection attacks, especially when developers use parameterized queries.
   - **Encryption**: PostgreSQL supports data encryption both at rest and in transit, protecting sensitive data from unauthorized access.

All three tools prioritize security in their design and implementation. However, it's essential for us to stay updated with the latest versions and best practices to ensure maximum safety.