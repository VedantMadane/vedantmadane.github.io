import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
RAW_TXT_PATH = ROOT / "shatakam_raw.txt"
ENGLISH_TXT_PATH = ROOT / "english.txt"
OUT_YML_PATH = ROOT / "_data" / "shatakam.yml"

# First verse of each paddhati (section): chapter_title + chapter_meta for the reader layout.
CHAPTER_HEADERS: dict[int, dict] = {
    1: {
        "chapter_title": "१. मूल्यपद्धतिः (Mūlya-Paddhati - On Value & Price)",
        "chapter_meta": {
            "keyword": "मूल्य (Mūlya) - Value",
            "theme": "Intrinsic Value & Price",
            "sages": "Benjamin Graham & Warren Buffett",
            "concepts": (
                "Price vs. Value (The shadow vs. the essence), Discounted Cash Flows "
                "(Roka-mūlyaṃ), Fractional Ownership (Buying the whole house), "
                "The Margin of Safety."
            ),
        },
    },
    11: {
        "chapter_title": "२. कालपद्धतिः (Kāla-Paddhati - On Market Cycles)",
        "chapter_meta": {
            "keyword": "काल (Kāla) - Cycles",
            "theme": "Market Cycles & Time",
            "sages": "Howard Marks",
            "concepts": (
                "The Pendulum of Greed and Fear, Mean Reversion (Mādhya-pratyāvartanam), "
                "The Illusion of Eternal Growth (Trees do not grow to the sky), "
                "Contrarian accumulation."
            ),
        },
    },
    21: {
        "chapter_title": "३. वृद्धिपद्धतिः (Vṛddhi-Paddhati - On Compounding)",
        "chapter_meta": {
            "keyword": "वृद्धि (Vṛddhi) - Compounding",
            "theme": "Uninterrupted Growth",
            "sages": "Warren Buffett & Charlie Munger",
            "concepts": (
                "The Power of Uninterrupted Time (The Banyan Tree), Reinvestment of Yield "
                "(Kāmadhenu), The destructive friction of trading and taxes, "
                "Inflation as the hidden moth."
            ),
        },
    },
    31: {
        "chapter_title": "४. मूर्खपद्धतिः (Mūrkha-Paddhati - On the Folly of the Crowd)",
        "chapter_meta": {
            "keyword": "मूर्ख (Mūrkha) - Folly",
            "theme": "The Madness of the Crowd",
            "sages": "Charles Mackay / Crowd Psychology",
            "concepts": (
                "The Greater Fool Theory (The Red-Hot Iron Ball), FOMO (The Golden Deer), "
                "\"This Time is Different\" syndrome, Valuing companies on dreams instead of "
                "cash flow, Liquidity Traps."
            ),
        },
    },
    41: {
        "chapter_title": "५. स्वरूपपद्धतिः (Svarūpa-Paddhati - On Knowing What You Own)",
        "chapter_meta": {
            "keyword": "स्वरूप (Svarūpa) - True Nature",
            "theme": "Knowing What You Own",
            "sages": "Peter Lynch",
            "concepts": (
                "The Circle of Competence (Sva-dharma), The Economic Moat (Ajeya-Meru), "
                "The \"Idiot-Proof\" Business, Boots on the Ground / Scuttlebutt "
                "(Pratyakṣa-pramāṇa), The danger of hidden debt."
            ),
        },
    },
    51: {
        "chapter_title": "६. विवेकपद्धतिः (Viveka-Paddhati - On Rationality & Mental Models)",
        "chapter_meta": {
            "keyword": "विवेक (Viveka) - Rationality",
            "theme": "Mental Models & Logic",
            "sages": "Charlie Munger",
            "concepts": (
                "The Latticework of Mental Models (Indra-jāla), Inversion (Viparīta-buddhi), "
                "Opportunity Cost, Mean Reversion, The 10 Traps of Human Misjudgment."
            ),
        },
    },
    61: {
        "chapter_title": "७. आपत्पद्धतिः (Āpad-Paddhati - On Risk Management)",
        "chapter_meta": {
            "keyword": "आपद् (Āpad) - Risk Management",
            "theme": "Survival & Protection",
            "sages": "Howard Marks & Benjamin Graham",
            "concepts": (
                "Rule No. 1 (Never Lose Money), The Math of Recovery, Avoiding the Single "
                "Point of Failure (The Multi-hulled Boat), The Theology of Survival over Profit."
            ),
        },
    },
    71: {
        "chapter_title": "८. अहङ्कारपद्धतिः (Ahaṅkāra-Paddhati - On Ego and Humility)",
        "chapter_meta": {
            "keyword": "अहङ्कार (Ahaṅkāra) - Ego",
            "theme": "Intellectual Humility",
            "sages": "Charlie Munger",
            "concepts": (
                "The Man with a Hammer syndrome, The Folly of Forecasting, Physics Envy "
                "(False precision in finance), The supreme power of saying \"I do not know.\""
            ),
        },
    },
    81: {
        "chapter_title": "९. साधनपद्धतिः (Sādhana-Paddhati - On the Discipline of Research)",
        "chapter_meta": {
            "keyword": "साधन (Sādhana) - Discipline",
            "theme": "The Process of Research",
            "sages": "Philip Fisher & Peter Lynch",
            "concepts": (
                "Independent Verification (Haṁsa-nyāya / Separating milk from water), "
                "Reading the fine print, Discarding Wall Street promoters, "
                "The pairing of intellect and stomach (emotional fortitude)."
            ),
        },
    },
    91: {
        "chapter_title": "१०. फलपद्धतिः (Phala-Paddhati - The Pathway of Results)",
        "chapter_meta": {
            "keyword": "फल (Phala) - Results",
            "theme": "The Ultimate Fruit of Wealth",
            "synthesis": "The ultimate goal of capital allocation",
            "concepts": (
                "Reclaiming your own time (Kāla-dhana), The logic of \"Enough\" (Paryāptam), "
                "The power to walk away, The Sthitaprajña (Equanimous) Investor, "
                "Financial Independence (Svatantratā)."
            ),
        },
    },
}

