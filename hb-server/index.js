const express = require('express');
const app = express();
const ehbs = require('express-handlebars');
const MongoClient = require('mongodb').MongoClient;


app.set('view engine', 'hbs');
app.engine('hbs',  ehbs.engine({ defaultLayout: 'main',exturl: '.hbs'}));
app.use(express.static('public'))



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


/*

app.get('/slug_phrases', (req, res) => {

  var dbo = db.db("textgen");
  var slug = req.query.slug;
  console.log(keyphrase);
  var db_query={slug: slug}
  dbo.collection("slug_phrases").find(db_query).toArray(function(err, result) {
    if (err) throw err;
    //console.log(result);
    res.render('main', {layout: 'index', url_cards: result, listExists: true});

   });

});
*/

const linkPreviewGenerator = require("link-preview-generator");


function on_success(data) {
  if(data==null)
    return
  console.log(data);
  var dbo = db.db("textgen");

  dbo.collection("urlmaster").insertOne(data, function(err, res) {  
    if (err) {console.log("Error inserting"+data)}
    else console.log("1 record inserted"+data);  
  
  }); 
} 


async function gen_preview(the_url){

   try{
       const previewData = await linkPreviewGenerator(the_url);
       //console.log(previewData);
       previewData["_id"]=the_url;
       return previewData;
    }
    catch(err) {
       console.log("IGN"+the_url);
       return null;
    }
}

app.get('/urlinfo', (req, res) => {
  var tmp = req.query.url_param;

  //tmp="https://www.khanacademy.org/math/ap-statistics/gathering-data-ap/sampling-observational-studies/e/identifying-population-sample"
  gen_preview(tmp).then(on_success);
  res.send("queued");   

});
                                                                           