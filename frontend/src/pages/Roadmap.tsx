import { useState } from "react";
import api from "../api/axios";

export default function Roadmap() {
  const [targetRole, setTargetRole] = useState("");
  const [targetCompany, setTargetCompany] = useState("");
  const [weeklyHours, setWeeklyHours] = useState(10);
  const [currentSkills, setCurrentSkills] = useState("");

  const [loading, setLoading] = useState(false);
  const [roadmap, setRoadmap] = useState<any>(null);

  const generateRoadmap = async () => {
    try {
      setLoading(true);

      const response = await api.post(
        "/roadmap/generate",
        {
          target_role: targetRole,
          target_company: targetCompany,
          weekly_hours: weeklyHours,
          current_skills: currentSkills
            .split(",")
            .map((s) => s.trim())
            .filter(Boolean),
        }
      );

      setRoadmap(response.data);
    } catch (error: any) {
      console.error(error);

      alert(
        error?.response?.data?.detail ||
          "Roadmap generation failed"
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
        <h1>🗺️ AI Roadmap Generator</h1>

        <p
          style={{
            color: "#94a3b8",
            marginBottom: "20px",
          }}
        >
          Generate a personalized placement roadmap
        </p>

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
            placeholder="Target Role (e.g. Data Analyst)"
            style={{
              width: "100%",
              padding: "15px",
              marginBottom: "15px",
              borderRadius: "12px",
              border: "none",
            }}
          />

          <input
            value={targetCompany}
            onChange={(e) =>
              setTargetCompany(e.target.value)
            }
            placeholder="Target Company (e.g. JPMorgan)"
            style={{
              width: "100%",
              padding: "15px",
              marginBottom: "15px",
              borderRadius: "12px",
              border: "none",
            }}
          />

          <label
            style={{
              display: "block",
              marginBottom: "8px",
              color: "#cbd5e1",
            }}
          >
            Weekly Study Hours
          </label>

          <input
            type="number"
            value={weeklyHours}
            onChange={(e) =>
              setWeeklyHours(
                Number(e.target.value)
              )
            }
            placeholder="10"
            style={{
              width: "100%",
              padding: "15px",
              marginBottom: "15px",
              borderRadius: "12px",
              border: "none",
            }}
          />

          <textarea
            value={currentSkills}
            onChange={(e) =>
              setCurrentSkills(
                e.target.value
              )
            }
            rows={5}
            placeholder="Python, SQL, Excel"
            style={{
              width: "100%",
              padding: "15px",
              borderRadius: "12px",
              border: "none",
            }}
          />

          <button
            onClick={generateRoadmap}
            disabled={loading}
            style={{
              marginTop: "20px",
              background: "#8b5cf6",
              color: "white",
              border: "none",
              padding: "14px 28px",
              borderRadius: "12px",
              cursor: "pointer",
            }}
          >
            {loading
              ? "Generating..."
              : "Generate Roadmap"}
          </button>
        </div>

        {roadmap && (
          <div
            style={{
              marginTop: "30px",
            }}
          >
            <h2>
              🚀 {roadmap.total_weeks}
              Week Roadmap
            </h2>

            {roadmap.weeks?.map(
              (
                week: any,
                index: number
              ) => (
                <div
                  key={index}
                  style={{
                    background:
                      "rgba(255,255,255,0.05)",
                    padding: "25px",
                    borderRadius:
                      "24px",
                    marginTop: "20px",
                  }}
                >
                  <h2>
                    Week {week.week}
                  </h2>

                  <h3>
                    {week.theme}
                  </h3>

                  <p>
                    <strong>
                      Topics
                    </strong>
                  </p>

                  <ul>
                    {week.topics?.map(
                      (
                        topic: string,
                        i: number
                      ) => (
                        <li
                          key={i}
                        >
                          {topic}
                        </li>
                      )
                    )}
                  </ul>

                  <p>
                    <strong>
                      Resources
                    </strong>
                  </p>

                  <ul>
                    {week.resources?.map(
                      (
                        resource: string,
                        i: number
                      ) => (
                        <li
                          key={i}
                        >
                          {resource}
                        </li>
                      )
                    )}
                  </ul>

                  <p>
                    <strong>
                      Project:
                    </strong>{" "}
                    {week.project}
                  </p>

                  <p>
                    <strong>
                      Interview Prep:
                    </strong>{" "}
                    {
                      week.interview_prep
                    }
                  </p>
                </div>
              )
            )}
          </div>
        )}
      </div>
    </div>
  );
}