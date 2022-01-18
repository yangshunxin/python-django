console.log("^^^^^^^^^^^")
$(document).ready(function () {
    document.getElementById("btn").onclick = function(){
        $.ajax({
            type:"get",
            url:"/myapp/studentsinfo/",
            dataType:"json",
            success:function(data, status){
//                console.log(data)
                var d = data["data"]
                for (var i = 0; i < d.length; i++ ){
                    document.write('<p>'+d[i]+'</p>')
                }
                document.write()

            }
        })
    }
})