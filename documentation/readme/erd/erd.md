## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/)

# Entity Relationship Diagram ERD

Musa is working with a Django project that uses PostgreSQL as its database backend, and Psycopg2 as the PostgreSQL adapter for Python. The project leverages Django's Object-Relational Mapping (ORM) system for database operations. Here's an enhanced explanation of the components and their interrelations:

**Django**:
Django is a high-level web framework written in Python. It encourages rapid development and adheres to the "Don't Repeat Yourself" (DRY) principle. One of Django's most powerful features is its built-in ORM system, which allows developers to interact with the database in an object-oriented manner.

**PostgreSQL**:
PostgreSQL is an open-source relational database management system (RDBMS) that emphasizes extensibility and standards-compliance. It's known for its robustness, performance, and features.

**Psycopg2**:
Psycopg2 is the most popular PostgreSQL adapter for the Python programming language. In the context of a Django project, Psycopg2 acts as the bridge between the Django application and the PostgreSQL database, translating Pythonic queries into SQL queries that PostgreSQL can understand.

**Django ORM**:
The Django ORM (Object-Relational Mapping) is a component of Django that allows developers to define their database schema using Python classes. Each class corresponds to a table in the database, and instances of the class correspond to rows in that table. The ORM provides a high-level, Pythonic way to query the database, abstracting away the underlying SQL. This means developers can write database queries using Python, and Django will automatically convert these into the appropriate SQL for the chosen database backend.

In Musa's project:
1. Django is the foundational framework providing the structure and mechanisms for web interactions.
2. PostgreSQL is the database storing all the data Musa's application will use and manipulate.
3. Psycopg2 acts as the intermediary, ensuring that data flows between the Django app and PostgreSQL database smoothly.
4. When Musa wants to interact with the data stored in PostgreSQL, he would use Django's ORM to define and query the database models. This approach not only abstracts the underlying SQL intricacies but also ensures that the code remains readable and Pythonic.

In essence, Musa is harnessing the power of both Django and PostgreSQL to create an efficient and scalable web application. This combination is quite popular in the industry due to its robustness and the ease of development it offers.

## ERD Diagram

![ERD Diagram Image](https://github.com/plexoio/musa/blob/main/documentation/assets/img/erd/erd.png)

- [Edrawmax](https://www.edrawmax.com/online/share.html?code=3cce5a7c28ec11ee94660a951ba8b83d): Check our ERD Online

## Markdown Table Models

### VoteCard Model

| Attribute    | Type           | Unique  | Relationship    | Model Linked To                |
|--------------|----------------|---------|-----------------|-------------------------------|
| id           | PrimaryKey     | Yes     | -               | -                             |
| title        | CharField(33)       | Yes     | -               | -                             |
| category     | **ForeignKey**    | -       | Many to one     | Category Model                |
| mission      | CharField(33)       | -       | -               | -                             |
| location     | CharField(33)       | -       | -               | -                             |
| description  | TextField(258)     | -       | -               | -                             |
| event_image  | CloudinaryField     | -       | -               | -                             |
| vote_record  | **ManyToManyField**| -       | Many to many    | UserProfile Model through VoteRecord Model |
| candidates  | **ManyToManyField**| -       | Many to many    | ElectedPerson Model |
| expire       | DateField      | -       | -               | -                             |
| author       | **ForeignKey**    | -       | Many to one    | UserProfile Model                    |
| slug         | SlugField(200)     | Yes     | -               | -                             |
| status       | IntegerField        | -       | -               | -                             |
| excerpt       | TextField        | -       | -               | -                             |
| type       | IntegerField        | -       | -               | -                             |
| created_on       | DataField        | -       | -               | -                             |

### Category Model

| Attribute     | Type       | Unique  | Relationship | Model Linked To |
|---------------|------------|---------|--------------|-----------------|
| id            | PrimaryKey | Yes     | -            | -               |
| category_name | CharField(50)   | Yes     | -            | -               |

### UserProfile Model (AbstractUser)

| Attribute   | Type           | Unique  | Relationship | Model Linked To                             |
|-------------|----------------|---------|--------------|---------------------------------------------|
| id         | PrimaryKey    | Yes    | -            | -               |
| verified    | BooleanField   | -       | -            | -                                           |
| role        | IntegerField   | -       | -            | -                                           |
| user_card  | **ManyToManyField**| -       | Many to many | VoteCard Model through VoteRecord Model    |

### ElectedPerson Model

| Attribute  | Type          | Unique | Relationship | Model Linked To |
|------------|---------------|--------|--------------|-----------------|
| id         | PrimaryKey    | Yes    | -            | -               |
| name       | CharField(80) | Yes    | -            | -               |
| is_elected | BooleanField  | -      | -            | -               |
| vote_card  | **ForeignKey**| -       | Many to one | VoteCard Model   |

### VoteRecord Model

| Attribute      | Type           | Unique  | Relationship | Model Linked To |
|----------------|----------------|---------|--------------|-----------------|
| id             | PrimaryKey     | Yes     | -            | -               |
| vote_card      | **ForeignKey**    | -       | Many to one  | VoteCard Model  |
| voter          | **ForeignKey**    | -       | Many to one  | UserProfile Model      |
| elected_person | **ForeignKey**    | -       | Many to one  | ElectedPerson Model |
| timestamp      | DateTimeField  | -       | -            | -               |

## Developer Experience

Our intention is to deliver an intuitive and productive experience for developers diving into this project. With this aim, we've curated a specialized section dedicated to giving an in-depth understanding of the database model and, in the process, serving as a handy refresher for enthusiasts keen on deepening their grasp of Django's relational databases.

The content within this section isn't just a result of the author's expertise, but also a collaborative effort. We enlisted the aid of advanced language models, specifically ``ChatGPT`` and ``Bard``, to refine and clarify the concepts, ensuring that the information is both accurate and easily digestible.

### Dive Deeper:

1. **[General Set up Instructions](https://github.com/plexoio/musa/blob/main/documentation/readme/set-up-and-deployment/set_up_and_deployment.md)**: 
   Begin your journey here. This guide provides step-by-step procedures on setting up the project, ensuring you can get started without any hiccups.

2. **[ERD Reminder](https://github.com/plexoio/musa/blob/main/documentation/developer/reminder.md)**: 
   Need a quick refresher on Entity-Relationship Diagrams (ERD) or want to grasp how they're utilized in our project? This reminder is tailored for you.

3. **[ERD & Code recommendations](https://github.com/plexoio/musa/blob/main/documentation/developer/recommendations.md)**:
   Drawing from our experiences and insights, we've compiled recommendations on how the ERD can be effectively implemented in code. If you're aiming to optimize your database interactions or seeking best practices, you'll find invaluable advice here.

Whether you're a seasoned developer or someone just starting out, these resources are designed to provide clarity, guidance, and a deeper appreciation for the intricate workings of Django and its relational databases.