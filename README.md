# The Midnight Times | JSE

## Objective
The objective of The Midnight Times project is to build a customer-facing web-based application where users can search for news articles from around the world based on the entered keyword. Additionally, it provides a web portal for users to view the results of their previous searches. This project utilizes the [News API](https://newsapi.org/) to fetch live news and blog articles.

## Here is the video demonstration 

[![Watch the video](https://img.youtube.com/vi/jTaA61uWRdM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jTaA61uWRdM)

## Register Page 
Both user and Admin can register from this page and create an account and they can be specified by clicking on the role button (Admin, User)

![Image Alt text](/frontend/TMC/images/register.png "Resgister of User OR Admin")

## Login Page
Both the user and Admin can log in from this page and create an account and this can be specified by clicking on the role button (Admin, User)


![Image Alt text](/frontend/TMC/images/login.png "Login of User OR Admin")

## Home Screen for User 

Here is the Home screen after the User Login In this screen user can search the news and can also apply for a filter while searching the news

![Image Alt text](/frontend/TMC/images/user_home.png "Home screen for User")

## New search result screen for user

Here is the result after searching for any news from the user along with the filter

Search result for China news
![Image Alt text](/frontend/TMC/images/user_after_search.png "News search result china")

Search result for news of the election
![Image Alt text](/frontend/TMC/images/user_after_search_result.png "News search result election")

Filter like language and category of the news
![Image Alt text](/frontend/TMC/images/user_home_search_filter.png "Filter for new search")

## Admin Dashboard

Here is the dashboard screen for admin login we can see here the trending keyword 

![Image Alt text](/frontend/TMC/images/admin_dashboard.png "Trending Keyword on admin dashboard")

and also can filter to see any specific keyword data and how many times it is used by the user 

![Image Alt text](/frontend/TMC/images/admin_keyword_search.png "Filter for trending keyword")


# All user views for admin

Here the admin can see the users under him
![Image Alt text](/frontend/TMC/images/admin_view_user.png "List of all user on the admin dashboard")

## Edit User Quota by the admin

Here user can edit the details of its users like user name, password, and quota 
![Image Alt text](/frontend/TMC/images/admin_edit_user.png "Edit user details")

## Finally the swagger for listing all backend api with their CRUD and their details 

![Image Alt text](/frontend/TMC/images/swagger.png "Swagger")
![Image Alt text](/frontend/TMC/images/swagger2.png "Swagger")



## Swagger

[Swagger](http://127.0.0.1:8000/swagger/)

## Features

### User-Facing Features
1. **Search Page**: 
   - Users can search for news articles by entering a specific phrase or keyword.
   - Results are stored locally for quick access.

2. **Sorting**: 
   - Users can sort search results based on the publication date.

3. **Filters**: 
   - Users can filter search results by category of the source and article language.

4. **User Authentication**: 
   - Each user can only see the keywords they have added.
   - No new keyword search is created for pre-existing keywords in the user's account, enhancing UX.

5. **UI Choice**: 
   - Original news pages are shown in the same window using appropriate UI elements to provide a seamless user experience.

### Admin Features
1. **User Management**: 
   - Admin can add or block users.
   - Admin can set a per-user quota for the number of keywords they can track.

2. **Dashboard**: 
   - Displays trending keywords (most searched keywords from multiple accounts).
   - Admin can select custom intervals for background searches of these keywords.

3. **Background Job**: 
   - Automatically refreshes search results at a given interval.

### Technical Features
1. **Documentation**: 
   - Proper documentation for each method/module using docstrings.

2. **HTML5**: 
   - Ensures proper usage of HTML5 tags for a semantic and accessible markup.

3. **Environment Variables**: 
   - Proper usage of environment variables and global configurations for managing sensitive data and settings.

4. **Clean Code**: 
   - Ensures readability and maintainability of the codebase through clean coding practices.

## Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/sdeadarsh/the_midnight_times.git
   cd the_midnight_times
   ```

2. Create a virtual environment and activate it I have used Python-3.9:
   ```sh
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root directory.
   - Add your environment-specific variables in the format `VARIABLE=value`.

5. Run database migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser for accessing the admin dashboard:
   ```sh
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```sh
   python manage.py runserver
   ```

8. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Time Taken and Experience
- **Total Time Taken**: Approximately 14 hours.
- **Experience**: 
  Working on The Midnight Times was an enriching experience. It allowed me to delve deep into Django's capabilities and best practices. Integrating with an external API, managing user authentication and authorization, and ensuring efficient data handling were challenging yet rewarding. This project enhanced my understanding of web application development, UX optimization, and the importance of clean, maintainable code.

## Conclusion
The Midnight Times project showcases a robust news search application built with Django, offering both user-facing features and comprehensive admin controls. It adheres to modern web development practices, ensuring a seamless user experience and efficient backend management.
