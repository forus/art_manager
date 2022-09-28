# Art Manager

## 1. Fix Authorization

The current REST api of the application does not have authorization mechanism configured. Without letting system know who you are any user can perform not just read, but creation, modification or removal of entitities via any REST endpoint of the system at the moment.
Your first task will be to fix the authorization mechanism as described below.

**NOTE:**
- **Authentication** (**AuthN**) is a process that verifies that someone or something is who they say they are. e.g. Employing password, passport scan, face recognition,...
- **Authorization** (**AuthZ**) is a process of giving users or services permission to access some data or perform a particular action. e.g. adding new work items, removing users

The system has preloaded example data that includes users and groups.
*If you are curious how uploading of the data is done, you can find the code in one of the db bigrations [here](./inventory/migrations/0006_load_example_data.py).*

Here is the list of users preloaded to the system.

| username | password | group | admin |
| --- | --- | --- | --- |
| `admin` | `admin!12345` | | Yes |
| `janneke` | `janneke!12345` | `municipality_workers` | No |
| `jeroen` | `jeroen!12345` | `municipality_workers` | No |
| `sjoerd` | `sjoerd!12345` | `art_managers` | No |

Here are groups and what users that belong to them allowed do on model entities:

| group | `Building` | `Spots` | `ArtItems` | `ArtLocation` | `ArtBorrowingRequest` |
| --- | --- | --- | --- | --- | --- |
| `municipality_workers` | `view` | `view` | `view` | `view` | `view` + `add` |
| `art_managers` | `view` + `add` + `change` + `delete` | `view` + `add` + `change` + `delete` | `view` + `add` + `change` + `delete` | `view` + `add` + `change` + `delete` | `view` + `delete` |

As admin user (having `is_staff=True`) you don't have limits on what you can do using the admin panel.

Note that being part of the art managers group gives you permissions for viewing and deleting the art borrowing request only. And as the municipality worker you can view and add one. We want to add a possibility to a municipality worker to remove the requests he/she created further on in the tutorial using employing object level permissions.

### 1.1. Start the application

Go to project folder and create the database:

```
  python manage.py migrate
```

Start the application:

```
  python manage.py runserver
```

## 1.2. Investigating application from the browser

Go to http://localhost:8000/admin and use the admin credentials from the above table to login to the admin panel. Scan the preloaded data.

Log out to become Anonymous again.

Go to http://localhost:8000/inventory/api/. Explore the endpoints and all operations UI gives you opportunity to do. As you see public user can do everything he/she wants with the data via the api. We don't employ the model permissions mentioned above yet.

*NOTE:* If you changed the data and want to start over you can achieve that by stopping the server, removing the database file (`db.sqlite3`) and starting server again.

## 1.3. Test permissions

There are automatic test that check permissions for the endpoints given different users.
**Check the code [here](./inventory/tests.py)**

You can run those test with:

```
python manage.py test
```

As you see most of them are failing. After fixing the authrorization all of them has to pass. You can the above testing command iteratively, after each change, to see whether you've impoved the code towards the goal.

## 1.4. First assignment. Setting the correct permission policy

The permission policy can be set globally (in `settings.py`) or for each APIView/ViewSet.
Read more on this [here](https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy).
Django REST framework comes with multiple permission classes. Read about them [here](https://www.django-rest-framework.org/api-guide/permissions/#api-reference) and set the correct one for your application to fix the authorization for the app according with the model permissions.

All tests have to pass after you'll set the correct policy.

## 1.5. Second assignment. Object level permissions (ADVANCED)

The second assignment requires you to write a custom policy that defines permissions for each object, not for the whole class of objects as we had before.

As we mentioned before a municipality worker can't remove his own art borrowing requests at the moment. The goal of this is to change this.

Start with reading [the documentation on object level permissions](https://www.django-rest-framework.org/api-guide/permissions/#object-level-permissions).

Check [the tests](./inventory/tests.py). There are two tests that are skipped. It's `test_delete_art_borrowing_request_as_municipality_worker` and `test_delete_art_borrowing_request_as_another_municipality_worker`. Remove `@unittest.skip` line and run all tests. You will see those tests failing. After implementing the object level permissions correctly they have to pass.

Check examples of custom permission definition [here](https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions).