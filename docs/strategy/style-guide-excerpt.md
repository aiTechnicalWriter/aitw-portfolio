# Qbank Application Documentation Style Guide (Excerpt)
This document provides standards for creating clear, consistent, and helpful documentation for Qbank products.

## Voice and Tone
Our voice is who we are; our tone is how we express it in different situations.

### Our Voice
Our documentation voice is _confident, knowledgeable, and approachable_. We are experts in our field, but we are not arrogant. We write with clarity and precision, reflecting the trust our customers place in us.

#### Use active voice
> **Good:** "You must provide an API key."
> **Bad:** "An API key must be provided."

#### Address the user as "you"
> **Good:** "You will see a successful response."
> **Bad:** "The user will see a successful response."

### Our Tone
Our documentation tone is professional, direct, and helpful. The tone adapts to the context of different document types:

#### Tutorials and how-to guides
Be encouraging and straightforward. Guide them through the process as a helpful partner. For example:
> "You can get your API keys from the developer portal."

#### Reference and architectural documents
Be more formal and descriptive. Focus on accuracy and objective explanation. For example:
> "The service authenticates requests using a bearer token."

#### Troubleshooting guides
Be empathetic and solution-oriented. Acknowledge the user's frustration and guide them directly to a solution. Avoid blaming the user.
> **Good:** "Couldn't connect to the database. Check if the database is running and the connection string is correct."
> **Bad:** "You entered the wrong database credentials."

#### Error Messages
Every error message should answer three questions:
- What happened? (The problem)
- Why did it happen? (The cause)
- What can I do about it? (The solution)

For example:
> **Error:** Unable to Save Changes
> **Cause:** Your session has expired due to inactivity.
> **Solution:** Please log in again to continue editing. Unsaved changes may be lost if not recovered promptly.

#### API Error Responses
Document all NexusGateway API errors in the OpenAPI specification, using a standardized Error schema. For example:
>  **Message**:  Authentication token is missing or invalid.
>  **Cause**: The request was made without a valid Authorization header containing a bearer token, or the provided token has expired or is malformed.
>  **Solution**: Ensure you are including the Authorization: Bearer <YOUR_TOKEN> header in your request. If the token has expired, request a new one from the /oauth/token endpoint. Verify that you are copying the entire token string.