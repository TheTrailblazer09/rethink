const express= require('express')
const files= require('./routes/files')
const controller= require('./controller/fileController')
const bodyParser=require('body-parser');

const app= express()
app.use(express.urlencoded({ extended: true }));

app.use((req,res,next)=>{
    res.setHeader('Access-Control-Allow-Origin','*')
    res.setHeader('Access-Control-Allow-Methods','GET, POST , PUT,DELETE')
    res.setHeader('Access-Control-Allow-Headers','Content-Type, Authorization')
    console.log("CORS headers set")
    next();
});

app.use(bodyParser.json());

app.use(files)

app.listen(8000,()=>{
    console.log("Backend is working")
})