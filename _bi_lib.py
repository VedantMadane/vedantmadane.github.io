# -*- coding: utf-8 -*-
from pathlib import Path
import re
import sys

_METER = Path(__file__).resolve().parent / ".grok" / "skills" / "sanskrit-verse-blog" / "scripts"
if str(_METER) not in sys.path:
    sys.path.insert(0, str(_METER))
from meter import assert_anu_pair, assert_upa_quatrain, purity_flags  # noqa: E402

EM, EN = "\u2014", "\u2013"
CSS = "{{ '/assets/css/reader.css' | relative_url }}"
JS = "{{ '/assets/js/audio-sync.js' | relative_url }}"

def check(t):
    assert EM not in t and EN not in t
    assert '<p class="prose-text"><strong>English.</strong>' not in t
    for ln in t.splitlines():
        if re.search(r",[^,\n]+,\s+and\s+", ln) and sum(c.isascii() and c.isalpha() for c in ln) >= 12:
            raise AssertionError("oxford: " + ln[:100])
    # verse span purity (belt and suspenders with pack12 asserts)
    for m in re.finditer(
        r'<div class="sanskrit-text sanskrit-verse-lines"[^>]*>(.*?)</div>', t, re.S
    ):
        for span in re.findall(r"<span[^>]*>([^<]+)</span>", m.group(1)):
            bad = purity_flags(span)
            if bad:
                raise AssertionError("verse purity %s :: %s" % (bad, span[:100]))

def ox(s):
    return re.sub(r",(\s+)and\s+", r"\1and ", s)

def dev(i):
    return "".join("०१२३४५६७८९"[int(c)] for c in str(i))

def shell(title, subtitle, date_s, slug, tags):
    return ("---\nlayout: post\n"
        f'title: "{title}"\nsubtitle: "{subtitle}"\n'
        f'permalink: "/{date_s}-{slug}/"\nslug: "{slug}"\n'
        f'tags: [{", ".join(tags)}]\n'
        "audio_sync: false\n# audio_file: /assets/audio/FILENAME.mp3\n---\n\n"
        f'<link rel="stylesheet" href="{CSS}">\n\n'
        '<div class="reader-container audio-sync-root">\n\n')

def ch(title, meter, theme):
    return (f'<aside class="chapter-header" aria-label="Section">\n'
        f'  <h2 class="chapter-title">{title}</h2>\n'
        f'  <p class="chapter-keyword">{meter}</p>\n'
        f'  <p class="chapter-theme">{theme}</p>\n</aside>\n\n')

def det(summ, body):
    return '<details>\n<summary>%s</summary>\n<div class="prose-text" markdown="1">\n\n%s\n\n</div>\n</details>\n\n' % (summ, body)

def fin(t):
    return t.rstrip() + '\n\n</div>\n\n<script src="%s"></script>\n' % JS

def save(name, t):
    t = fin(t)
    check(t)
    assert t.count("verse-topic") == 12 and "Word-for-word" in t and "minimizable" in t
    path = Path("_posts") / name
    assert len(path.name.encode("utf-8")) < 200
    path.write_text(t, encoding="utf-8", newline="\n")
    print("W", name, len(t))

def prior(rows):
    h = "| पूर्वं / Prior | अत्र / Adds | न पुनः / Does not repeat |\n| :---- | :---- | :---- |\n"
    return h + "\n".join("| %s | %s | %s |" % r for r in rows)

def plan_default():
    rows = [("१","मङ्गलं बीजं च / Opening","अनुष्टुभ्","२"),("२","मूलतत्त्वानि / Core","अनुष्टुभ्","२"),
            ("३","मुख्यविधिः / Method","उपजाति","१"),("४","रक्षा · विधिः / Guards","अनुष्टुभ्","२"),
            ("५","विवेक · सीमा / Judgment","अनुष्टुभ्","२"),("६","पूर्वसन्धिः / Series links","उपजाति","१"),
            ("७","उपसंहारः / Close","अनुष्टुभ्","२")]
    h = "| प्रकरणम् | विषयः | छन्दः | श्लोकाः |\n| :---- | :---- | :---- | :---: |\n"
    return h + "\n".join("| %s | %s | %s | %s |" % r for r in rows)

