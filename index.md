---
layout: page
full-width: true
---
<!-- Note: portfolio.md has title/subtitle for /portfolio URL; this index.md omits them for / landing page -->

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
  background: linear-gradient(90deg, #ff7b00 0%, #e65100 100%);
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
  border: 1px solid rgba(255, 123, 0, 0.1);
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
  background: linear-gradient(90deg, #ff7b00 0%, #e65100 50%, #ffab40 100%);
}

.project-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(255, 123, 0, 0.2);
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
  background: linear-gradient(135deg, #ff7b00 0%, #e65100 100%);
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
  color: #ff7b00;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.project-link:hover {
  color: #e65100;
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
  border-left: 4px solid #ff7b00;
  transition: all 0.3s ease;
}

.contribution-item:hover {
  box-shadow: 0 4px 20px rgba(255, 123, 0, 0.15);
  border-left-color: #e65100;
}

.contribution-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #ff7b00 0%, #e65100 100%);
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
  color: #ff7b00;
  text-decoration: none;
}

.contribution-content a:hover {
  text-decoration: underline;
}

/* Skills Section - Option 3: Deep Orange */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.skill-category {
  background: linear-gradient(135deg, #c45000 0%, #b34700 50%, #e65100 100%);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 8px 24px rgba(196, 80, 0, 0.3);
  transition: all 0.3s ease;
}

.skill-category:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(196, 80, 0, 0.4);
}

.skill-category h4 {
  color: #ffd93d;
  margin-bottom: 1rem;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

.skill-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.skill-item {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.85rem;
  transition: all 0.2s;
}

.skill-item:hover {
  background: rgba(255, 255, 255, 0.35);
  color: #ffd93d;
}

/* Quote section */
.quote-section {
  text-align: center;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, #c45000 0%, #b34700 50%, #e65100 100%);
  border-radius: 20px;
  margin: 3rem 0;
  color: white;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.quote-section blockquote {
  font-size: 1.8rem;
  font-weight: 600;
  font-style: normal;
  margin-bottom: 1rem;
  border: none;
  padding: 0.5rem 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  letter-spacing: 0.05em;
  position: relative;
  min-height: 2.5em;
}

.sanskrit-quote {
  display: block;
  position: relative;
}

.typewriter-text {
  display: inline-block;
  border-right: 3px solid white;
  animation: blink 0.7s step-end infinite;
  white-space: nowrap;
  overflow: hidden;
}

@keyframes blink {
  0%, 100% { border-color: white; }
  50% { border-color: transparent; }
}

.quote-section cite {
  font-size: 1rem;
  opacity: 1;
  display: block;
  margin-top: 0.5rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
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
  background: linear-gradient(135deg, #ff7b00 0%, #e65100 100%);
  color: white;
}

.cta-btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(255, 123, 0, 0.4);
}

.cta-btn.secondary {
  background: white;
  color: #ff7b00;
  border: 2px solid #ff7b00;
}

.cta-btn.secondary:hover {
  background: #ff7b00;
  color: white;
}

/* Carousel Styles */
.carousel-section {
  margin: 3rem 0;
  overflow: hidden;
}

.carousel-container {
  position: relative;
  width: 100%;
  overflow: hidden;
  padding: 1rem 0;
}

.carousel-track {
  display: flex;
  gap: 1.5rem;
  animation: scroll 30s linear infinite;
  width: max-content;
}

.carousel-track:hover {
  animation-play-state: paused;
}

@keyframes scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(calc(-50% - 0.75rem));
  }
}

/* Option 3: Deep Orange for Merged Cards */
.merged-card {
  flex-shrink: 0;
  width: 320px;
  background: linear-gradient(135deg, #c45000 0%, #b34700 50%, #e65100 100%);
  border-radius: 16px;
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 24px rgba(196, 80, 0, 0.3);
}

.merged-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #ffab40 0%, #ffd93d 100%);
}

.merged-card::after {
  content: '✓ MERGED';
  position: absolute;
  top: 12px;
  right: 12px;
  background: linear-gradient(135deg, #ffd93d 0%, #ffab40 100%);
  color: #7a3300;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  letter-spacing: 0.5px;
}

.merged-card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 20px 40px rgba(196, 80, 0, 0.4);
}

