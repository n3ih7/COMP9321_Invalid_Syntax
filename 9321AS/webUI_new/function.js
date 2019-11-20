
    document.getElementById("button").addEventListener("click",function(){
      alert("Success!");
      let city_name = document.getElementById("city").value
      $.ajax({
        url:"http://vau.nono.fi/todo/api/v1.0/weather",
        data:{cityName:'shanghai'},
        type:'get',
        function(res){
            console.log(res); 
        }
    });    
    })
