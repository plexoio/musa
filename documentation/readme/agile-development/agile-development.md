## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/user-centric.md)

Agile Development prioritizes adaptability and swift responses to changing requirements. By promoting close collaboration between cross-functional teams and stakeholders, it ensures a clearer understanding of end-user needs. Frequent iterations and feedback loops result in a product that's more aligned with customer demands, often leading to higher satisfaction, improved quality, and faster time-to-market.

# Development Process

An agile approach was used before, during and after development. We have used `user stories `and `product backlog`, `timeboxing` and `MoSCoW Prioritization`.

## User Stories

The user stories have undergone some modifications since their initial conception during the `user-centric design` phase at the `scope plane`. What follows is the finalized user story that guided our development process.

### Must-have

| Theme                 | Epics                                | User Stories | Story Point |
|-----------------------|--------------------------------------|--------------|-------------|
| Homepage              | Design Header                        | As a user, I want a clean, user-friendly header at the top of the page so that I can easily navigate and access the key features of the system. | **2** |
|                       | Arrange Mixed Campaign Cards in Row  | As a user, I want to see a general campaign section displayed prominently under the header, providing a recent mix of 'official' and 'community' created campaigns so that I can quickly overview current campaigns. | **4** |
|                       |                                      | As a user, I want each card to display key information in the 'Campaign' section related to the event, so I understand what I'm clicking on. | **2** |
|                       |                                      | As a user, I want to see a 'see more' button under the 'Campaigns' section so that I can view more comprehensive results on a separate page. | **1** |
|                       | Present Official Cards in Row        | As a user, I want to see an 'Official' section beneath the 'Campaign' row, presenting single-related events so that I can preview events related to this category. | **4** |
|                       |                                      | As a user, I want each card to display key information in the 'Official' section related to the event, so I understand what I'm clicking on. | **2** |
|                       |                                      | As a user, I want to see a 'see more' button under the 'Official' section so that I can view more comprehensive results on a separate page. | **1** |
|                       | Display Community Cards in Row       | As a user, I want to see a 'Community' section beneath the 'Official' row, presenting single-related events so that I can preview events related to this category. | **4** |
|                       |                                      | As a user, I want each card to display key information in the 'Community' section related to the event, so I understand what I'm clicking on. | **2** |
|                       |                                      | As a user, I want to see a 'see more' button under the 'Community' section so that I can view more comprehensive results on a separate page. | **1** |
|                       | Construct Footer                     | As a user, I want to scroll to the end of the page to see the footer so that I have access to extra key information, useful links, and legal data. | **2** |
| Sign in/up & Dashboard| Link & Page from Header                       | As a user or admin, I want to click on the header 'sign in/sign up' and be able to validate my login details on a separate page so that I can access my dashboard. | **1** |
|                       | Create User & Admin Dashboard        | As a user or admin, I want to log in and signup so that I can find a useful dashboard with key stats & menu options, based on my role, to interact with the system securely and smoothly. | **7** |
|       Voting system             | Establish User & Admin Event Creation           | As a user or admin, I want to create voting events from my dashboard and make them visible on the homepage once I have been verified, to make use of the powerful voting system. | **7** |
|                       | Design Voting Page         | As a user, I want to see voting events and participate, I can also click on 'Vote' to start the voting process on a separate page to have a more comprehensive section related to the event, seeing information not available on the homepage. | **7** |
|                       | Enable Voting Feedback             | As a user, I want to see a success alert or message after voting on an event as well as an update about the current stats, to have a better perception of the event situation and my contribution. | **7** |
|                       | Develop Voting Counter & Timer | As a user, I want to see a Vote Count & Progress Bar (time-related) on the homepage for each voting card and on the single page, to know how many people have participated and how much time is left for the event to end. | **13** |
|                       | Configure Role Visualization                   | As a user, visitor, or admin, I want to have a visual understanding of my privileges depending on my role, to grasp the full potential of the site.|**4**|
| Search & Filter         | Develop 'See More' Page               | As a user, I want to see a 'see more' button after each section on the homepage which will take me to another page where I can see all the active events. | **4** |
|       KYC             | 	Authorize Publisher Role       | As a user with a publisher role, I want to create events once verified, but still need approval from the admin side, for my voting event to be published. | **7** |
|     Accountability        | Construct Contact Form         | As a user, I want a well-designed contact page to get in touch with the support team. | **2** |
|                           | Assemble FAQ Section           | As a user, I want to find a FAQ section on the support page, to see videos or articles for troubleshooting or other questions related to the voting system. | **4** |
|          Voting system    | Display winner and general results with numbers               | As a User I want to see displayed in a structured manner the winner, the challengers, and the vote numbers So that I have a transparent view of the event, especially for tied results. | **7** |

### Won't have

| Theme                 | Epics                                | User Stories | Story Point |
|-----------------------|--------------------------------------|--------------|-------------|
| Sign in/up & Dashboard              | Implement Verification Badge                        | As a user or admin, I want to verify my account via email or KYC, to get access to a verified badge and participate in certain voting events. | **4** |
|              | Develop Anonymity option                        | As a user, I want to select from my dashboard whether my actions across the platform are anonymous or not, to protect my privacy, allowing only the company or third-party services to know my identity for security reasons. | **4** |
| Search & Filter             | Incorporate Search Bar                        | As a user, I want a search engine on the recently opened page of all events, to search for a particular created or finished event. | **4** |
|              | Integrate Filter Function                        | As a user, I want a filter section on the very same page, to filter out by categories, location, in progress, or ended. | **4** |
|        KYC      | Design KYC Section in Dashboard                        | As a user, I want to verify my account in the KYC section at the dashboard by submitting legal information about myself, to get a proper badge after verification and get some privileges to use the voting system. | **4** |
|                 | Implement Badge Activation                        | As a user, I want to use KYC along with other verification methods to get a badge that will be visible on my dashboard and on my created events, to enhance trust in the campaign. | **7** |            |                 | Authorize Publisher Role                     | As a user, I want to get the publisher role once I verify my account legally, to create and publish events.| **7** |
  |        Accountability         | Transportation & Internet Accessibility               | As a user, I want to see extra information on the same page regarding the transportation system or internet accessibility near me, to increase my possibilities of participating in real life, if applicable.| **7** |
  |                | Develop System Status Page               | As a user, I want to go to the support page to find the system status page, and to know the state of some functionalities in case something is not working properly on my side. | **4** |


## Product Backlog
## Timeboxing
## MoSCoW Prioritization