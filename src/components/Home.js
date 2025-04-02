import { useState } from "react";
import './Home.css'

export default function Home() {
    const [portraitZip, setPortraitZip] = useState(null);
    const [candidZip, setCandidZip] = useState(null);
    const [error, setError] = useState("");

    const handleFileChange = (e, isPortrait) => {
        const file = e.target.files[0];
        if (file && file.name.endsWith(".zip")) {
            setError("");
            if (isPortrait) {
                setPortraitZip(file);
            } else {
                setCandidZip(file);
            }
        } else {
            setError("Only .zip files are allowed!");
        }
    };

    const uploadFiles = async () => {
        if (!portraitZip || !candidZip) {
            setError("Please upload both portrait and candid zip files.");
            return;
        }

        const formData = new FormData();
        formData.append("portrait_zip", portraitZip);
        formData.append("candids_zip", candidZip);

        try {
            const response = await fetch("http://localhost:5000/upload", {
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
                {error && <p className="error-message">{error}</p>}
                <div className="upload-box">
                    <label className="upload-label">
                        Upload Portraits (.zip)
                        <input type="file" accept=".zip" className="hidden-input"
                            onChange={e => handleFileChange(e, true)}
                        />
                    </label>
                    <label className="upload-label">
                        Upload Candids (.zip)
                        <input type="file" accept=".zip" className="hidden-input"
                            onChange={e => handleFileChange(e, false)}
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
