# -*- coding: utf-8 -*-
"""Akṣara count and purity helpers for vedantmadane.github.io padya."""
from __future__ import annotations
import re

_LATIN = re.compile(r"[A-Za-z0-9]")
_LOAN = re.compile(
    r"(?:टोकन्|टोकन(?![ा-ौ])|हैश|बैच|कनारी|आउटबॉक्स|स्नैप|ब्राउजर्|"
    r"वेबहुक|गेटवे|साइडकार|पार्टिशन|कन्ज्यूमर|प्रोड्यूसर|ब्रोकर|टॉपिक|"
    r"स्कीमा|रेजिस्ट्री|लेजर|शार्ड|क्लाउड|सर्वर|क्लाइंट|"
    r"API|HTTP|HTTPS|DNS|TLS|SSL|JWT|SQL|CPU|GPU|CDN|"
    r"JSON|XML|gRPC|TCP|UDP|UUID|SLA|SLO|SLI|WAL|CDC|CQRS|CRDT|"
    r"HPA|TTL|DLQ|ACL|RBAC|IAM|SSO|MFA|PKI|CSP|HSTS|CORS|CSRF|SSRF|"
    r"XSS|CVE|SBOM|Redis|Kafka|Nginx|Postgres|MySQL|Mongo|"
    r"p99|p95|OOM|SPOF|RPO|RTO|JIT|BFF|WAF|HSM|KMS|ACME|"
    r"fsync|checksum|CRC|LSN|prod|canary|sidecar|mesh|proxy|"
    r"outbox|inbox|webhook|gateway|blob|queue)",
    re.I,
)
_TECH_PUNCT = re.compile(r"[=<>%#@\\$]|!=|==")
_STRIP_END = re.compile(r"[।॥\s0-9०-९]+$")


def count_aksharas(text: str) -> int:
    text = re.sub(r"[^\u0900-\u097F]", "", text)
    i, n = 0, 0
    while i < len(text):
        ch = text[i]
        if ch == "\u094d":
            i += 1
            continue
        if "\u093e" <= ch <= "\u094c" or ch in "\u0901\u0902\u0903\u093c":
            i += 1
            continue
        n += 1
        i += 1
        while i < len(text):
            c = text[i]
            if "\u093e" <= c <= "\u094c" or c in "\u0901\u0902\u0903\u093c":
                i += 1
                continue
            if c == "\u094d":
                i += 1
                if i < len(text) and "\u0915" <= text[i] <= "\u0939":
                    i += 1
                    while i < len(text) and (
                        "\u093e" <= text[i] <= "\u094c" or text[i] in "\u0901\u0902\u0903\u093c"
                    ):
                        i += 1
                continue
            break
    return n


def line_body(s: str) -> str:
    return _STRIP_END.sub("", s.strip())


def purity_flags(s: str) -> list[str]:
    flags = []
    if _LATIN.search(s):
        flags.append("latin_ascii")
    if _LOAN.search(s):
        flags.append("hybrid_loan")
    if _TECH_PUNCT.search(s):
        flags.append("tech_punct")
    if re.search(r"[\u4e00-\u9fff\u0400-\u04ff]", s):
        flags.append("foreign_script")
    return flags


def assert_pure(s: str, where: str = "") -> None:
    f = purity_flags(s)
    if f:
        raise AssertionError(f"purity {where}: {f} :: {s[:80]}")


def assert_anu_line(s: str, where: str = "") -> int:
    assert_pure(s, where)
    n = count_aksharas(line_body(s))
    if not (14 <= n <= 18):
        raise AssertionError(f"anu line {where}: aksharas={n} want 14-18 :: {s}")
    return n


def assert_upa_line(s: str, where: str = "") -> int:
    assert_pure(s, where)
    n = count_aksharas(line_body(s))
    if n != 11:
        raise AssertionError(f"upa line {where}: aksharas={n} want 11 :: {s}")
    return n


def assert_anu_pair(s1: str, s2: str, where: str = "") -> None:
    a = assert_anu_line(s1, where + ".s1")
    b = assert_anu_line(s2, where + ".s2")
    tot = a + b
    if not (28 <= tot <= 36):
        raise AssertionError(f"anu total {where}: {tot} want 28-36")


def assert_upa_quatrain(lines: list[str], where: str = "") -> None:
    if len(lines) != 4:
        raise AssertionError(f"upa {where}: need 4 lines got {len(lines)}")
    for i, ln in enumerate(lines):
        assert_upa_line(ln, f"{where}.l{i+1}")
