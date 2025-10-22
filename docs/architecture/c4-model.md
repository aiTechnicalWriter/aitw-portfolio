Architectural Overview: The Qbank System (C4 Model)
This document provides a conceptual overview of the Qbank software architecture using the C4 model. The C4 model is a visual and structured approach to documenting software architecture that simplifies complex systems into a clear, hierarchical set of diagrams. This approach makes the architecture accessible to both technical and non-technical stakeholders by allowing them to "zoom in" to different levels of detail as needed.   

The Four Levels of the C4 Model
The C4 model is based on four core levels of abstraction: Context, Container, Component, and Code. Each level provides a different view of the system, tailored to a specific audience and purpose.   

Level 1: System Context Diagram
A System Context diagram provides a high-level, "bird's eye view" of the system.   

Purpose: To show how the system fits into its environment and how it interacts with external entities. It helps stakeholders understand the overall scope of the project and the problem it solves.   

Audience: Intended for anyone who needs a general understanding of the system, including both technical and non-technical audiences like business stakeholders, product managers, and developers.   

Scope: Focuses on the system as a single entity, its users (Person), and other systems it interacts with (System). The internal details of the system are not shown at this level.   

<<INSERT MERMAID DIAGRAM HERE: A simple context diagram with boxes for 'Retail Customer', 'Operations Analyst', 'Third-Party Fraud Detection Service', 'Qbank Connect API', and 'Legacy Mainframe System'. Arrows will show the high-level flow of information between them, with a note that the Qbank Connect API is the system under discussion.>>

Level 2: Container Diagram
A Container diagram zooms into a single system to reveal its main, independently deployable and runnable parts.   

Purpose: To show how the system is deployed and how its major parts communicate. It provides a more technical view for architects and developers.   

Audience: Primarily for technical audiences such as architects and developers, as it includes details on technology choices and communication protocols.

Scope: The scope includes the users, external systems, and the containers that make up the system being diagrammed. It explicitly notes technologies used (e.g.,    

Java, Kubernetes, JSON/HTTPS).   

<<INSERT LUCIDCHART/FIGMA DIAGRAM HERE: A more detailed diagram showing the containers of Qbank Connect and their interactions, with technology notes (e.g., Java, Kubernetes, JSON over HTTPS). This will be a professionally rendered, complex diagram that explicitly shows connections to Legacy Mainframe and Legacy Payment Gateway containers.>>

Level 3: Component Diagram
A Component diagram provides a detailed view of a single container, breaking it down into its internal software components.

Purpose: To illustrate the structural building blocks within a container, their responsibilities, and their interactions. It is especially useful for developers working on specific parts of the system.   

Audience: Geared toward a low-level technical audience, specifically architects and developers.   

Scope: The scope includes users, external systems, containers, and the components within the container being detailed. This is where the documentation would show the    

LegacyAdapter component translating modern API requests into the legacy system's format.

<<INSERT DIAGRAM HERE: A component diagram for the Customer Profile Microservice container. It should show the internal components like AuthModule, CustomerDataController, and LegacyAdapter, and their relationships. The LegacyAdapter should have a clear connection to the external Legacy Mainframe System box.>>

Level 4: Code Diagram
A Code diagram is the lowest level of abstraction in the C4 model, focusing on the implementation details of a single component.   

Purpose: To detail the internal structure of a component, often using a UML class diagram, and how it is implemented in code. This level is typically auto-generated from the source code.   

Audience: This is a very technical view, intended for a low-level audience of architects and developers who need to understand the codebase.   

Scope: The scope includes users, systems, containers, and the specific components and classes being documented. It is the level least frequently used due to its high level of detail.   

<<INSERT DIAGRAM HERE: A UML class diagram for the LegacyAdapter component. It should show a few key classes and their methods, such as MainframeClient, RequestTranslator, and ResponseParser, illustrating the data structures and methods used to communicate with the Legacy Mainframe System.>>

I have now provided the full content for the Architectural Overview, organized in a way that is ready for DITA XML authoring. Please let me know when you are ready for the next document.




===

# ALT TEXT

Architectural Overview: The Qbank System (C4 Model)
This document provides a visual overview of the Qbank software ecosystem using the C4 model. This model helps us to describe a complex system at different levels of abstraction, making the architecture accessible to both technical and non-technical audiences.

Level 1: System Context Diagram
The System Context diagram is a high-level view that shows the Qbank ecosystem as a single system and how it interacts with its users and external systems. It answers the question, "How does the system fit into its environment?".

<<INSERT MERMAID DIAGRAM HERE: A simple context diagram with boxes for 'Retail Customer', 'Operations Analyst', 'Third-Party Fraud Detection Service', 'Qbank Connect API', and 'Legacy Mainframe System'. Arrows will show the high-level flow of information between them, with a note that the Qbank Connect API is the system under discussion.>>

Level 2: Container Diagram
The Container diagram zooms into the system to show the main, high-level building blocks or containers. This view is intended for a technical audience, as it shows how the system is deployed and the technologies used for communication.

<<INSERT LUCIDCHART/FIGMA DIAGRAM HERE: A more detailed diagram showing the containers of Qbank Connect and their interactions, with technology notes (e.g., Java, Kubernetes, JSON over HTTPS). This will be a professionally rendered, complex diagram that explicitly shows connections to Legacy Mainframe and Legacy Payment Gateway containers.>>

