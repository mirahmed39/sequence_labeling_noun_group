# sequence_labeling_noun_group
Machine learning program that creates feature files to train the noun_group labeling system and later performs on a test file with accuracy of 90% 

## What does "Labeling Noun Group" mean?
Let me answer this queestions directly with an example sentence: "My name is Mir Ahmed and I attend New York University."
If this sentence is ran through the trained system it will label the sentence in the following way:

| Tokens        |  BIO tags |
|---------------|-----------|
| My            | B         |
|  name         |  I        |
| is            |  O        |
|  Mir          |  B        |
|  Ahmed        | I         |
|  and          |  O        |
|  I            |  B        |
|  attend       | O         |
|  New          | B         |
|  York         | I         |
|  University   | I         |
|  .            | O         |

### BIO Tag description
**B** -- Beginning Tag
**I** -- Intermdeiate Tag
**O** -- End tag

Therefore, it is not hard to see that a noun-group has begins with a **B** tag and continues until it encounters an **O** tag (token related to O tag is excluded).
