// $(document).ready(function(){

//   $('form').on('submit', function(){

//       var temp = {
//         firstname: $('form')[0].elements.namedItem("first_name").value,
//         lastname: $('form')[0].elements.namedItem("last_name").value,
//         institution: $('form')[0].elements.namedItem("company").value,
//         email: $('form')[0].elements.namedItem("email").value,
//         username : $('form')[0].elements.namedItem("username").value,
//         password : $('form')[0].elements.namedItem("password").value,
//         phoneareacode: $('form')[0].elements.namedItem("area_code").value,
//         phonenumber: $('form')[0].elements.namedItem("phone").value,
//         language: $('form')[0].elements.namedItem("subject").value,
//         usertype: $('form')[0].elements.namedItem("usertype").value,
//       }

//       $.ajax({
//         type: 'POST',
//         url: '/register',
//         data: temp,
//         success: function(data){
//           //do something with the data via front-end framework
//           // location.reload();
//           return false;
//         }
//       });


//   });

// });
