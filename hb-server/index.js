const express = require('express');
const app = express();
const ehbs = require('express-handlebars');
const MongoClient = require('mongodb').MongoClient;


app.set('view engine', 'hbs');
app.engine('hbs',  ehbs.engine({ defaultLayout: 'main2',exturl: '.hbs'}));
app.use(express.static('public'))


Array.prototype.extend = function (other_array) {
    /* You should include a test to check whether other_array really is an array */
    other_array.forEach(function(v) {this.push(v)}, this);
}

var urlinfo=[];



// connect to the db and start the express server
let db;

 

const url =  'mongodb://bookgist.in:27017/';

MongoClient.connect(url, (err, database) => {
  if(err) {
    return console.log(err);
  }
  db = database;
  // start the express web server listening on 8080
  app.listen(8080, () => {
    console.log('listening on 8080');
  });
});

all_vids=[]
function parse(result)
{
  var length = result.length;
  console.log("LEN"+length);
  for (var i = 0; i < length; i++) {
      //console.log(result[i]['vids']);
      all_vids.extend(result[i]['vids'])

  }
 
}

app.get('/', (req, res) => {
    res.send("hello world");
});


app.get('/test', (req, res) => {

  var dbo = db.db("textgen");
  var keyphrase = req.query.keyphrase;
  console.log(keyphrase);
  keyphrase="basic-statistics"
  var db_query={"category": keyphrase}
  dbo.collection("group_vids").find(db_query).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    parse(result)
    console.log(all_vids);
    res.render('main', {layout: 'index', url_cards: all_vids, listExists: true});

   });

});
 
 