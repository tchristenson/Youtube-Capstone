## <h1>YoohooTube</h1>

YoohooTube is a website clone, inspired by [Youtube](https://www.youtube.com/). YoohooTube can be used to post videos, comment on videos, create playlists of your favorite videos, like videos, and subscribe to other users on the platform. Interested parties can sign up to post content at their leisure.

**Live Site: [YoohooTube](https://yoohootube.onrender.com)**

### Please visit the links below to see the feature list, database schema and Youtube wireframes:
* [Feature List](https://github.com/tchristenson/Youtube-Capstone/wiki/MVP-Feature-List)
* [Database Schema](https://github.com/tchristenson/Youtube-Capstone/wiki/DB-Schema)
* [Wireframes](https://github.com/tchristenson/Youtube-Capstone/wiki/YouTube-Wireframes-(combined))

### How to start the project locally:
1. Clone the project repo into the desired location on your machine
2. Create a **.env** file based on the example with proper settings for your development environment
3. cd into the react-app directory and run the command below to install all dependencies
      ```bash
      npm install
      ```
4. Inside the root directory, run the following command:
      ```bash
      pipenv install -r requirements.txt
      ```
5. Still inside the root directory, run the commands below. Once executed, the database should be seeded and running:

      ```bash
      pipenv shell
      flask db init
      flask db migrate
      flask db upgrade
      flask seed all
      flask run
      ```

6. cd into the react-app directory and run the following command:
      ```bash
      npm start
      ```

7. Browse the site and enjoy

### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /api/auth | To authenticate a user |
| POST | /api/auth/login | To login an existing user account |
| GET | /api/auth/logout | To logout the current user |
| POST | /api/auth/signup | To create a new user and log them in |
| GET | /api/auth/unauthorized | To return unauthorized JSON when login authentication fails |
| GET | /api/users | Queries for all users and returns each user as an object inside an array |
| GET | /api/users/:userId | Queries for a single user and returns that user as an object |
| POST | /api/users/:targetUserId/subscribe/:currentUserId | Queries for a target user, and subscribes/unsubscribes the current user from the target user |
| POST | /api/videos/new | Allows a user to upload a new video |
| GET | /api/videos/:videoId | Queries for a single video and returns that video as an object |
| GET | /api/videos | Queries for all videos and returns each video as an object inside an array |
| PUT | /api/videos/:videoId/edit | Queries for a single video and applies the edits provided by the logged in user |
| DELETE | /api/videos/:videoId/delete | Queries for and deletes a single video if the owner of the video is the logged in user |
| POST | /api/videos/:videoId/likes/:userId | Queries for a video and user, and, if the user has not liked that video, adds the user's like. Otherwise, the user's like is removed from the video |
| POST | /api/videos/:videoId/playlists/new | Queries for a video and adds that video to the newly created user playlist |
| POST | /api/comments/new | Allows a user to add a comment to a video |
| GET | /api/comment/:videoId | Queries for all the comments belonging to a single video, and returns each comment as an object inside an array |
| DELETE | /api/comment/:commentId/delete | Queries for and deletes a single comment if the owner of the comment is the logged in user |
| PUT | /api/comments/:commentId/edit | Queries for a single comment and applies the edits provided by the logged in user |
| GET | /api/playlists/:playlistId | Retrieves a single playlist specified by ID |
| GET | /api/playlists | Queries for all playlists and returns each playlist as an object inside an array |
| PUT | /api/playlists/:playlistId/edit | Queries for a single playlist and applies the edits provided by the logged in user |
| DELETE | /api/playlists/:playlistId/delete | Queries for and deletes a single playlist if the owner of the playlist is the logged in user |

### Technologies Used:
* [Python](https://docs.python.org/3/)
* [JavaScript](https://devdocs.io/javascript/)
* [PostgreSQL](https://www.postgresql.org/docs/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [React](https://react.dev/)
* [Redux](https://redux.js.org/)

### Landing Page
You can access the landing page at the link below. You may create a new user account, or there is a demo user button for you to check out the website.

**Home Page: [YoohooTube](https://yoohootube.onrender.com)**

### Author
+ [Tommy Christenson](https://github.com/tchristenson)
