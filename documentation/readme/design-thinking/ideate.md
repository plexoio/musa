## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/design-thinking.md)
1. [Idea Outline](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/idea-outline.md)
2. [Empathy](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/the-process.md)
3. [Personas](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/personas.md)
4. [Definition](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/define.md)
5. [Persona](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/persona.md)
6. [Ideate](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/ideate.md)
7. [Conclusion](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/conclusion.md)
8. [PoC Prototype](https://github.com/plexoio/musa/blob/main/documentation/readme/design-thinking/prototype.md)
# 6. Ideate

## Let’s go green

1. **Transparency:** Event creators must be verified - a badge of verification is essential. In addition, they need to offer an open and transparent profile on the app. Official support could play a role in ensuring this. We should also provide a specific page for system status updates.
2. **Presentation:** The use of Materialize can enhance the display, layout, description, and metadata of candidates, thereby providing comprehensive information to voters. Considerations for color contrast, auditory feedback, and appropriate user response should also be made.
3. **Device Compatibility:** The advantage of using a website is that it is accessible by default on various devices. Implementing PWA functionality could further enhance this.
4. **Low Data Consumption:** Image compression when uploading from the user’s side is crucial to reduce data usage. As administrators, we should also implement this. We should aim to reduce the amount of data loaded by utilizing proper caching and DNS infrastructure, like Cloudflare.
5. **Motivation for Participation:** The faster users can access important data, the less likely they are to give up midway. Progress bars, colors, shapes, interactivity, news, and key information are critical. Show users through keywords and phrases that they are about to change the world. Consider accumulating exchangeable points for participating (optional).
6. **Reduce External Influences:** The presented information should not be persuasive; it cannot unintentionally favor a particular candidate or decision. Displaying how many people have voted compared to the expected turnout, and presenting this as a progress bar, might be effective. Comments and reactions should not compromise the event.
7. **KYC (Know Your Customer):** Both voters and creators should verify their accounts. The backend system should be robust enough to prevent duplicates or deceased individuals from voting. We could also rely on a third-party system for this.
8. **Security:** Prioritize user security with measures such as two-factor authentication, Google verification, SMS, email verification, security questions, and extra codes for actions. The backend should incorporate security measures like SiteLock. Connect the database to the blockchain, submitting only relevant data, to protect user privacy. Ensure both databases always match.
9. **Anonymity:** Users should have the option to display only one name or remain completely anonymous.
10. **Assistance System:** Incorporate FAQs and videos. Company staff or a third-party organization could provide online assistance.
11. **Legality:** Obtain necessary authorization before running legal events. Special verification for the user and the event should be in place. Follow imposed regulations.
12. **Paper-based and Electronic Options:** We might need to expand as a company to handle this ourselves. Initially, we could rely on a third-party, while also improving our systems.
13. **Blockchain:** Blockchain could utilize an oracle blockchain (Chainlink), its own smart contract for automation, and centralized systems combined. Consider including MetaMask real login method for the next iteration.
14. **Inclusivity:** Pay attention to accessibility. Include a library for reading aloud the event or recommend apps, choose the right font size and style. Always display an assistance button. An AI chatbot could help resolve questions.
15. **Internet Connection:** Use our own or a third-party service to display nearby Internet Connectivity, or if the event offers internet connection using Starlink to provide the data. Offer different working methods of our own or others.
16. **Transportation System:** Same as the last one. Include it in the voting card.
17. **Fast System:** Use the best technology, servers, and clean code that runs the system. Pass all different performance tests.

## Let’s go red

**Must-haves:**
- **Front-end:** Verification badge, Comprehensive User Profile, System Status Page, Materialize, JQuery, continuous user feedback, vote counting and progress bar (no persuasive data) on homepage, FAQs, video tutorials, contact form, accessibility, user dashboard (Event creation, CRUD where needed), Sign up/in.
- **Back-end:** Image compression, lazy loading, caching, DNS, Cloudflare, KYC, Anonymity option, clean code and tests, admin dashboard (CRUD).
- **Databases:** Database model, user and admin roles.
- **Culture:** Engagement, keywords, colors, progress bars, shapes, interactivity (they are about to change the world): Lottie files, illustrations.

**Considerations:** PWA, two-factor authentication, Email Verification, Internet and transportation map.

**Must-have prototype:** Proof-of-concept, Database model.

**Next steps:** Proof-of-concept, Database model.

**Questions:** Template examples and video learning about databases models? RDBMS.

**Session name:** Musa Attack.

**Reminder:** Always refer back to these documents for more detailed explanations.

**Notes:**
- This decision was made based on the two-week timeframe for the MVP creation. Keep document and more sessions for next iterations.
- Yellow highlighting represents a large number of features in the current block.
- Guerrilla Test not possible for this iteration.

**Final word on this session:**
We believe, using Darek Cabrera's measure of difficulty, that the product complexity can range from Complicated to Complex. As we can't control how users handle their variables, we need to consider:

1. **Option to make it worldwide or local:** The product should offer flexibility to cater both global and local needs, providing features that can be customized or adapted based on specific cultural contexts.
2. **Filtering options:** Implementing filtering options can allow users to tailor their experience according to their preferences and cultural sensitivities. This empowers users to control the content they engage with, ensuring a more personalized and relevant experience.
3. **Making things look more familiar, approachable, and less bureaucratic:** To instill a sense of purpose and pride among users, it is vital to design the product in a way that resonates with their cultural values and aesthetics. This can be achieved by using familiar concepts, language, and design elements.

Finding solutions goes beyond coding and technical aspects. It requires understanding the underlying concepts, applying logical thinking, making good design decisions, and considering the cultural implications of those choices. By incorporating these elements, the product can better address the needs and preferences of its users, promoting a more inclusive and user-friendly experience.