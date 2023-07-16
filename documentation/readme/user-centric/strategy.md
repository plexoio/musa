## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/user-centric.md)

1. [Strategy Plane - Reason, Solution and Value](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/strategy.md)
2. [Scope Plane - Feature and Capability](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/scope.md)
3. [Structure Plane - Content, Priority and Organization](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/structure.md)
4. [Skeleton Plane - Layout, Interaction and Relationship](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/skeleton.md)
5. [Surface Plane - Color, Typography, Effect and Images](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/surface.md)

# Strategy Plane - Reason, Solution, and Value

In this phase, we analyze the data obtained from conducting 4 different interviews with individuals from diverse backgrounds. These interviews have provided valuable insights into the general and specific aspects of a `voting system`.

Based on our findings from the `design thinking` process, we have reached the following conclusions, which will serve as our `official source of information` for Musa's MVP:

Although our users may not have had a complete understanding of their needs, we made every effort to comprehend their requirements and propose the best possible solutions.

Recognizing that users are the key stakeholders, our primary focus is to create a platform that benefits both business professionals and future users.

Transparency, security, presentation, accessibility, and performance are critical concerns for our users. To address these issues, we will tackle specific problems and fulfill their desires, enabling them to thrive within the ecosystem.

For this iteration, we have identified the following core technologies to utilize:

- Django (MVC/MVT)
- JQuery
- Materialize
- PostgreSQL
- psycopg2
- SQLAlchemy
- Font Awesome
- Lottie Files

To address individual issues, tasks, or desires, please refer to the following resources:

- [Design-Thinking Conclusion](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/conclusion.md)
- [Design-Thinking Prototype](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/prototype.md)

Our insights are grounded in sufficient research, supported by the accompanying table and graphic:

- From this table, we can extract the themes, epics, and potential ideas for user stories.

### Research

| Goals                         | Relevancy (0-5) | Viability (0-5) | N. Items (0-~) |
| ----------------------------- | --------------- | --------------- | -------------- |
| Display voting cards on homepage | 5               | 5               | 1              |
| Sign in/up option             | 5               | 5               | 1              |
| User/Admin dashboard          | 5               | 5               | 1              |
| Contact form                  | 5               | 5               | 1              |
| Event Voting (Single-Page)    | 5               | 4               | 1              |
| User Profile                  | 5               | 4               | 1              |
| System Status Page            | 5               | 4               | 1              |
| FAQs                          | 5               | 4               | 1              |
| Feedback after voting         | 5               | 4               | 1              |
| Vote count and progress bar| 4               | 4               | 1              |
| Anonymity option              | 5               | 4               | 1              |
| KYC                           | 5               | 3               | 1              |
| Search Engine & Filters       | 5               | 3               | 1              |
| Verification badge            | 5               | 3               | 1              |
| N. Items                      |                 |                 | 14             |
| Max. Points                   |                 |                 | 70             |
| Results                       | 69              | 57              |                |
| Percentage                    | 98.57% (Strategy) | 81.42% (Scope)|                |

## Research Graphic

![Table Graphic](https://github.com/plexoio/musa/blob/main/documentation/assets/img/user-centric/uc-table.png)

We've conducted an estimation based on our experience, and we are pleasantly surprised by the `design thinking` results. The decisions about which features to implement felt grounded in real factors and user needs, rather than personal assumptions or ideas.

As indicated in the table and the graphic, most of the features have high relevancy for this iteration. An exception is the `Vote Count & Progress bar` feature, which received a '4' in both relevancy and viability. This feature could take various forms, and its style is subject to continuous changes to improve the user experience.

Looking at the viability column, the most important features range from 4 to 5, which isn't a significant difference. This slight variation represents our ability to fulfill potential requirements within our time and resource constraints. This applies especially to the last three items in the table:
- KYC
- Search Engine & Filters
- Verification badge

Despite being powerful features, their full implementation might be constrained by our limited resources and time. However, we will strive to add functional aspects for each to meet the Minimum Viable Product (MVP) requirements.

We should highlight that achieving most of the features described above doesn't necessarily mean they are all perfect or that the development process has come to an end. On the contrary, this MVP is the foundation for a much more robust and reliable voting system.

## Key Results:

- Items: 14
- Strategy: 98.57%
- Scope: 81.42%

We plan to implement 14 key features, with a 98.57% alignment with our MVP's strategy and an 81.42% viability based on our estimation. All this is taking into account our current resources and deadlines.

These percentages will inform our overall strategy, as they consider the relevancy and viability of the features. This data will guide us in planning the upcoming `scope`, as these factors are interconnected.

Armed with this information, we can now move to the next stage, which is defining the `scope` of our project.
