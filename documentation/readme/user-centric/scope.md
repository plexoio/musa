## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/user-centric.md)

1. [Strategy Plane - Reason, Solution and Value](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/strategy.md)
2. [Scope Plane - Feature and Capability](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/scope.md)
3. [Structure Plane - Content, Priority and Organization](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/structure.md)
4. [Skeleton Plane - Layout, Interaction and Relationship](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/skeleton.md)
5. [Surface Plane - Color, Typography, Effect and Images](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/surface.md)

# Scope Plane - Features and Capabilities

On this plane, we must be realistic and carefully consider the features that will be implemented. We need to brainstorm and keep in mind that we have less than two weeks for the first iteration of our Minimum Viable Product (MVP). Time, technologies, and knowledge all play a crucial role in making the final decision.

- It is important to clarify that in Agile Development, nothing is set in stone. We make flexible estimations that may change over time, either positively or negatively. We allow for changes at any stage of the development process.

Fortunately, we are utilizing the `Django framework`, which aligns with the philosophy of "for perfectionists with deadlines." This framework empowers us to build a functional application within a remarkably short timeframe.

For this iteration, we have made the decision to incorporate features and functionalities based on the following conditions and goals:

| Condition                     | Iteration                                                          | Goals                         |
|------------------------------|--------------------------------------------------------------------|-------------------------------|
| MVP Version                  | Display voting cards on homepage<br>Sign in/up option<br>Event Voting page<br>User Profile (roles)<br>Vote count and progress bar<br>Anonymity option | Culture acquisition            |
| Simple design                | Contact Form<br>User/Admin Dashboard<br>System Status Page<br>FAQ<br>Feedback after voting<br>Previous features* | Tech Showcase                 |
| Low leading rates<br>& Non-functional | KYC, Search Engine & Filters<br>Verification Badge                              | Long-term Investment<br>& Future Implementation |

- As evident from the table, the items listed under the `MVP Version` row will be included in the development process. However, it is important to note that the level of sophistication may not be the highest objectively speaking. Nonetheless, these features will be functional and meet the necessary requirements.

- In the subsequent `Simple Design` row, these items are also crucial for the project, although some may not receive the same level of attention as the key functional features. This approach applies to all features in general, as the primary purpose is to showcase our powerful technology.

- Regarding the last row, `Low leading rates & Non-functional`, incorporating the listed items will pose a challenge, and we will make an attempt to include them. However, due to the limited timeframe, we cannot make any promises about including all of them. These items will definitely be prioritized for the next iteration.

## User Stories

The following table is a well-equipped draft designed to facilitate the development process. Some user stories may be disregarded, while new ones may be added. This table has been motivated and fed by the results of the `design thinking`, `strategy plane`, and `scope plane`, as well as some elements of agile philosophy.

- **User Story Count:** 35
- **Capability:** 8 user stories per iteration  
- **Iteration Duration:** 1 day  
- **Estimation:** 8 user stories per day
- **Total Duration:** 4.37 days

### **Note**