Level 3: Component Diagram
The Component diagram is a more detailed view that zooms into a single container to show the software components within it. This level is for a low-level technical audience, primarily architects and developers. It breaks down the structural building blocks of a container, detailing each component's responsibilities and how it interacts with other components. For our fictional system, we will use the 

Customer Profile Microservice as the container to document.

This diagram would show the internal components of the microservice, such as:

AuthModule: A component responsible for validating the incoming API key.

CustomerDataController: Handles the business logic for retrieving and updating customer data.

LegacyAdapter: A critical component that translates modern API requests into a format the Legacy Mainframe System can understand, demonstrating the system's need to bridge old and new technologies.

<<INSERT DIAGRAM HERE: A component diagram for the Customer Profile Microservice container. It should show the internal components like AuthModule, CustomerDataController, and LegacyAdapter, and their relationships. The LegacyAdapter should have a clear connection to the external Legacy Mainframe System box.>>

Level 4: Code Diagram
The Code diagram represents the lowest level of abstraction in the C4 model, focusing on the implementation details of a single component. This level is typically represented by UML class diagrams and is often auto-generated directly from the source code. Because of its high level of detail, it is the level that is least frequently used.

For our portfolio, we would create a Code diagram that zooms into a specific component from Level 3, such as the LegacyAdapter. This diagram would show the major classes, interfaces, and their relationships, providing an in-depth view of how the component is implemented and how it interacts with the legacy system's protocol. This would demonstrate an understanding of code-level documentation and the ability to work closely with engineering teams on implementation details.

<<INSERT DIAGRAM HERE: A UML class diagram for the LegacyAdapter component. It should show a few key classes and their methods, such as MainframeClient, RequestTranslator, and ResponseParser, illustrating the data structures and methods used to communicate with the Legacy Mainframe System.>>


===

# ALT TEXT

LoanSphere Platform Architecture
This document provides a high-level architectural overview of the LoanSphere platform using the C4 model for visualizing software architecture. It is intended for software developers, architects, and technical project managers at Qbank.

Level 1: System Context
The System Context diagram shows how the LoanSphere Platform fits into the broader Qbank IT ecosystem. It shows the key systems it interacts with and the user groups who use it.

<<INSERT DIAGRAM HERE: A C4 System Context diagram. It should show a central box for the "LoanSphere Platform". Arrows should connect it to the following:

A "Loan Officer" (Persona) using the system.

The "Qbank NexusGateway API" (System), which LoanSphere calls to get customer data and push loan decisions.

The "Qbank CoreConnect Mainframe" (System), showing a dotted-line relationship via the NexusGateway.

An "Email Service" (System) for sending notifications to customers.

A "Credit Bureau API" (External System) for pulling credit reports.>>

Key Interactions:
Loan Officers use the LoanSphere Platform to manage the entire loan application and approval workflow.

The platform fetches customer account and history data from the NexusGateway API, which acts as a facade for both modern services and the legacy CoreConnect Mainframe.

It calls external Credit Bureau APIs to pull applicant credit scores and history.

It uses an internal Email Service to send status updates to customers.

Approved loan data is pushed back through the NexusGateway API to update the customer's profile in the core banking systems.

Level 2: Containers
The Container diagram zooms into the LoanSphere Platform itself, showing the high-level technical building blocks (the "containers" in C4 terminology).

<<INSERT DIAGRAM HERE: A C4 Container diagram. It should have a boundary labeled "LoanSphere Platform". Inside the boundary, show the following containers (boxes):

Single-Page Application (SPA): (Technology: React) The user interface running in the Loan Officer's browser.

Loan Workflow Service: (Technology: Java/Spring Boot) A REST API that manages the business logic of the loan application lifecycle.

Document Management Service: (Technology: Python/Django) A REST API responsible for uploading and storing applicant documents (e.g., pay stubs).

Database: (Technology: PostgreSQL) Stores all data related to loan applications, statuses, and user actions.

File Storage: (Technology: AWS S3) Blob storage for the actual document files.

Show arrows indicating the primary interactions:

The SPA communicates with the Loan Workflow Service and the Document Management Service.

The Loan Workflow Service reads/writes to the Database and calls the Document Management Service.

The Document Management Service reads/writes to the Database and stores files in the File Storage.

Both services make outbound calls to the external systems defined in the Level 1 diagram (NexusGateway, Credit Bureau, etc.).>>

Container Descriptions:
Single-Page Application (SPA): A React-based frontend that provides the user interface for Loan Officers. It is a pure client-side application that communicates with the backend services via REST APIs.

Loan Workflow Service: The core of the platform. This Java-based microservice contains the business logic for processing loan applications, managing state transitions (e.g., 'submitted' -> 'under review' -> 'approved'), and orchestrating calls to other services.

Document Management Service: A dedicated Python microservice for handling file uploads. This isolates the concerns of file processing and storage, allowing it to be scaled independently.

Database: A relational PostgreSQL database that serves as the single source of truth for all loan application data.

File Storage: Uses AWS S3 for durable, secure storage of sensitive customer documents, separating large binary files from the primary database.

This container-based architecture allows for independent development, deployment, and scaling of the different components of the LoanSphere platform.