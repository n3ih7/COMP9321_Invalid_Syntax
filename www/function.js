

    document.getElementById("ta").style.display = 'none';
    document.getElementById("resimg1").style.display = 'none';
    document.getElementById("resimg2").style.display = 'none';
    document.getElementById("resimg3").style.display = 'none';
    document.getElementById("resimg4").style.display = 'none';
    document.getElementById("resimg5").style.display = 'none';
    document.getElementById("resimg6").style.display = 'none';
    document.getElementById("b9").style.display = 'none';
    // document.getElementById("img1").src = 'data:image;base64, + base64
    document.getElementById("b1").addEventListener("click",function(){

        let city_name = document.getElementById("city").value
        if (city_name == ''){
            alert("invaid input");
          }
        
          $.ajax({
              url:'http://vau.nono.fi/api/weather?cityName='+city_name+'&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1',
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
                document.getElementById('data2').textContent = keys[1]
                document.getElementById('hum2').textContent = response[keys[1]]['humidity']
                document.getElementById('pre2').textContent = response[keys[1]]['pressure']
                document.getElementById('temp2').textContent = response[keys[1]]['temp']
                document.getElementById('ws2').textContent = response[keys[1]]['speed']
                document.getElementById('wd2').textContent = response[keys[1]]['deg']
                document.getElementById('f2').textContent = response[keys[1]]['fire_probability']
                document.getElementById('data3').textContent = keys[2]
                document.getElementById('hum3').textContent = response[keys[2]]['humidity']
                document.getElementById('pre3').textContent = response[keys[2]]['pressure']
                document.getElementById('temp3').textContent = response[keys[2]]['temp']
                document.getElementById('ws3').textContent = response[keys[2]]['speed']
                document.getElementById('wd3').textContent = response[keys[2]]['deg']
                document.getElementById('f3').textContent = response[keys[2]]['fire_probability']
                document.getElementById('data4').textContent = keys[3]
                document.getElementById('hum4').textContent = response[keys[3]]['humidity']
                document.getElementById('pre4').textContent = response[keys[3]]['pressure']
                document.getElementById('temp4').textContent = response[keys[3]]['temp']
                document.getElementById('ws4').textContent = response[keys[3]]['speed']
                document.getElementById('wd4').textContent = response[keys[3]]['deg']
                document.getElementById('f4').textContent = response[keys[3]]['fire_probability']
                document.getElementById('data5').textContent = keys[4]
                document.getElementById('hum5').textContent = response[keys[4]]['humidity']
                document.getElementById('pre5').textContent = response[keys[4]]['pressure']
                document.getElementById('temp5').textContent = response[keys[4]]['temp']
                document.getElementById('ws5').textContent = response[keys[4]]['speed']
                document.getElementById('wd5').textContent = response[keys[4]]['deg']
                document.getElementById('f5').textContent = response[keys[4]]['fire_probability']
               
              }
              
          });
  
  
  
      })
    document.getElementById("b2").addEventListener("click",function(){

      let st = document.getElementById("st1").value
      let end = document.getElementById("ed1").value
        $.ajax({
            url:' http://vau.nono.fi/api/cause_of_fire?start_date=' + st +'&end_date=' + end+'&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1',
            type:'get',
            success:function(response){
              document.getElementById("resimg1").style.display = 'block';
              document.getElementById("resimg1").src = 'data:image;base64,' + response

              
            }
            
        });
    })
    document.getElementById("b3").addEventListener("click",function(){
      let st = document.getElementById("st2").value
      let end = document.getElementById("ed2").value
        $.ajax({
            url:' http://vau.nono.fi/api/severity_rating?start_date=' + st +'&end_date=' + end+'&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1',
            type:'get',
            success:function(response){
              document.getElementById("resimg2").style.display = 'block';
              document.getElementById("resimg2").src = 'data:image;base64,' + response

              
            }
            
        });
    })
    document.getElementById("b4").addEventListener("click",function(){

      let st = document.getElementById("st3").value
      let end = document.getElementById("ed3").value

        $.ajax({
            url:'http://vau.nono.fi/api/cause_analysis?start_date=' + st +'&end_date=' + end+'&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1',
            type:'get',
            success:function(response){
              document.getElementById("resimg3").style.display = 'block';
              document.getElementById("resimg3").src = 'data:image;base64,' + response

              
            }
            
        });
    })
    document.getElementById("b5").addEventListener("click",function(){

      let st = document.getElementById("st4").value
      let city = document.getElementById('ct4').value
        $.ajax({
            url:' http://vau.nono.fi/api/fire_factors?city_name='+city+'&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1&start_date='+st,
            type:'get',
            success:function(response){
              document.getElementById("resimg4").style.display = 'block';
              document.getElementById("resimg4").src = 'data:image;base64,' + response
            }
        });
    })
    document.getElementById("b6").addEventListener("click",function(){

      let st = document.getElementById("st5").value
      let end = document.getElementById("ed5").value

        $.ajax({
            url:'http://vau.nono.fi/api/happened_times?start_date=' + st +'&end_date=' + end+'&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1',
            type:'get',
            success:function(response){
              document.getElementById("resimg5").style.display = 'block';
              document.getElementById("resimg5").src = 'data:image;base64,' + response

              
            }
            
        });
    })
    document.getElementById("b7").addEventListener("click",function(){
      let st = document.getElementById("st6").value
      let end = document.getElementById("ed6").value

        $.ajax({
            url:'http://vau.nono.fi/api/state_and_fire?start_date=' + st +'&end_date=' + end+'&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1',
            type:'get',
            success:function(response){
              document.getElementById("resimg6").style.display = 'block';
              document.getElementById("resimg6").src = 'data:image;base64,' + response

              
            }
            
        });
    })
    document.getElementById("b8").addEventListener("click",function(){

        $.ajax({
            url:'http://vau.nono.fi/api/api_usage?APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1',
            type:'get',
            success:function(response){

              document.getElementById("b9").style.display = 'block';
              document.getElementById("value1").style.display = 'block'
              document.getElementById("value2").style.display = 'block'
              document.getElementById("value3").style.display = 'block'
              document.getElementById("value4").style.display = 'block'
              document.getElementById("value5").style.display = 'block'
              document.getElementById("value6").style.display = 'block'
              document.getElementById("value7").style.display = 'block'  
              document.getElementById("value1").textContent = "the usage of fire prediction api:" + response["weather_usage"]
              document.getElementById("value2").textContent = "the usage of fire reason of fire api:" + response["cause_of_fire_usage"]
              document.getElementById("value3").textContent = "the usage of cause analysis api:" + response["severity_rating_usage"]
              document.getElementById("value4").textContent = "the usage of The impact of fire in US api:" + response["cause_analysis_usage"]
              document.getElementById("value5").textContent = "the usage of fire factors of fire api:" + response["fire_factors_usage"]
              document.getElementById("value6").textContent = "the usage of fire happend time api:" + response["happened_times_usage"]
              document.getElementById("value7").textContent = "the usage of The stats & fire analysis api:" + response["state_and_fire_usage"]

            }
            
        });
    })
    document.getElementById("b9").addEventListener("click",function(){

      
            document.getElementById("b9").style.display = 'none';
            document.getElementById("value1").style.display = 'none'
            document.getElementById("value2").style.display = 'none'
            document.getElementById("value3").style.display = 'none'
            document.getElementById("value4").style.display = 'none'
            document.getElementById("value5").style.display = 'none'
            document.getElementById("value6").style.display = 'none'
            document.getElementById("value7").style.display = 'none'

          
          
  })
