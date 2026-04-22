## Prompt 1: 

**Prompt:** ```what immediate issues do you see in the code```

**Response:**
```
I’m checking the current code and the issue notes first so I can give you concrete findings instead of guessing. After that I’ll summarize the highest-risk problems and any gaps that need follow-up.

I’ve got the main risks now and I’m just checking for any obvious parser/runtime issues so I don’t miss something trivial. Then I’ll give you the review in severity order.

The immediate problems are security-related.

Critical: backend.py:40 and backend.py:45 build SQL with f-strings using untrusted webhook fields. email, role, and the raw JSON body can break out of the query and inject arbitrary SQL. This is the same issue noted in issues.txt:1.
High: backend.py:9 falls back to dev-secret when WEBHOOK_SECRET is unset, which makes webhook forgery trivial in any environment that forgets to set the variable. The signature check in backend.py:19 also uses a plain equality comparison instead of a constant-time compare.
Medium: backend.py:35 opens a database connection and never closes it, and there is no rollback or error handling around the writes. A bad payload or DB error can leak connections and leave the request failing with a 500.
There are no syntax errors in the file. If you want, I can fix the security issues directly next.
```

<br>

**Review:**

I asked AI to quickly identify any issues that the code may or may not have. I just wanted to get a quick view of potential problems, so that I could scan through and quickly determine what issues were relevant and which ones weren't. The AI listed potential issues and ranked them from highest to lowest priority. I had to re-prompt to clarify on areas where I wasn't 100% sure about. If I had to change my approach here - I would simply ask the AI to shorten each point so that I could read through them quickly.

## Prompt 2

**Prompt:** would you recommend using a try statement in case something goes wrong and we still want to return?


**Response:**

```
Yes, I would recommend it.

Best practice in a Flask route is:

Use try for work that can fail (DB writes, JSON parsing, external calls).
Use except to return a controlled response (for example 400 for bad input, 500 for internal failure).
Use finally to always close resources like DB connections.
If a transaction started, rollback inside except before returning.
The key is to catch expected failures intentionally, not to hide everything with a blanket except that swallows bugs. A good pattern is:

specific except blocks first (like JSON decode / sqlite errors),
one final generic except for unexpected errors (log + safe 500 response).
```

<br>

**Review:**

The code originally didn't return anything if something on the backend crashed. To make sure that I wasn't wrong here - I asked the agent if they would recommend using a try-block to return a response even if an exception/error happens. The AI responded with reasons to implement the backend functions with try-blocks that backed up my point. I didn't reprompt based on this output. If I had to change my approach, I would probably ask the AI to walk through a specific example of where a try-block would excel that the current code doesn't. 




