import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Resume from "./pages/Resume";
import JobMatch from "./pages/JobMatchPage";
import Skills from "./pages/Skills";
import Roadmap from "./pages/Roadmap";
import Interview from "./pages/Interview";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/resume"
          element={<Resume />}
        />

        <Route
          path="/job-match"
          element={<JobMatch />}
        />

        <Route
          path="/skills"
          element={<Skills />}
        />

        <Route
          path="/roadmap"
          element={<Roadmap />}
        />

        <Route
          path="/interview"
          element={<Interview />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;