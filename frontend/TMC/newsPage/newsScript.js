const filterBtn = document.getElementById('filterBtn');
const filterPopup = document.getElementById('filterPopup');
const applyFilterBtn = document.getElementById('applyFilterBtn');
const searchBtn = document.getElementById('searchBtn');
const closeBtn = document.getElementById('closeBtn');
// const toggleButton = document.getElementById('togglebtn');
const newsDetail = document.getElementById('newsDetail');
const attachNews = document.getElementById('attachNews');

const url = "http://127.0.0.1:8000";

// toggleButton.addEventListener('click', () => {
//     if (newsDetail.style.display === 'none') {
//         newsDetail.style.display = 'block';
//     } else {
//         newsDetail.style.display = 'none';
//     }
// });

filterBtn.addEventListener('click', () => {
    filterPopup.classList.toggle('hidden');
});

applyFilterBtn.addEventListener('click', () => {
    // Retrieve selected filter options
    const language = document.getElementById('language').value;
    const category = document.getElementById('category').value;

    // Implement your filter logic here
    console.log('Language:', language);
    console.log('Category:', category);

    // Close the filter popup
    filterPopup.classList.add('hidden');
});

searchBtn.addEventListener('click', () => {
    // Retrieve search input
    const searchInput = document.getElementById('searchInput').value;
    const userId = localStorage.getItem('token');

    fetch(`${url}/news/search/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "searchBar": searchInput, "user_id":userId }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {

        if (!data.error) {
            console.log(data.result.data.results)
            for(const key in data.result.data.results){
                console.log(key)
                const news = data.result.data.results[key];
                const formattedDate = new Date(news.published_at).toLocaleString('en-US', {
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric',
                    hour: 'numeric',
                    minute: 'numeric'
                });
                const html = `            <div class="bg-white rounded-lg shadow-md p-4">
                <div class="flex justify-between items-center">
                    <h2 class="text-xl font-bold">${news.title}</h2>
                    <button id="togglebtn" class="bg-blue-500 rounded-md  text-white px-4 py-2"><i class="bi bi-chevron-down"></i></button>
                </div>
                
                <p class="text-gray-500 mb-1">Published Date: September 1, 2022</p>
                <div id="newsDetail">
                <div class="flex justify-center py-2">
                    <img src=" ${news.img} alt="News Image" class="aspect-[4/3]">
                </div>
                <div class="flex justify-center px-4">
                    <p class="text-gray-700">${news.description}</p>
                </div>
            </div>
            </div>`;
            attachNews.innerHTML += html
            }
            
        }
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });


    // Implement your search logic here
    console.log('Search Query:', searchInput);
});

closeBtn.addEventListener('click', () => {
    filterPopup.classList.add('hidden');
});