---
layout: post
title: "मुक्तस्रोत-रणकथाः — Open Source War Stories"
subtitle: "From Docker internals to CockroachDB transaction plumbing, fifteen PRs across the stack"
tags: [open-source, golang, docker, cockroachdb, calico, opentelemetry, sanskrit]
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

<div class="reader-container">

## मङ्गलाचरणम् (Invocation)

<div class="sanskrit-text sanskrit-verse-lines">
  <span>मुक्तस्रोतसि कोऽपि कर्म कुरुते श्रद्धापुरःसारतः ।</span><br />
  <span>दत्त्वा कोडं प्ररोहति प्रतिफलं कीर्तिश्च सौहार्दतः ॥</span>
</div>
<details>
<summary>शब्दार्थाः</summary>
मुक्तस्रोतसि (In the open-source world) कोऽपि (someone) कर्म कुरुते (does work) श्रद्धापुरःसारतः (with sincerity at the forefront). दत्त्वा (Having given) कोडं (code) प्ररोहति (there sprouts) प्रतिफलं (fruit) कीर्तिश्च (and reputation) सौहार्दतः (from goodwill).
</details>

---

In February 2026 I decided to systematically contribute to large, well-known open-source projects. Not a Hacktoberfest drive where you fix a typo and collect a T-shirt. The idea was to pick real issues — the kind that sit open for hundreds of days because they look intimidating, or because the codebase is massive, or because the maintainers labelled it "help-wanted" and the world collectively said "somebody else will do it."

Here is how it went. Some PRs merged in hours. Some are still under review. One was closed without merge and I learned from that too.

---

## I. The Heavyweights

### CockroachDB — Exposing Byte Limits in the KV Transaction API