# Verse-level sūtra-style topics (Sanskrit + English gloss). Index 0 = Verse 1.
VERSE_TOPICS: tuple[str, ...] = (
    "मङ्गलाचरणम् (Invocation)",
    "लक्ष्मणरेखा (The Boundary of Safety)",
    "मूल्य-मूल्याङ्क-भेदः (Value vs. Price)",
    "पूर्णस्वामित्वम् (Fractional Ownership)",
    "रोकमूल्यम् (Discounted Cash Flow)",
    "यन्त्रभ्रमः (The Ticker Illusion)",
    "सार-छाया-भेदः (Essence vs. Shadow)",
    "सत्यान्वेषणम् (The Search for Intrinsic Value)",
    "मूल्यलाभः (Buying at a Discount)",
    "उपेक्षित-निधिः (The Ignored Treasure)",
    "कालचक्रम् (The Pendulum of Time)",
    "ऋतुपरिवर्तनम् (The Seasons of the Market)",
    "अनन्तवृद्धि-भ्रमः (The Illusion of Eternal Growth)",
    "माध्यप्रत्यावर्तनम् (Mean Reversion)",
    "इतिहासपुनरावृत्तिः (History Repeats)",
    "विपत्काले प्रवेशः (Entering in Panic)",
    "भय-लोभ-विपर्ययः (The Inversion of Greed and Fear)",
    "कालप्रकोपः (The Wrath of Time)",
    "कालचेष्टा (The Behavior of Time)",
    "कालजयी (The Conqueror of Cycles)",
    "वटवृक्षन्यायः (The Banyan Tree)",
    "हिमपिण्डन्यायः (The Snowball Effect)",
    "शृङ्खला-च्छेद-दोषः (The Flaw of Interruption)",
    "धैर्यफलम् (The Fruit of Patience)",
    "कामधेनु-संस्था (The Compounding Enterprise)",
    "वृथाव्यय-त्यागः (Avoiding Capital Destruction)",
    "छिद्रकुम्भ-दोषः (The Leaky Pot / Friction)",
    "मध्यस्थ-माया (The Illusion of the Middleman)",
    "मुद्रास्फीति-दोषः (The Invisible Moth of Inflation)",
    "गज-मृग-गतिः (The Limit of Size)",
    "अन्धपरम्परा (The Blind Herd)",
    "मेषवृत्तम् (The Flock of Sheep)",
    "तप्तलौह-कन्दुकः (The Greater Fool Theory)",
    "काच-स्वर्ण-भ्रमः (Buying Glass as Gold)",
    "परधन-द्यूतम् (Margin Debt / Leverage)",
    "नूतनयुग-भ्रमः (This Time is Different)",
    "शृगाल-कथा (Wall Street Promoters)",
    "चक्रव्यूह-प्रवेशः (The Liquidity Trap)",
    "गगनवृक्ष-भ्रमः (Trees Growing to the Sky)",
    "बुद्बुद-नाशः (The Bursting Bubble)",
    "स्वधर्मः (The Circle of Competence)",
    "ज्ञानसीमा (Knowing the Boundaries of Your Mind)",
    "बीजवृक्षः (Behind the Ticker is a Business)",
    "बालबोधः (The Two-Minute Drill)",
    "अजेयमेरुः (The Economic Moat)",
    'स्वचलितरथः (The "Idiot-Proof" Business)',
    "प्रत्यक्षप्रमाणम् (Boots on the Ground)",
    "सामान्यकार्यम् (The Beauty of the Boring Business)",
    "गूढव्याधिः (The Balance Sheet / Avoiding Debt)",
    "दृढनिश्चयः (The Ultimate Conviction)",
    "विपरीतबुद्धिः (Inversion)",
    "वृद्धिक्रमः (Compounding)",
    "वैकल्पिकव्ययः (Opportunity Cost)",
    "लक्ष्मणरेखा (Margin of Safety)",
    "स्वधर्मसीमा (Circle of Competence)",
    "अभिप्रेरणम् (Incentives)",
    "अनुकरणदोषः (Social Proof / Herd Mentality)",
    "माध्यप्रत्यावर्तनम् (Mean Reversion)",
    "इन्द्रजालम् (The Latticework)",
    "मोहजालम् (The Psychology of Misjudgment)",
    "प्रथमविधिः (Rule No. 1: Never Lose Money)",
    "हानिगणितम् (The Math of Recovery)",
    "साहसस्वरूपम् (Defining True Risk)",
    "सुरक्षासीमा (The Margin of Safety)",
    "सम्भाव्यफलम् (Probability vs. Outcome)",
    "बहुकोश-नौका (The Multi-hulled Boat / Redundancy)",
    "एकाधारविनाशः (Avoiding the Single Point of Failure)",
    "वात्यायां विवेकः (Rationality During the Storm)",
    "प्रतिकूलचिन्तनम् (Thinking of What Can Go Wrong)",
    "दोषनिवारणम् (Avoid Losers)",
    "कूपमण्डूकन्यायः (The Frog in the Well)",
    "कुठारिकान्यायः (The Man with a Hammer)",
    "भविष्यवाणि-दोषः (The Folly of Forecasting)",
    '"न जानामि" इति वाक्यम् (The "I Don\'t Know" Box)',
    "मिथ्या-परिशुद्धता (Physics Envy / False Precision)",
    "आत्मवञ्चना (Self-Deception / Denial)",
    "सिद्धान्त-बन्धः (Ideological Blindness)",
    "पूर्वसफलता-पाशः (The Trap of Past Success)",
    "विपरीत-विमर्षः (The Check on Ego / Pre-Mortem)",
    "प्रज्ञावतः लक्षणम् (The Mark of the Humble Sage)",
    "हंसन्यायः (Separating Milk from Water)",
    "सूक्ष्मदृष्टिः (Reading the Fine Print)",
    "क्षेत्रदर्शनम् (Scuttlebutt / Boots on the Ground)",
    "लोककथा-श्रवणम् (Listening to the Crowd / Verification)",
    "स्वतन्त्र-शोधनम् (Independent Research)",
    "वर्म-अन्वेषणम् (Searching for the Moat)",
    "सत्यमार्ग-संस्था (Integrity of Management)",
    "निर्मल-पत्रम् (The Spotless Balance Sheet)",
    "बुद्धि-धैर्य-योगः (Intellect and Fortitude)",
    "निरन्तर-श्रमः (Continuous Discipline)",
    "स्वातन्त्र्यलक्षणम् (The Definition of Freedom)",
    "त्यागशक्तिः (The Power to Walk Away)",
    "कालधनम् (Time as the True Currency)",
    'पर्याप्तबोधः (The Logic of "Enough")',
    "स्थितप्रज्ञ-वणिक् (The Sthitaprajña Investor)",
    "सत्यनिवेशः (Wealth with Integrity)",
    "ज्ञानदायः (The Legacy of Wisdom)",
    "चतुर्मुनि-स्मरणम् (Salutations to the Four Sages)",
    "ग्रन्थसमाप्तिः (Conclusion of the Work)",
    "मङ्गलम् (The Final Dedication)",
)

