Explainer: The InsightEngine Fraud Detection Model
This document provides a conceptual overview of the machine learning model used by the InsightEngine platform to detect potentially fraudulent transactions. It is intended for product managers, developers, and data analysts who need to understand what the model does and how to interpret its output.

This is not a deep dive into the mathematical implementation.

What is the Goal of the Model?
The primary goal of the Fraud Detection Model is to assign a risk score to every financial transaction in near real-time. This score, ranging from 0 to 100, represents the model's calculated probability that a given transaction is fraudulent.

The model helps Qbank to:

Automatically block high-risk transactions.

Flag moderate-risk transactions for review by a human analyst.

Reduce financial losses due to fraud while minimizing the number of legitimate transactions that are incorrectly declined (false positives).

How Does the Model Work?
The model is a gradient boosting classifier that has been trained on millions of historical Qbank transactions (both legitimate and fraudulent). It analyzes incoming transactions by looking at a wide range of features, or data points, to identify patterns that are similar to past fraudulent activity.

Key Input Features
The model doesn't just look at the transaction amount. It considers a rich set of contextual data, including:

Transaction Features:

Amount

Time of day

Merchant category (e.g., online retail, travel, groceries)

Customer Historical Features:

Average transaction amount for this customer.

Frequency of transactions (e.g., is this the 10th transaction in an hour?).

Types of merchants the customer usually shops at.

Geographical Features:

Is the transaction location far from the customer's home address?

Has the customer's card been used in multiple countries in a short period?

Session Features (for online transactions):

IP address location.

Time since the customer's last transaction.

<<INSERT DIAGRAM HERE: A simple flowchart diagram.

On the left, a box labeled "New Transaction Data" with bullet points of the features listed above (Amount, Time, Location, etc.).

An arrow points to the middle box labeled "InsightEngine Fraud Model".

An arrow points from the middle box to a box on the right labeled "Output: Fraud Score (0-100)".>>

Interpreting the Output: The Fraud Score
The model's output is a single number: the fraud score.

Score 0-40 (Low Risk): The transaction has characteristics of typical, everyday user behavior. Action: Automatically approved.

Score 41-75 (Medium Risk): The transaction has some unusual characteristics but isn't definitively fraudulent. It might be a legitimate but atypical purchase (e.g., a large, one-time purchase while on vacation). Action: Automatically approved, but flagged for logging and potential later review.

Score 76-90 (High Risk): The transaction exhibits several strong indicators of fraud. Action: Automatically declined, and a notification is sent to the customer.

Score 91-100 (Critical Risk): The transaction patterns are highly consistent with known fraud tactics. Action: Automatically declined, the account is temporarily locked, and a fraud alert is created for immediate human investigation.

Important Consideration: This is a Probabilistic System
The model is highly accurate, but it is not perfect. It is possible for a legitimate transaction to receive a high score (a "false positive"). The scoring thresholds above are continuously tuned by our data science team to strike the right balance between security and customer convenience.