import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const navigate = useNavigate();

  const cards = [
    {
      title: "Resume Analysis",
      icon: "📄",
      route: "/resume",
      desc: "Analyze ATS score and resume quality",
    },
    {
      title: "Job Match",
      icon: "🎯",
      route: "/job-match",
      desc: "Compare your resume with job descriptions",
    },
    {
      title: "Skill Gap Analysis",
      icon: "📈",
      route: "/skills",
      desc: "Identify missing skills for your target role",
    },
    {
      title: "AI Roadmap",
      icon: "🗺️",
      route: "/roadmap",
      desc: "Generate personalized learning roadmaps",
    },
    {
      title: "Interview Preparation",
      icon: "🎤",
      route: "/interview",
      desc: "Generate company-specific interview questions",
    },
  ];

  const stats = [
    {
      title: "AI Features",
      value: "5/5",
      subtitle: "Active",
    },
    {
      title: "AI Provider",
      value: "Gemini",
      subtitle: "Google AI",
    },
    {
      title: "System",
      value: "Online",
      subtitle: "Operational",
    },
    {
      title: "Version",
      value: "1.0",
      subtitle: "Production",
    },
  ];

  return (
    <div
      style={{
        minHeight: "100vh",
        background:
          "linear-gradient(135deg,#020617,#0f172a,#1e293b)",
        color: "white",
        display: "flex",
      }}
    >
      {/* Sidebar */}
      <div
        style={{
          width: "260px",
          background: "rgba(255,255,255,0.04)",
          borderRight:
            "1px solid rgba(255,255,255,0.1)",
          padding: "30px",
        }}
      >
        <h2>🚀 AI Placement Copilot</h2>

        <div style={{ marginTop: "40px" }}>
          <div
            style={{
              marginBottom: "20px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/")}
          >
            🏠 Dashboard
          </div>

          <div
            style={{
              marginBottom: "20px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/resume")}
          >
            📄 Resume Analysis
          </div>

          <div
            style={{
              marginBottom: "20px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/job-match")}
          >
            🎯 Job Match
          </div>

          <div
            style={{
              marginBottom: "20px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/skills")}
          >
            📈 Skill Gap
          </div>

          <div
            style={{
              marginBottom: "20px",
              cursor: "pointer",
            }}
            onClick={() => navigate("/roadmap")}
          >
            🗺️ Roadmap
          </div>

          <div
            style={{
              cursor: "pointer",
            }}
            onClick={() => navigate("/interview")}
          >
            🎤 Interview Prep
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div
        style={{
          flex: 1,
          padding: "40px",
        }}
      >
        <h1
          style={{
            fontSize: "56px",
            marginBottom: "10px",
          }}
        >
          AI Placement Copilot 🚀
        </h1>

        <p
          style={{
            color: "#94a3b8",
            marginBottom: "40px",
            fontSize: "18px",
          }}
        >
          Your AI-powered placement preparation
          platform powered by Gemini.
        </p>

        {/* Stats */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(auto-fit,minmax(220px,1fr))",
            gap: "20px",
            marginBottom: "50px",
          }}
        >
          {stats.map((item) => (
            <div
              key={item.title}
              style={{
                background:
                  "rgba(255,255,255,0.05)",
                borderRadius: "24px",
                padding: "25px",
                border:
                  "1px solid rgba(255,255,255,0.1)",
              }}
            >
              <h4
                style={{
                  color: "#94a3b8",
                }}
              >
                {item.title}
              </h4>

              <h1
                style={{
                  marginTop: "10px",
                  fontSize: "42px",
                }}
              >
                {item.value}
              </h1>

              <p
                style={{
                  color: "#94a3b8",
                }}
              >
                {item.subtitle}
              </p>
            </div>
          ))}
        </div>

        <h2
          style={{
            marginBottom: "25px",
          }}
        >
          AI Career Tools
        </h2>

        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(auto-fit,minmax(280px,1fr))",
            gap: "25px",
          }}
        >
          {cards.map((card) => (
            <div
              key={card.title}
              onClick={() =>
                navigate(card.route)
              }
              style={{
                cursor: "pointer",
                background:
                  "rgba(255,255,255,0.05)",
                borderRadius: "24px",
                padding: "30px",
                border:
                  "1px solid rgba(255,255,255,0.1)",
                transition:
                  "all 0.3s ease",
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform =
                  "translateY(-6px)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform =
                  "translateY(0px)";
              }}
            >
              <div
                style={{
                  fontSize: "50px",
                  marginBottom: "15px",
                }}
              >
                {card.icon}
              </div>

              <h2>{card.title}</h2>

              <p
                style={{
                  color: "#94a3b8",
                }}
              >
                {card.desc}
              </p>

              <button
                style={{
                  marginTop: "15px",
                  padding:
                    "10px 18px",
                  borderRadius:
                    "10px",
                  border: "none",
                  background:
                    "#3b82f6",
                  color: "white",
                  cursor: "pointer",
                }}
              >
                Open Tool
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}