_DEV_TO_ASCII = str.maketrans("०१२३४५६७८९", "0123456789")


def _devanagari_int(s: str) -> int:
    return int(s.translate(_DEV_TO_ASCII))


def load_verses_from_raw(path: Path) -> list[dict]:
    """Parse shatakam_raw.txt: section headings skipped; each śloka ends with ॥ <devanagari> ॥."""
    lines = path.read_text(encoding="utf-8").splitlines()
    section_re = re.compile(r"^[०-९]+\.\s")
    verse_end_re = re.compile(r"॥\s*([०-९]+)\s*॥\s*$")

    verses: list[dict] = []
    buf: list[str] = []
    skip_title = True

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if skip_title:
            if stripped.startswith("॥") and stripped.endswith("॥"):
                skip_title = False
            continue

        if section_re.match(stripped):
            continue

        if not buf and stripped.endswith("॥") and not verse_end_re.search(stripped):
            continue

        buf.append(line.rstrip())
        if verse_end_re.search(stripped):
            m = verse_end_re.search(stripped)
            num = _devanagari_int(m.group(1))
            verses.append(
                {
                    "number": num,
                    "sanskrit": "\n".join(buf),
                    "audio_start": 0.0,
                    "audio_end": 0.0,
                    "words": [],
                }
            )
            buf.clear()

    if buf:
        raise ValueError(f"Unclosed verse block at end of file ({len(buf)} lines left)")

    return verses


