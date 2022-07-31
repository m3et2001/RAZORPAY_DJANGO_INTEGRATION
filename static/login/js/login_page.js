var otp_from_back =0;

function send_otp() {
    var email=document.getElementById ("email").value;
    var password=document.getElementById ("password").value;
    var login_card=document.getElementsByClassName("login-card")[0];
    var verification_card=document.getElementsByClassName("verification-card")[0];
    console.log(verification_card)
      $.ajax({
        url: "/send-otp",
        data: {
          email: email,
          password: password,
        },
        success: function (data) {
          if(data["isUserAuthorized"]=="True"){
            otp_from_back =data['otp']
            login_card.style.display='none';
            verification_card.style.display='block';
          }
          else{
            alert("email or password is invalid")
          }
        }
    });
  }

function verify(){
  var userotp=document.getElementById ("otp").value;
  if(userotp==otp_from_back ){
    document.getElementById("loginForm").submit();
  }
  else{
    alert('wrong otp, check your otp')
  }
}