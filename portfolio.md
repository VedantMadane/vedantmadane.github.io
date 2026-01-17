---
layout: page
title: Portfolio
subtitle: Building bridges between ancient wisdom and modern technology
full-width: true
---

<style>
/* Portfolio-specific styles */
.portfolio-section {
  margin: 3rem 0;
}

.portfolio-header {
  text-align: center;
  margin-bottom: 2rem;
}

.portfolio-header h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
  position: relative;
  display: inline-block;
  padding-bottom: 0.5rem;
}

.portfolio-header h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  border-radius: 2px;
}

/* Project Cards */
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
  padding: 1rem 0;
}

.project-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(102, 126, 234, 0.1);
  position: relative;
  overflow: hidden;
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
}

.project-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(102, 126, 234, 0.2);
}

.project-card h3 {
  color: #2c3e50;
  margin-bottom: 0.75rem;
  font-size: 1.25rem;
  font-weight: 600;
}

.project-card p {
  color: #5a6c7d;
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.tag {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.tag.secondary {
  background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
}

.tag.accent {
  background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%);
}

.project-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.project-link:hover {
  color: #764ba2;
}

/* Open Source Contributions */
.contribution-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.contribution-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.25rem;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  border-left: 4px solid #667eea;
  transition: all 0.3s ease;
}

.contribution-item:hover {
  box-shadow: 0 4px 20px rgba(102, 126, 234, 0.15);
  border-left-color: #764ba2;
}

.contribution-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 1.25rem;
  flex-shrink: 0;
}

.contribution-content h4 {
  margin: 0 0 0.25rem 0;
  color: #2c3e50;
  font-size: 1rem;
}

.contribution-content p {
  margin: 0;
  color: #5a6c7d;
  font-size: 0.9rem;
}

.contribution-content a {
  color: #667eea;
  text-decoration: none;
}

.contribution-content a:hover {
  text-decoration: underline;
}

/* Skills Section */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.skill-category {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
}