def load_english_translations(path: Path) -> dict[int, dict[str, str]]:
    """
    Parse english.txt: blocks anchored by [Verse N], optional Poetic: then Prose:.
    """
    text = path.read_text(encoding="utf-8")
    if text.startswith("\ufeff"):
        text = text[1:]

    blocks = re.split(r"(?=^\[Verse \d+\]\s*$)", text, flags=re.MULTILINE)
    out: dict[int, dict[str, str]] = {}

    header_re = re.compile(r"^\[Verse (\d+)\]\s*", re.MULTILINE)
    prose_start = re.compile(r"(?m)^Prose:\s*")

    for block in blocks:
        block = block.strip()
        if not block:
            continue
        hm = header_re.match(block)
        if not hm:
            continue
        vid = int(hm.group(1))
        body = block[hm.end() :].strip()

        prose = ""
        poetic = ""

        if body.startswith("Poetic:"):
            rest = body[len("Poetic:") :].lstrip("\n")
            pm = prose_start.search(rest)
            if pm:
                poetic = rest[: pm.start()].strip()
                prose = rest[pm.end() :].strip()
            else:
                poetic = rest.strip()
        elif body.startswith("Prose:"):
            prose = body[len("Prose:") :].strip()
        else:
            prose = body

        out[vid] = {"prose": prose, "poetic": poetic}

    return out


def generate_shatakam_yaml() -> None:
    if len(VERSE_TOPICS) != 100:
        raise ValueError(f"VERSE_TOPICS must have 100 entries, got {len(VERSE_TOPICS)}")

    raw_data = load_verses_from_raw(RAW_TXT_PATH)
    english = load_english_translations(ENGLISH_TXT_PATH)

    missing = [v["number"] for v in raw_data if v["number"] not in english]
    if missing:
        raise ValueError(f"Missing English blocks for verses: {missing[:10]}{'...' if len(missing) > 10 else ''}")

    yaml_output: list[dict] = []

    for verse in raw_data:
        n = verse["number"]
        eng = english[n]
        lines = verse["sanskrit"].split("\n")

        entry: dict = {
            "number": n,
            "topic": VERSE_TOPICS[n - 1],
            "audio_start": verse["audio_start"],
            "audio_end": verse["audio_end"],
            "sanskrit_lines": lines,
            "words": verse["words"],
            "prose": eng["prose"],
        }
        if eng["poetic"]:
            entry["poetic"] = eng["poetic"]

        ch = CHAPTER_HEADERS.get(n)
        if ch:
            entry["chapter_title"] = ch["chapter_title"]
            entry["chapter_meta"] = ch["chapter_meta"]

        yaml_output.append(entry)

    OUT_YML_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_YML_PATH.open("w", encoding="utf-8") as f:
        yaml.dump(yaml_output, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    with_poetic = sum(1 for e in yaml_output if "poetic" in e)
    print(f"Successfully generated {OUT_YML_PATH} ({len(yaml_output)} verses, {with_poetic} with poetic).")


if __name__ == "__main__":
    generate_shatakam_yaml()
