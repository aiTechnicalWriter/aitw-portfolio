# Software Development Lifecycle (SDLC)

## Overview
The Software Development Lifecycle (SDLC) defines the structured process by which the QBank AppDev Team plans, designs, builds, tests, and deploys custom software applications. The SDLC provides a phased framework that ensures the software is developed efficiently and meets the standards defined in the QBank Application Development Policy.

## Audience
Application Development Team

## SDLC Process
The SDLC framework consists of the following phases:
1. Initiation
2. Requirements
3. Design
4. Development
5. Testing
6. Deployment

The diagram below provides a visual summary of the SDLC process.

[View SDLC Diagram PDF](assets/sdlc-diagram.pdf)
![A workflow diagram of the SDLC process](assets/sdlc-diagram.jpeg "SDLC Diagram")

### PHASE ONE: Initiation
**Objective:** Surface, prioritize, and convert product ideas into a tracked story.

The Product Team maintains a Backlog of ideas collected from users and stakeholders. In the Initiation Phase, the team selects a set of ideas to be developed. For each idea selected, the Product Owner drafts a brief story describing the proposed functionality. The system sets newly created stories to REQ status and automatically assigns the story to the author. The REQ status marks the transition to the Requirements Phase.

### PHASE TWO: Requirements
**Objective:** Turn a prioritized idea into a complete story.

The Product Owner gathers detailed requirements and completes the story — the formal description of what is to be developed. The story includes the following:
- Acceptance Criteria — concrete, testable statements that define when the feature will be considered complete. 
- Nonfunctional requirements regarding any special performance, security, and compliance needs.
- Flags for any risk assessments needed, such as architectural or security review. 

When the story is complete, the Product Owner assigns the story to a Developer on the Software Engineering Team and moves the story to DESIGN status.

### PHASE THREE: Design
**Objective:** Define a producible technical solution.

The Developer designs a technical solution and assigns the story to the Dev Lead to review the design against security, compliance, and scalability standards. The Dev Lead has two choices:
- Reject the design, describe the improvements needed, and assign the story back to the Developer.
- Approve the design, assign the story back to the Developer, and move the story to DEV status.

### PHASE FOUR: Development
**Objective:** Implement the design as executable code.

The Developer codes the solution and verifies its functionality locally. When ready, the Developer assigns the Story to a Code Reviewer to review the code against coding standards, and verify the completeness of required artifacts (unit tests, linters green, and architecture notes). The Code Reviewer has two choices:
- Reject the coded solution, describe the improvements needed, and assign the story back to the Developer.
- Approve the coded solution, assign the story to a QA (Quality Assurance) Tester, and move the Story to QA status.

### PHASE FIVE: Testing
**Objective:** Verify the functionality against the story’s Acceptance Criteria.

The QA Tester runs test cases derived from the Acceptance Criteria and exploratory tests focused on regression, edge cases, and nonfunctional concerns as needed. The QA Tester has two choices:
- Reject the solution, document the failures, move the story back to DEV status, and assign it back to the Developer to re-code.
- Approve the solution and assign it to the User Acceptance Group for UAT (User Acceptance Testing)

The UAT Tester executes user-focused testing scenarios, and then has two choices:
- Reject the solution, document the user-facing issues, move the story back to DEV status, and assign it back to the Developer to re-code.
- Accept the solution, move the story to DEPLOY status, and assign it to the Product Owner.

### PHASE SIX: Deployment
**Objective:** Obtain release approval and move validated code into Production.

When a Story reaches DEPLOY status, the Product Owner requests release approval from the Change Advisory Board (CAB). After CAB approval, the Software Engineering and QA teams jointly execute the deployment to the PRODUCTION environment, and QA moves the story into DONE status. 

## Post-Deployment
After a deployment is complete, the software's lifecycle continues with a retrospective meeting, the Maintenance phase, and eventual retirement.

### Retrospective
A post-deployment retrospective is a meeting held shortly after a deployment to review the development and release process. The goal is to identify what went well, what could be improved, and create actionable steps for future iterations. This practice drives a culture of continuous improvement.

### Maintenance
After a successful deployment, the software enters the longest phase of its lifecycle: maintenance. During this stage, the focus shifts from new feature development to ensuring the software's continued operation, security, and relevance.

### Retirement
The retirement, or "sunsetting," phase marks the official end of the software's life cycle. This happens when the software is no longer needed, becomes obsolete, or is replaced by a newer system. A controlled retirement process minimizes disruption to the business and its users.

## Roles and Responsibilities
The following details the duties associated with each role in the project, to ensure clarity and accountability.

### Product Owner
Backlog prioritization, drafting Stories, collecting requirements, defining Acceptance Criteria, requesting CAB approval.

### Developer
Designing and coding solutions, re-coding as needed. 

### Dev Lead
Design Review and approval authority.

### Code Reviewer
Ensure code quality and adherence to standards before QA.

### QA Tester
Validate functionality against Acceptance Criteria and report defects.

### UAT Tester
Validate the feature from an end-user perspective and approve for deployment.

### Change Advisory Board
Grant release approval for production deployment.

## Hotfixes and Emergency Deployments
When addressing hotfixes and emergency deployments, the standard Software Development Life Cycle (SDLC) is bypassed to allow for rapid production releases to mitigate critical issues. Unlike a normal release, these deployments do not follow the full, multi-staged testing and approval process. A hotfix is a focused patch created directly from the stable production branch to correct a specific, high-priority defect, such as a security vulnerability or system-wide crash. An emergency deployment, conversely, may be used for a temporary, reactive fix when a rollback is not feasible or to restore a known good state immediately. In both cases, the priority shifts from a comprehensive SDLC to minimizing downtime and restoring service stability, with documentation and full integration testing performed retroactively once the immediate incident is resolved.

## Related Documents
- Application Development Policy
### Requirements
- Story Template
- Acceptance Criteria Guidelines
- Software Risk Assessment Checklist
### Design
- Software Design Template
- Design Review Checklist
### Development
- Coding Standards
- Code Review Checklist
### Testing
- QA Test Plan Template
- UAT Script Template
### Deployment
- CAB Procedure
- Deployment Runbook
- Rollback Procedure
- Deployment Checklist
### Post-Deployment
- Retrospective Agenda Template
- Operations Manual Template
- Deprecation and Retirement Procedure