.skill-category h4 {
  color: #2c3e50;
  margin-bottom: 1rem;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.skill-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.skill-item {
  background: #f1f3f4;
  color: #5a6c7d;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.85rem;
  transition: all 0.2s;
}

.skill-item:hover {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

/* Quote section */
.quote-section {
  text-align: center;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  border-radius: 20px;
  margin: 3rem 0;
  color: white;
}

.quote-section blockquote {
  font-size: 1.5rem;
  font-style: italic;
  margin-bottom: 0.5rem;
  border: none;
  padding: 0;
}

.quote-section cite {
  font-size: 0.95rem;
  opacity: 0.9;
}

/* Contact CTA */
.contact-cta {
  text-align: center;
  padding: 2rem;
  background: #f8f9fa;
  border-radius: 16px;
  margin-top: 2rem;
}

.contact-cta h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.cta-buttons {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.cta-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s;
}

.cta-btn.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.cta-btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.cta-btn.secondary {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
}

.cta-btn.secondary:hover {
  background: #667eea;
  color: white;
}

@media (max-width: 768px) {
  .project-grid {
    grid-template-columns: 1fr;
  }
  
  .contribution-item {
    flex-direction: column;
    text-align: center;
  }
  
  .contribution-icon {
    margin: 0 auto;
  }
}
</style>

<div class="portfolio-section">
  <div class="portfolio-header">
    <h2>🚀 Featured Projects</h2>
  </div>
  
  <div class="project-grid">
    <div class="project-card">
      <h3>महाभारत (Mahābhārata) NLP Pipeline</h3>
      <p>A comprehensive NLP pipeline for processing and analyzing the Sanskrit epic Mahābhārata. Features text preprocessing, morphological analysis, and semantic search capabilities.</p>
      <div class="project-tags">
        <span class="tag">Sanskrit</span>
        <span class="tag secondary">NLP</span>
        <span class="tag accent">Python</span>
      </div>
      <a href="https://vedantmadane.github.io/maha/poster" class="project-link">
        View Project →
      </a>
    </div>
    
    <div class="project-card">
      <h3>पक्षी (Pakshī) - Bird Identification</h3>
      <p>An interactive web application for identifying Indian bird species using machine learning. Built with modern web technologies and computer vision models.</p>
      <div class="project-tags">
        <span class="tag">ML</span>
        <span class="tag secondary">Computer Vision</span>
        <span class="tag accent">JavaScript</span>
      </div>
      <a href="https://vedantmadane.github.io/pakshi/" class="project-link">
        Play Now →
      </a>
    </div>
    
    <div class="project-card">
      <h3>Real-time Face Detection</h3>
      <p>Browser-based multi-face detection system using WebRTC and TensorFlow.js. Detects and tracks multiple faces in real-time with bounding boxes.</p>
      <div class="project-tags">
        <span class="tag">TensorFlow.js</span>
        <span class="tag secondary">WebRTC</span>
        <span class="tag accent">Real-time</span>
      </div>
      <a href="https://vedantmadane.github.io/mkcl/camera/detect/#/" class="project-link">
        Try Demo →
      </a>
    </div>
    
    <div class="project-card">
      <h3>Posture Detection System</h3>
      <p>AI-powered posture analysis tool that helps users maintain proper sitting posture. Uses pose estimation to provide real-time feedback.</p>
      <div class="project-tags">
        <span class="tag">Pose Estimation</span>
        <span class="tag secondary">AI</span>
        <span class="tag accent">Health Tech</span>
      </div>
      <a href="https://vedantmadane.github.io/mkcl/camera/posture/" class="project-link">
        Launch App →
      </a>
    </div>
    
    <div class="project-card">
      <h3>Telecom Analytics Dashboard</h3>
      <p>Data visualization dashboard for telecom sector analytics, featuring interactive charts and real-time data processing capabilities.</p>
      <div class="project-tags">
        <span class="tag">Data Viz</span>
        <span class="tag secondary">Analytics</span>
        <span class="tag accent">Vue.js</span>
      </div>
      <a href="https://vedantmadane.github.io/telecom/" class="project-link">
        Explore →
      </a>
    </div>
    
    <div class="project-card">
      <h3>दानव (Dānav) - Sanskrit Game</h3>
      <p>An educational game that teaches Sanskrit vocabulary through interactive gameplay. Combines language learning with entertainment.</p>
      <div class="project-tags">
        <span class="tag">EdTech</span>
        <span class="tag secondary">Sanskrit</span>
        <span class="tag accent">Game Dev</span>
      </div>
      <a href="https://vedantmadane.github.io/krida/danav/" class="project-link">
        Play Game →
      </a>
    </div>
  </div>
</div>

<div class="portfolio-section">
  <div class="portfolio-header">
    <h2>🌟 Open Source Contributions</h2>
  </div>
  
  <div class="contribution-list">
    <div class="contribution-item">
      <div class="contribution-icon">🤖</div>
      <div class="contribution-content">
        <h4>CrewAI - OpenAI Responses API Integration</h4>
        <p>Implemented support for OpenAI's new Responses API with structured outputs, streaming, and tool calling. <a href="https://github.com/crewAIInc/crewAI/pull/4248" target="_blank">PR #4248</a></p>
      </div>
    </div>
    
    <div class="contribution-item">
      <div class="contribution-icon">🦙</div>
      <div class="contribution-content">
        <h4>LanceDB - BigInt Row ID Support</h4>
        <p>Fixed TypeScript bindings to properly handle 64-bit row IDs using BigInt, resolving precision loss issues. <a href="https://github.com/lancedb/lancedb/pull/2944" target="_blank">PR #2944</a></p>
      </div>
    </div>
    
    <div class="contribution-item">
      <div class="contribution-icon">🐼</div>
      <div class="contribution-content">
        <h4>Pandas - PyArrow dtype retention</h4>
        <p>Added tests ensuring groupby aggregations preserve PyArrow float64 dtype with arrow-backed input. <a href="https://github.com/pandas-dev/pandas" target="_blank">pandas-dev/pandas</a></p>
      </div>
    </div>
    
    <div class="contribution-item">
      <div class="contribution-icon">🦖</div>
      <div class="contribution-content">
        <h4>Docusaurus - Markdown link resolution</h4>
        <p>Implemented cross-page markdown link resolution for the content-pages plugin with comprehensive tests. <a href="https://github.com/facebook/docusaurus/pull/11666" target="_blank">PR #11666</a></p>
      </div>
    </div>
    
    <div class="contribution-item">
      <div class="contribution-icon">🔥</div>
      <div class="contribution-content">
        <h4>RAGFlow - Docker pip installation fix</h4>
        <p>Fixed ModuleNotFoundError for pip in uv-based Docker builds by ensuring pip is installed in the virtual environment. <a href="https://github.com/infiniflow/ragflow" target="_blank">infiniflow/ragflow</a></p>
      </div>
    </div>
    
    <div class="contribution-item">
      <div class="contribution-icon">📚</div>
      <div class="contribution-content">
        <h4>Sphinx HTMLHelp - Typo fix</h4>
        <p>Corrected a typo in the epilog message (`.htp` → `.hhp`). <a href="https://github.com/sphinx-doc/sphinxcontrib-htmlhelp" target="_blank">sphinxcontrib-htmlhelp</a></p>
      </div>
    </div>
  </div>
</div>

<div class="portfolio-section">
  <div class="portfolio-header">
    <h2>🛠️ Technical Skills</h2>
  </div>
  
  <div class="skills-grid">
    <div class="skill-category">
      <h4>💻 Languages</h4>
      <div class="skill-list">
        <span class="skill-item">Python</span>
        <span class="skill-item">JavaScript</span>
        <span class="skill-item">TypeScript</span>
        <span class="skill-item">Go</span>
        <span class="skill-item">Rust</span>
        <span class="skill-item">SQL</span>
      </div>
    </div>
    
    <div class="skill-category">
      <h4>🧠 AI/ML</h4>
      <div class="skill-list">
        <span class="skill-item">PyTorch</span>
        <span class="skill-item">TensorFlow</span>
        <span class="skill-item">scikit-learn</span>
        <span class="skill-item">spaCy</span>
        <span class="skill-item">Hugging Face</span>
        <span class="skill-item">LangChain</span>
      </div>
    </div>
    
    <div class="skill-category">
      <h4>🌐 Web</h4>
      <div class="skill-list">
        <span class="skill-item">React</span>
        <span class="skill-item">Vue.js</span>
        <span class="skill-item">Node.js</span>
        <span class="skill-item">FastAPI</span>
        <span class="skill-item">WebRTC</span>
        <span class="skill-item">REST APIs</span>
      </div>
    </div>
    
    <div class="skill-category">
      <h4>🔧 Tools & Infra</h4>
      <div class="skill-list">
        <span class="skill-item">Docker</span>
        <span class="skill-item">Git</span>
        <span class="skill-item">Linux</span>
        <span class="skill-item">CI/CD</span>
        <span class="skill-item">PostgreSQL</span>
        <span class="skill-item">Redis</span>
      </div>
    </div>
    
    <div class="skill-category">
      <h4>📖 NLP & Languages</h4>
      <div class="skill-list">
        <span class="skill-item">Sanskrit</span>
        <span class="skill-item">Hindi</span>
        <span class="skill-item">Marathi</span>
        <span class="skill-item">Russian</span>
        <span class="skill-item">Morphological Analysis</span>
        <span class="skill-item">Text Processing</span>
      </div>
    </div>
    
    <div class="skill-category">
      <h4>📊 Data</h4>
      <div class="skill-list">
        <span class="skill-item">Pandas</span>
        <span class="skill-item">Polars</span>
        <span class="skill-item">NumPy</span>
        <span class="skill-item">Dask</span>
        <span class="skill-item">Data Visualization</span>
        <span class="skill-item">ETL Pipelines</span>
      </div>
    </div>
  </div>
</div>

<div class="quote-section">
  <blockquote>
    "यदिहास्ति तदन्यत्र यन्नेहास्ति न तत्क्वचित्"
  </blockquote>
  <cite>— What exists here may be found elsewhere; what does not exist here exists nowhere.</cite>
</div>

<div class="contact-cta">
  <h3>Let's Build Something Together</h3>
  <p>Interested in collaborating on open source, NLP, or Sanskrit computational linguistics?</p>
  <div class="cta-buttons">
    <a href="https://github.com/VedantMadane" class="cta-btn primary" target="_blank">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
      </svg>
      GitHub
    </a>
    <a href="https://linkedin.com/in/vedant-madane-7b129ba8" class="cta-btn secondary" target="_blank">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" viewBox="0 0 16 16">
        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
      </svg>
      LinkedIn
    </a>
  </div>
</div>
