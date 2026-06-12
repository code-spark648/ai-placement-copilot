import { useState } from "react";
import api from "../api/axios";

export default function Resume() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

     const response = await api.post(
  "/resume/upload",
  formData,
  {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  }
);
      setResult(response.data);
    } catch (error: any) {
  console.log("FULL ERROR:", error);

  if (error.response) {
    console.log("RESPONSE:", error.response.data);
    alert(JSON.stringify(error.response.data));
  } else {
    alert(error.message);
  }
}   finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background:
          "linear-gradient(135deg,#020617,#0f172a,#1e293b)",
        color: "white",
        padding: "40px",
      }}
    >
      <div
        style={{
          maxWidth: "1100px",
          margin: "auto",
        }}
      >
        <h1
          style={{
            textAlign: "center",
            fontSize: "48px",
            marginBottom: "10px",
          }}
        >
          Resume Analysis 📄
        </h1>

        <p
          style={{
            textAlign: "center",
            color: "#94a3b8",
            marginBottom: "40px",
          }}
        >
          Upload your resume and get AI-powered insights
        </p>

        <div
          style={{
            background: "#1e293b",
            padding: "30px",
            borderRadius: "20px",
            textAlign: "center",
            marginBottom: "30px",
          }}
        >
         <div
  style={{
    marginBottom: "20px",
    padding: "15px",
    background: "#0f172a",
    borderRadius: "12px",
    border: "1px solid #334155",
    color: "#cbd5e1",
    fontSize: "14px",
    textAlign: "left",
  }}
>
  <strong>📄 Resume Upload Requirements</strong>

  <ul
    style={{
      marginTop: "10px",
      paddingLeft: "20px",
      lineHeight: "1.8",
    }}
  >
    <li>Only PDF files are supported</li>
    <li>Maximum file size: 5 MB</li>
    <li>Ensure text is selectable (not scanned images)</li>
    <li>Use a clean resume format for best AI analysis</li>
  </ul>
</div>

<input
  type="file"
  accept=".pdf"
  onChange={(e) =>
    setFile(
      e.target.files
        ? e.target.files[0]
        : null
    )
  }
  style={{
    padding: "12px",
    background: "#0f172a",
    borderRadius: "10px",
    border: "1px solid #334155",
    color: "white",
    width: "100%",
  }}
/>

{file && (
  <p
    style={{
      marginTop: "10px",
      color: "#22c55e",
      fontSize: "14px",
    }}
  >
    Selected File: {file.name}
  </p>
)}

          <br />
          <br />

          <button
            onClick={uploadResume}
            disabled={loading}
            style={{
              background: "#3b82f6",
              border: "none",
              color: "white",
              padding: "12px 24px",
              borderRadius: "10px",
              cursor: "pointer",
              fontSize: "16px",
            }}
          >
            {loading
              ? "Analyzing..."
              : "Upload Resume"}
          </button>
        </div>

        {result && (
          <>
            <div
              style={{
                background: "#1e293b",
                borderRadius: "20px",
                padding: "30px",
                textAlign: "center",
                marginBottom: "30px",
              }}
            >
              <h2>ATS Score</h2>

              <div
                style={{
                  fontSize: "72px",
                  fontWeight: "bold",
                  color:
                    result.ats_score > 75
                      ? "#22c55e"
                      : "#f59e0b",
                }}
              >
                {result.ats_score}
              </div>
            </div>

            <div
              style={{
                display: "grid",
                gridTemplateColumns:
                  "repeat(auto-fit,minmax(300px,1fr))",
                gap: "20px",
              }}
            >
              <div
                style={{
                  background: "#1e293b",
                  padding: "20px",
                  borderRadius: "20px",
                }}
              >
                <h2>🚀 Skills</h2>

                {result.skills?.map(
                  (
                    skill: string,
                    index: number
                  ) => (
                    <span
                      key={index}
                      style={{
                        display: "inline-block",
                        background: "#3b82f6",
                        padding:
                          "8px 14px",
                        margin: "6px",
                        borderRadius:
                          "999px",
                      }}
                    >
                      {skill}
                    </span>
                  )
                )}
              </div>

              <div
                style={{
                  background: "#1e293b",
                  padding: "20px",
                  borderRadius: "20px",
                }}
              >
                <h2>✅ Strengths</h2>

                <ul>
                  {result.strengths?.map(
                    (
                      item: string,
                      index: number
                    ) => (
                      <li key={index}>
                        {item}
                      </li>
                    )
                  )}
                </ul>
              </div>

              <div
                style={{
                  background: "#1e293b",
                  padding: "20px",
                  borderRadius: "20px",
                }}
              >
                <h2>⚠ Weaknesses</h2>

                <ul>
                  {result.weaknesses?.map(
                    (
                      item: string,
                      index: number
                    ) => (
                      <li key={index}>
                        {item}
                      </li>
                    )
                  )}
                </ul>
              </div>

              <div
                style={{
                  background: "#1e293b",
                  padding: "20px",
                  borderRadius: "20px",
                }}
              >
                <h2>💡 Recommendations</h2>

                <ul>
                  {result.recommendations?.map(
                    (
                      item: string,
                      index: number
                    ) => (
                      <li key={index}>
                        {item}
                      </li>
                    )
                  )}
                </ul>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}