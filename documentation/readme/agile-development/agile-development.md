## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/)

Agile Development prioritizes adaptability and swift responses to changing requirements. By promoting close collaboration between cross-functional teams and stakeholders, it ensures a clearer understanding of end-user needs. Frequent iterations and feedback loops result in a product that's more aligned with customer demands, often leading to higher satisfaction, improved quality, and faster time-to-market.

# Development Process

An agile approach was used before, during and after development. We have used:

- `User stories `and `Product Backlog`
- `Timeboxing` and `MoSCoW Prioritization`.

## User Stories

The user stories have undergone some modifications since their initial conception during the `user-centric design` phase at the `scope plane`. What follows is the finalized user story that guided our development process.

- In total there are `34` user stories.
- Only `24 must-have` user stories 
- Only `10 won't have` user stories 

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

### Won't-have

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

These user stories have undergone several phases to arrive at their current iteration in this module. Their progression included:

- Starting from `Theme`, transitioning to `Epic`, followed by `Brief` and `User Story`.

Additionally, we adopted `Story Points` using a `modified Fibonacci sequence`, culminating in their `Complete` status.

Simultaneously, each user story was structured using a comprehensive template that captures essential data, metadata, progress logs, and developer comments.

To view the detailed journey of these user stories, visit:

- [Musa's Github Issues](https://github.com/plexoio/musa/issues)



## Timeboxing

Timeboxing in agile development involves allocating a fixed duration, termed "timebox", to a specific task. Regardless of whether the task is fully completed by the end of this period, the team proceeds to the next task. This methodology ensures consistent progress, on-time task management, and regular reprioritization.

To facilitate this approach, we employed Github's project boards within the projects section. This board segmented tasks into `Todo`, `In progress`, and `Done` categories, effectively assisting us in sprint creation.

This strategy was paramount to our development workflow. It championed organic and structured software development, while simultaneously emphasizing task prioritization and our predictive measures, as outlined in 'RELEASE: Estimation and Team Velocity'.

For an in-depth perspective, please refer to:

- [Project Boards (Sprints or Iterations)](https://github.com/plexoio/musa/projects?query=is%3Aopen)
- [RELEASE: Estimation and Team Velocity]()

## MoSCoW Prioritization

**MoSCoW Prioritization** in agile development is a technique used to prioritize requirements by categorizing them into:

- **Must have**: Essential requirements necessary for a successful release.
- **Should have**: Important but not vital; can be delayed if necessary.
- **Could have**: Desirable features that are beneficial but not essential.
- **Won't have**: Items agreed upon as not necessary for the current release but might be considered in the future.

This method helped us clarify and agree on priorities, ensuring that the most crucial features were delivered first.

We applied the `MoSCoW Prioritization` method as `labels` within our product backlog and during timeboxing. For a comprehensive overview of these labels in action, please visit:

- [Musa's Labels](https://github.com/plexoio/musa/labels)
- [Open Issues](https://github.com/plexoio/musa/issues)
- [Closed Issues](https://github.com/plexoio/musa/issues?q=is%3Aissue+is%3Aclosed)
- [Last Sprint](https://github.com/users/plexoio/projects/11)