.merged-card-icon {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.merged-card h4 {
  color: #ffffff;
  font-size: 1rem;
  font-weight: 600;
  margin: 0 0 0.5rem 0;
  line-height: 1.3;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

.merged-card .repo-name {
  color: #ffd93d;
  font-size: 0.8rem;
  font-weight: 500;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.merged-card .repo-name svg {
  width: 14px;
  height: 14px;
}

.merged-card p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.85rem;
  line-height: 1.5;
  margin: 0 0 1rem 0;
}

.merged-card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1rem;
}

.merged-tag {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 500;
}

.merged-card-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: #ffd93d;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.2s;
}

.merged-card-link:hover {
  color: #ffffff;
  gap: 0.6rem;
}

/* Option 1: Dark + Orange Accents for Ongoing Cards */
.ongoing-card {
  flex-shrink: 0;
  width: 320px;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  border-radius: 16px;
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.ongoing-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #ff7b00 0%, #e65100 50%, #ffab40 100%);
}

.ongoing-card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 20px 40px rgba(255, 123, 0, 0.2);
}

.ongoing-card .merged-card-icon {
  background: linear-gradient(135deg, rgba(255, 123, 0, 0.2) 0%, rgba(230, 81, 0, 0.2) 100%);
}

.ongoing-card h4 {
  color: #ffffff;
  font-size: 1rem;
  font-weight: 600;
  margin: 0 0 0.5rem 0;
  line-height: 1.3;
}

.ongoing-card .repo-name {
  color: #ff7b00;
  font-size: 0.8rem;
  font-weight: 500;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.ongoing-card .repo-name svg {
  width: 14px;
  height: 14px;
}

.ongoing-card p {
  color: #a0aec0;
  font-size: 0.85rem;
  line-height: 1.5;
  margin: 0 0 1rem 0;
}

.ongoing-card .merged-tag {
  background: rgba(255, 123, 0, 0.2);
  color: #ffab40;
}

.ongoing-card .merged-card-link {
  color: #ff7b00;
}

.ongoing-card .merged-card-link:hover {
  color: #ffab40;
}

.carousel-controls {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 1.5rem;
}

.carousel-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #cbd5e0;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
}

.carousel-dot.active,
.carousel-dot:hover {
  background: linear-gradient(135deg, #ff7b00 0%, #e65100 100%);
  transform: scale(1.2);
}

.merged-stats {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin-top: 2rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, rgba(255, 123, 0, 0.05) 0%, rgba(230, 81, 0, 0.08) 100%);
  border-radius: 12px;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, #ff7b00 0%, #e65100 50%, #c45000 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  color: #5a6c7d;
  font-size: 0.85rem;
  margin-top: 0.25rem;
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
  
  .merged-card {
    width: 280px;
  }
  
  .merged-stats {
    gap: 1.5rem;
    flex-wrap: wrap;
  }
  
  .stat-number {
    font-size: 2rem;
  }
}
</style>

