
const url = "http://127.0.0.1:8000";
document.addEventListener('DOMContentLoaded', function() {
    // Default to the user tab
    const userTab = document.getElementById('user-tab');
    const adminTab = document.getElementById('admin-tab');
    const loginForm = document.getElementById('login-form');

    // Event listener for user tab
    userTab.addEventListener('click', function() {
        userTab.classList.add('bg-gray-200');
        adminTab.classList.remove('bg-gray-200');
        // Any specific logic for user tab
    });

    // Event listener for admin tab
    adminTab.addEventListener('click', function() {
        adminTab.classList.add('bg-gray-200');
        userTab.classList.remove('bg-gray-200');
        // Any specific logic for admin tab
    });

    // Event listener for form submission
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;


        fetch(`${url}/users/user/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_name: username, password: password }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {

            if (!data.error) {
                console.log(data.result.data.id)
                localStorage.setItem('token', data.result.data.id);
                if (data.result.is_admin) {
                    window.location.replace('admin/admin.html');
                } else {
                    window.location.replace('newsPage/newsPage.html');
                }

            } else {
                alert('Invalid username or password');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    });

});