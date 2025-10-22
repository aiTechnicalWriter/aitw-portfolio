# Positive Pay Endpoint Overview

Positive Pay is a fraud-prevention service that allows account holders to share outgoing check details with their bank, so the bank can verify each check before clearing it. 

When an ERP Software Partner integrates their platform with the **Positive Pay Endpoints** in QBank Connect API (QAPI), they can provide positive pay service to their users - giving them automated, real-time control over their check verification workflows.

The Positive Pay Endpoints support the following use cases:

- Adding a Positive Pay

- Canceling a Positive Pay

- Updating Positive Pay Data

- Listing Positive Pays

- Finding Positive Pays Using a Filter

- Getting an Individual Positive Pay


## Adding a Positive Pay

Platform Users can add Positive Pay service to an outgoing check.

![A diagram showing the systems and interactions involved in adding a positive pay](assets/positivepay-add.png)

When a Partner Platform User requests Positive Pay service for a check:

1. The Partner Platform calls the **PositivePay/Add** endpoint with a POST request that contains the check information. 

2. The endpoint adds a record to the Positive Pay database and returns a confirmation reply to the Platform.

3. Every 15 minutes an automated **mETL Hub** job (**QAPI Process Positive Pay**) downloads any new Positive Pay records, generates a Positive Pay file, and moves the file to a Fiserv SFTP Location.

4. **Fiserv** processes the request.

## Canceling a Positive Pay

Platform Users can cancel a Positive Pay request.

![A diagram showing the systems and interactions involved in canceling a positive pay request](assets/positivepay-cancel.png)

When a Platform User requests to cancel a Positive Pay request:

1. The Platform calls the **PositivePay/Add** endpoint with a POST request that contains a **VOID** entry with the relevant check's information. 

2. The endpoint adds a VOID record to the Positive Pay database and returns a confirmation reply to the Platform.

3. Every 15 minutes an automated **mETL Hub** job (**QAPI Process Positive Pay**) downloads any new Positive Pay records, generates a Positive Pay file, and moves the file to a Fiserv SFTP Location.

4. **Fiserv** processes the VOID request, canceling the Positive Pay request for the relevant check.

## Updating Positive Pay Data

The **Positive Pay Database** is updated every 24 hours in QBank's Nightly Process. 

![A diagram showing the systems and interactions involved in updating Positive Pay data](assets/positivepay-data.png)

In the night after each business day, at 1:00 am, an automated **mETL Hub** job (**QAPI Import Fiserv Data**) imports the day's data from Fiserv and updates the QAPI databases.

This includes all records of Fiserv's Positive Pay processing. 

Once the Positive Pay Database is updated, Platform Users have visibility to their Positive Pay activity from the previous day.

## Listing Positive Pays

Platform Users can get a list of Positive Pay records from the previous day.

![A diagram showing the systems and interactions involved in listing Positive Pays](assets/positivepay-list.png)

When a User requests a list of Positive Pay records:

1. The Platform calls the **PositivePay/List** endpoint with a GET request.

2. The endpoint retrieves the records from the previous day and returns the list to the Platform.

## Finding Positive Pays Using a Filter

Platform Users can use a filter to find Positive Pay records that match specified parameters.

![A diagram showing the systems and interactions involved in Finding Positive Pays Using a Filter](assets/positivepay-find.png)

When a User requests records that match a set of parameters, such as a Date, Date Range, or Account #:

1. The Platform calls the **PositivePay/Find** endpoint with a POST request that contains the parameters.

2. The endpoint retrieves the matching records and returns them to the Platform.

## Getting an Individual Positive Pay

Platform Users can retrieve individual Positive Pay records.

![A diagram showing the systems and interactions involved in Getting an Individual Positive Pay](assets/positivepay-get.png)

When a User requests a record with a specific PositivePay ID #:

1. The Platform calls the **PositivePay/ID/{ID}** endpoint with a GET request that contains the ID #.

2. The endpoint retrieves the specified record and returns it to the Platform.

## Related Documents

**Related Custom Applications:**

- QBank Connect API

- mETL Hub (Automation Engine)

**Related ETL Jobs:**

- QAPI Process Positive Pay

- QAPI Import Fiserv Data

**Related Third-Party Applications & Integrations:**

- Fiserv

- Fiserv Positive Pay Loader

- Fiserv Extract

**Related Business Units:**

- TM (Treasury Management)