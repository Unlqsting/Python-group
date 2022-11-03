
  //weather stuff:

  let weather = {
    apiKey: "b95c3461498620c129a3d6a6b675c29b",
    fetchWeather: function (city) {
      fetch(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=b95c3461498620c129a3d6a6b675c29b"
      )
        .then((res) => res.json())
        .then((data) => this.displayWeather(data));
    },
    
  };
