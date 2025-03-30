exports.useFiles=(req,res)=>{
    console.log(req.body)
    console.log(req.files)
    res.json({message:"Done!"})
    
}