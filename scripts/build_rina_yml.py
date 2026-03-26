"""Build _data/rina.yml from C:\\Projects\\shatakam\\Sanskrit Verse on Debt, Nations, Decisions.txt"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from indic_transliteration import sanscript as S
except ImportError:
    print("pip install indic-transliteration", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(r"C:\Projects\shatakam\Sanskrit Verse on Debt, Nations, Decisions.txt")
OUT = ROOT / "_data" / "rina.yml"


def normalize_iast_for_transliteration(s: str) -> str:
    """Split common compound hyphens so indic_transliteration produces readable Devanāgarī."""
    t = s
    # hi + āsa / ā… sandhi written hy- in file
    t = re.sub(r"\bhy-ā", "hi ā", t)
    t = re.sub(r"\bHy-ā", "Hi ā", t)
    # tv-ali → tu ali (tv alīsā)
    t = re.sub(r"\btv-ali", "tu ali", t)
    # Break compound before vowel-initial piece: ṛṇam-ādau → ṛṇam ādau
    t = re.sub(
        r"-([āīūṛṝḷēōaAiIuUeEoOR̥r̥̄ḷĀĪŪṚṜḶ])",
        r" \1",
        t,
    )
    return t


def to_devanagari(iast: str) -> str:
    iast = normalize_iast_for_transliteration(iast.strip())
    dev = S.transliterate(iast, S.IAST, S.DEVANAGARI)
    # Remaining hyphens between aksaras: use space for pada-like readability
    prev = None
    while prev != dev:
        prev = dev
        dev = re.sub(r"([\u0900-\u097F])-([\u0900-\u097F])", r"\1 \2", dev)
    return dev


# Verse IAST lines (cleaned of trailing citation / prose); order matches document
VERSES_IAST: list[tuple[int, str, str, str]] = [
    # (num, meter, iast_one_line, notes)
    (
        1,
        "Anuṣṭubh",
        "ṛṇam-ādau purā hy-āsa na vinimaya-saṃśrayaḥ । lekhyāny-eva pradhānāni dravya-māpanam-antare ॥ 1 ॥",
        "",
    ),
    (
        2,
        "Anuṣṭubh",
        "mānavā hy-ṛṇa-sambandhair-baddhāḥ prāyeṇa sarvadā । na tad-dravyasya doṣas-tu mānasaḥ kila vā-bhavaḥ ॥ 2 ॥",
        "",
    ),
    (
        3,
        "Upajāti",
        "na vai suvarṇena kṛtā hi vṛddhir na cāpi śulkena vinimaya-yuktiḥ । ṛṇaṃ hi sāmājika-bandhanam syād yuddhais-tathaivātra samṛddhi-pāśaḥ ॥ 3 ॥",
        "",
    ),
    (
        4,
        "Mandākrāntā",
        "akṣa-kāle yuddha-dravya-dāsa-parigrahaḥ nāṇakānāṃ bahula-pracaro rāṣṭra-mūlam । bhautika-vādaḥ prabhavati sadā dāsa-vṛddhyā dharmas-tatra pratikṛti-vidhau jāyate vai ॥ 4 ॥",
        "",
    ),
    (
        5,
        "Vaṃśastha",
        "ṛṇaṃ ca pāpaṃ ca samānam uktaṃ vedeṣu pūrveṣu maharṣibhiś-ca । ṛṇāt-pramuktaḥ puruṣaḥ sa jīved yathā mṛteḥ pāśa-vabandhanāni ॥ 5 ॥",
        "",
    ),
    (
        6,
        "Śārdūlavikrīḍita",
        "1971-varṣe niksanaḥ prāha niścitam svarṇena naiva sambandho dollar-dravyasya vidyate । ṛṇa-dhūmena guptā vai rāṣṭra-vitta-sthitir-hi sā yuddha-kośaiḥ samṛddhā hi dāsa-yantraṃ pravartate ॥ 6 ॥",
        "",
    ),
    (
        7,
        "Hariṇī",
        "na hi vijayo vācyaḥ pūrvaṃ vināśapatho hi saḥ kathamapi bhaved rāṣṭraṃ naṣṭaṃ tadeva vicintyatām । tadanu matimān doṣān sarvān pramuñcati yatnataḥ viparītamidaṃ buddherdvāraṃ vadanti manīṣiṇāḥ ॥ 7 ॥",
        "",
    ),
    (
        8,
        "Śārdūlavikrīḍita",
        "śoṣaka-saṃsthāḥ kila tatra rāṣṭre yeṣu prabhuṇāṃ hi hitaṃ vidheyam । mita-vyakti-hitāya niiti-racanā rāṣṭraṃ vinaṣṭiṃ vrajet nūnam-eva ॥ 8 ॥",
        "",
    ),
    (
        9,
        "Vasantatilakā",
        "yo vā mārga-virodha-dharmir-upajaḥ śoṣo rathānāṃ nṛṇām mita-vyakti-hitāya niiti-racanā rāṣṭraṃ vinaṣṭiṃ vrajet । yadvat nogalesa-khaṇḍa-dvayam-idaṃ dṛṣṭānta-mūlaṃ bhavet tatraikaṃ tu dhanaḍhyam-asti ruciraṃ cānyaṃ tu dīnaṃ kila ॥ 9 ॥",
        "",
    ),
    (
        10,
        "Mālinī",
        "anubhavati daridraḥ klesham-atra tri-vāraṃ adhama-vibhavatā syād-anistatvaṃ ca mūlam । na ca sa-vidha-kośāḥ santi saṃrakṣaṇāya tad-api vibhu-kuśalaḥ kosa-yuktaḥ sadaiva ॥ 10 ॥",
        "",
    ),
    (
        11,
        "Anuṣṭubh",
        "vitta-grāsa-tri-guṇa-nihito dīna-lokas-tv-anantam klesham bhuñkte tad api kuśalaḥ kośa-yukto viviktā । ṛṇa-vyāptiṃ sa khalu kurute bandhu-vargaiḥ samam vai viparīta-buddhyā rakṣati jīvanam ॥ 11 ॥",
        "",
    ),
    (
        12,
        "Upajāti",
        "dvau suparṇau sayujā sakhāyā samānaṃ vṛkṣaṃ pariṣasvajāte । tayoranyaḥ pippalaṃ svādvatti anaśnannanyo abhicākaśīti ॥ 12 ॥",
        "",
    ),
    (
        13,
        "Vasantatilakā",
        "śīghra-buddhis-tv-aliisā syān-manda-buddhiśca jaḍimaḥ ubhayor-mela-bhedena nirṇayo vidyate subhaḥ । yadvat kṛṣṇa-vakaḥ purā na viditaḥ siddhānta-haṃsa-bhramaḥ bhāgyasyaiva hi khelanam-atra dṛśyate prāyeṇa loke kila ॥ 13 ॥",
        "",
    ),
    (
        14,
        "Śārdūlavikrīḍita",
        "prakruṣṭasya ca mañcake kila yathā saṃkoca-śoṣa-bhramo vidyā-tarkam-idaṃ tathaiva hi kṛtaṃ satyasya vinaṣṭaye । yadvat-saṃkhyā-vido doṣāḥ prabhavanti hi mānavānām intrinsic-value-iti tasya nāma mārga-bhrama-tyāga-vidhau samartham ॥ 14 ॥",
        "",
    ),
    (
        15,
        "Anuṣṭubh",
        "mungaraḥ prāha tat-sarvaṃ lollapalooza-lakṣaṇam । pañca-viṃśati-doṣaiśca nirṇayo bhramyate dhruvam ॥ 15 ॥",
        "",
    ),
    (
        16,
        "Anuṣṭubh",
        "inseptiva-super-response ca śaktiḥ parama-dāruṇā । mānasas-tu vyavasthāyāṃ dvitīya-caraṇaṃ viduḥ ॥ 16 ॥",
        "",
    ),
    (
        17,
        "Puṣpitāgrā",
        "iti kila nirṇaya-vidhi-bhedaiḥ prabhavati tipping-point-iti bhāvyate loke । chasm-iti langhanam-iha ca vighna-hetuṃ position-iti sthiratāṃ prayāti ॥ 17 ॥",
        "",
    ),
    (
        18,
        "Mandākrāntā",
        "vilar-vākye prabhavati sadā dāsa-nando nṛṇāṃ vai mānasa-yantre dṛḍha-vaśa-vidhau śoṣaṇaṃ dṛśyate vai । pre-suasion ca kila manas-capturing cāldini-yuktyā bhramayatikāñcana-maya-mṛgaṃ nirṇayeṣu pradhānam ॥ 18 ॥",
        "",
    ),
    (
        19,
        "Sragdharā",
        "it-thaṃ rāṣṭre ca vitte kila niviśati yo vā nirṇayaḥ sa-prakāraḥ viparītaṃ tu dṛṣṭvā prapashyati budho naiva mohaṃ prayāti । ṛṇa-pāśāt pramuktaḥ prabhavati jaya-kṛd rāṣṭra-pālas-tathaiva satyasya mārga-darśī hita-m-iha sakalaṃ sādhu-yogaṃ vidheyam ॥ 19 ॥",
        "",
    ),
    (
        20,
        "Anuṣṭubh",
        "ṛṇa-saṃsthā-viveka-jñaḥ pāpa-śoṣa-nivārakaḥ । rāṣṭrasya-mānasa-jñānaṃ pūrṇaṃ siddhi-pathaṃ vrajet ॥ 20 ॥",
        "",
    ),
]


def clean_verse_iast(line: str) -> str:
    """Remove trailing citation markers like ' ॥ 1 ॥ 1' → keep single verse number in devanagari later."""
    line = line.strip()
    line = re.sub(r"\s*\(Verse\s+[^)]+\)\s*", " ", line)
    # Normalize multiple closing numbers to one
    line = re.sub(r"(॥\s*\d+\s*॥)\s*\d+\s*$", r"\1", line)
    line = re.sub(r"\s+\d+\s*$", "", line)
    line = line.replace("prabhuuṇāṃ", "prabhuṇāṃ")
    line = line.replace("mungaraḥ", "maṅgaraḥ")
    return line.strip()


DIGIT_MAP = str.maketrans("0123456789", "०१२३४५६७८९")


def devanagari_digits_from_suffix(s: str) -> str:
    return s.translate(DIGIT_MAP)


def extract_prose_blocks(path: Path, verse_indices: list[int], lines: list[str]) -> list[str]:
    """English prose after each verse line until the next verse (by line index)."""
    verse_line_pattern = re.compile(
        r"^[a-zA-ZṛṇśṣḍṭḥṅñāīūēōûĀĪŪṚṢḌṬḤṀṁṝ0-9].*॥\s*\d+\s*॥"
    )
    prose: list[str] = []
    for k, vi in enumerate(verse_indices):
        start = vi + 1
        end = verse_indices[k + 1] if k + 1 < len(verse_indices) else len(lines)
        buf: list[str] = []
        for j in range(start, end):
            n = lines[j].strip()
            if not n:
                continue
            if n.startswith("Vṛttam:") or verse_line_pattern.match(lines[j].strip()):
                break
            if n.startswith("Prathamaḥ") or n.startswith("Dvitīyaḥ") or n.startswith("Tṛtīyaḥ"):
                break
            if n.startswith("Historical Cycle") or n.startswith("Institutional Element"):
                break
            if n.startswith("Cognitive Bias") or n.startswith("Statistical"):
                break
            if n.startswith("Book / Research") or n.startswith("Works cited"):
                break
            if n.startswith("Through this exhaustive"):
                break
            if n.startswith("____"):
                break
            if re.match(r"^\d+$", n):
                continue
            if n.startswith("\t"):
                continue
            buf.append(lines[j])
        prose.append(" ".join(x.strip() for x in buf if x.strip()))
    # Consecutive ślokas share one gloss (e.g. vv. 15–16)
    for k in range(len(prose) - 1):
        if not prose[k] and prose[k + 1]:
            prose[k] = prose[k + 1]
    for k in range(1, len(prose)):
        if not prose[k] and prose[k - 1]:
            prose[k] = prose[k - 1]
    return prose


# Mixed IAST–English ślokas: Devanāgarī with Latin technical terms in parentheses
TEXT_SA_OVERRIDES: dict[int, str] = {
    6: (
        "१९७१ वर्षे निक्सनः प्राह निश्चितम् स्वर्णेन नैव सम्बन्धो डॉलर-द्रव्यस्य विद्यते । "
        "ऋण-धूमेन गुप्ता वै राष्ट्र-वित्त-स्थितिर्हि सा युद्ध-कोशैः समृद्धा हि दास-यन्त्रं प्रवर्तते ॥ ६ ॥"
    ),
    14: (
        "प्रक्रुष्टस्य च मञ्चके किल यथा संकोच-शोष-भ्रमो विद्या-तर्कम् इदं तथैव हि कृतं सत्यस्य विनष्टये । "
        "यद्वत् संख्या-विदो दोषाः प्रभवन्ति हि मानवानाम् (intrinsic value) इति तस्य नाम "
        "मार्ग-भ्रम-त्याग-विधौ समर्थम् ॥ १४ ॥"
    ),
    17: (
        "इति किल निर्णय-विधि-भेदैः प्रभवति (tipping-point) इति भाव्यते लोके । "
        "(chasm) इति लङ्घनम् इह च विघ्न-हेतुं (position) इति स्थिरतां प्रयाति ॥ १७ ॥"
    ),
    18: (
        "विलर्-वाक्ये प्रभवति सदा दास-नन्दो नृणां वै मानस-यन्त्रे दृढ-वश-विधौ शोषणं दृश्यते वै । "
        "(pre-suasion) च किल (manas-capturing) चाल्दिनि-युक्त्या भ्रमयति काञ्चन-मय-मृगं निर्णयेषु प्रधानम् ॥ १८ ॥"
    ),
    19: (
        "इत्थं राष्ट्रे च वित्ते किल निविशति यो वा निर्णयः स-प्रकारः विपरीतं तु दृष्ट्वा प्रपश्यति बुधो नैव मोहं प्रयाति । "
        "ऋण-पाशात् प्रमुक्तः प्रभवति जय-कृद् राष्ट्र-पालस् तथैव सत्यस्य मार्ग-दर्शी हितम् इह सकलं साधु-योगं विधेयम् ॥ १९ ॥"
    ),
}


def main() -> int:
    if not SRC.is_file():
        print("Missing", SRC, file=sys.stderr)
        return 1

    lines = SRC.read_text(encoding="utf-8").splitlines()
    verse_line_pattern = re.compile(
        r"^[a-zA-ZṛṇśṣḍṭḥṅñāīūēōûĀĪŪṚṢḌṬḤṀṁṝ0-9].*॥\s*\d+\s*॥"
    )

    verse_indices: list[int] = []
    auto_verses: list[str] = []
    for i, line in enumerate(lines):
        s = line.strip()
        if not s or s.startswith("Vṛttam:"):
            continue
        if s.startswith("Prathamaḥ") or s.startswith("Dvitīyaḥ") or s.startswith("Tṛtīyaḥ"):
            continue
        if s.startswith("Historical") or s.startswith("Institutional"):
            continue
        if s.startswith("Cognitive Bias") or s.startswith("Statistical"):
            continue
        if s.startswith("Book /") or s.startswith("Works cited") or s.startswith("Through this"):
            continue
        if s.startswith("Ṛṇa-Saṃsthā") or s.startswith("The following research"):
            continue
        if "॥" in s and re.search(r"॥\s*\d+\s*॥", s) and verse_line_pattern.match(s):
            verse_indices.append(i)
            auto_verses.append(clean_verse_iast(s))

    verses_src = auto_verses if len(auto_verses) == 20 else [clean_verse_iast(v[2]) for v in VERSES_IAST]

    if len(verses_src) != 20:
        print("Expected 20 verses, got", len(verses_src), file=sys.stderr)
        return 1

    meters = [v[1] for v in VERSES_IAST]

    prose_blocks = extract_prose_blocks(SRC, verse_indices, lines)
    if len(prose_blocks) != 20:
        print("Warning: prose blocks", len(prose_blocks), "expected 20", file=sys.stderr)

    import yaml

    title_line = lines[0].strip().lstrip("\ufeff")
    intro = lines[1].strip() if len(lines) > 1 else ""

    verses_out: list[dict] = []
    for idx, iast in enumerate(verses_src, start=1):
        iast_clean = clean_verse_iast(iast)
        # English loanwords: transliterate in chunks
        if idx in TEXT_SA_OVERRIDES:
            dev = TEXT_SA_OVERRIDES[idx]
        else:
            dev = to_devanagari(iast_clean)
            dev = re.sub(
                r"॥\s*(\d+)\s*॥",
                lambda m: f"॥ {devanagari_digits_from_suffix(m.group(1))} ॥",
                dev,
            )
        meaning = prose_blocks[idx - 1] if idx - 1 < len(prose_blocks) else ""
        verses_out.append(
            {
                "id": idx,
                "meter_en": meters[idx - 1] if idx <= len(meters) else "",
                "text_iast": iast_clean,
                "text_sa": dev.strip(),
                "meaning": meaning,
            }
        )

    khandas = [
        {
            "slug": "prathama",
            "title_iast": "Prathamaḥ Khaṇḍaḥ: Ṛṇa-Tattva-Mīmāṃsā — Graeber-Siddhāntaḥ",
            "title_en": "First section: Inquiry into the nature of debt — Graeber’s teaching",
            "verse_range": [1, 6],
        },
        {
            "slug": "dvitiya",
            "title_iast": "Dvitīyaḥ Khaṇḍaḥ: Rāṣṭra-Vinaṣṭi-Mīmāṃsā — Viparīta-buddhi-Paddhatiḥ",
            "title_en": "Second section: Why nations fail — the method of inverted intellect",
            "verse_range": [7, 11],
        },
        {
            "slug": "trtiya",
            "title_iast": "Tṛtīyaḥ Khaṇḍaḥ: Nirṇaya-Viveka-Siddhāntaḥ — Indra-jāla-Paddhatiḥ",
            "title_en": "Third section: Decision and discernment — Indra’s net (mental models)",
            "verse_range": [12, 20],
        },
    ]

    by_id = {v["id"]: v for v in verses_out}
    sections_out = []
    for kh in khandas:
        lo, hi = kh["verse_range"]
        sections_out.append(
            {
                "slug": kh["slug"],
                "title_iast": kh["title_iast"],
                "title_en": kh["title_en"],
                "verses": [by_id[i] for i in range(lo, hi + 1)],
            }
        )

    data = {
        "title_iast": title_line,
        "intro_en": intro,
        "sections": sections_out,
    }

    OUT.write_text(
        yaml.dump(
            data,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=118,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(OUT, "verses", len(verses_out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
