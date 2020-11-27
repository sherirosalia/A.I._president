$(document).ready(function() {
    $('table.display').DataTable();
  } );
var tweets = data;
console.log(tweets);

var tweet=tweets.forEach(element => {

    console.log(element['tweet']);
    $('tbody').append(element['tweet'] + "\n" + "<br>" +  "<br>"  )


});