def gloss(rows):
    h = "| Modern English | संस्कृतम् | Note |\n| :---- | :---- | :---- |\n"
    return h + "\n".join("| %s | %s | %s |" % r for r in rows)

def keep_drop(keep, drop):
    k = "\n".join("%s. **%s**: %s  " % (dev(i), a, b) for i, (a, b) in enumerate(keep, 1))
    d = "\n".join("- %s  " % x for x in drop)
    return "### ग्राह्यम् / Keep\n%s\n\n### त्याज्यम् / Avoid\n%s" % (k, d)

def R(a, b): return (a, b)

def wfw_table(pairs):
    h = "| संस्कृतपदम् | Word-for-word English |\n| :---- | :---- |\n"
    return h + "\n".join("| %s | %s |" % (a, b) for a, b in pairs)

def v_anu(n, s1, s2, pad, rows, wfw, sense, ctx="", note=""):
    rows_md = "\n".join("| %s | %s |" % (a, b) for a, b in rows)
    extra = "\n\n%s\n" % note if note else "\n"
    ctx_b = "\n\n**Context / topic**  \n%s\n" % ox(ctx) if ctx else "\n"
    return (
        '<p class="verse-topic">श्लोकः %s (अनुष्टुभ्)</p>\n'
        '<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v%d">\n'
        '  <span data-line="1" data-start="" data-end="">%s</span><br />\n'
        '  <span data-line="2" data-start="" data-end="">%s</span>\n</div>\n'
        '<details>\n<summary>पदच्छेदः · Word-for-word · English (minimizable)</summary>\n'
        '<div class="prose-text" markdown="1">\n\n**पदच्छेदः**  \n%s\n\n**Word-for-word**\n\n%s\n\n'
        '**Gloss table**\n\n| पदम् | अर्थः / sense |\n| :---- | :---- |\n%s\n\n'
        '**English sense**  \n%s\n%s%s\n**वृत्तमिति**: ८-८-८-८।\n\n</div>\n</details>\n\n'
    ) % (dev(n), n, s1, s2, pad, wfw_table(wfw), rows_md, ox(sense), ctx_b, extra)

def v_upa(n, lines, pad, rows, wfw, sense, ctx="", note=""):
    spans = "<br />\n  ".join('<span data-line="%d" data-start="" data-end="">%s</span>' % (i+1, lines[i]) for i in range(4))
    rows_md = "\n".join("| %s | %s |" % (a, b) for a, b in rows)
    extra = "\n\n%s\n" % note if note else "\n"
    ctx_b = "\n\n**Context / topic**  \n%s\n" % ox(ctx) if ctx else "\n"
    return (
        '<p class="verse-topic">श्लोकः %s (उपजाति)</p>\n'
        '<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v%d">\n  %s\n</div>\n'
        '<details>\n<summary>पदच्छेदः · Word-for-word · English (minimizable)</summary>\n'
        '<div class="prose-text" markdown="1">\n\n**पदच्छेदः**  \n%s\n\n**Word-for-word**\n\n%s\n\n'
        '**Gloss table**\n\n| पदम् | अर्थः / sense |\n| :---- | :---- |\n%s\n\n'
        '**English sense**  \n%s\n%s%s\n**वृत्तमिति**: एकादशाक्षराः पादाः।\n\n</div>\n</details>\n\n'
    ) % (dev(n), n, spans, pad, wfw_table(wfw), rows_md, ox(sense), ctx_b, extra)

def An(n,s1,s2,pad,rows,wfw,sense,ctx="",note=""):
    return v_anu(n,s1,s2,pad,rows,wfw,sense,ctx,note)
def Up(n,lines,pad,rows,wfw,sense,ctx="",note=""):
    return v_upa(n,lines,pad,rows,wfw,sense,ctx,note)