**Issue**: [cockroachdb/cockroach#63661](https://github.com/cockroachdb/cockroach/issues/63661) (open **1823 days** when I picked it up)  
**PR**: [#168394](https://github.com/cockroachdb/cockroach/pull/168394)

<div class="sanskrit-text sanskrit-verse-lines">
  <span>पञ्चवर्षं स्थितं प्रश्नं कोऽपि नैव स्पृशत्यहो ।</span><br />
  <span>बाइट्-सीमां प्रकाशय्य कुटिलं जालं विमुच्यते ॥</span>
</div>
<details>
<summary>शब्दार्थाः</summary>
पञ्चवर्षं (For five years) स्थितं (standing) प्रश्नं (the question) कोऽपि (nobody) नैव (not at all) स्पृशत्यहो (touched — what a wonder!). बाइट्सीमां (The byte limit) प्रकाशय्य (having exposed) कुटिलं (the tangled) जालं (web/network) विमुच्यते (is freed).
</details>

CockroachDB's `kv.Txn` and `kv.DB` had a `Scan` method with a `maxRows` limit, but no way to say "stop scanning after you've collected this many bytes." The proto layer already had a `TargetBytes` field — it was plumbed through `Batch.Header` — but the convenience methods on `Txn` and `DB` didn't expose it. If you wanted byte-bounded scans, you had to drop down to the Batch API, set headers by hand, call `Run`, and parse the `Result`.

The issue sat open since **April 2020**. Filed by Nathan VanBenschoten, a core CockroachDB developer. Help-wanted label, zero PRs, zero claims.

The challenge was: `Scan`, `ScanForUpdate`, `ScanForShare`, `ReverseScan`, `ReverseScanForUpdate`, `ReverseScanForShare` — six methods on `Txn`, six on `DB`. Changing their signatures would break 130+ callers across the monorepo. So I used **variadic functional options**:

```go
type ScanOption func(*scanConfig)

func WithTargetBytes(targetBytes int64) ScanOption

// All existing callers keep working. New callers add one argument:
rows, err := txn.Scan(ctx, begin, end, maxRows, kv.WithTargetBytes(1<<20))
```

Zero callers break. Future options (say `AllowEmpty` or `WholeRowsOfSize`) can be added to `ScanOption` without touching any signatures again. The internal `scan()` helper on both `Txn` and `DB` applies the config to `b.Header.TargetBytes`.

The clone alone took ten minutes. CockroachDB is not a small repo.

---

### Moby (Docker Engine) — Removing a Nine-Year-Old Workaround

**Issue**: [moby/moby#51209](https://github.com/moby/moby/issues/51209)  
**PR**: [#52364](https://github.com/moby/moby/pull/52364)

<div class="sanskrit-text sanskrit-verse-lines">
  <span>गो-भाषायां पुरातन्यां न्यूनता सञ्चिता चिरम् ।</span><br />
  <span>एकविंशे तु संस्करणे समाधानं प्रकाशितम् ॥</span>
</div>
<details>
<summary>शब्दार्थाः</summary>
गोभाषायां (In the Go language) पुरातन्यां (in the old version) न्यूनता (a deficiency) सञ्चिता (was accumulated) चिरम् (for a long time). एकविंशे (In the twenty-first) तु (but) संस्करणे (in the version [Go 1.21]) समाधानं (the solution) प्रकाशितम् (was revealed/released).
</details>

In 2017, Docker's build endpoint had a problem: the HTTP handler needed to write build progress to the response while still reading the build context tarball from the request body. Go's `net/http` didn't support full-duplex HTTP/1 at the time ([golang/go#15527](https://github.com/golang/go/issues/15527), [golang/go#22209](https://github.com/golang/go/issues/22209)), so someone wrote `wrapOutputBufferedUntilRequestRead` — a hairy piece of concurrency code with a mutex-guarded buffer, a `Peek(1)` trigger, and a `notify()` callback — roughly 100 lines of workaround types (`wcf`, `rcNotifier`, `flusher`, `nopFlusher`).

Go 1.21 landed `http.ResponseController.EnableFullDuplex()` — the official fix.

Moby already requires Go 1.25. So the entire workaround was dead code walking. Filed by thaJeztah (Sebastiaan van Stijn, Docker maintainer), help-wanted, expert-level. Some UT Austin students showed interest in November 2025 but never submitted a PR.

My change: one call to `EnableFullDuplex()` at the top of `postBuild`, delete everything below the fold. The `bufio` import goes away. Five types deleted. The function body shrinks by half.

```go
rc := http.NewResponseController(w)
if err := rc.EnableFullDuplex(); err != nil {
    log.G(ctx).WithError(err).Warn("failed to enable full-duplex HTTP; falling back to default behavior")
}
```

That is the entire replacement. Satisfying.

---

## II. The Networking & Observability Layer

### Project Calico — LoadBalancer IPAM Fallback

**Issue**: [projectcalico/calico#11815](https://github.com/projectcalico/calico/issues/11815)  
**PR**: [#12447](https://github.com/projectcalico/calico/pull/12447)

Calico's LoadBalancer IPAM controller would only look at `Service.spec.loadBalancerIP` for the requested IP. But that field is deprecated. Some users set their desired IP in `Service.spec.externalIPs` instead, and Calico would ignore it — allocating a random IP from the pool and leaving the user confused.

I added a `requestedLoadBalancerIPs` method that checks `externalIPs` first, then falls back to the deprecated `loadBalancerIP`. Updated `IsCalicoManagedLoadBalancer`, `syncService`, and `assignIP`. Wrote tests for every combination. The CLA signing was its own adventure — CockroachDB wanted all commit emails to match, and I had to squash commits to fix that.

### OpenTelemetry Go — HTTP/JSON Encoding for Log Exporters

**Issue**: [open-telemetry/opentelemetry-go#8151](https://github.com/open-telemetry/opentelemetry-go/issues/8151)  
**PR**: [#8199](https://github.com/open-telemetry/opentelemetry-go/pull/8199)

The OTLP log HTTP exporter only supported Protobuf. The spec says `http/json` encoding should also be available. I added an `Encoding` type (`ProtoEncoding`, `JSONEncoding`), a `WithEncoding` option, encoding-aware marshaling using `protojson.Marshal` for JSON, updated the mock collector in tests to accept both content types, and added integration tests for the JSON path. Updated the CHANGELOG.

### OpenTelemetry Collector — Schema-Generated README Embedding

**PR**: [open-telemetry/opentelemetry-collector#15099](https://github.com/open-telemetry/opentelemetry-collector/pull/15099)

Phase 2 of the schemagen tool — auto-embedding generated config documentation into component READMEs.

---

## III. The Infrastructure Tier

### HashiCorp Nomad — Run Change Scripts on First Render

**Issue**: [hashicorp/nomad#27429](https://github.com/hashicorp/nomad/issues/27429)  
**PR**: [#27819](https://github.com/hashicorp/nomad/pull/27819)

Nomad's template `change_script` only ran when the template *changed*, not on first render. So if you had a script that needed to run when a job first started, you were out of luck. Maintainer gave design direction in January 2026. I implemented `change_script_on_first_render` option.

### HashiCorp Packer — PowerShell NonInteractive Default

**Issue**: [hashicorp/packer#12637](https://github.com/hashicorp/packer/issues/12637)  
**PR**: [#13607](https://github.com/hashicorp/packer/pull/13607)

927 days old, help-wanted. PowerShell provisioner wasn't running with `-NonInteractive` by default, causing hangs when scripts tried to prompt. Simple fix, niche problem, nobody bothered.

### etcd-io/bbolt — Deadlock on Corrupted File Check

**Issue**: [etcd-io/bbolt#877](https://github.com/etcd-io/bbolt/issues/877)  
**PR**: [#1189](https://github.com/etcd-io/bbolt/pull/1189)

The word "deadlock" in the title scared everyone away for 478 days. Lock ordering issue in one code path when checking file integrity.

### Containers/Podman — WSL DNS Fallback

**PR**: [containers/podman#28491](https://github.com/containers/podman/pull/28491)

WSL user-mode networking was not getting a fallback DNS in `resolv.conf`. Merged.

### Docker Setup QEMU Action — Multi-Platform Build Example

**PR**: [docker/setup-qemu-action#274](https://github.com/docker/setup-qemu-action/pull/274)

Documentation gap. People kept asking on StackOverflow how to do multi-platform builds with QEMU. Added a working example to the README. Merged.

### Docker Model Runner — Richer Model Metadata

**PR**: [docker/model-runner#721](https://github.com/docker/model-runner/pull/721)

Exposed richer model metadata in the v1/models API. Merged.

---

## IV. The Wider Net

### Astral Ruff — Stack Overflow Fix

**PR**: [astral-sh/ruff#23912](https://github.com/astral-sh/ruff/pull/23912)

`ANN401` rule was hitting a stack overflow on quoted annotations with escape sequences. Merged.

### Dragonfly — Helm Chart Cluster Mode

**Issue**: [dragonflydb/dragonfly#3861](https://github.com/dragonflydb/dragonfly/issues/3861)  
**PR**: [#7123](https://github.com/dragonflydb/dragonfly/pull/7123)

555 days, good-first-issue + hacktoberfest. Helm values for cluster mode were missing. YAML boolean coercion was the tricky part — Helm treats unquoted `yes` as boolean `true`, but Dragonfly expects the string `"yes"`.

### OPA Gatekeeper — Caller Context Propagation

**Issue**: [open-policy-agent/gatekeeper#4477](https://github.com/open-policy-agent/gatekeeper/issues/4477)  
**PR**: [#4508](https://github.com/open-policy-agent/gatekeeper/pull/4508)

Mechanical refactor: replace `context.Background()` with caller context throughout the export system.

### Strawberry GraphQL — Schema Breaking Change Detection

**Issue**: [strawberry-graphql/strawberry#3161](https://github.com/strawberry-graphql/strawberry/issues/3161)  
**PR**: [#4361](https://github.com/strawberry-graphql/strawberry/pull/4361)

903 days old! Good-first-issue. Schema comparison to detect breaking changes.

### BentoML — SQLite Concurrency Fix

**PRs**: [#5551](https://github.com/bentoml/BentoML/pull/5551), [#5555](https://github.com/bentoml/BentoML/pull/5555), [#5558](https://github.com/bentoml/BentoML/pull/5558)

Three PRs merged. "Database is locked" under high concurrency — set `busy_timeout` and WAL mode. Then added native src-layout support.

### Conda — Type Hints for common/io

**PR**: [conda/conda#15773](https://github.com/conda/conda/pull/15773)

Added type hints to `conda/common/io`. Merged.

### Ansible — Multiple Repos

**PRs**: [receptor-collection#118](https://github.com/ansible/receptor-collection/pull/118), [galaxy_collection#457](https://github.com/ansible/galaxy_collection/pull/457), [ansible-dev-tools#697](https://github.com/ansible/ansible-dev-tools/pull/697)

Debian 12 support fix, working directory cleanup after publish, and test robustness. All merged.

---

## उपसंहारः (Conclusion)

<div class="sanskrit-text sanskrit-verse-lines">
  <span>पञ्चदश प्रदानानि विविधेषु प्रकल्पके ।</span><br />
  <span>डॉकर-कॉक्रोच-कालिको गो-रस्ट-पायथन-त्रये ॥</span>
</div>
<details>
<summary>शब्दार्थाः</summary>
पञ्चदश (Fifteen) प्रदानानि (contributions) विविधेषु (in diverse) प्रकल्पके (projects). डॉकरकॉक्रोचकालिको (Docker, CockroachDB, Calico) गोरस्टपायथनत्रये (in the Go-Rust-Python triad).
</details>

<div class="sanskrit-text sanskrit-verse-lines">
  <span>कोऽपि प्रश्नः पुरातनः कोऽपि नूतन एव च ।</span><br />
  <span>सर्वत्र शिक्षणं लब्धं मुक्तस्रोते हि जीवनम् ॥</span>
</div>
<details>
<summary>शब्दार्थाः</summary>
कोऽपि (Some) प्रश्नः (issue) पुरातनः (was ancient) कोऽपि (some) नूतन एव च (was indeed new). सर्वत्र (Everywhere) शिक्षणं (learning) लब्धं (was obtained) मुक्तस्रोते (in open-source) हि (indeed) जीवनम् (life [itself]).
</details>

The pattern I noticed: the scariest-looking issues were usually the most tractable once you actually read the code. A five-year-old issue in CockroachDB turned out to need a clean variadic-options pattern and some doc comments. A "deadlock" in bbolt was a lock ordering fix. A 900-day "breaking change detection" in Strawberry had the comparison internals already written — just needed wiring up.

The ones that genuinely required deep understanding were Calico (Kubernetes LoadBalancer semantics, IPAM pools, the deprecation path from `loadBalancerIP` to `externalIPs`) and Docker (understanding why full-duplex HTTP matters for streaming build contexts). Those were the most rewarding.

If you are reading this and thinking "but I'm not good enough to contribute to Docker or CockroachDB" — I had the same thought. The secret is that these repos are large enough that most issues are *not* in the critical path. They are in the helper functions, the configuration layer, the convenience API. Start there.

---

*All PRs created with clean commit histories, no automated trailers, DCO/CLA signed where required. Code reviewed manually before submission.*

</div>
