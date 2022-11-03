
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
    displayWeather: function(data) {
      const { name } = data;
      const { icon, description } = data.weather[0];
      const { temp } = data.main;
      const { temp_max, temp_min } = data.main
      console.log(name,icon,description,temp,temp_max,temp_min)
      document.querySelector(".city").innerText = "Weather in " + name;
      document.querySelector(".icon").src = "https://openweathermap.org/img/wn/" + icon + "@2x.png"
      document.querySelector(".weather").innerText = "Weather description:" + " " + description;
      document.querySelector(".currenttemp").innerText = temp + "℉"
      document.querySelector(".H").innerText = "High: " + temp_max + "℉"
      document.querySelector(".L").innerText = "Low: " + temp_min + "℉"
    },
    search: function () {
      this.fetchWeather(document.querySelector(".searchbar").value);
    },
  };


  