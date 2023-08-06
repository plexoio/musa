## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/user-centric.md)

1. [Strategy Plane - Reason, Solution and Value](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/strategy.md)
2. [Scope Plane - Feature and Capability](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/scope.md)
3. [Structure Plane - Content, Priority and Organization](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/structure.md)
4. [Skeleton Plane - Layout, Interaction and Relationship](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/skeleton.md)
5. [Surface Plane - Color, Typography, Effect and Images](https://github.com/plexoio/musa/blob/main/documentation/readme/user-centric/surface.md)

# Surface Plane - Color, Typography, Effect and Images

After extensive research, strategy formulation, and brainstorming, we've crafted a solid project skeleton. With our groundwork in place, we're poised to initiate the next phase: building the surface plane. While this foundational work is crucial, it's in the actual creation and coding stages that we anticipate uncovering any potential challenges or nuances. Now is the ideal time to transform our ideas into reality and refine them as we progress. We eagerly anticipate witnessing our project evolve.

Here's a revised version for clarity and conciseness:

**Approach:**

We model our project strategy after the wisdom of Isaac Newton, who once remarked, `"My method is different. I do not rush into actual work. When I get a new idea, I start at once building it up in my imagination, and make improvements and operate the device in my mind. When I have gone so far as to embody everything in my invention, every possible improvement I can think of, and when I see no fault anywhere, I put into concrete form the final product of my brain."` Just as Newton painstakingly refined his ideas mentally before realization, we meticulously plan and polish our project prior to the actual programming phase.

At this juncture, our primary attention is on the surface plane. This encompasses not just the design of the interface but also the user's entire interaction journey. Our aim is to establish a coherent visual language that shapes each step and touchpoint, ensuring a fluid and intuitive user experience.

Every nuance matters for the project's success, and we are unyieldingly committed to perfecting them.

### Color

|                                                                  | Color Type      | Color Name      | Hex Code  |
| ---------------------------------------------------------------- | --------------- | --------------- | --------- |
| ![Color](https://via.placeholder.com/50x50/34495e/34495e?text=+) | Primary Color   | Shade of Blue   | `#34495e` |
| ![Color](https://via.placeholder.com/50x50/ffffff/ffffff?text=+) | Secondary Color | White   | `#ffffff` |
| ![Color](https://via.placeholder.com/50x50/f8f9fa/f8f9fa?text=+) | Secondary Color | Shade of White      | `#f8f9fa` |
| ![Color](https://via.placeholder.com/50x50/dadada/dadada?text=+) | Secondary Color | Shade of White      | `#dadada` |
| ![Color](https://via.placeholder.com/50x50/333333/333333?text=+) | Secondary Color | Shade of Black  | `#333333` |
| ![Color](https://via.placeholder.com/50x50/2D4F2F/2D4F2F?text=+) | Secondary Color | Shade of Green  | `#2D4F2F` |
| ![Color](https://via.placeholder.com/50x50/763135/763135?text=+) | Secondary Color | Shade of red    | `#763135` |
| ![Color](https://via.placeholder.com/50x50/ffbe00/ffbe00?text=+) | Secondary Color | Shade of orange | `#ffbe00` |
| ![Color](https://via.placeholder.com/50x50/0000000d/0000000d?text=+) | Secondary Color | Shade of black | `#0000000d` |


#### Pallet

The following color palette was used as a reference throughout the project:

- [My Color Space](https://mycolor.space/?hex=%2334495E&sub=1)


### Layout

- The welcoming page features is a full-page banner with a `h2-sized` title and a `Swap` button to enter the system.

- For the login section, `containers` and a `form` are used to manage it. All elements are well-connected and interactive, thanks to `JavaScript`.

- The swapping sections for `Fiat & Crypto` are `containers` holding `forms` for the swapping functionality. In every section where a `submit or call-to-action` is present, the same style is used to maintain consistency.

- The `contact form` also follows the consistency of the containers and features a powerful form and a related `submit button`, as mentioned before.

- Finally, the layouts will naturally adjust to different `sizes` when media queries are set for `responsive design`.

### Fonts

- We used `Roboto` for all fonts until specified otherwise. 

- We used `Poppins` for some titles and subtitles.

### Images

- No additional images were needed, except for the `interactive logo` of a third-party service about `Metamask` on the login page.

### Order

- We prioritized the elements as already described throughout the different planes: Welcome page > Login Page > Fiat or Crypto Swap > Contact page.

- The navbar and footer are always present (sticky) after the welcome page.

- For the Contact page, a container similar to the others was applied to maintain consistency.

### Sequences

- Attention to the `progressive disclosure` allowed us to build a smooth application flow. Users see the `welcome page` first, then they can `log in` using either Fiat or Crypto methods. Once logged in, they can start `swapping` in a straightforward manner. If they have any inquiries, they can visit the `contact page` as well.

- The `swapping pages` are the core of the project and what users are looking for in most cases. They are consistent and allow users to swap from one coin to another and `confirm` the swap with a submit `button`.

For each section and interaction, economy had to be taken into account, with the most important elements easily recognized. We had already noticed many patterns throughout the product layouts and interactions. It was readable, with colors creating good contrasts, and different fonts were added when necessary.

Users cannot get lost on the site as we have ensured that value is evident everywhere.

**We had to be careful of the following concerns:**

- Repetition
- Contrast
- Proximity
- Alignment
- Accessibility
- Interaction
- Visual engagement
- Easy learning experience

We focused on keeping things as simple as possible, presenting fewer choices to the users while highlighting concrete features and content.

After considering these factors, we were able to turn our ideas from the skeleton and surface into code with ease. The coding process was less complicated and more enjoyable. This approach required less time, energy, and other resources, resulting in less human work and fewer errors, and ultimately, a nobler product.