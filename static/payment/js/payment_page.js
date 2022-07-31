function pay() {

    var amount=document.getElementById ("amount").value
    console.log(amount);
    if (amount !=  0)
  
      $.ajax({
        url: "/payment/user-payment/",
        data: {
          event: "pay",
          amount: amount,
        },
        
        success: function (data) {
          // $("#idImg").html(data);
          console.log(data)
  
          var options = {
         
            key: data["razorpay_merchant_key"],
            amount: data['razorpay_amount'],
            currency: data["currency"],
            name: "Demo Razorpay",
            order_id: data["razorpay_order_id"],
            callback_url: data["callback_url"],
          };
           
          var rzp1 = new Razorpay(options);

          rzp1.on('payment.su', function (response){
            alert(response.error.code);
            alert(response.error.description);
            alert(response.error.source);
            alert(response.error.step);
            alert(response.error.reason);
            alert(response.error.metadata.order_id);
            alert(response.error.metadata.payment_id);
    });
          rzp1.on('payment.failed', function (response){
            alert(response.error.code);
            alert(response.error.description);
            alert(response.error.source);
            alert(response.error.step);
            alert(response.error.reason);
            alert(response.error.metadata.order_id);
            alert(response.error.metadata.payment_id);
    });
          rzp1.open();
          e.preventDefault();
        },
      });
      else{
        alert('please add coin')
      }
    }


function payment_detail(response){

  $.ajax({
    url: "/payment-details/",
    data: {
      response: response,
      
    },
    
    success: function (data) {}
  
});
}
