Converting skins to views:
==========================

[x] ISiteRoot @@login.html:
---------------------------
- [x] login_form.pt -> LoginFormView
                       login.pt

[x] ISiteRoot @@logged_in.html:
-------------------------------
- [x] logged_in.py -> LoggedInView
- [x] logged_in_template.pt -> logged_in.pt

[x] ISiteRoot @@logout.html:
----------------------------
- [x] logout.py -> LogoutView
- [x] logged_out.pt -> logged_out.pt

[x] ISiteRoot @@mail_password.html:
-----------------------------------
- [x] mail_password_form.pt -> mail_password.pt
- [x] mail_password.py -> MailPasswordFormView
- [x] mail_password_response.pt -> MailPasswordFormView

[x] ISiteRoot @@join.html:
--------------------------
- [x] join_form.py,
- [x] validatePassword.py,
- [x] members_add_control.py -> JoinFormView
- [x] join_template.pt -> join.pt

[x] ISiteRoot @@preferences.html:
---------------------------------
- [x] personalize_form.pt -> formlib based
- [x] personalize.py -> PreferencesFormView

[x] ISiteRoot @@password.html:
------------------------------
- [x] password_form.py,
- [x] change_password.py -> PasswordFormView
- [x] password_form_template.pt -> formlib based

[x] ISiteRoot @@members.html:
-----------------------------
- [x] members_manage_form.py,
- [x] validateMemberIds.py -> members.Manage
- [x] members_manage_template.pt -> members.pt

- [x] members_delete_form.py,
- [x] members_delete_control.py -> members.Manage
- [x] members_delete_template.pt -> members_delete.pt

[x] IFolderish @@roster:
------------------------
- [x] roster.pt -> members.Roster
                   members_list.pt

[x] IRegistrationTool @@registered_email:
-----------------------------------------
- [x] registered_email.py -> notify.RegisteredEmail
- [x] registered_email_template.pt -> notify_registered.pt

[x] IRegistrationTool @@password_email:
---------------------------------------
- [x] password_email.py -> notify.PasswordEmail
- [x] password_email_template.pt -> notify_password.pt
