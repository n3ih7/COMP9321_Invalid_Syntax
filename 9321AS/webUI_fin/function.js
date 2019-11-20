

    document.getElementById("ta").style.display = 'none';
    document.getElementById("b1").addEventListener("click",function(){

        let city_name = document.getElementById("city").value
        if (city_name == ''){
            alert("invaid input");
          }
        console.log('http://vau.nono.fi/todo/api/v1.0/weather_current?cityName='+city_name)
          $.ajax({
              url:'http://vau.nono.fi/todo/api/v1.0/weather_current?cityName=' + city_name,
              type:'get',
              success:function(response){
                document.getElementById("ta").style.display = 'block';
                const keys= Object.keys(response)
                document.getElementById('data1').textContent = keys[0]
                document.getElementById('hum1').textContent = response[keys[0]]['humidity']
                document.getElementById('pre1').textContent = response[keys[0]]['pressure']
                document.getElementById('temp1').textContent = response[keys[0]]['temp']
                document.getElementById('ws1').textContent = response[keys[0]]['speed']
                document.getElementById('wd1').textContent = response[keys[0]]['deg']
                document.getElementById('f1').textContent = response[keys[0]]['fire_probability']

              }
              
          });
  
  
  
      })
  