# User Stories

## Users

### Sign Up

* As an unregistered and unauthorized user, I want to be able to sign up for the website via a sign-up form.
  * When I'm on the `/signup` page:
    * I would like to be able to enter my email, username, and preferred password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the sign-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the sign-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
    * So that I can try again without needing to refill forms I entered valid data into.

### Log in

* As a registered and unauthorized user, I want to be able to log in to the website via a log-in form.
  * When I'm on the `/login` page:
    * I would like to be able to enter my email and password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the lob-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the log-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
      * So that I can try again without needing to refill forms I entered valid data into.

### Demo User

* As an unregistered and unauthorized user, I would like an easy to find and clear button on both the `/signup` and `/login` pages to allow me to visit the site as a guest without signing up or logging in.
  * When I'm on either the `/signup` or `/login` pages:
    * I can click on a Demo User button to log me in and allow me access as a normal user.
      * So that I can test the site's features and functionality without needing to stop and enter credentials.

### Log Out

* As a logged in user, I want to log out via an easy to find log out button on the navigation bar.
  * While on any page of the site:
    * I can log out of my account and be redirected to the home page excluding all non-user specific video recommendations, playlists, etc.
      * So that I can easily log out to keep my information secure.

## Videos

### Upload Videos

* As a logged in user, I want to upload videos.
  * When I'm on the `/new-videos` page:
    * I can upload and submit a new video and give it a name.

### Viewing Videos

* As a logged in _or_ logged out user, I want to be able to view a selection of all the videos.
  * When I'm on the `/` page:
    * I can view the most recently posted videos and videos by sub-categories.

* As a logged in _or_ logged out user, I want to be able to view a specific video and its associated comments and likes.
  * When I'm on the `/videos/:id` page:
    * I can view the content of the video, as well as the associated comments and likes.

### Updating Videos

* As a logged in user, I want to be able to edit my videos by clicking an Edit button associated with the video at the `/videos/:id` page.

### Deleting Videos

* As a logged in user, I want to be able to delete my videos by clicking a Delete button associated with the video at the `/videos/:id` page.

## Comments

### Write Comments

* As a logged in user, I want to be able to write comments underneath the videos on the `/videos/:id` page.

### Viewing Comments

* As a logged in _or_ logged out user, I want to be able to view all comments on the `/videos/:id` page.

### Updating Comments

* As a logged in user, I want to be able to edit my comments on a specific video by clicking an Edit button associated with the comment at the `/videos/:id` page.

### Deleting Comments

* As a logged in user, I want to be able to delete my comments on a specific video by clicking a Delete button associated with the comment at the `/videos/:id` page.
