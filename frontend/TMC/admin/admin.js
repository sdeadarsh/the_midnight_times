const url = "http://127.0.0.1:8000/users/user";

const searchBtn = document.getElementById('searchBtn');
const searchInput = document.getElementById('searchInput');
const logoutbtn = document.getElementById('logoutbtn');
const viewAllUser = document.getElementById('viewAllUser');
const viewUser = document.getElementById('viewUser');
const viewKeyword = document.getElementById('viewKeyword');
const closeBtn = document.getElementById('closeBtn');
const applyFilterBtn = document.getElementById('applyFilterBtn');

const userId = localStorage.getItem('token');

const hideTheDiv = (div) => {   
    if (div === 'user') {
        viewUser.classList = 'block';
        viewKeyword.classList = 'hidden';
    } else {
        viewUser.classList = 'hidden';
        viewKeyword.classList = 'block';
    }
}

applyFilterBtn.addEventListener('click', () => { 
    const userEditID = document.getElementById('userIdEdit').value;
    const usernameEdit = document.getElementById('usernameEdit').value;
    const passwordEdit = document.getElementById('passwordEdit').value;
    const quotaEdit = document.getElementById('quotaEdit').value;

    fetch(`${url}/${userEditID}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_name: usernameEdit, password: passwordEdit, quota: quotaEdit}),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        filterPopup.classList.add('hidden');
        viewKeyword.classList = 'hidden';
        viewUser.classList = 'block';

        return response.json();
    })

});

viewAllUser.addEventListener('click', () => {  
    if(viewAllUser.innerHTML === 'View Keywords'){
        viewAllUser.innerHTML = 'View User';
        hideTheDiv('keyword');
    }else{
        fetchAndAppendUser();
        viewAllUser.innerHTML = 'View Keywords';
        hideTheDiv('user');
    }

});

document.getElementById('editbtn').addEventListener('click', () => {
    console.log('edit');
    filterPopup.classList.toggle('hidden');
});
closeBtn.addEventListener('click', () => {
    filterPopup.classList.add('hidden');
});

if(userId==null){
    window.location.replace('../index.html');
}
logoutbtn.addEventListener('click', () => {
    localStorage.removeItem('token');
    window.location.replace('../index.html');
});

searchBtn.addEventListener('click', () => {
    fetchAndAppendRows(searchInput.value)
});

async function fetchAndAppendRows(word) {
    console.log(word);
    const tableBody = document.getElementById("tableBody");
    tableBody.innerHTML = "";
    try {
        // Fetch data from a URL
        if(word!==undefined && word!==""){
            response = await fetch(`http://127.0.0.1:8000/users/user/get_keyword/${userId}/?keyword_searched=${word}`);
        }else{
            response = await fetch(`http://127.0.0.1:8000/users/user/get_keyword/${userId}/`);
        }
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Parse the response as JSON
        const data = await response.json();
        console.log(data);
        // Get the table body element

        for(const k of data.result.data){
            console.log(k);
            const row = document.createElement("tr");
            row.innerHTML = `
            <td class="py-2 px-4 border-b">${k.keyword}</td>
            <td class="py-2 px-4 border-b">${k.count}</td>
            `;
            tableBody.appendChild(row);
        }

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

async function fetchAndAppendUser() {

    const tableBody = document.getElementById("userTable");
    tableBody.innerHTML = "";
    try {
        // Fetch data from a URL
        const response = await fetch(`http://127.0.0.1:8000/users/user/`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Parse the response as JSON
        const data = await response.json();
        console.log(data);
        // Get the table body element

        for(const k of data.result.data){
            console.log(k);
            const row = document.createElement("tr");
            row.innerHTML = `
            <td class="py-2 px-4 border-b">${k.id}</td>
            <td class="py-2 px-4 border-b">${k.user_name}</td>
            <td class="py-2 px-4 border-b">${k.password}</td>
            <td class="py-2 px-4 border-b">${k.quota}</td>
            `;
            tableBody.appendChild(row);
        }

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchAndAppendRows();