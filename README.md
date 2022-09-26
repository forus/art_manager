# Art Manager

The current REST api of the application does not have authorization mechanism configured. Without letting system know who you are any user can perform not just read, but creation, modification or removal of entitities via any REST endpoint of the system at the moment.
Your first task will be to fix the authorization mechanism as described below.

**NOTE:**
- **Authentication** (**AuthN**) is a process that verifies that someone or something is who they say they are. e.g. Employing password, passport scan, face recognition,...
- **Authorization** (**AuthZ**) is a process of giving users or services permission to access some data or perform a particular action. e.g. adding new work items, removing users

The system has preloaded example data that includes users and groups.