<div class="portfolio-section carousel-section">
  <div class="portfolio-header">
    <h2>Merged Contributions</h2>
  </div>
  
  <div class="carousel-container">
    <div class="carousel-track">
      <!-- First set of cards -->
      <div class="merged-card">
        <div class="merged-card-icon">🤖</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          OpenHands/OpenHands
        </div>
        <h4>Dismissible Error Banner UX</h4>
        <p>Improved frontend error banner with dismiss and expand functionality.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">TypeScript</span>
          <span class="merged-tag">React</span>
          <span class="merged-tag">UX</span>
        </div>
        <a href="https://github.com/OpenHands/OpenHands/pull/12354" class="merged-card-link" target="_blank">
          View PR #12354 →
        </a>
      </div>
      
      <div class="merged-card">
        <div class="merged-card-icon">🧪</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          tox-dev/tox
        </div>
        <h4>Fix misleading ENVDIR reference</h4>
        <p>Aligned devenv docs with the actual CLI parameter to avoid confusion.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">Docs</span>
          <span class="merged-tag">CLI</span>
        </div>
        <a href="https://github.com/tox-dev/tox/pull/3670" class="merged-card-link" target="_blank">
          View PR #3670 →
        </a>
      </div>

      <div class="merged-card">
        <div class="merged-card-icon">🔧</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          jd/tenacity
        </div>
        <h4>Fix wait_chain docstring syntax</h4>
        <p>Repaired the example to prevent syntax errors when copied by users.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">Docs</span>
          <span class="merged-tag">Resilience</span>
        </div>
        <a href="https://github.com/jd/tenacity/pull/548" class="merged-card-link" target="_blank">
          View PR #548 →
        </a>
      </div>

      <div class="merged-card">
        <div class="merged-card-icon">📦</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          pnpm/pnpm
        </div>
        <h4>Show workspace versions on mismatch</h4>
        <p>Improved workspace resolution hints to speed up monorepo troubleshooting.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">JavaScript</span>
          <span class="merged-tag">CLI</span>
          <span class="merged-tag">Monorepo</span>
        </div>
        <a href="https://github.com/pnpm/pnpm/pull/10466" class="merged-card-link" target="_blank">
          View PR #10466 →
        </a>
      </div>
      
      <div class="merged-card">
        <div class="merged-card-icon">🔥</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          infiniflow/ragflow
        </div>
        <h4>Chunk Retrieval Fix</h4>
        <p>Ensure deleted chunks are not returned in retrieval results.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">RAG</span>
          <span class="merged-tag">Backend</span>
        </div>
        <a href="https://github.com/infiniflow/ragflow/pull/12546" class="merged-card-link" target="_blank">
          View PR #12546 →
        </a>
      </div>
      
      <div class="merged-card">
        <div class="merged-card-icon">🎯</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          optuna/optuna
        </div>
        <h4>Replace .format() with f-strings</h4>
        <p>Modernized string formatting in codebase using Python f-strings for better readability.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">ML</span>
          <span class="merged-tag">Refactor</span>
        </div>
        <a href="https://github.com/optuna/optuna/pull/6412" class="merged-card-link" target="_blank">
          View PR #6412 →
        </a>
      </div>
      
      <!-- Duplicate set for infinite scroll effect -->
      <div class="merged-card">
        <div class="merged-card-icon">🤖</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          OpenHands/OpenHands
        </div>
        <h4>Dismissible Error Banner UX</h4>
        <p>Improved frontend error banner with dismiss and expand functionality.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">TypeScript</span>
          <span class="merged-tag">React</span>
          <span class="merged-tag">UX</span>
        </div>
        <a href="https://github.com/OpenHands/OpenHands/pull/12354" class="merged-card-link" target="_blank">
          View PR #12354 →
        </a>
      </div>
      
      <div class="merged-card">
        <div class="merged-card-icon">🧪</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          tox-dev/tox
        </div>
        <h4>Fix misleading ENVDIR reference</h4>
        <p>Aligned devenv docs with the actual CLI parameter to avoid confusion.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">Docs</span>
          <span class="merged-tag">CLI</span>
        </div>
        <a href="https://github.com/tox-dev/tox/pull/3670" class="merged-card-link" target="_blank">
          View PR #3670 →
        </a>
      </div>

      <div class="merged-card">
        <div class="merged-card-icon">🔧</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          jd/tenacity
        </div>
        <h4>Fix wait_chain docstring syntax</h4>
        <p>Repaired the example to prevent syntax errors when copied by users.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">Docs</span>
          <span class="merged-tag">Resilience</span>
        </div>
        <a href="https://github.com/jd/tenacity/pull/548" class="merged-card-link" target="_blank">
          View PR #548 →
        </a>
      </div>

      <div class="merged-card">
        <div class="merged-card-icon">📦</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          pnpm/pnpm
        </div>
        <h4>Show workspace versions on mismatch</h4>
        <p>Improved workspace resolution hints to speed up monorepo troubleshooting.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">JavaScript</span>
          <span class="merged-tag">CLI</span>
          <span class="merged-tag">Monorepo</span>
        </div>
        <a href="https://github.com/pnpm/pnpm/pull/10466" class="merged-card-link" target="_blank">
          View PR #10466 →
        </a>
      </div>
      
      <div class="merged-card">
        <div class="merged-card-icon">🔥</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          infiniflow/ragflow
        </div>
        <h4>Chunk Retrieval Fix</h4>
        <p>Ensure deleted chunks are not returned in retrieval results.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">RAG</span>
          <span class="merged-tag">Backend</span>
        </div>
        <a href="https://github.com/infiniflow/ragflow/pull/12546" class="merged-card-link" target="_blank">
          View PR #12546 →
        </a>
      </div>
      
      <div class="merged-card">
        <div class="merged-card-icon">🎯</div>
        <div class="repo-name">
          <svg viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
          optuna/optuna
        </div>
        <h4>Replace .format() with f-strings</h4>
        <p>Modernized string formatting in codebase using Python f-strings for better readability.</p>
        <div class="merged-card-tags">
          <span class="merged-tag">Python</span>
          <span class="merged-tag">ML</span>
          <span class="merged-tag">Refactor</span>
        </div>
        <a href="https://github.com/optuna/optuna/pull/6412" class="merged-card-link" target="_blank">
          View PR #6412 →
        </a>
      </div>
    </div>
  </div>
  
  <div class="merged-stats">
    <div class="stat-item">
      <div class="stat-number">30</div>
      <div class="stat-label">PRs Merged</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">53</div>
      <div class="stat-label">Ongoing PRs</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">5</div>
      <div class="stat-label">Languages</div>
    </div>
    <div class="stat-item">
      <div class="stat-number">80+</div>
      <div class="stat-label">Repos Contributed</div>
    </div>
  </div>
