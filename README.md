## 📡 Social Network - A Twitter-like Social Network

Network is a Django-powered web application that mimics core features of Twitter, allowing users to create posts, follow others, like content, and manage social interactions—all within a dynamic and responsive interface.

## 🚀 Features

* User Authentication: Secure registration, login, and logout flows.
* Post Creation & Editing: Compose, edit, and publish text-based posts.
* All Posts Feed: View all posts in reverse chronological order with pagination.
* User Profiles: View user-specific post history and follower/following counts.
* Follow System: Follow or unfollow users directly from their profile page.
* Following Feed: View posts only from followed users.
* Likes: Like or unlike posts with real-time count updates via JavaScript.
* Pagination: 10 posts per page with navigation for older/newer content.
* AJAX-Powered UX: Dynamic interactions without full page reloads (e.g., editing posts, liking posts).

## 🛠️ Getting Started

### Installation

1. Clone or Download the Project
2. Apply Migrations
   bash```
   python manage.py makemigrations network
   python manage.py migrate
   ```
3. Run the Server
   bash```
   python manage.py runserver
   ```
4. Open in Browser
   Visit http://127.0.0.1:8000/ in your browser to register and start posting!

## 🧠 Key Implementation Notes

* Models:
  * User: Inherits from Django's AbstractUser.
  * Post: Stores content, author, timestamp, and likes.
  * Follow: Self-referential model linking users to their followers/following.
  * Like: Many-to-many mapping of users liking posts.

* Frontend:
  * Bootstrap for responsive layout.
  * Custom JavaScript for AJAX interactions (likes, edit posts).
  * Conditional rendering based on authentication status.

* Pagination:
  * Django’s Paginator class for backend pagination.
  * Bootstrap's pagination components on the frontend.

## 💡 Future Improvements

* Profile pictures and bio support.
* Notifications for likes/follows.
* Infinite scroll instead of pagination.
* REST API support for external client consumption.

## 📃 License

This project is part of Harvard's CS80 Web Programming course.
