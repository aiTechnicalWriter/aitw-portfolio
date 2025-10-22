# Qbank Core Internal User Guide

Tutorial: Getting Started with a Customer Lookup
Goal: To perform your first successful customer lookup in the Qbank Core application. This tutorial will build muscle memory and introduce the core workflow.

Log in to the Qbank Core application using your credentials.

On the dashboard, locate the "Customer Search" field in the top-right corner.

Enter the sample CIF 1234567 and press Enter.

The system will load the customer profile. You should see a new tab titled "Jane Doe" appear. This indicates a successful lookup.

<<INSERT SCREENSHOT HERE: A clean screenshot of the Qbank Core application UI showing the customer search field and the successfully loaded customer profile page with the name 'Jane Doe' in the tab.>>

How-To Guide: How to Correct a Transaction Error
Problem: A transaction was posted incorrectly, and a customer needs a credit.
Solution: Follow these steps to post a corrected transaction.

Locate the customer's account using a customer lookup.

Navigate to the "Transactions" tab.

Click the + New Transaction button.

In the pop-up window, select the transaction type "Manual Credit."

Enter the correct amount.

<<INSERT SCREENSHOT HERE: A screenshot of the pop-up window showing the 'Manual Credit' transaction type selected. The Amount field should be highlighted.>>

Add a note in the "Comments" field. For a transaction correction, use the format: CORRECTION: <reason for correction>.

Click Submit. The corrected transaction will appear in the transaction list with a "Pending" status.

Explanation: The Qbank Transaction Lifecycle
The Qbank Core application processes transactions through a complex, multi-stage lifecycle. Understanding this process is key to resolving customer issues. This explanation provides a high-level overview of the why behind the process.

<<INSERT DIAGRAM HERE: A flowchart or state diagram showing the transaction lifecycle. It will show states such as Initiated, Pending Validation, Authorized, Posted, and Reversed, with arrows showing the flow between them. A note about the Legacy Mainframe System handling validation will be included.>>

Reference: Qbank Core Field Definitions
This section is a factual list of all fields and their definitions within the application's UI, intended for quick look-up.

