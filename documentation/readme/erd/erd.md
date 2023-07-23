## VoteCard Model

| Attribute    | Type           | Unique  | Relationship    | Model Linked To                |
|--------------|----------------|---------|-----------------|-------------------------------|
| id           | PrimaryKey     | Yes     | -               | -                             |
| title        | CharField(80)       | Yes     | -               | -                             |
| category     | **ForeignKey**    | -       | One to many     | Category Model                |
| mission      | CharField(80)       | -       | -               | -                             |
| location     | CharField(80)       | -       | -               | -                             |
| description  | TextField      | -       | -               | -                             |
| image        | Cloudinary     | -       | -               | -                             |
| vote_record  | **ManyToManyField**| -       | Many to many    | User Model through VoteRecord Model |
| expire       | Datetime       | -       | -               | -                             |
| author       | **ForeignKey**    | -       | One to many     | User Model                    |
| slug         | SlugField      | Yes     | -               | -                             |
| status       | Integer        | -       | -               | -                             |

## Category Model

| Attribute     | Type       | Unique  | Relationship | Model Linked To |
|---------------|------------|---------|--------------|-----------------|
| id            | PrimaryKey | Yes     | -            | -               |
| category_name | CharField(50)   | Yes     | -            | -               |

## User Model

| Attribute   | Type           | Unique  | Relationship | Model Linked To                             |
|-------------|----------------|---------|--------------|---------------------------------------------|
| id          | PrimaryKey     | Yes     | -            | -                                           |
| last_name   | CharField(80)  | -       | -            | -                                           |
| first_name  | CharField(80)  | -       | -            | -                                           |
| email       | EmailField     | Yes     | -            | -                                           |
| verified    | BooleanField   | -       | -            | -                                           |
| role        | IntegerField   | -       | -            | -                                           |
| password    | PasswordField  | -       | -            | -                                           |
| vote_cards  | **ManyToManyField**| -       | Many to many | VoteCard Model through VoteRecord Model    |
| username    | CharField      | Yes     | -            | -                                           |

## ElectedPerson Model

| Attribute  | Type          | Unique | Relationship | Model Linked To |
|------------|---------------|--------|--------------|-----------------|
| id         | PrimaryKey    | Yes    | -            | -               |
| name       | CharField(80) | Yes    | -            | -               |
| is_elected | BooleanField  | -      | -            | -               |

## VoteRecord Model

| Attribute      | Type           | Unique  | Relationship | Model Linked To |
|----------------|----------------|---------|--------------|-----------------|
| id             | PrimaryKey     | Yes     | -            | -               |
| vote_card      | **ForeignKey**    | -       | Many to one  | VoteCard Model  |
| voter          | **ForeignKey**    | -       | Many to one  | User Model      |
| elected_person | **ForeignKey**    | -       | Many to one  | ElectedPerson Model |
| timestamp      | DateTimeField  | -       | -            | -               |