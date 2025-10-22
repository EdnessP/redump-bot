`articles.json` contains the list of articles and exceptions for my cleanup bot running on the VGPC server and mirrored to the Redump IRC.

- The `"articles"` key contains a global list of articles that will be picked up and reported if found at the beginning of a datname.
  - The language subkeys are purely for readability, it has no effect on the bot as it runs.
  - If the article is not joined to another word with an apostrophe, it should have a space at the end.
- The `"strict"` key contains a list of articles that will only be reported if the datname contains the subkey.
- The `"exclude"` key contains a list of phrases that should be ignored if a datname starts with it.