def chs(n2,n3,n4,n5,n6,th1,th2,th3,th4,th5,th6,th7="सारधर्मः / Close."):
    return [("प्रथमं प्रकरणम्: मङ्गलं बीजं च","अनुष्टुभ्: अष्टावक्षराणि प्रतिपादम्",th1),
            ("द्वितीयं प्रकरणम्: %s"%n2,"अनुष्टुभ्",th2),("तृतीयं प्रकरणम्: %s"%n3,"उपजातिः",th3),
            ("चतुर्थं प्रकरणम्: %s"%n4,"अनुष्टुभ्",th4),("पञ्चमं प्रकरणम्: %s"%n5,"अनुष्टुभ्",th5),
            ("षष्ठं प्रकरणम्: %s"%n6,"उपजातिः",th6),("सप्तमं प्रकरणम्: उपसंहारः","अनुष्टुभ्",th7)]

def emit(meta, chapter_list, verses):
    title = meta["title"]
    t = shell(title, meta["sub"], meta["date"], title, meta["tags"])
    t += '<p class="prose-text"><strong>%s।</strong> %s</p>\n\n' % (title, meta["intro_sa"])
    t += det("English (minimizable)", ox(meta["intro_en"]))
    t += det("पूर्ण-शीर्षकम् / Full title", "# **%s**: %s" % (title, meta["full"]))
    t += det("English · overview and topics (minimizable)", ox(meta["overview"]))
    t += det("परम्परा-सन्धिः / Series links", prior(meta["prior"]))
    t += det("ग्राह्य-त्याज्य-विवेकः / Keep and avoid", keep_drop(meta["keep"], meta["drop"]))
    t += det("अध्याय-योजना / Chapter plan", meta.get("plan") or plan_default())
    t += det("पारिभाषिक-कोशः / Glossary", gloss(meta["gloss"]))
    if meta.get("extra"):
        t += det(meta["extra"][0], ox(meta["extra"][1]))
    counts = [2,2,1,2,2,1,2]; vi=0
    for (ct,cm,cth), n in zip(chapter_list, counts):
        t += ch(ct, cm, cth)
        for _ in range(n):
            t += verses[vi]; vi += 1
    assert vi==12
    t += det("श्लोकसूची / Verse index", "\n".join("%s. %s  " % (dev(i), s) for i,s in enumerate(meta["shlist"],1)))
    t += det("सन्दर्भाः / References", "\n".join("%d. %s  " % (i, ox(s)) for i,s in enumerate(meta["refs"],1)))
    save("%s-%s.md" % (meta["date"], title), t)

def pack12(specs):
    out=[]
    for i,sp in enumerate(specs,1):
        if sp["k"]=="a":
            assert_anu_pair(sp["s1"], sp["s2"], "v%d" % i)
            out.append(An(i,sp["s1"],sp["s2"],sp.get("pad",sp["s1"]+"\n"+sp["s2"]),sp["r"],sp["w"],sp["en"],sp.get("cx",""),sp.get("n","")))
        else:
            assert_upa_quatrain(sp["l"], "v%d" % i)
            out.append(Up(i,sp["l"],sp.get("pad","\n".join(sp["l"])),sp["r"],sp["w"],sp["en"],sp.get("cx",""),sp.get("n","")))
    return out

def P(k,**kw):
    d={"k":k}; d.update(kw); return d

def base_meta(date,title,en_short,full,tags,intro_sa,intro_en,overview,prior,keep,drop,gloss,shlist,refs,extra=None):
    return dict(date=date,title=title,
        sub="द्वादश पद्यानि अनुष्टुभ्-उपजातिषु: %s. English in minimizable details."%en_short,
        tags=list(tags)+["english","panini"], intro_sa=intro_sa, intro_en=intro_en, full=full,
        overview=overview, prior=prior, keep=keep, drop=drop, gloss=gloss, shlist=shlist, refs=refs, extra=extra)

def emit_post(date, title, en_short, full, tags, intro_sa, intro_en, overview, prior, keep, drop, gloss, shlist, refs, ch_args, specs):
    emit(base_meta(date, title, en_short, full, tags, intro_sa, intro_en, overview, prior, keep, drop, gloss, shlist, refs),
         chs(*ch_args), pack12(specs))

print("lib ok")