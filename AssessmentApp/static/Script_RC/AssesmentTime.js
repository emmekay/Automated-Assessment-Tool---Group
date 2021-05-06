function countdown(H, M){


  var dateObject = new Date();
  dateObject.setHours(H);
  dateObject.setMinutes(M);
  dateObject.setSeconds(0);


  dateObject.setHours(0);
  dateObject.setMinutes(1);
  dateObject.setSeconds(30);





  var t = 100000
  var x = setInterval(function() {

    // t -=1;
    dateObject.setSeconds(dateObject.getSeconds() - 1);
    if (dateObject.getHours() > 0 || dateObject.getMinutes() > 0 || dateObject.getSeconds() > 0 ){
      document.getElementById("testTimer").textContent =   dateObject.getHours() + ":" + dateObject.getMinutes() + ":" + dateObject.getSeconds();
    } else {
      // mainForm
      document.getElementById("mainForm").submit();
    }


  }, 1000)
}


function test4(x, y){

  var dateObject = new Date();
  dateObject.setHours(x);
  dateObject.setMinutes(y);
  dateObject.setSeconds(0);





  console.log(x);
  console.log(y);
  dateObject.setSeconds(dateObject.getSeconds() - 1);
  console.log(dateObject.getHours() + ":" + dateObject.getMinutes() + ":" + dateObject.getSeconds()  );


  // var dateObject = new Date(x);
  // console.log(dateObject);

}
// var d = new Date()

// countdown()
// console.log("Hello World")

// document.getElementById("testTimer").textContent = 100;

// countdown()
