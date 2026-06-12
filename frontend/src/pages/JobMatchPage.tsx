import { useState } from "react";
import api from "../api/axios";

export default function JobMatch() {
  const [jobDescription, setJobDescription] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const [result, setResult] =
    useState<any>(null);

  const analyzeMatch = async () => {
    try {
      setLoading(true);

      const token =
        localStorage.getItem("token");

      const response = await api.post(
        "/job-match/analyze",
        {
          job_title: "Software Engineer",
          job_description: jobDescription,
          resume_text: "",
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      setResult(response.data);
    } catch (error: any) {
      console.error(error);

      alert(
        error.response?.data?.detail ||
          "Analysis Failed"
      );
    } finally {
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
          maxWidth: "1200px",
          margin: "auto",
        }}
      >
        <h1
          style={{
            fontSize: "48px",
            marginBottom: "10px",
          }}
        >
          🎯 Job Match Analysis
        </h1>

        <p
          style={{
            color: "#94a3b8",
            marginBottom: "30px",
          }}
        >
          Compare your resume against a job
          description using AI
        </p>

        <div
          style={{
            background:
              "rgba(255,255,255,0.05)",
            backdropFilter: "blur(12px)",
            borderRadius: "24px",
            padding: "25px",
            border:
              "1px solid rgba(255,255,255,0.1)",
          }}
        >
          <textarea
            value={jobDescription}
            onChange={(e) =>
              setJobDescription(
                e.target.value
              )
            }
            placeholder="Paste Job Description Here..."
            rows={10}
            style={{
              width: "100%",
              padding: "20px",
              borderRadius: "16px",
              border: "none",
              background: "#1e293b",
              color: "white",
              fontSize: "15px",
            }}
          />

          <button
            onClick={analyzeMatch}
            disabled={loading}
            style={{
              marginTop: "20px",
              background: "#3b82f6",
              color: "white",
              border: "none",
              padding:
                "14px 28px",
              borderRadius: "12px",
              cursor: "pointer",
              fontSize: "16px",
            }}
          >
            {loading
              ? "Analyzing..."
              : "Analyze Match"}
          </button>
        </div>

        {result && (
          <>
            <div
              style={{
                marginTop: "40px",
                display: "grid",
                gridTemplateColumns:
                  "repeat(auto-fit,minmax(250px,1fr))",
                gap: "20px",
              }}
            >
              <div
                style={{
                  background:
                    "rgba(255,255,255,0.05)",
                  borderRadius:
                    "24px",
                  padding: "30px",
                  textAlign:
                    "center",
                }}
              >
                <h3>
                  Match Score
                </h3>

                <h1
                  style={{
                    fontSize:
                      "72px",
                    color:
                      "#22c55e",
                  }}
                >
                  {
                    result.match_score
                  }
                  %
                </h1>
              </div>

              <div
                style={{
                  background:
                    "rgba(255,255,255,0.05)",
                  borderRadius:
                    "24px",
                  padding: "30px",
                }}
              >
                <h3>
                  Target Role
                </h3>

                <h2>
                  Software
                  Engineer
                </h2>

                <p
                  style={{
                    color:
                      "#94a3b8",
                  }}
                >
                  AI Analysis
                </p>
              </div>
            </div>

            <div
              style={{
                marginTop: "30px",
                display: "grid",
                gridTemplateColumns:
                  "repeat(auto-fit,minmax(350px,1fr))",
                gap: "20px",
              }}
            >
              <div
                style={{
                  background:
                    "rgba(255,255,255,0.05)",
                  borderRadius:
                    "24px",
                  padding: "25px",
                }}
              >
                <h2>
                  ⚠ Missing Skills
                </h2>

                {result.missing_skills?.map(
                  (
                    skill: string
                  ) => (
                    <span
                      key={
                        skill
                      }
                      style={{
                        display:
                          "inline-block",
                        background:
                          "#ef4444",
                        padding:
                          "8px 16px",
                        borderRadius:
                          "999px",
                        margin:
                          "8px",
                      }}
                    >
                      {skill}
                    </span>
                  )
                )}
              </div>

              <div
                style={{
                  background:
                    "rgba(255,255,255,0.05)",
                  borderRadius:
                    "24px",
                  padding: "25px",
                }}
              >
                <h2>
                  🔍 Missing
                  Keywords
                </h2>

                {result.missing_keywords?.map(
                  (
                    keyword: string
                  ) => (
                    <span
                      key={
                        keyword
                      }
                      style={{
                        display:
                          "inline-block",
                        background:
                          "#f59e0b",
                        padding:
                          "8px 16px",
                        borderRadius:
                          "999px",
                        margin:
                          "8px",
                      }}
                    >
                      {keyword}
                    </span>
                  )
                )}
              </div>
            </div>

            <div
              style={{
                marginTop: "30px",
                background:
                  "rgba(255,255,255,0.05)",
                borderRadius:
                  "24px",
                padding: "25px",
              }}
            >
              <h2>
                💡 AI
                Recommendations
              </h2>

              <ul>
                {result.improvements?.map(
                  (
                    item: string,
                    index: number
                  ) => (
                    <li
                      key={
                        index
                      }
                    >
                      {item}
                    </li>
                  )
                )}
              </ul>
            </div>
          </>
        )}
      </div>
    </div>
  );
}