</div>

<div class="portfolio-section carousel-section">
  <div class="portfolio-header">
    <h2>🔥 Ongoing Contributions</h2>
  </div>
  
  <div class="carousel-container">
    <div class="carousel-track" style="animation-duration: 60s;">
      <div class="ongoing-card">
        <div class="merged-card-icon">🤖</div>
        <div class="repo-name">vllm-project/vllm</div>
        <h4>KV Cache Refactor</h4>
        <p>Refactoring KV cache updates across attention backends.</p>
        <div class="merged-card-tags"><span class="merged-tag">Python</span><span class="merged-tag">CUDA</span></div>
        <a href="https://github.com/vllm-project/vllm/pull/32509" class="merged-card-link">View PR #32509 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🧠</div>
        <div class="repo-name">stanfordnlp/dspy</div>
        <h4>Cost Tracking</h4>
        <p>Add cost tracking with budget constraints for LLM calls.</p>
        <div class="merged-card-tags"><span class="merged-tag">Python</span><span class="merged-tag">AI</span></div>
        <a href="https://github.com/stanfordnlp/dspy/pull/9207" class="merged-card-link">View PR #9207 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🚀</div>
        <div class="repo-name">crewAIInc/crewAI</div>
        <h4>OpenAI Responses API</h4>
        <p>Add OpenAI Responses API integration with streaming.</p>
        <div class="merged-card-tags"><span class="merged-tag">Python</span><span class="merged-tag">AI</span></div>
        <a href="https://github.com/crewAIInc/crewAI/pull/4248" class="merged-card-link">View PR #4248 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🔗</div>
        <div class="repo-name">langchain-ai/langchain</div>
        <h4>vLLM Fix</h4>
        <p>Handle null choices from model_dump() for vLLM compatibility.</p>
        <div class="merged-card-tags"><span class="merged-tag">Python</span><span class="merged-tag">LLM</span></div>
        <a href="https://github.com/langchain-ai/langchain/pull/34791" class="merged-card-link">View PR #34791 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">⚡</div>
        <div class="repo-name">vitejs/vite</div>
        <h4>HTML Path Fix</h4>
        <p>Handle trailing slash in htmlPath for relative URL pre-transform.</p>
        <div class="merged-card-tags"><span class="merged-tag">TypeScript</span><span class="merged-tag">Build</span></div>
        <a href="https://github.com/vitejs/vite/pull/21429" class="merged-card-link">View PR #21429 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🐳</div>
        <div class="repo-name">moby/moby</div>
        <h4>Goroutine Leak Fix</h4>
        <p>Fix goroutine leak in TestRingLogger.</p>
        <div class="merged-card-tags"><span class="merged-tag">Go</span><span class="merged-tag">Docker</span></div>
        <a href="https://github.com/moby/moby/pull/51854" class="merged-card-link">View PR #51854 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🐼</div>
        <div class="repo-name">pandas-dev/pandas</div>
        <h4>PyArrow Tests</h4>
        <p>Add test for groupby.var() pyarrow dtype retention.</p>
        <div class="merged-card-tags"><span class="merged-tag">Python</span><span class="merged-tag">Data</span></div>
        <a href="https://github.com/pandas-dev/pandas/pull/63704" class="merged-card-link">View PR #63704 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🤗</div>
        <div class="repo-name">huggingface/transformers</div>
        <h4>MobileNet Fix</h4>
        <p>Fix MobileNet v1/v2 image processor default interpolation.</p>
        <div class="merged-card-tags"><span class="merged-tag">Python</span><span class="merged-tag">ML</span></div>
        <a href="https://github.com/huggingface/transformers/pull/43313" class="merged-card-link">View PR #43313 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🦖</div>
        <div class="repo-name">facebook/docusaurus</div>
        <h4>MD Links</h4>
        <p>Add support for Markdown file path links in pages plugin.</p>
        <div class="merged-card-tags"><span class="merged-tag">TypeScript</span><span class="merged-tag">Docs</span></div>
        <a href="https://github.com/facebook/docusaurus/pull/11666" class="merged-card-link">View PR #11666 →</a>
      </div>
      <div class="ongoing-card">
        <div class="merged-card-icon">🌬️</div>
        <div class="repo-name">apache/airflow</div>
        <h4>E2E Tests</h4>
        <p>Add E2E tests for Pools and Variables page functionality.</p>
        <div class="merged-card-tags"><span class="merged-tag">Python</span><span class="merged-tag">DevOps</span></div>
        <a href="https://github.com/apache/airflow/pull/60592" class="merged-card-link">View PR #60592 →</a>
      </div>
    </div>
  </div>
