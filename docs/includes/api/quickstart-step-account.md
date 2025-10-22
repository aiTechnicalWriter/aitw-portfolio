## Step 2: Retrieve Account ID

Use a sample CIF (Customer Information File) number to look up a customer’s account:

```bash
curl -X GET "https://api.qbank.com/v2/accounts/{accountId}" \
  -H "Authorization: Bearer $QBANK_API_KEY"
```

> Expected response: JSON object with `accountId`, `accountType`, and `balance`.  
> 📸 *Insert screenshot showing account details*
