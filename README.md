# Departmetal Employee Management
Super admin panel view
Will have following sections or menu links:
Manage Manager – The super admin can add and edit the details of
the manager.
Fields: Full Name, profile picture, contact number, email address,
username, manual password text field (with view/hide password icon)
with Generate Password button. On clicking the Generate Password
button random password will be generated in the same password field
(password should have minimum 8 characters)

Manage Coordinator – The super admin can add and edit the details
of the coordinator.
Fields: Full Name, profile picture, contact number, email address,
username, manual password text field (with view/hide password icon)
with Generate Password button. On clicking the Generate Password
button random password will be generated in the same password field
(password should have minimum 8 characters)

Manage Inspectors – The coordinator / super admin can add and edit
the details of the inspector.
Fields: Full Name, profile picture, contact number, email address,
username, manual password text field (with view/hide password icon)
with Generate Password button. On clicking the Generate Password
button random password will be generated in the same password field
(password should have minimum 8 characters)

Login: By default, super admin must first login to gain access to the
admin panel (default username and password should be set for super
admin).
Logout: super admin has the ability to logout out of the admin panel
Coordinator admin panel view
Will have following sections or menu links:
1. Inspector Master: Coordinator can add or edit inspectors from
here.
Fields: Full Name, Profile picture, contact number, email address,
username, randomly generated password with minimum 8 characters
2. Client Master: Show table with columns SL No, Client Name,
Location (Show few dummy records)
3. Job Master: Coordinator can add jobs and assign them to
inspector from here.
Fields: Dropdown Select Client (Show data from Client Master),
Dropdown Select Location (should load respective location of
Client added from Client Master), Date time picker (label: Schedule
Date Time), Dropdown Select Inspector (show data from Inspector
Master)
4. Profile: Show profile details of Coordinator
5. Logout


Notification :A notification should be shown in super admin panel when
coordinator adds an inspector from inspector master or creates a job
from job master. The admin panel should be designed using bootstrap
or any other front-end framework of your choice. Proper pagination and
validation should be implemented in Inspector Master, Job Master and
Client master. Packages should work properly both in windows and
Linux.
