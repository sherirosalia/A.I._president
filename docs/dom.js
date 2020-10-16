
var tweets = data;
// console.log(tweets);

var tweet=tweets.forEach(element => {
    console.log(element['tweet']);
    $('tbody').append(element['tweet'] + "\n" + "<br>" +  "<br>"  )


});


// let tweets=data;

// let tbody = d3.select('tbody');

// let fields = ['tweets'];

// function writeRow(oneTweet) {
//     // console.log('hello');
//     var row = tbody.append('tr');
//     var cell;
//     for(field of fields){
//         cell = row.append('td')
//         cell.text(oneTweet[field])
//     }
//     // tbody.append(writeRow);
//     // console.log('hello');
    
// }
// // tbody.append(writeRow);

// console.log('hello');