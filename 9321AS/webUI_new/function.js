
    document.getElementById("button").addEventListener("click",function(){

      let city_name = document.getElementById("city").value
      console.log('http://vau.nono.fi/todo/api/v1.0/weather?cityName='+city_name)
        $.ajax({
            url:'http://vau.nono.fi/todo/api/v1.0/weather?cityName=' + city_name,
            type:'get',
            success:function(response){
                console.log(response.text);   //jquery框架会自动处理json，直接用key获取值就可以了
            }
        });



    })