</div>

<div class="portfolio-section">
  <div class="portfolio-header">
    <h2>🚀 Featured Projects</h2>
  </div>
  
  <div class="project-grid">
    <!-- <div class="carousel-container">
    <div class="carousel-track" style="animation-duration: 120s;"> -->

            <div class="project-card">
      <h3>दीर्घायु (Dīrghayu) - DNA Analysis</h3>
      <p>India-First Longevity Genomics Platform for Whole Genome Analysis with AI-powered health insights.</p>
      <div class="project-tags">
        <span class="tag">MedTech</span>
        <span class="tag secondary">Biopython</span>
        <span class="tag accent">Genomics</span>
        <span class="tag accent">DNA Mapping and Analysis</span>
      </div>
      <a href="https://github.com/VedantMadane/dirghayu" class="project-link">
        Map My DNA for Hereditary Risks
      </a>
    </div>

        <div class="project-card">
      <h3>वेदयुत्  (vedyut) - Sanskrit Grammar Parser</h3>
      <p>High-performance Sanskrit NLP toolkit with Rust core + Python bindings using FastAPI REST API which is LLM-ready.</p>
      <div class="project-tags">
        <span class="tag">NLP</span>
        <span class="tag secondary">Sanskrit</span>
        <span class="tag accent">Computational Linguistics</span>
      </div>
      <a href="https://github.com/VedantMadane/vedyut" class="project-link">
        Generate Language →
      </a>
    </div>

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
<!-- </div></div> -->
  </div>
</div>

<!--
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
-->

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
  <blockquote class="sanskrit-quote">
    <span class="typewriter-text" id="sanskrit-typewriter"></span>
  </blockquote>
  <cite>— What exists here may be found elsewhere; what does not exist here exists nowhere.</cite>
</div>

<script>
(function() {
  const quotes = [
    'यत् इह अस्ति तत् अन्यत्र यत् न अस्ति न तत् क्वचित्',
    'यद् इह अस्ति तद् अन्यत्र यद् न अस्ति न तद् क्वचित्',
    'यदिह अस्ति तदन्यत्र यद्न अस्ति न तद्क्वचित्',
    'यदिहास्ति तदन्यत्र यद्नास्ति न तद्क्वचित्'
  ];
  
  // Split into grapheme clusters for proper Devanagari handling
  function toGraphemes(str) {
    if (typeof Intl !== 'undefined' && Intl.Segmenter) {
      return [...new Intl.Segmenter().segment(str)].map(s => s.segment);
    }
    // Fallback: split by spaces and treat each word as unit
    return str.split(/(\s+)/).filter(s => s.length > 0);
  }
  
  let quoteIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let currentGraphemes = [];
  const element = document.getElementById('sanskrit-typewriter');
  const typeSpeed = 100;
  const deleteSpeed = 50;
  const pauseTime = 2000;
  
  function typeWriter() {
    if (currentGraphemes.length === 0) {
      currentGraphemes = toGraphemes(quotes[quoteIndex]);
    }
    
    if (isDeleting) {
      charIndex--;
      element.textContent = currentGraphemes.slice(0, charIndex).join('');
    } else {
      charIndex++;
      element.textContent = currentGraphemes.slice(0, charIndex).join('');
    }
    
    let delay = isDeleting ? deleteSpeed : typeSpeed;
    
    if (!isDeleting && charIndex === currentGraphemes.length) {
      delay = pauseTime;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      quoteIndex = (quoteIndex + 1) % quotes.length;
      currentGraphemes = toGraphemes(quotes[quoteIndex]);
      delay = 500;
    }
    
    setTimeout(typeWriter, delay);
  }
  
  if (element) {
    typeWriter();
  }
})();
</script>

<div class="contact-cta">
  <h3>Let's Build Something Together</h3>
  <p>Interested in collaborating on open source, NLP or Sanskrit computational linguistics?</p>
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
