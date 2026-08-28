---
layout: page
title: Open Source
subtitle: Merged pull requests across upstream projects
full-width: true
---

<style>
.oss-page {
  max-width: 820px;
  margin: 0 auto;
  padding: 0 1rem 3rem;
  color: #2c3e50;
  line-height: 1.65;
  font-size: 1.05rem;
}
.oss-intro {
  font-size: 1.1rem;
  color: #5a6c7d;
  margin-bottom: 2rem;
  padding-bottom: 1.25rem;
  border-bottom: 2px solid rgba(255, 123, 0, 0.25);
}
.oss-intro a {
  color: #e65100;
  font-weight: 600;
}
.oss-toc {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1.25rem 0 2rem;
}
.oss-toc a {
  display: inline-block;
  padding: 0.3rem 0.75rem;
  border-radius: 999px;
  background: linear-gradient(135deg, #ff7b00 0%, #e65100 100%);
  color: #fff !important;
  text-decoration: none !important;
  font-size: 0.85rem;
  font-weight: 600;
}
.oss-toc a:hover {
  filter: brightness(1.05);
}
.oss-section {
  margin: 2.25rem 0;
  padding: 1.5rem 1.5rem 1.25rem;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  border-radius: 14px;
  border: 1px solid rgba(255, 123, 0, 0.12);
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.05);
  border-left: 4px solid #ff7b00;
}
.oss-section h2 {
  margin: 0 0 0.9rem 0;
  font-size: 1.35rem;
  font-weight: 700;
  color: #2c3e50;
}
.oss-list {
  list-style: none;
  margin: 0;
  padding: 0;
}
.oss-list li {
  margin: 0;
  padding: 0.45rem 0;
  color: #3d4f5f;
  border-bottom: 1px solid rgba(0, 0, 0, 0.04);
  line-height: 1.55;
}
.oss-list li:last-child {
  border-bottom: none;
  padding-bottom: 0;
}
.oss-list a {
  color: #e65100;
  text-decoration: none;
  border-bottom: 1px solid rgba(230, 81, 0, 0.35);
}
.oss-list a:hover {
  color: #bf360c;
  border-bottom-color: #bf360c;
}
.oss-footer {
  margin-top: 2.5rem;
  padding-top: 1.25rem;
  border-top: 1px solid #e0e0e0;
  color: #78909c;
  font-size: 0.95rem;
}
.oss-footer a { color: #e65100; }
@media (max-width: 600px) {
  .oss-section { padding: 1.1rem; }
  .oss-page { font-size: 1rem; }
}
</style>

<div class="oss-page">
  <p class="oss-intro">
    A plain-language tour of upstream open-source work by
    <a href="https://github.com/VedantMadane" target="_blank" rel="noopener noreferrer">VedantMadane</a>.
    Each line is one project. Names link to the merged pull request (or repo) on GitHub.
    About 191 upstream repositories and 217+ merged PRs.
  </p>

  <nav class="oss-toc" aria-label="Sections">
    <a href="#ai">AI / ML</a>
    <a href="#data">Data</a>
    <a href="#infra">Infra</a>
    <a href="#web">Web</a>
    <a href="#python">Python</a>
    <a href="#search">Search</a>
    <a href="#security">Security</a>
    <a href="#obs">Observability</a>
    <a href="#lang">Language</a>
    <a href="#chain">Blockchain</a>
    <a href="#systems">Systems</a>
    <a href="#misc">Everything else</a>
  </nav>

<section class="oss-section" id="ai">
  <h2>AI, LLMs & ML</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/BerriAI/litellm/pull/19266" target="_blank" rel="noopener noreferrer" title="BerriAI/litellm (merged PR)"><strong>litellm</strong></a>: fixed prompt-caching when messages are plain strings</li>
  <li><a href="https://github.com/lancedb/lancedb/pull/3193" target="_blank" rel="noopener noreferrer" title="lancedb/lancedb (merged PR)"><strong>LanceDB</strong></a>: better Node vector types and bigint row IDs</li>
  <li><a href="https://github.com/bentoml/BentoML/pull/5558" target="_blank" rel="noopener noreferrer" title="bentoml/BentoML (merged PR)"><strong>BentoML</strong></a>: stopped SQLite lock storms and learned src-layout projects</li>
  <li><a href="https://github.com/deepset-ai/haystack/pull/10400" target="_blank" rel="noopener noreferrer" title="deepset-ai/haystack (merged PR)"><strong>Haystack</strong></a>: smarter document cleaning</li>
  <li><a href="https://github.com/run-llama/llama_index/pull/20537" target="_blank" rel="noopener noreferrer" title="run-llama/llama_index (merged PR)"><strong>LlamaIndex</strong></a>: gained an OpenAI-like VllmServer mode</li>
  <li><a href="https://github.com/OpenHands/OpenHands/pull/12354" target="_blank" rel="noopener noreferrer" title="OpenHands/OpenHands (merged PR)"><strong>OpenHands</strong></a>: friendlier error banner</li>
  <li><a href="https://github.com/openlit/openlit/pull/981" target="_blank" rel="noopener noreferrer" title="openlit/openlit (merged PR)"><strong>OpenLIT</strong></a>: plays nicer with newer Qdrant</li>
  <li><a href="https://github.com/infiniflow/ragflow/pull/12546" target="_blank" rel="noopener noreferrer" title="infiniflow/ragflow (merged PR)"><strong>RAGFlow</strong></a>: stopped returning deleted chunks</li>
  <li><a href="https://github.com/invoke-ai/InvokeAI/pull/1821" target="_blank" rel="noopener noreferrer" title="invoke-ai/InvokeAI (merged PR)"><strong>InvokeAI</strong></a>: fixed a broken notebook link</li>
  <li><a href="https://github.com/docker/model-runner/pull/721" target="_blank" rel="noopener noreferrer" title="docker/model-runner (merged PR)"><strong>Docker Model Runner</strong></a>: exposes richer model metadata</li>
  <li><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1215" target="_blank" rel="noopener noreferrer" title="TransformerLensOrg/TransformerLens (merged PR)"><strong>TransformerLens</strong></a>: fixed LayerNorm folding on load</li>
  <li><a href="https://github.com/optuna/optuna/pull/6418" target="_blank" rel="noopener noreferrer" title="optuna/optuna (merged PR)"><strong>Optuna</strong></a>: stopped GPSampler crashing on CUDA defaults</li>
  <li><a href="https://github.com/kedro-org/kedro/pull/5399" target="_blank" rel="noopener noreferrer" title="kedro-org/kedro (merged PR)"><strong>Kedro</strong></a>: docs now point at the right MLflow starter</li>
  <li><a href="https://github.com/onnx/onnx/pull/7684" target="_blank" rel="noopener noreferrer" title="onnx/onnx (merged PR)"><strong>ONNX</strong></a>: cleaned up evaluator tests</li>
  <li><a href="https://github.com/tensorflow/docs/pull/1898" target="_blank" rel="noopener noreferrer" title="tensorflow/docs (merged PR)"><strong>TensorFlow docs</strong></a>: notebook/doc touch-ups</li>
  <li><a href="https://github.com/mrdbourke/tensorflow-deep-learning/pull/69" target="_blank" rel="noopener noreferrer" title="mrdbourke/tensorflow-deep-learning (merged PR)"><strong>mrdbourke's TF course</strong></a>: notebook/doc touch-ups</li>
  <li><a href="https://github.com/Farzad-R/Advanced-QA-and-RAG-Series/pull/18" target="_blank" rel="noopener noreferrer" title="Farzad-R/Advanced-QA-and-RAG-Series (merged PR)"><strong>Advanced-QA-and-RAG-Series</strong></a>: fixed a dead LangChain link</li>
  <li><a href="https://github.com/NexusInitiative/AI-Agent-Advisor/pull/69" target="_blank" rel="noopener noreferrer" title="NexusInitiative/AI-Agent-Advisor (merged PR)"><strong>AI-Agent-Advisor</strong></a>: changelog</li>
  <li><a href="https://github.com/Plantcore-AI/Iteron/pull/368" target="_blank" rel="noopener noreferrer" title="Plantcore-AI/Iteron (merged PR)"><strong>Iteron</strong></a>: install PATH notes</li>
  <li><a href="https://github.com/OthmaneBlial/swiftagent/pull/9" target="_blank" rel="noopener noreferrer" title="OthmaneBlial/swiftagent (merged PR)"><strong>swiftagent</strong></a>: failed-run fixture</li>
  <li><a href="https://github.com/daichunghy/agentsmd/pull/10" target="_blank" rel="noopener noreferrer" title="daichunghy/agentsmd (merged PR)"><strong>agentsmd</strong></a>: Windows npm notes</li>
  <li><a href="https://github.com/agentic-lineage/lineage/pull/213" target="_blank" rel="noopener noreferrer" title="agentic-lineage/lineage (merged PR)"><strong>lineage</strong></a>: confirm-before-publish</li>
  <li><a href="https://github.com/LAA-Software-Engineering/raglogs/pull/90" target="_blank" rel="noopener noreferrer" title="LAA-Software-Engineering/raglogs (merged PR)"><strong>raglogs</strong></a>: better trigger diffs</li>
  <li><a href="https://github.com/lablup/mlxcel/pull/1393" target="_blank" rel="noopener noreferrer" title="lablup/mlxcel (merged PR)"><strong>mlxcel</strong></a>: docs cleanup</li>
  <li><a href="https://github.com/Terminay/leanpass/pull/40" target="_blank" rel="noopener noreferrer" title="Terminay/leanpass (merged PR)"><strong>leanpass</strong></a>: divide-by-zero guard</li>
  <li><a href="https://github.com/JohannsenLum/canvas-api-mcp/pull/37" target="_blank" rel="noopener noreferrer" title="JohannsenLum/canvas-api-mcp (merged PR)"><strong>canvas-api-mcp</strong></a>: configurable timeout</li>
  <li><a href="https://github.com/JohannsenLum/linkedin-api-mcp/pull/12" target="_blank" rel="noopener noreferrer" title="JohannsenLum/linkedin-api-mcp (merged PR)"><strong>linkedin-api-mcp</strong></a>: untrusted-data fencing</li>
  </ul>
</section>
<section class="oss-section" id="data">
  <h2>Data science & scientific computing</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/pandas-dev/pandas/pull/63704" target="_blank" rel="noopener noreferrer" title="pandas-dev/pandas (merged PR)"><strong>pandas</strong></a>: regression test so groupby keeps PyArrow dtypes</li>
  <li><a href="https://github.com/pola-rs/polars/pull/28749" target="_blank" rel="noopener noreferrer" title="pola-rs/polars (merged PR)"><strong>Polars</strong></a>: pivot filter bugfix</li>
  <li><a href="https://github.com/matplotlib/matplotlib/pull/30975" target="_blank" rel="noopener noreferrer" title="matplotlib/matplotlib (merged PR)"><strong>matplotlib</strong></a>: Windows cache/config under LOCALAPPDATA</li>
  <li><a href="https://github.com/statsmodels/statsmodels/pull/9561" target="_blank" rel="noopener noreferrer" title="statsmodels/statsmodels (merged PR)"><strong>statsmodels</strong></a>: fixed citation paper link</li>
  <li><a href="https://github.com/aeon-toolkit/aeon/pull/3763" target="_blank" rel="noopener noreferrer" title="aeon-toolkit/aeon (merged PR)"><strong>aeon</strong></a>: inverted MERLIN std check</li>
  <li><a href="https://github.com/skfolio/skfolio/pull/218" target="_blank" rel="noopener noreferrer" title="skfolio/skfolio (merged PR)"><strong>skfolio</strong></a>: CombinatorialPurgedCV splits + tests</li>
  <li><a href="https://github.com/apache/datasketches-rust/pull/211" target="_blank" rel="noopener noreferrer" title="apache/datasketches-rust (merged PR)"><strong>datasketches-rust</strong></a>: safer empty intersection</li>
  <li><a href="https://github.com/conda/conda/pull/15773" target="_blank" rel="noopener noreferrer" title="conda/conda (merged PR)"><strong>conda</strong></a>: type hints in common I/O</li>
  <li><a href="https://github.com/openbabel/openbabel/pull/2862" target="_blank" rel="noopener noreferrer" title="openbabel/openbabel (merged PR)"><strong>Open Babel</strong></a>: three real CVE memory bugs</li>
  <li><a href="https://github.com/rust-bio/rust-bio/pull/651" target="_blank" rel="noopener noreferrer" title="rust-bio/rust-bio (merged PR)"><strong>rust-bio</strong></a>: POA docs URL</li>
  <li><a href="https://github.com/NOAA-FIMS/FIMS/pull/1703" target="_blank" rel="noopener noreferrer" title="NOAA-FIMS/FIMS (merged PR)"><strong>FIMS</strong></a>: broken vignette links</li>
  <li><a href="https://github.com/Hebbian-Robotics/hflow/pull/174" target="_blank" rel="noopener noreferrer" title="Hebbian-Robotics/hflow (merged PR)"><strong>hflow</strong></a>: reject bad interval bounds</li>
  <li><a href="https://github.com/jarl-hoyem/pyrigor/pull/171" target="_blank" rel="noopener noreferrer" title="jarl-hoyem/pyrigor (merged PR)"><strong>pyrigor</strong></a>: code of conduct</li>
  </ul>
</section>
<section class="oss-section" id="infra">
  <h2>Infra, containers & cloud</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/moby/moby/pull/52364" target="_blank" rel="noopener noreferrer" title="moby/moby (merged PR)"><strong>moby</strong></a>: build duplex fix + test goroutine leak</li>
  <li><a href="https://github.com/moby/buildkit/pull/7050" target="_blank" rel="noopener noreferrer" title="moby/buildkit (merged PR)"><strong>buildkit</strong></a>: OTLP tracing docs</li>
  <li><a href="https://github.com/distribution/distribution/pull/4936" target="_blank" rel="noopener noreferrer" title="distribution/distribution (merged PR)"><strong>distribution</strong></a>: CloudFront/S3 path docs</li>
  <li><a href="https://github.com/containerd/nerdctl/pull/5140" target="_blank" rel="noopener noreferrer" title="containerd/nerdctl (merged PR)"><strong>nerdctl</strong></a>: SELinux volume flags documented</li>
  <li><a href="https://github.com/ansible-collections/community.docker/pull/1307" target="_blank" rel="noopener noreferrer" title="ansible-collections/community.docker (merged PR)"><strong>community.docker</strong></a>: command_as_args for swarm services</li>
  <li><a href="https://github.com/ansible/ansible-dev-tools/pull/697" target="_blank" rel="noopener noreferrer" title="ansible/ansible-dev-tools (merged PR)"><strong>ansible-dev-tools</strong></a>: tougher devspaces tests</li>
  <li><a href="https://github.com/ansible/galaxy_collection/pull/457" target="_blank" rel="noopener noreferrer" title="ansible/galaxy_collection (merged PR)"><strong>galaxy_collection</strong></a>: cleanup after publish</li>
  <li><a href="https://github.com/ansible/receptor-collection/pull/118" target="_blank" rel="noopener noreferrer" title="ansible/receptor-collection (merged PR)"><strong>receptor-collection</strong></a>: Debian 12 support</li>
  <li><a href="https://github.com/kubernetes-sigs/external-dns/pull/6626" target="_blank" rel="noopener noreferrer" title="kubernetes-sigs/external-dns (merged PR)"><strong>external-dns</strong></a>: release vs kustomize lag clarified</li>
  <li><a href="https://github.com/flyteorg/flyte/pull/7844" target="_blank" rel="noopener noreferrer" title="flyteorg/flyte (merged PR)"><strong>Flyte</strong></a>: cache enqueue race fixed</li>
  <li><a href="https://github.com/hashicorp/nomad/pull/27819" target="_blank" rel="noopener noreferrer" title="hashicorp/nomad (merged PR)"><strong>Nomad</strong></a>: RunOnFirstRender for change scripts</li>
  <li><a href="https://github.com/bitnami/sealed-secrets/pull/2025" target="_blank" rel="noopener noreferrer" title="bitnami/sealed-secrets (merged PR)"><strong>sealed-secrets</strong></a>: early HTTP for big namespace lists, flaky test, docs</li>
  <li><a href="https://github.com/open-policy-agent/gatekeeper/pull/4508" target="_blank" rel="noopener noreferrer" title="open-policy-agent/gatekeeper (merged PR)"><strong>Gatekeeper</strong></a>: context through Publish</li>
  <li><a href="https://github.com/kube-vip/kube-vip/pull/1696" target="_blank" rel="noopener noreferrer" title="kube-vip/kube-vip (merged PR)"><strong>kube-vip</strong></a> / <a href="https://github.com/kube-vip/website/pull/91" target="_blank" rel="noopener noreferrer" title="kube-vip/website (merged PR)"><strong>website</strong></a>: in-place upgrade docs</li>
  <li><a href="https://github.com/InftyAI/Nebula/pull/76" target="_blank" rel="noopener noreferrer" title="InftyAI/Nebula (merged PR)"><strong>Nebula</strong></a>: show all nodepool providers</li>
  <li><a href="https://github.com/aquasecurity/trivy/pull/10351" target="_blank" rel="noopener noreferrer" title="aquasecurity/trivy (merged PR)"><strong>Trivy</strong></a>: Go 1.26 version format</li>
  <li><a href="https://github.com/gofiber/fiber/pull/4603" target="_blank" rel="noopener noreferrer" title="gofiber/fiber (merged PR)"><strong>Fiber</strong></a>: source-aware extractors</li>
  <li><a href="https://github.com/ktrubilo9/edge-proxy/pull/31" target="_blank" rel="noopener noreferrer" title="ktrubilo9/edge-proxy (merged PR)"><strong>edge-proxy</strong></a>: proper 4xx on admin validation</li>
  <li><a href="https://github.com/hubfly-space/hubcdn/pull/40" target="_blank" rel="noopener noreferrer" title="hubfly-space/hubcdn (merged PR)"><strong>hubcdn</strong></a>: panic recovery on HTTPS</li>
  <li><a href="https://github.com/floci-io/floci/pull/2496" target="_blank" rel="noopener noreferrer" title="floci-io/floci (merged PR)"><strong>floci</strong></a>: MWAA in the service matrix</li>
  <li><a href="https://github.com/sagar2395/snowopslabs/pull/6" target="_blank" rel="noopener noreferrer" title="sagar2395/snowopslabs (merged PR)"><strong>snowopslabs</strong></a>: stray chaos manifest cleanup</li>
  <li><a href="https://github.com/stjude-rust-labs/sprocket/pull/560" target="_blank" rel="noopener noreferrer" title="stjude-rust-labs/sprocket (merged PR)"><strong>sprocket</strong></a>: lint when outputs do not match the task</li>
  <li><a href="https://github.com/lfreleng-actions/dependamerge/pull/453" target="_blank" rel="noopener noreferrer" title="lfreleng-actions/dependamerge (merged PR)"><strong>dependamerge</strong></a>: do not call blocked PRs mergeable</li>
  <li><a href="https://github.com/Open-Source-Kigali/docksight/pull/151" target="_blank" rel="noopener noreferrer" title="Open-Source-Kigali/docksight (merged PR)"><strong>docksight</strong></a>: platform-neutral doctor help</li>
  <li><a href="https://github.com/harsh-pandhe/fleetcommand-platform/pull/50" target="_blank" rel="noopener noreferrer" title="harsh-pandhe/fleetcommand-platform (merged PR)"><strong>fleetcommand-platform</strong></a>: pilot review template</li>
  </ul>
</section>
<section class="oss-section" id="web">
  <h2>Web & product UIs</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/vercel/next.js/pull/90370" target="_blank" rel="noopener noreferrer" title="vercel/next.js (merged PR)"><strong>Next.js</strong></a>: file:// cache-handler paths</li>
  <li><a href="https://github.com/facebook/docusaurus/pull/11666" target="_blank" rel="noopener noreferrer" title="facebook/docusaurus (merged PR)"><strong>Docusaurus</strong></a>: markdown path links on pages</li>
  <li><a href="https://github.com/QwikDev/qwik/pull/8549" target="_blank" rel="noopener noreferrer" title="QwikDev/qwik (merged PR)"><strong>Qwik</strong></a>: eslint rule against await-navigate in use-task</li>
  <li><a href="https://github.com/pnpm/pnpm/pull/10466" target="_blank" rel="noopener noreferrer" title="pnpm/pnpm (merged PR)"><strong>pnpm</strong></a>: show workspace versions on mismatch</li>
  <li><a href="https://github.com/twentyhq/twenty/pull/17160" target="_blank" rel="noopener noreferrer" title="twentyhq/twenty (merged PR)"><strong>Twenty</strong></a>: custom domain without Cloudflare key</li>
  <li><a href="https://github.com/bachdgvn/vue-otp-input/pull/60" target="_blank" rel="noopener noreferrer" title="bachdgvn/vue-otp-input (merged PR)"><strong>vue-otp-input</strong></a>: README</li>
  <li><a href="https://github.com/BaryoDev/rnxjs/pull/46" target="_blank" rel="noopener noreferrer" title="BaryoDev/rnxjs (merged PR)"><strong>rnxjs</strong></a>: focus rings + tall accordion clipping</li>
  <li><a href="https://github.com/BaryoDev/rnxORM/pull/27" target="_blank" rel="noopener noreferrer" title="BaryoDev/rnxORM (merged PR)"><strong>rnxORM</strong></a>: contributing guide</li>
  <li><a href="https://github.com/AryanSharma48/smoothAPI/pull/37" target="_blank" rel="noopener noreferrer" title="AryanSharma48/smoothAPI (merged PR)"><strong>smoothAPI</strong></a>: deprecation warning</li>
  <li><a href="https://github.com/corsairdev/corsair/pull/1050" target="_blank" rel="noopener noreferrer" title="corsairdev/corsair (merged PR)"><strong>corsair</strong></a>: fail closed if HubSpot secret missing</li>
  <li><a href="https://github.com/SmartDropLabs/smartdrop-frontend/pull/185" target="_blank" rel="noopener noreferrer" title="SmartDropLabs/smartdrop-frontend (merged PR)"><strong>smartdrop-frontend</strong></a>: one error-handler path</li>
  <li><a href="https://github.com/Neurowealth/NeuroWealth-Frontend/pull/828" target="_blank" rel="noopener noreferrer" title="Neurowealth/NeuroWealth-Frontend (merged PR)"><strong>NeuroWealth</strong></a>: theme-aware headers</li>
  <li><a href="https://github.com/FlowwStar/FlowStar/pull/615" target="_blank" rel="noopener noreferrer" title="FlowwStar/FlowStar (merged PR)"><strong>FlowStar</strong></a>: stale tx preview + toggle type</li>
  <li><a href="https://github.com/openslop/openslop/pull/652" target="_blank" rel="noopener noreferrer" title="openslop/openslop (merged PR)"><strong>openslop</strong></a>: loading skeleton + narrow composer wrap</li>
  <li><a href="https://github.com/milepost-labs/milepost/pull/138" target="_blank" rel="noopener noreferrer" title="milepost-labs/milepost (merged PR)"><strong>milepost</strong></a>: orphaned recipient routes</li>
  <li><a href="https://github.com/Wayfare-labs/wayfare/pull/342" target="_blank" rel="noopener noreferrer" title="Wayfare-labs/wayfare (merged PR)"><strong>wayfare</strong></a>: live measure button + cleaner loss JSON</li>
  <li><a href="https://github.com/Techhackontime999/wacrm/pull/36" target="_blank" rel="noopener noreferrer" title="Techhackontime999/wacrm (merged PR)"><strong>wacrm</strong></a>: typed webhooks + shared supabase admin</li>
  <li><a href="https://github.com/Techhackontime999/NAdot/pull/39" target="_blank" rel="noopener noreferrer" title="Techhackontime999/NAdot (merged PR)"><strong>NAdot</strong></a>: stop committing get-pip</li>
  <li><a href="https://github.com/ritsth/job-autofill-extension/pull/268" target="_blank" rel="noopener noreferrer" title="ritsth/job-autofill-extension (merged PR)"><strong>job-autofill-extension</strong></a>: doc dedupe + phone in AI context</li>
  <li><a href="https://github.com/super-productivity/super-productivity/pull/6786" target="_blank" rel="noopener noreferrer" title="super-productivity/super-productivity (merged PR)"><strong>super-productivity</strong></a>: clearer sub-tasks in search</li>
  <li><a href="https://github.com/Rohan-Shridhar/HopTab/pull/41" target="_blank" rel="noopener noreferrer" title="Rohan-Shridhar/HopTab (merged PR)"><strong>HopTab</strong></a>: changelog</li>
  <li><a href="https://github.com/Xoshbin/asyar/pull/688" target="_blank" rel="noopener noreferrer" title="Xoshbin/asyar (merged PR)"><strong>asyar</strong></a>: help topic scrolls into view</li>
  <li><a href="https://github.com/nmeylan/nostalro-client/pull/11" target="_blank" rel="noopener noreferrer" title="nmeylan/nostalro-client (merged PR)"><strong>nostalro-client</strong></a>: underscores in skill names</li>
  <li><a href="https://github.com/vyncint/termlens/pull/177" target="_blank" rel="noopener noreferrer" title="vyncint/termlens (merged PR)"><strong>termlens</strong></a>: mouse bounds + dep pin</li>
  <li><a href="https://github.com/vyncint/launchbound/pull/27" target="_blank" rel="noopener noreferrer" title="vyncint/launchbound (merged PR)"><strong>launchbound</strong></a>: cleaner tune/config copy</li>
  <li><a href="https://github.com/mathnotes-app/mobile-ink/pull/55" target="_blank" rel="noopener noreferrer" title="mathnotes-app/mobile-ink (merged PR)"><strong>mobile-ink</strong></a>: native load edge-case tests</li>
  <li><a href="https://github.com/Adithya-Jayan/MyRepertoirApp/pull/246" target="_blank" rel="noopener noreferrer" title="Adithya-Jayan/MyRepertoirApp (merged PR)"><strong>MyRepertoirApp</strong></a>: quick filters after tag rename</li>
  <li><a href="https://github.com/Binit06/LNCrawler/pull/37" target="_blank" rel="noopener noreferrer" title="Binit06/LNCrawler (merged PR)"><strong>LNCrawler</strong></a>: Reddit icon</li>
  <li><a href="https://github.com/Lee-Dongwook/convert-image-to-webp/pull/12" target="_blank" rel="noopener noreferrer" title="Lee-Dongwook/convert-image-to-webp (merged PR)"><strong>convert-image-to-webp</strong></a>: clear unknown-plugin errors</li>
  <li><a href="https://github.com/jason5ng32/MyIP/pull/433" target="_blank" rel="noopener noreferrer" title="jason5ng32/MyIP (merged PR)"><strong>MyIP</strong></a>: long names do not truncate in nav</li>
  <li><a href="https://github.com/rishiyaduwanshi/boiler/pull/80" target="_blank" rel="noopener noreferrer" title="rishiyaduwanshi/boiler (merged PR)"><strong>boiler</strong></a>: validate template dest</li>
  <li><a href="https://github.com/muhammadyusufpov/hyper/pull/22" target="_blank" rel="noopener noreferrer" title="muhammadyusufpov/hyper (merged PR)"><strong>hyper</strong></a>: Array/Dict spellings</li>
  </ul>
</section>
<section class="oss-section" id="python">
  <h2>Python libs & dev tools</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/pydantic/pydantic/pull/12707" target="_blank" rel="noopener noreferrer" title="pydantic/pydantic (merged PR)"><strong>pydantic</strong></a>: pickle + @validate_call regression test</li>
  <li><a href="https://github.com/jd/tenacity/pull/548" target="_blank" rel="noopener noreferrer" title="jd/tenacity (merged PR)"><strong>tenacity</strong></a>: wait_chain docstring syntax</li>
  <li><a href="https://github.com/tox-dev/tox/pull/3670" target="_blank" rel="noopener noreferrer" title="tox-dev/tox (merged PR)"><strong>tox</strong></a>: ENVDIR docs</li>
  <li><a href="https://github.com/astral-sh/ruff/pull/23912" target="_blank" rel="noopener noreferrer" title="astral-sh/ruff (merged PR)"><strong>ruff</strong></a>: ANN401 stack overflow on weird quotes</li>
  <li><a href="https://github.com/marimo-team/marimo/pull/7881" target="_blank" rel="noopener noreferrer" title="marimo-team/marimo (merged PR)"><strong>marimo</strong></a>: SQL f-string intervals + pyiceberg permissions</li>
  <li><a href="https://github.com/rs/zerolog/pull/786" target="_blank" rel="noopener noreferrer" title="rs/zerolog (merged PR)"><strong>zerolog</strong></a>: console does not double-print PartsOrder</li>
  <li><a href="https://github.com/klauspost/compress/pull/1192" target="_blank" rel="noopener noreferrer" title="klauspost/compress (merged PR)"><strong>klauspost/compress</strong></a>: jitter hash bounded</li>
  <li><a href="https://github.com/jackc/pgx/pull/2632" target="_blank" rel="noopener noreferrer" title="jackc/pgx (merged PR)"><strong>pgx</strong></a>: quick start into README</li>
  <li><a href="https://github.com/pwntester/octo.nvim/pull/1441" target="_blank" rel="noopener noreferrer" title="pwntester/octo.nvim (merged PR)"><strong>octo.nvim</strong></a>: @ in PR titles</li>
  <li><a href="https://github.com/adamtheturtle/strict-kwargs-pre-commit/pull/54" target="_blank" rel="noopener noreferrer" title="adamtheturtle/strict-kwargs-pre-commit (merged PR)"><strong>strict-kwargs</strong></a> / <a href="https://github.com/adamtheturtle/coderpad-macos-releases/pull/82" target="_blank" rel="noopener noreferrer" title="adamtheturtle/coderpad-macos-releases (merged PR)"><strong>coderpad-macos-releases</strong></a>: SECURITY.md</li>
  <li><a href="https://github.com/gradle/gradle/pull/37282" target="_blank" rel="noopener noreferrer" title="gradle/gradle (merged PR)"><strong>gradle</strong></a>: Kotlin compiler doc links</li>
  <li><a href="https://github.com/bowbahdoe/ModernJava/pull/264" target="_blank" rel="noopener noreferrer" title="bowbahdoe/ModernJava (merged PR)"><strong>ModernJava</strong></a>: &quot;Avocado&quot; typo</li>
  <li><a href="https://github.com/saimskywalker/binary-sdk-bridge/pull/5" target="_blank" rel="noopener noreferrer" title="saimskywalker/binary-sdk-bridge (merged PR)"><strong>binary-sdk-bridge</strong></a>: skip chmod on Windows</li>
  <li><a href="https://github.com/UnityInFlow/injection-scanner/pull/66" target="_blank" rel="noopener noreferrer" title="UnityInFlow/injection-scanner (merged PR)"><strong>injection-scanner</strong></a>: fill reserved pattern IDs</li>
  <li><a href="https://github.com/StudentSuite/awesome-skills-plugins-for-students/pull/115" target="_blank" rel="noopener noreferrer" title="StudentSuite/awesome-skills-plugins-for-students (merged PR)"><strong>awesome-skills-plugins-for-students</strong></a>: PR template markers</li>
  </ul>
</section>
<section class="oss-section" id="search">
  <h2>Search, storage & data systems</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/meilisearch/meilisearch/pull/6109" target="_blank" rel="noopener noreferrer" title="meilisearch/meilisearch (merged PR)"><strong>Meilisearch</strong></a>: faster parallel deletes</li>
  <li><a href="https://github.com/meilisearch/meilisearch-python/pull/1195" target="_blank" rel="noopener noreferrer" title="meilisearch/meilisearch-python (merged PR)"><strong>meilisearch-python</strong></a>: CI/pipenv Python pin</li>
  <li><a href="https://github.com/dragonflydb/dragonfly/pull/7123" target="_blank" rel="noopener noreferrer" title="dragonflydb/dragonfly (merged PR)"><strong>Dragonfly</strong></a>: Helm cluster-mode values</li>
  <li><a href="https://github.com/ipfs/kubo/pull/11147" target="_blank" rel="noopener noreferrer" title="ipfs/kubo (merged PR)"><strong>kubo</strong></a>: ipfs key ls alias</li>
  <li><a href="https://github.com/Mikedan37/BlazeDB/pull/472" target="_blank" rel="noopener noreferrer" title="Mikedan37/BlazeDB (merged PR)"><strong>BlazeDB</strong></a>: RANK() ties</li>
  <li><a href="https://github.com/timescale/Tiger-Data-Docs/pull/464" target="_blank" rel="noopener noreferrer" title="timescale/Tiger-Data-Docs (merged PR)"><strong>Tiger-Data-Docs</strong></a>: generated columns are not partition keys</li>
  <li><a href="https://github.com/Fayupable/pgscope/pull/3" target="_blank" rel="noopener noreferrer" title="Fayupable/pgscope (merged PR)"><strong>pgscope</strong></a>: hull fallback for collinear clusters</li>
  <li><a href="https://github.com/cachebag/tonneau/pull/11" target="_blank" rel="noopener noreferrer" title="cachebag/tonneau (merged PR)"><strong>tonneau</strong></a>: content-type + uint64 compare</li>
  <li><a href="https://github.com/wuisabel-gif/MemWhale/pull/207" target="_blank" rel="noopener noreferrer" title="wuisabel-gif/MemWhale (merged PR)"><strong>MemWhale</strong></a>: vuln disclosure policy</li>
  </ul>
</section>
<section class="oss-section" id="security">
  <h2>Security & privacy</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/bitwarden/clients/pull/18381" target="_blank" rel="noopener noreferrer" title="bitwarden/clients (merged PR)"><strong>Bitwarden clients</strong></a>: keep card brand when editing</li>
  <li><a href="https://github.com/common-voice/common-voice/pull/5471" target="_blank" rel="noopener noreferrer" title="common-voice/common-voice (merged PR)"><strong>Common Voice</strong></a>: skip animation + sentence-migration docs</li>
  <li><a href="https://github.com/crazy-goat/ScanMePHP/pull/196" target="_blank" rel="noopener noreferrer" title="crazy-goat/ScanMePHP (merged PR)"><strong>ScanMePHP</strong></a> / <a href="https://github.com/cyber-excel10/Sorocheck/pull/15" target="_blank" rel="noopener noreferrer" title="cyber-excel10/Sorocheck (merged PR)"><strong>Sorocheck</strong></a>: contributing guide / Actions example</li>
  <li><a href="https://github.com/earsenio/session-signals/pull/36" target="_blank" rel="noopener noreferrer" title="earsenio/session-signals (merged PR)"><strong>session-signals</strong></a>: capture hook in copy-paste block</li>
  </ul>
</section>
<section class="oss-section" id="obs">
  <h2>Observability, ads & analytics</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/getsentry/sentry-docs/pull/19075" target="_blank" rel="noopener noreferrer" title="getsentry/sentry-docs (merged PR)"><strong>Sentry docs</strong></a>: gauge vs distribution</li>
  <li><a href="https://github.com/matomo-org/matomo/pull/24110" target="_blank" rel="noopener noreferrer" title="matomo-org/matomo (merged PR)"><strong>Matomo</strong></a>: textarea max-height</li>
  <li><a href="https://github.com/mautic/mautic/pull/15888" target="_blank" rel="noopener noreferrer" title="mautic/mautic (merged PR)"><strong>Mautic</strong></a>: scrollable dashboard widgets</li>
  <li><a href="https://github.com/prebid/Prebid.js/pull/14498" target="_blank" rel="noopener noreferrer" title="prebid/Prebid.js (merged PR)"><strong>Prebid.js</strong></a>: typos</li>
  <li><a href="https://github.com/revive-adserver/revive-adserver/pull/1643" target="_blank" rel="noopener noreferrer" title="revive-adserver/revive-adserver (merged PR)"><strong>Revive</strong></a>: &quot;occurred&quot; in locales</li>
  <li><a href="https://github.com/InteractiveAdvertisingBureau/openrtb2.x/pull/171" target="_blank" rel="noopener noreferrer" title="InteractiveAdvertisingBureau/openrtb2.x (merged PR)"><strong>openrtb2.x</strong></a>: dead metro-codes link</li>
  <li><a href="https://github.com/galax-io/gatling-picatinny/pull/324" target="_blank" rel="noopener noreferrer" title="galax-io/gatling-picatinny (merged PR)"><strong>gatling-picatinny</strong></a>: contributing</li>
  <li><a href="https://github.com/stacknil/LogLens/pull/113" target="_blank" rel="noopener noreferrer" title="stacknil/LogLens (merged PR)"><strong>LogLens</strong></a>: pam_unix parser test pin</li>
  </ul>
</section>
<section class="oss-section" id="lang">
  <h2>Language, Sanskrit & learning</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/kmadathil/sanskrit_parser/pull/189" target="_blank" rel="noopener noreferrer" title="kmadathil/sanskrit_parser (merged PR)"><strong>sanskrit_parser</strong></a>: big parse speedups (cache + no debug spam)</li>
  <li><a href="https://github.com/yajnadevam/lipi/pull/6" target="_blank" rel="noopener noreferrer" title="yajnadevam/lipi (merged PR)"><strong>lipi</strong></a>: lexicon senses</li>
  <li><a href="https://github.com/bhavykhatri/DharmicData/pull/7" target="_blank" rel="noopener noreferrer" title="bhavykhatri/DharmicData (merged PR)"><strong>DharmicData</strong></a>: Mah&#257;bh&#257;rata Critical Edition</li>
  <li><a href="https://github.com/lingdojo/kana-dojo/pull/6760" target="_blank" rel="noopener noreferrer" title="lingdojo/kana-dojo (merged PR)"><strong>kana-dojo</strong></a>: a Japanese false friend</li>
  <li><a href="https://github.com/scribe-org/Scribe-Server/pull/94" target="_blank" rel="noopener noreferrer" title="scribe-org/Scribe-Server (merged PR)"><strong>Scribe-Server</strong></a>: safer language stats + tests</li>
  <li><a href="https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/pull/4237" target="_blank" rel="noopener noreferrer" title="Ebazhanov/linkedin-skill-assessments-quizzes (merged PR)"><strong>linkedin-skill-assessments-quizzes</strong></a>: a pile of quiz updates</li>
  <li><a href="https://github.com/github-education-resources/GitHubGraduation-2022/pull/6592" target="_blank" rel="noopener noreferrer" title="github-education-resources/GitHubGraduation-2022 (merged PR)"><strong>GitHubGraduation-2022</strong></a>: my graduation profile card</li>
  </ul>
</section>
<section class="oss-section" id="chain">
  <h2>Blockchain & contracts</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/accensa/accensa-contracts/pull/168" target="_blank" rel="noopener noreferrer" title="accensa/accensa-contracts (merged PR)"><strong>accensa-contracts</strong></a>: expose max batch size</li>
  <li><a href="https://github.com/chioma-housing-protocol-I/chioma/pull/1721" target="_blank" rel="noopener noreferrer" title="chioma-housing-protocol-I/chioma (merged PR)"><strong>chioma</strong></a>: contributing</li>
  <li><a href="https://github.com/Orbit-Wal/contract/pull/64" target="_blank" rel="noopener noreferrer" title="Orbit-Wal/contract (merged PR)"><strong>Orbit-Wal</strong></a>: allowance cold-read tests</li>
  <li><a href="https://github.com/Stellar-kraal/stellar-kraal-contract/pull/160" target="_blank" rel="noopener noreferrer" title="Stellar-kraal/stellar-kraal-contract (merged PR)"><strong>stellar-kraal-contract</strong></a>: circuit-breaker tests</li>
  <li><a href="https://github.com/StellarRouter/StellarRouter/pull/242" target="_blank" rel="noopener noreferrer" title="StellarRouter/StellarRouter (merged PR)"><strong>StellarRouter</strong></a>: drop unused RPC metric fields</li>
  <li><a href="https://github.com/Maki-Zeninn/stellar-router/pull/1133" target="_blank" rel="noopener noreferrer" title="Maki-Zeninn/stellar-router (merged PR)"><strong>stellar-router</strong></a>: saturating cleanup + amount checks</li>
  <li><a href="https://github.com/ArmanX-Labs/SnowIDv2/pull/14" target="_blank" rel="noopener noreferrer" title="ArmanX-Labs/SnowIDv2 (merged PR)"><strong>SnowIDv2</strong></a>: clearer machine-ID errors</li>
  </ul>
</section>
<section class="oss-section" id="systems">
  <h2>Systems, media, graphics & embedded</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/IndianArjun94/3D-Path-Tracer-CUDA/pull/3" target="_blank" rel="noopener noreferrer" title="IndianArjun94/3D-Path-Tracer-CUDA (merged PR)"><strong>3D-Path-Tracer-CUDA</strong></a>: local-color comments</li>
  <li><a href="https://github.com/costott/cpu_rasteriser/pull/15" target="_blank" rel="noopener noreferrer" title="costott/cpu_rasteriser (merged PR)"><strong>cpu_rasteriser</strong></a>: OrbitControls axis swap</li>
  <li><a href="https://github.com/yangseungsang/cesiumjs-copc-runtime/pull/31" target="_blank" rel="noopener noreferrer" title="yangseungsang/cesiumjs-copc-runtime (merged PR)"><strong>cesiumjs-copc-runtime</strong></a>: human-readable bench sizes</li>
  <li><a href="https://github.com/streamcoreai/esp32/pull/14" target="_blank" rel="noopener noreferrer" title="streamcoreai/esp32 (merged PR)"><strong>esp32</strong></a>: Cargo.toml URL + category</li>
  <li><a href="https://github.com/diondokter/device-driver/pull/293" target="_blank" rel="noopener noreferrer" title="diondokter/device-driver (merged PR)"><strong>device-driver</strong></a>: optional address offset</li>
  <li><a href="https://github.com/OpenSauce/nam-rs/pull/56" target="_blank" rel="noopener noreferrer" title="OpenSauce/nam-rs (merged PR)"><strong>nam-rs</strong></a>: reject bad LSTM input size</li>
  <li><a href="https://github.com/jonathanmcmichael/Rustit/pull/37" target="_blank" rel="noopener noreferrer" title="jonathanmcmichael/Rustit (merged PR)"><strong>Rustit</strong></a>: classification provenance fixtures</li>
  <li><a href="https://github.com/SteelCrab/firecrab/pull/188" target="_blank" rel="noopener noreferrer" title="SteelCrab/firecrab (merged PR)"><strong>firecrab</strong></a>: Rust toolchain bump</li>
  <li><a href="https://github.com/VinayakGhai/TinyFS-UNO/pull/10" target="_blank" rel="noopener noreferrer" title="VinayakGhai/TinyFS-UNO (merged PR)"><strong>TinyFS-UNO</strong></a>: Doxygen on public headers</li>
  <li><a href="https://github.com/blairess/Ariadnis/pull/3" target="_blank" rel="noopener noreferrer" title="blairess/Ariadnis (merged PR)"><strong>Ariadnis</strong></a>: brush rings on tall terrain</li>
  <li><a href="https://github.com/oscarbol09/audiobard/pull/87" target="_blank" rel="noopener noreferrer" title="oscarbol09/audiobard (merged PR)"><strong>audiobard</strong></a>: TTS gender words, Piper download lock, FFmpeg/M4B</li>
  <li><a href="https://github.com/OthmaneBlial/audio-capture/pull/11" target="_blank" rel="noopener noreferrer" title="OthmaneBlial/audio-capture (merged PR)"><strong>audio-capture</strong></a>: fake-provider contract test</li>
  <li><a href="https://github.com/0jc1/py-autovod/pull/141" target="_blank" rel="noopener noreferrer" title="0jc1/py-autovod (merged PR)"><strong>py-autovod</strong></a>: multi-language Whisper</li>
  <li><a href="https://github.com/luohoa97/cordial/pull/20" target="_blank" rel="noopener noreferrer" title="luohoa97/cordial (merged PR)"><strong>cordial</strong></a>: WebRTC BuildInfo JNI hooks</li>
  <li><a href="https://github.com/lizhelang/codexbar/pull/41" target="_blank" rel="noopener noreferrer" title="lizhelang/codexbar (merged PR)"><strong>codexbar</strong></a>: crash on duplicate session ids</li>
  </ul>
</section>
<section class="oss-section" id="misc">
  <h2>Everything else</h2>
  <ul class="oss-list">
  <li><a href="https://github.com/achird-labs/rift/pull/972" target="_blank" rel="noopener noreferrer" title="achird-labs/rift (merged PR)"><strong>rift</strong></a>: runnable lint doctest</li>
  <li><a href="https://github.com/achird-labs/rift-cluster/pull/447" target="_blank" rel="noopener noreferrer" title="achird-labs/rift-cluster (merged PR)"><strong>rift-cluster</strong></a>: real HTTP method in errors</li>
  <li><a href="https://github.com/anoopcodehack/DevBoard/pull/373" target="_blank" rel="noopener noreferrer" title="anoopcodehack/DevBoard (merged PR)"><strong>DevBoard</strong></a> / <a href="https://github.com/evgen0xb/uLister/pull/12" target="_blank" rel="noopener noreferrer" title="evgen0xb/uLister (merged PR)"><strong>uLister</strong></a> / <a href="https://github.com/NexusInitiative/AI-Agent-Advisor/pull/69" target="_blank" rel="noopener noreferrer" title="NexusInitiative/AI-Agent-Advisor (merged PR)"><strong>NexusInitiative</strong></a> / <a href="https://github.com/NovaFest-Labs/NovaEvents-api/pull/9" target="_blank" rel="noopener noreferrer" title="NovaFest-Labs/NovaEvents-api (merged PR)"><strong>NovaEvents-api</strong></a>: changelogs and contributing</li>
  <li><a href="https://github.com/aviskaar/zorp/pull/99" target="_blank" rel="noopener noreferrer" title="aviskaar/zorp (merged PR)"><strong>zorp</strong></a>: fail release on self-pinned crate versions</li>
  <li><a href="https://github.com/chaudhary-lakshay/CashCard-API/pull/9" target="_blank" rel="noopener noreferrer" title="chaudhary-lakshay/CashCard-API (merged PR)"><strong>CashCard-API</strong></a>: Location header + owner stamp</li>
  <li><a href="https://github.com/chaudhary-lakshay/Task-Tracker/pull/9" target="_blank" rel="noopener noreferrer" title="chaudhary-lakshay/Task-Tracker (merged PR)"><strong>Task-Tracker</strong></a>: honest deletes + UTF-8</li>
  <li><a href="https://github.com/Cyrax321/CONTINUUM/pull/347" target="_blank" rel="noopener noreferrer" title="Cyrax321/CONTINUUM (merged PR)"><strong>CONTINUUM</strong></a>: idempotent SQLite close</li>
  <li><a href="https://github.com/electr1fy0/okane/pull/1" target="_blank" rel="noopener noreferrer" title="electr1fy0/okane (merged PR)"><strong>okane</strong></a>: error messages and route methods</li>
  <li><a href="https://github.com/cs0lar/knk/pull/50" target="_blank" rel="noopener noreferrer" title="cs0lar/knk (merged PR)"><strong>knk</strong></a>: query semantics docs</li>
  <li><a href="https://github.com/fior512/Nott/pull/27" target="_blank" rel="noopener noreferrer" title="fior512/Nott (merged PR)"><strong>Nott</strong></a>: image-op / metric tests</li>
  <li><a href="https://github.com/h5i-dev/h5i/pull/540" target="_blank" rel="noopener noreferrer" title="h5i-dev/h5i (merged PR)"><strong>h5i</strong></a>: git-hooks showcase</li>
  <li><a href="https://github.com/lextpf/seal/pull/10" target="_blank" rel="noopener noreferrer" title="lextpf/seal (merged PR)"><strong>seal</strong></a>: rename test temp dirs</li>
  <li><a href="https://github.com/lacs-project/sysknife/pull/275" target="_blank" rel="noopener noreferrer" title="lacs-project/sysknife (merged PR)"><strong>sysknife</strong></a>: treat EACCES as &quot;present&quot;</li>
  <li><a href="https://github.com/Stiven-Gjekaj/MiruScriptX/pull/54" target="_blank" rel="noopener noreferrer" title="Stiven-Gjekaj/MiruScriptX (merged PR)"><strong>MiruScriptX</strong></a>: non-negative mod</li>
  <li><a href="https://github.com/Owenb135/THE-MULTIVERSE/pull/24" target="_blank" rel="noopener noreferrer" title="Owenb135/THE-MULTIVERSE (merged PR)"><strong>THE-MULTIVERSE</strong></a>: README matches multi.cpp</li>
  <li><a href="https://github.com/sorotrail/SoroTrail/pull/604" target="_blank" rel="noopener noreferrer" title="sorotrail/SoroTrail (merged PR)"><strong>SoroTrail</strong></a>: return configured network</li>
  <li><a href="https://github.com/yakew7/Fair-Code/pull/312" target="_blank" rel="noopener noreferrer" title="yakew7/Fair-Code (merged PR)"><strong>Fair-Code</strong></a>: no hardcoded min-group-size</li>
  <li><a href="https://github.com/zosmaai/openzosma/pull/33" target="_blank" rel="noopener noreferrer" title="zosmaai/openzosma (merged PR)"><strong>openzosma</strong></a>: Slack Socket Mode adapter</li>
  <li><a href="https://github.com/yeqown/go-qrcode/pull/75" target="_blank" rel="noopener noreferrer" title="yeqown/go-qrcode (merged PR)"><strong>go-qrcode</strong></a>: &quot;terminal&quot; typo</li>
  <li><a href="https://github.com/tmorelli/GitKit-FarmData2/pull/47" target="_blank" rel="noopener noreferrer" title="tmorelli/GitKit-FarmData2 (merged PR)"><strong>GitKit-FarmData2</strong></a>: &quot;component&quot; typo</li>
  <li><a href="https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/pull/132" target="_blank" rel="noopener noreferrer" title="Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io (merged PR)"><strong>chess club site</strong></a>: bad self-link off the anniversary page</li>
  <li><a href="https://github.com/turbohire-engg/TurboHireDS/pull/352" target="_blank" rel="noopener noreferrer" title="turbohire-engg/TurboHireDS (merged PR)"><strong>TurboHireDS</strong></a>: AWS workflow</li>
  <li><a href="https://github.com/Plantcore-AI/Iteron/pull/368" target="_blank" rel="noopener noreferrer" title="Plantcore-AI/Iteron (merged PR)"><strong>Plantcore Iteron</strong></a>: already covered under AI / ML</li>
  <li><a href="https://github.com/Owenb135/THE-MULTIVERSE/pull/24" target="_blank" rel="noopener noreferrer" title="Owenb135/THE-MULTIVERSE (merged PR)"><strong>Owenb135</strong></a>: README</li>
  </ul>
</section>

  <p class="oss-footer">
    Machine-readable mirror:
    <a href="https://gist.github.com/VedantMadane/5a45e50fc4bd3c69cefe0466aefb3387#file-merged-repo-descriptions-md" target="_blank" rel="noopener noreferrer">merged-repo-descriptions.md</a>
    in the PR Toolkit gist.
    Portfolio:
    <a href="{{ '/portfolio' | relative_url }}">/portfolio</a>.
  </p>
</div>
