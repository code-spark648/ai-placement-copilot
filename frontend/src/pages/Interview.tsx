import { useState } from "react";
import api from "../api/axios";

export default function Interview() {
  const [company, setCompany] = useState("");
  const [role, setRole] = useState("");

  const [loading, setLoading] = useState(false);
  const [questions, setQuestions] = useState<any>(null);

  const generateQuestions = async () => {
    try {
      setLoading(true);

      const response = await api.post(
        "/interview/questions",
        {
          company,
          role,
        }
      );

      setQuestions(response.data);
    } catch (error: any) {
      console.error(error);

      alert(
        error?.response?.data?.detail ||
          "Failed to generate questions"
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
          🎤 AI Interview Preparation
        </h1>

        <p
          style={{
            color: "#94a3b8",
            marginBottom: "30px",
          }}
        >
          Generate company-specific interview questions using AI
        </p>

        <div
          style={{
            background:
              "rgba(255,255,255,0.05)",
            backdropFilter: "blur(12px)",
            borderRadius: "24px",
            padding: "25px",
          }}
        >
          <input
            value={company}
            onChange={(e) =>
              setCompany(e.target.value)
            }
            placeholder="Target Company (e.g. Google)"
            style={{
              width: "100%",
              padding: "15px",
              borderRadius: "12px",
              border: "none",
              marginBottom: "20px",
            }}
          />

          <input
            value={role}
            onChange={(e) =>
              setRole(e.target.value)
            }
            placeholder="Target Role (e.g. Software Engineer)"
            style={{
              width: "100%",
              padding: "15px",
              borderRadius: "12px",
              border: "none",
              marginBottom: "20px",
            }}
          />

          <button
            onClick={generateQuestions}
            disabled={loading}
            style={{
              background: "#ef4444",
              color: "white",
              border: "none",
              padding: "14px 28px",
              borderRadius: "12px",
              cursor: "pointer",
              fontSize: "16px",
            }}
          >
            {loading
              ? "Generating..."
              : "Generate Questions"}
          </button>
        </div>

        {questions && (
          <>
            <div
              style={{
                marginTop: "30px",
                background:
                  "rgba(255,255,255,0.05)",
                borderRadius: "24px",
                padding: "25px",
              }}
            >
              <h2>
                🧠 Technical Questions
              </h2>

              <ol>
                {questions.technical_questions?.map(
                  (
                    question: string,
                    index: number
                  ) => (
                    <li
                      key={index}
                      style={{
                        marginBottom:
                          "10px",
                      }}
                    >
                      {question}
                    </li>
                  )
                )}
              </ol>
            </div>

            <div
              style={{
                marginTop: "20px",
                background:
                  "rgba(255,255,255,0.05)",
                borderRadius: "24px",
                padding: "25px",
              }}
            >
              <h2>
                🤝 Behavioral Questions
              </h2>

              <ol>
                {questions.behavioral_questions?.map(
                  (
                    question: string,
                    index: number
                  ) => (
                    <li
                      key={index}
                      style={{
                        marginBottom:
                          "10px",
                      }}
                    >
                      {question}
                    </li>
                  )
                )}
              </ol>
            </div>

            <div
              style={{
                marginTop: "20px",
                background:
                  "rgba(255,255,255,0.05)",
                borderRadius: "24px",
                padding: "25px",
              }}
            >
              <h2>
                💼 HR Questions
              </h2>

              <ol>
                {questions.hr_questions?.map(
                  (
                    question: string,
                    index: number
                  ) => (
                    <li
                      key={index}
                      style={{
                        marginBottom:
                          "10px",
                      }}
                    >
                      {question}
                    </li>
                  )
                )}
              </ol>
            </div>
          </>
        )}
      </div>
    </div>
  );
}