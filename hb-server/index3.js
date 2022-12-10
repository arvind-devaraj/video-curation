const express = require('express');
const app = express();
const ehbs = require('express-handlebars');
const MongoClient = require('mongodb').MongoClient;


app.set('view engine', 'hbs');
app.engine('hbs',  ehbs.engine({ defaultLayout: 'main2',exturl: '.hbs'}));
app.use(express.static('public'))

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


fakeApi = () => {
return [];


}

app.get('/', (req, res) => {
    res.send("hello world");
});

app.get('/test', (req, res) => {

  var dbo = db.db("textgen");
  var keyphrase = req.query.keyphrase;
  console.log(keyphrase);
  //var db_query = { phrase: "Clustering + Machine Learning" };
  var db_query={phrase: keyphrase}
  dbo.collection("phrase_urls").find(db_query).toArray(function(err, result) {
    if (err) throw err;
    //console.log(result);
    res.render('main', {layout: 'index', url_cards: result, listExists: true});

   });

});
 
async function url_feed(the_url) {


  var dbo = db.db("textgen");
  var db_query={"_id": the_url};
  data = await dbo.collection("url_info").find(db_query).toArray();
  //simulating find_one
  return data[0];

}

function on_data(data) {
   //console.log(data);
   if(data !=null)
      urlinfo.push(data);
  
}

var promises = [];

app.get('/group', (req, res) => {
  console.log("GET Group");

  var dbo = db.db("textgen");
  var coll= dbo.collection("group_info");
  
  var g = req.query.g;
  console.log(g);
  //var db_query={"_id": "basic-statistics#0"};
  var db_query={"_id": g};


  urlinfo=[]

  
  coll.find(db_query).toArray(function(err, result) {
    if (err) throw err;
    
    
     urls=result[0]["urls"];
     //console.log(urls);

    
    for (let item of urls) {
        console.log(item);
        prom=url_feed(item).then(on_data);
        promises.push(prom)
    }

    Promise.all(promises).then((results) => {
        console.log("All done");
        console.log(urlinfo);
        res.render('main', {layout: 'index', url_cards: urlinfo, listExists: true});

    });
    
    
    


   });


});
 