- This User Story table is not the same as the [**Final User Story**](https://github.com/plexoio/musa/blob/main/documentation/readme/agile-development/agile-development.md) found in the `Agile Development` section.


| Theme                 | Epics                                | User Stories |
|-----------------------|--------------------------------------|--------------|
| Homepage              | Design Header                        | As a user, I want a clean, user-friendly header at the top of the page so that I can easily navigate and access the key features of the system. |
|                       | Arrange Mixed Campaign Cards in Row  | As a user, I want to see a general campaign section displayed prominently under the header, providing a recent mix of 'official' and 'community' created campaigns so that I can quickly overview current campaigns. |
|                       |                                      | As a user, I want each card to display key information related to the event, so I understand what I'm clicking on. |
|                       |                                      | As a user, I want to see a 'see more' button under the 'Campaigns' section so that I can view more comprehensive results on a separate page. |
|                       | Present Official Cards in Row        | As a user, I want to see an 'Official' section beneath the 'Campaign' row, presenting single-related events so that I can preview events related to this category. |
|                       |                                      | As a user, I want each card to display key information related to the event, so I understand what I'm clicking on. |
|                       |                                      | As a user, I want to see a 'see more' button under the 'Official' section so that I can view more comprehensive results on a separate page. |
|                       | Display Community Cards in Row       | As a user, I want to see a 'Community' section beneath the 'Official' row, presenting single-related events, so that I can preview events related to this category. |
|                       |                                      | As a user, I want each card to display key information related to the event, so I understand what I'm clicking on. |
|                       |                                      | As a user, I want to see a 'see more' button under the 'Community' section so that I can view more comprehensive results on a separate page. |
|                       | Construct Footer                     | As a user, I want to scroll to the end of the page to see the footer so that I have access to extra key information, useful links, and legal data. |
| Sign in/up & Dashboard| Link to Header                       | As a user or admin, I want to click on the header 'sign in or sign up' and be able to validate my login details on a separate page so that I can access my dashboard. |
|                       | Create User & Admin Dashboard        | As a user or admin, I want to log in or signup so that I can find a useful dashboard with key stats & menu options, based on my role, to interact with the system securely and smoothly. |
|                       | Build User & Admin Profile           | As a user or admin, I want to find a section on the dashboard to edit and control my profile on the system, to have full control over my data, and protect my privacy. |
|                       | Implement Verification Badge         | As a user or admin, I want to verify my account via email or KYC, to get access to a verified badge and participate in certain voting events. |
|                       | Develop Anonymity option             | As a user, I want to select from my dashboard whether my actions across the platform are anonymous or not, to protect my privacy, allowing only the company or third-party services to know my identity for security reasons. |
| Voting system         | Establish User & Admin Event Creation| As a user or admin, I want to create voting events from my dashboard and make them visible on the homepage once I have been verified, to make use of the powerful voting system. |
|                       | Design Voting Page                   | As a user or admin, I want to see my own or other people's voting events and participate, I can also click on 'Vote' to start the voting process on a separate page to have a more comprehensive section related to the event, seeing information not available on the homepage. |
|                       |                                      | As a user, visitor, or admin, I want to see the results of the event on the card once it has finished to stay informed about decision-making for this particular event. |
|                       | Enable Voting Feedback               | As a user or admin, I want to see a success alert or message after voting on an event as well as an update about the current stats, to have a better perception of the event situation and my contribution. |
|                       | Develop Voting Counter & Timer       | As a user or admin, I want to see a Vote Count & Progress Bar (time-related) on the homepage for each voting card and on the single page, to know how many people have participated and how much time is left for the event to end. |
|                       | Configure Role Visualization         | As a user, visitor, or admin, I want to have a visual understanding of my privileges depending on my role, to grasp the full potential of the site. |
| Search & Filter       | Develop 'See More' Page              | As a user, I want to see a 'see more' button after each section on the homepage which will take me to another page where I can see all the active events. |
|                       | Incorporate Search Bar               | As a user, I want a search engine on the recently opened page of all events, to search for a particular created or finished event. |
|                       | Integrate Filter Function            | As a user, I want a filter section on the very same page, to filter out by categories, country, in progress, or ended. |
| KYC                   | Design KYC Section in Dashboard      | As a user, I want to verify my account in the KYC section at the dashboard by submitting legal information about myself, to get a proper badge after verification and get some privileges to use the voting system. |
|                       | Implement Badge Activation           | As a user, I want to use KYC along with other verification methods to get a badge that will be visible on my dashboard and on my created events, to enhance trust in the campaign. |
|                       | Authorize Publisher Role             | As a user, I want to get the publisher role once I verify my account legally, to create and publish events. |
|                       |                                      | As a user with a publisher role, I want to create events once verified, but still need approval from the admin side, for my voting event to be published. |
| Accountability        | Construct Contact Form               | As a user, I want a well-designed contact page to get in touch with the support team. |
|                       |                                      | As a user, I want to see extra information on the same page regarding the transportation system or internet accessibility near me, to increase my possibilities of participating in real life, if applicable. |
|                       | Develop System Status Page           | As a user, I want to go to the support page to find the system status page, to know the state of some functionalities in case something is not working properly on my side. |
|                       | Assemble FAQ Section                 | As a user, I want to find a FAQ section on the support page, to see videos or articles for troubleshooting or other questions related to the voting system. |

### Useful Links

- [Final User Story](https://github.com/plexoio/musa/blob/main/documentation/readme/agile-development/agile-development.md)
- [Raw Data (user stories)](https://github.com/plexoio/musa/blob/main/documentation/readme/agile-development/raw_agile_start.md)

Consequently, we've aligned our scope with the insights gathered from our research in the `Strategy` plane. It's clear at this stage that our goal is to implement a Minimum Viable Product (MVP) iteration. This will effectively assist us in laying the groundwork for our next phase, the `Structure` stage.
