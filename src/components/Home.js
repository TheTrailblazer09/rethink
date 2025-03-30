import React from "react";
import "./Home.css"; // Import the CSS file
import { useState } from "react";

export default function Home() {
    const [portraits, setPortaits]= useState([]);
    const [candids, setCandids]= useState([])
    const [name,setNameP]= useState("Upload Portraits")
    const [nameC, setnameC]= useState("Upload Candids")

    const handleFolder =(e,isPortrait) =>{
      if(isPortrait==true){
        setPortaits(Array.from(e.target.files))
        setNameP("Portaits Uploaded Successfully")
        // call API here using these files 
      }
      else{
        setCandids(Array.from(e.target.files))
        setnameC("Candids Uploaded Successfully")
      }
    }

    const uploadFiles = async () => {
      const formData = new FormData();
      console.log(portraits)
      portraits.forEach((file) => {
        formData.append("portraits", file);
      });
      candids.forEach((file) => {
        formData.append("candids", file);
      });
  
      try {
        const response = await fetch("http://localhost:8000/sendFiles", {
          method: "POST",
          body: formData,
        });
        const result = await response.json();
        alert(result.message);
      } catch (error) {
        console.error("Upload failed:", error);
        alert("File upload failed!");
      }
    };

   
  return (
    <div className="yearbook-container">
      <div className="background-image"></div>
      <div className="upload-card">
        <h1 className="title">Rethink your yearbook</h1>
        <p className="subtitle">Upload your portraits and candids to get started!</p>
        <div className="upload-box">
          <label className="upload-label">
            {name}
            <input type="file" webkitdirectory="true" directory multiple className="hidden-input"
             onChange={e=>handleFolder(e, true)}
            />
          </label>

          <label className="upload-label">
            {nameC}
            <input type="file" webkitdirectory="true" directory multiple className="hidden-input" 
            onChange={e=>handleFolder(e, false)}
            />
          </label>
          <button className="upload-btn" onClick={uploadFiles}>
          Upload Files
        </button>
        </div>
      </div>
    </div>
  );
}
