## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/developer/erd.md)

## Relationship type

Yes, the nature of instances and how uniqueness is enforced largely determines the relationship type between tables in a relational database. Let's briefly go over the common relationship types and how they're determined by instances and uniqueness:

1. **One-to-One (1:1)**:
    - An instance in Table A can be related to only one instance in Table B, and vice versa.
    - Uniqueness is enforced on both sides of the relationship. For example, if Table B has a foreign key pointing to Table A, that foreign key must be unique in Table B.

2. **One-to-Many (1:M)**:
    - An instance in Table A can be related to multiple instances in Table B. However, an instance in Table B can be related to only one instance in Table A.
    - Uniqueness is enforced only on the "one" side (usually the primary key). The "many" side will have a foreign key pointing to the "one" side without a unique constraint, allowing multiple rows in Table B to reference the same row in Table A.

3. **Many-to-Many (M:M)**:
    - An instance in Table A can be related to multiple instances in Table B, and vice versa.
    - This relationship typically requires an intermediate table (also known as a "junction table" or "bridge table") to represent the relationship. Each row in this table represents a relationship instance between Table A and Table B. Uniqueness is often enforced through a composite key, combining the foreign keys of Table A and Table B, ensuring that each pairing is unique.

So, in essence, the combination of how instances relate to each other and how uniqueness constraints are applied helps define and enforce the specific relationship type between tables.

### Composite Key

Let's clarify:

A **composite key** is a type of key that consists of two or more columns used to uniquely identify rows in a table. These columns together enforce the uniqueness constraint, meaning their combined values cannot be duplicated in another row. A composite key is used when no single column is sufficient to uniquely identify rows.

An **ID** (often called a primary key when specifically referring to databases) is a unique identifier for a record in a database table. It's typically a single column. In many databases, this is often an auto-incrementing integer, but it could also be a UUID, a string, or other data types, depending on the system's design.

To contrast:

1. A **single-column primary key (like an ID)** uniquely identifies a row based on the value in one column.
2. A **composite key** uniquely identifies a row based on the combined values of two or more columns.

Here's an example to illustrate:

Consider a table that logs the courses taken by students, named `StudentCourses`. If students can only enroll in a course once, then the combination of `student_id` and `course_id` would uniquely identify each enrollment.

In this case, the table might look like this:

| student_id | course_id | enrollment_date |
|------------|-----------|-----------------|
| 1          | A         | 2023-01-01      |
| 1          | B         | 2023-01-05      |
| 2          | A         | 2023-01-02      |
| 3          | C         | 2023-01-03      |

Here, `(student_id, course_id)` together act as a composite key. No single column by itself guarantees uniqueness, but the combination of the two does. For example, a student with `student_id` of `1` can enroll in both course `A` and course `B`, but they can't enroll in course `A` twice.

To clarify, while the composite key uniquely identifies each row in this table, it's not necessarily the same as a single-column ID (or primary key). In some scenarios, the table might also include an additional `ID` column as a single primary key, but it's not always necessary. Whether to include such an ID depends on the specific requirements and design considerations of the database schema.

### Understanding the Core Concepts

Exactly! You've captured the essence of it.

- **VoteCard**: Represents a specific item or topic that users can vote on.
- **User**: Signifies individuals who can cast votes on various VoteCards.
- **VoteRecord**: Documents each individual vote, highlighting the "many to many" relationship between VoteCards and Users.

### Delving Deeper into the Voting Process

To expand further:

- **Voting Action**: Every time a **User** casts a vote for a **VoteCard**, a new entry is made in the **VoteRecord** table. This entry creates a link between the specific **User** and the **VoteCard** they voted on.
  
- **Accumulating Votes**: Over time, one **VoteCard** can amass numerous entries in the **VoteRecord** table, each signifying a vote from a different user.
  
- **User Voting History**: A single **User**, too, can have multiple entries in the **VoteRecord** table. These entries stand as a record of their votes on various VoteCards.

### Benefits of the Structured Approach

This structure assists in tracking who voted for what, guaranteeing each user's unique vote for every VoteCard and also streamlining the process of counting total votes for each VoteCard via related entries in the **VoteRecord** table.

### Weighing in on Direct ManyToMany Relationships

You've made a pertinent observation about many database systems and ORM (Object Relational Mapping) libraries. They often provide direct "ManyToMany" relationships, negating the necessity of an overt intermediate table. This automatic generation of an intermediate table, akin to your `VoteRecord`, is typically unseen but works in the background to manage the relationship.

However, consider the perks of setting up your distinct intermediate table like `VoteRecord`:

1. **Enhanced Flexibility**: This allows for the inclusion of extra fields in the intermediate table. For instance, your `VoteRecord` has distinctive fields like `elected_person` and `timestamp`.
 
2. **Clearer Representation**: An overt table elucidates the data model. It provides clarity, helping anyone reviewing your model to grasp the role of `VoteRecord` and the type of data it preserves.

3. **Greater Control**: Managing the intermediate table individually offers more power over its framework, permissible operations, and data retrieval methods.

### When to Opt for an Explicit Table

If the only requirement was to show that users can vote on VoteCards, a direct ManyToMany field in one of the models would suffice. However, the desire to chronicle more details about each vote (attributes like `timestamp` or `elected_person`) justifies the use of an explicit `VoteRecord` table.

To sum up, while it's feasible to depict a many-to-many tie without an overt table, such a method often proves restrictive once there's a need to detail more than just the relationship.