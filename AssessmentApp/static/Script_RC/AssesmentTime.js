function countdown(H, M, Staff){


  var dateObject = new Date();
  dateObject.setHours(H);
  dateObject.setMinutes(M);
  dateObject.setSeconds(0);


  // dateObject.setHours(0);
  // dateObject.setMinutes(1);
  // dateObject.setSeconds(30);
  // console.log();




  var t = 100000
  var x = setInterval(function() {

    // t -=1;
    dateObject.setSeconds(dateObject.getSeconds() - 1);
    if (dateObject.getHours() > 0 || dateObject.getMinutes() > 0 || dateObject.getSeconds() > 0 ){
      document.getElementById("testTimer").textContent =   dateObject.getHours() + ":" + dateObject.getMinutes() + ":" + dateObject.getSeconds();
    }

    // else {
    //   if (!Staff){
    //   document.getElementById("mainForm").submit();
  //      }
    // }


  }, 1000)
}
