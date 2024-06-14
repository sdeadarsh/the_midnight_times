const userTab = document.getElementById('user-tab');
const adminTab = document.getElementById('admin-tab');
const registerform = document.getElementById('register-form');
console.log('hello');
const url = "http://127.0.0.1:8000";

let is_admin = false;
// Event listener for user tab
userTab.addEventListener('click', function() {
    userTab.classList.add('bg-gray-200');
    adminTab.classList.remove('bg-gray-200');
    is_admin = false;
});

// Event listener for admin tab
adminTab.addEventListener('click', function() {
    adminTab.classList.add('bg-gray-200');
    userTab.classList.remove('bg-gray-200');
    is_admin = true;
});

registerform.addEventListener('submit', function(event) {
    console.log('submit');
    event.preventDefault(); // Prevent default form submission
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch(`${url}/users/user/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_name: username, password: password, is_admin: is_admin}),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        if (!data.result.error) {
            console.log(data.result.data.id)
            localStorage.setItem('token', data.result.data.id);
            if (data.result.data.is_admin) {
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