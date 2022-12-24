const express = require('express');
const app = express();
const ehbs = require('express-handlebars');
const MongoClient = require('mongodb').MongoClient;


app.set('view engine', 'hbs');
app.engine('hbs',  ehbs.engine({ defaultLayout: 'main2',exturl: '.hbs'}));
app.use(express.static('public'))

 
app.get('/', (req, res) => {
    res.send("hello world");
});

 
 
 



app.get('/tag', (req, res) => {

  var fs = require('fs');
  var obj = JSON.parse(fs.readFileSync('../tv.json', 'utf8'));
  console.log(obj);
  all_vids=obj["Clustering"];

    res.render('main', {layout: 'index', url_cards: all_vids, listExists: true});

  

});
 

app.listen(8080, () => {
    console.log('listening on 8080');
  });