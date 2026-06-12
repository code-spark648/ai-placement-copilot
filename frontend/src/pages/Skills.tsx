import { useState } from "react";
import api from "../api/axios";

export default function Skills() {
  const [targetRole, setTargetRole] = useState("");
  const [currentSkills, setCurrentSkills] = useState("");

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const analyzeSkills = async () => {
    if (!targetRole.trim()) {
      alert("Enter target role");
      return;
    }

    try {
      setLoading(true);

      const response = await api.post(
        "/skills/gap-analysis",
        {
          target_role: targetRole,
          current_skills: currentSkills
            .split(",")
            .map((s) => s.trim())
            .filter(Boolean),
        }
      );

      setResult(response.data);
    } catch (error: any) {
  console.error(error);

  alert(JSON.stringify(error.response?.data));
}
   finally {
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
        <h1>📈 Skill Gap Analysis</h1>

        <div
          style={{
            background:
              "rgba(255,255,255,0.05)",
            padding: "25px",
            borderRadius: "24px",
          }}
        >
          <input
            value={targetRole}
            onChange={(e) =>
              setTargetRole(e.target.value)
            }
            placeholder="Target Role"
            style={{
              width: "100%",
              padding: "15px",
              marginBottom: "15px",
              borderRadius: "12px",
            }}
          />

          <textarea
            value={currentSkills}
            onChange={(e) =>
              setCurrentSkills(
                e.target.value
              )
            }
            placeholder="Python, SQL, Excel..."
            rows={6}
            style={{
              width: "100%",
              padding: "15px",
              borderRadius: "12px",
            }}
          />

          <button
            onClick={analyzeSkills}
            disabled={loading}
            style={{
              marginTop: "20px",
              padding: "14px 24px",
              borderRadius: "12px",
              border: "none",
              background: "#3b82f6",
              color: "white",
              cursor: "pointer",
            }}
          >
            {loading
              ? "Analyzing..."
              : "Analyze Skills"}
          </button>
        </div>

        {result && (
          <div
            style={{
              marginTop: "30px",
            }}
          >
            <div
              style={{
                background:
                  "rgba(255,255,255,0.05)",
                padding: "25px",
                borderRadius: "24px",
                marginBottom: "20px",
              }}
            >
              <h2>🎯 Skill Score</h2>

              <h1
                style={{
                  color: "#22c55e",
                }}
              >
                {result.skill_score}%
              </h1>
            </div>

            <div
              style={{
                background:
                  "rgba(255,255,255,0.05)",
                padding: "25px",
                borderRadius: "24px",
                marginBottom: "20px",
              }}
            >
              <h2>
                ✅ Required Skills
              </h2>

              {result.required_skills?.map(
                (skill: string) => (
                  <span
                    key={skill}
                    style={{
                      display:
                        "inline-block",
                      padding:
                        "8px 16px",
                      margin: "6px",
                      borderRadius:
                        "999px",
                      background:
                        "#2563eb",
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
                padding: "25px",
                borderRadius: "24px",
                marginBottom: "20px",
              }}
            >
              <h2>
                ⚠ Missing Skills
              </h2>

              {result.missing_skills?.map(
                (skill: string) => (
                  <span
                    key={skill}
                    style={{
                      display:
                        "inline-block",
                      padding:
                        "8px 16px",
                      margin: "6px",
                      borderRadius:
                        "999px",
                      background:
                        "#dc2626",
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
                padding: "25px",
                borderRadius: "24px",
              }}
            >
              <h2>
                📚 Learning Priorities
              </h2>

              {result.learning_priorities?.map(
                (
                  item: any,
                  index: number
                ) => (
                  <div
                    key={index}
                    style={{
                      marginBottom:
                        "15px",
                    }}
                  >
                    <strong>
                      {item.skill}
                    </strong>

                    <p>
                      {
                        item.reason
                      }
                    </p>

                    <small>
                      Resource:{" "}
                      {
                        item.resource
                      }
                    </small>
                  </div>
                )
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}