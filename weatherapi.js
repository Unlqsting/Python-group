import axios from "axios";

const options = {
  method: 'GET',
  url: 'https://yahoo-weather5.p.rapidapi.com/weather',
  params: {location: 'sunnyvale', format: 'json', u: 'f'},
  headers: {
    'X-RapidAPI-Key': 'd52614d761mshb67fc7102590b16p1838c8jsne4eb059fe469',
    'X-RapidAPI-Host': 'yahoo-weather5.p.rapidapi.com'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});

// Fetch:

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'd52614d761mshb67fc7102590b16p1838c8jsne4eb059fe469',
		'X-RapidAPI-Host': 'yahoo-weather5.p.rapidapi.com'
	}
};

fetch('https://yahoo-weather5.p.rapidapi.com/weather?location=sunnyvale&format=json&u=f', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));