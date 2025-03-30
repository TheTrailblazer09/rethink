const express= require('express');
const router= express.Router();
const controller= require('../controller/fileController')
const multer = require("multer"); //for the files
const upload = multer({ dest: "uploads/" });


router.post('/sendFiles', upload.fields([{ name: "portraits" }, { name: "candids" }]),controller.useFiles)
// router.post('/getPictures',controller.returnPictures)

module.exports= router;