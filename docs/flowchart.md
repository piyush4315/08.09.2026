# MSETCL — Asset Retirement, Scrap Declaration & Disposal Policy
### The whole policy explained as flow charts

Source documents in this repo:
- `Policy.pdf` — the policy circular (Ref: MSETCL/CO/Trans(O&M)/…, signed by Director (Operations))
- `MSA wardha new scrapping policy.pdf` — the 19-slide presentation of the same policy
- `covering letter.pdf` — covering letter from the Chief Engineer (Trans O&M) dated 02.12.2024

The policy has **two halves** that run one after the other:

> **Part 1 — ASSET RETIREMENT** (take the asset out of the books/service) → **Part 2 — SCRAP DECLARATION & DISPOSAL** (sell/destroy the physical material and recover money).

---

## 0. Master flow — one page, end to end

```mermaid
flowchart TD
    A["ASSET IN SERVICE<br/>Transmission line &amp; sub-station material,<br/>machinery, vehicles, office furniture, IT equipment"]
    A --> B["<b>STEP 1 — IDENTIFY &amp; CATEGORISE</b><br/>Asset Owner sorts the asset into<br/>Category A(a), A(b), B, C, D or E<br/>(see Chart 1)"]
    B --> C["<b>STEP 2 — DECLARE RETIREMENT</b><br/>Proforma-A / Proforma-B → CLARC<br/>CLARC declares the asset retired from MSETCL<br/>(see Chart 2)"]
    C --> D["<b>STEP 3 — HAND OVER</b><br/>Asset owner hands the asset + retirement<br/>certificate to Executive Engineer (Store)"]
    D --> E["<b>STEP 4 — VALUE &amp; MAKE LOTS</b><br/>Check book value → physical survey →<br/>fix Reserve Price &amp; STA% → make lots<br/>(see Chart 3)"]
    E --> F["<b>STEP 5 — APPROVE</b><br/>ZSC scrutinises &amp; recommends MRP + STA% →<br/>Competent Authority approves as per GO 1 (F&amp;A)"]
    F --> G["<b>STEP 6 — DISPOSE</b><br/>e-Auction of approved lots through MSTC<br/>(see Chart 4)"]
    G --> H["<b>STEP 7 — REALISE</b><br/>H-1 bidder pays 10% EMD + balance by RTGS<br/>→ Delivery Order → material lifted"]
    H --> I["<b>STEP 8 — DE-CAPITALISE</b><br/>EE (Store) intimates item-wise scrap cost →<br/>Finance deletes item from Asset Register"]

    B -.->|"Category E<br/>(zero salvage value)"| X["Destroy / dispose as garbage-debris<br/>No auction"]
    B -.->|"IT equipment<br/>(PC, laptop, printer, scanner)"| IT["SCIT route<br/>(see Chart 5)"]
    D -.->|"Used lead acid batteries"| BT["Separate HAZARDOUS WASTE lot<br/>only registered recyclers may bid<br/>(see Chart 6)"]
    G -.->|"No bid / bid below STA% /<br/>H-1 defaults on EMD"| R["ZSC re-analysis → raise STA% or re-fix MRP<br/>→ re-auction → if still unsold, shift lot to Category E"]

    style B fill:#e3f2fd,stroke:#1565c0
    style C fill:#e8f5e9,stroke:#2e7d32
    style F fill:#fff8e1,stroke:#f9a825
    style G fill:#f3e5f5,stroke:#6a1b9a
    style I fill:#eceff1,stroke:#455a64
```

---

## 1. Chart 1 —Which category does the asset fall in? (the entry gate)

Every asset is first sorted into one of six buckets. The category decides **which form is used** and **how often** it is reported.

```mermaid
flowchart TD
    S(["Asset found unserviceable / aged / surplus"]) --> L{"Has it served its<br/>useful life?"}
    L -->|"Yes — but STILL IN ACTIVE USE"| AA["<b>CATEGORY A(a)</b><br/>Life over, still running"]
    L -->|"Yes — REMOVED from active use,<br/>or to be replaced by<br/>technologically advanced equipment"| AB["<b>CATEGORY A(b)</b><br/>Life over, taken out of service"]
    L -->|No| D1{"Damaged, unserviceable or<br/>beyond economic repair<br/>WITHIN its defined life?"}
    D1 -->|Yes| CC["<b>CATEGORY C</b><br/>Failed / beyond repair<br/>(incl. burnt, burst, degraded parameters)"]
    D1 -->|No| O1{"Obsolete and retention<br/>has become uneconomical?"}
    O1 -->|Yes| BB["<b>CATEGORY B</b><br/>Obsolete, uneconomic to keep"]
    O1 -->|No| V1{"Any salvage value left?"}
    V1 -->|"Meagre value — e-waste, packing boxes,<br/>empty containers, office furniture,<br/>discarded stationery, out-of-date spares"| DD["<b>CATEGORY D</b><br/>Misc. scrap with meagre salvage value"]
    V1 -->|"No worth at all — deteriorated wood,<br/>packing material, debris"| EE["<b>CATEGORY E</b><br/>Zero salvage value"]

    AA --> P1["Proforma-A — HALF-YEARLY to CLARC"]
    AB --> P2["Proforma-B — QUARTERLY to CLARC"]
    BB --> P2
    CC --> P2
    DD --> P2
    EE --> P3["Recommended for destruction /<br/>disposal as garbage-debris"]

    style AA fill:#e3f2fd,stroke:#1565c0
    style AB fill:#e3f2fd,stroke:#1565c0
    style BB fill:#fff8e1,stroke:#f9a825
    style CC fill:#ffebee,stroke:#c62828
    style DD fill:#f3e5f5,stroke:#6a1b9a
    style EE fill:#eceff1,stroke:#455a64
```

> **Gate before retiring (Policy 1.3):** before anything is retired, the asset owner must first satisfy that **no alternate economic use exists anywhere within MSETCL**. Only then is retirement started.

---

## 2. Chart 2 — Part 1: Asset Retirement approval chain

Four bodies sit in a row: **Asset Owner → CLARC → ZSC → CO R&D Committee**.

```mermaid
flowchart TD
    subgraph OWNER["ASSET OWNER (concerned division)"]
        O1["Identifies the asset &amp; its category"]
        O2["Prepares Asset Assessment Certificate<br/><b>Proforma-A</b> for Cat. A(a) — half-yearly<br/><b>Proforma-B</b> for Cat. A(b), B, C, D — quarterly"]
        O3["Organises JOINT INSPECTION of the<br/>items/materials through CLARC"]
        O1 --> O2 --> O3
    end

    subgraph CLARC["CLARC — Circle Level Asset Retirement Committee (one per Circle)"]
        C0["SE (O&amp;M) Circle — Chairman<br/>EE (O&amp;M) concerned division — Conveyor<br/>EE (Testing) concerned division — Member<br/>Manager (F&amp;A) concerned Circle — Member"]
        C1{"Category?"}
        C2["Cat. A(a): scrutinise &amp; ascertain whether the<br/>asset NEEDS TO CONTINUE in service<br/>→ give CONCURRENCE to continue"]
        C3["Cat. A(b), B, C, D: certify<br/>IDENTIFICATION → DECLARATION → RETIREMENT"]
        C4["Issue <b>Asset Retirement Report</b>:<br/>description, book value, reasons for retirement"]
        C0 --> C1
        C1 -->|"A(a)"| C2
        C1 -->|"A(b), B, C, D"| C3
        C3 --> C4
    end

    subgraph ZSC1["ZSC — Zonal Scrapping Committee (reporting leg)"]
        Z1["Consolidate CLARC reports of the zone"]
        Z2["Add views / observations / remarks"]
        Z3["Submit to CO R&amp;D Committee EVERY QUARTER"]
        Z1 --> Z2 --> Z3
    end

    subgraph CORD["CO R&amp;D Committee — Corporate Office"]
        R1["Director (Operations) — Chairman<br/>Chief Engineer (O&amp;M) — Conveyor<br/>Chief Engineer (Design) — Member<br/>CGM (Finance) — Member<br/>SE (CPA) — Member"]
        R2["Take CORRECTIVE ACTION on ZSC reports<br/>(technology / design / O&amp;M feedback loop)"]
        R1 --> R2
    end

    O3 --> CLARC
    C2 -->|"Concurrence given"| KEEP["Asset continues in service<br/>→ reviewed again next half-year"]
    KEEP -.-> O1
    C4 -->|"Cat. A, B, C (and items burnt/burst/<br/>degraded within life)"| ZSC1
    Z3 --> CORD
    C4 -->|"Cat. D / E"| NEXT(["Move to Part 2 —<br/>Scrapping &amp; Disposal"])
    C3 --> NEXT

    style CLARC fill:#e8f5e9,stroke:#2e7d32
    style ZSC1 fill:#fff8e1,stroke:#f9a825
    style CORD fill:#e3f2fd,stroke:#1565c0
```

---

## 3. Chart 3 — Part 2: Scrapping & disposal procedure

Once CLARC declares the asset retired, **EE (Store) drives the file from here till the money is realised** (General Guideline 6).

```mermaid
flowchart TD
    START(["CLARC declares asset RETIRED<br/>+ issues Retirement Certificate"]) --> H1["Asset owner hands over the asset and the<br/>retirement certificate to <b>EE (Store)</b>"]
    H1 --> S1["EE (Store) scrutinises the scrap proposal<br/>+ verifies the REASON for scrap declaration"]
    S1 --> S2["Check BOOK VALUE of every item;<br/>Manager (F&amp;A) plays the key role here"]
    S2 --> BV{"Book value readily<br/>available in the<br/>Asset Register?"}
    BV -->|No| BV1["Item not in Asset Register:<br/>ZSC arrives at a ROUGH book value from<br/>likely purchase price − depreciation;<br/>Finance Dept. fixes value during PPE<br/>physical verification;<br/>O&amp;M issues weight guidelines"]
    BV -->|Yes| S3
    BV1 --> S3["EE (Store) prepares CONSOLIDATED<br/>SCRAPPING LIST with book / depreciated value"]
    S3 --> Z1["<b>ZSC</b> grants IN-PRINCIPLE APPROVAL of the scrap"]
    Z1 --> Z2["EE (Store) conducts PHYSICAL SURVEY<br/>of the scrap material"]
    Z2 --> Z3["Fix <b>RESERVE PRICE</b> within 7 days from<br/>last auctioned rate or latest metal scrap<br/>rates published on the MSTC site"]
    Z3 --> Z4["MAKE LOTS — realistic lotting + realistic<br/>reserve price is the key to a successful auction"]
    Z4 --> Z5["<b>ZSC</b> scrutinises the whole proposal and<br/>recommends MRP + STA% + lot details"]
    Z5 --> CA{"Competent Authority<br/>approval as per<br/><b>GO No. 1 (F&amp;A)</b> MSETCL"}
    CA -->|"Returned / query"| Z5
    CA -->|"Approved"| AUC["<b>e-AUCTION through MSTC</b><br/>Disposal of the approved lot<br/>(see Chart 4)"]

    subgraph ZSCB["ZSC — Zonal Scrapping Committee (disposal leg)"]
        ZC["Chief Engineer, EHV PC O&amp;M Zone — Chairman<br/>Superintending Engineer (Testing) — Member<br/>AGM (F&amp;A) — Member<br/>Executive Engineer (Store) — Conveyor"]
    end

    style ZSCB fill:#fff8e1,stroke:#f9a825
    style CA fill:#ffebee,stroke:#c62828
    style AUC fill:#f3e5f5,stroke:#6a1b9a
```

**Valuation of high-value assets:** a *separate committee with Technical + Finance members* finalises the standardised valuation method.

---

## 4. Chart 4 — The MSTC e-auction: what happens to each lot

MSTC portal mechanics: catalogue prepared in 2–3 days, bidding runs **4 hours**, auto-extended by **8 minutes** whenever a bid lands in the last 8 minutes (**3 auto-extensions**). H-1 (highest bid) is always visible; bidder identity is not.

```mermaid
flowchart TD
    A0(["Lot approved by Competent Authority"]) --> A1["EE (Store) sends lot list, item specifications,<br/>HSN Nos. &amp; terms to MSTC → catalogue created"]
    A1 --> A2["E-bidding opens — 4 hours,<br/>auto-extension 8 min, max 3 extensions"]
    A2 --> A3["Auction closes — result visible online immediately"]
    A3 --> Q1{"Compare H-1 bid<br/>with Reserve Price (RP)<br/>and STA%"}

    Q1 -->|"H-1 ≥ RP"| SOLD["<b>CONFIRMED / SOLD</b><br/>MSTC auto-issues Sale Intimation Letter"]
    Q1 -->|"RP &gt; H-1 ≥ STA floor"| STA["<b>STA — Subject To Approval</b><br/>MSTC issues Provisional Sale Intimation Letter"]
    Q1 -->|"H-1 &lt; STA floor"| REJ["<b>REJECTED</b><br/>Lot cannot be sold at this price"]
    Q1 -->|"No bid at all"| NOBID["<b>NO BID</b><br/>ZSC / SDD Committee critically analyses why"]

    SOLD --> P1["H-1 pays 10% Security Deposit / EMD<br/>within 7 days"]
    STA --> P2["MSETCL reviews overall situation →<br/>Competent Authority approves/rejects<br/>within 7 working days"]
    P2 -->|Approved| P1
    P2 -->|Rejected| REJ

    P1 --> Q2{"Balance payment<br/>+ EMD received?"}
    Q2 -->|Yes| PAY["Payment by RTGS;<br/>CGM / AGM (F&amp;A) confirms receipt<br/>in writing within 2 days"]
    Q2 -->|"No — H-1 defaults"| DEF["ZSC may recommend re-auction<br/>(penal re-charges to MSTC)"]
    PAY --> DO["<b>Delivery Order issued</b> — EE (Store) facilitates<br/>security clearance, trucks, entry of personnel"]
    DO --> LIFT["Material lifted by buyer"]
    LIFT --> CLOSE(["Disposal complete"])

    REJ --> RE1["ZSC re-analysis: condition, location,<br/>loading/transport issues → increase STA%<br/>(0%–50% range) or re-fix MRP"]
    NOBID --> RE1
    DEF --> RE1
    RE1 --> Q3{"Sold on<br/>re-auction?"}
    Q3 -->|Yes| PAY
    Q3 -->|"No — still unsold"| SHIFT["ZSC may recommend SHIFTING THE LOT<br/>from Category A–D to <b>Category E</b><br/>(destroy / dispose as debris)<br/>— objective is to free the occupied space"]
    SHIFT --> CLOSE

    style SOLD fill:#e8f5e9,stroke:#2e7d32
    style STA fill:#fff8e1,stroke:#f9a825
    style REJ fill:#ffebee,stroke:#c62828
    style NOBID fill:#ffebee,stroke:#c62828
    style SHIFT fill:#eceff1,stroke:#455a64
```

**STA explained with the policy's own example**

| Entered by MSETCL | Example 1 | Example 2 |
|---|---|---|
| Reserve Price (RP) | ₹ 50,000 | ₹ 10,000 |
| % STA below RP | 10% (i.e. ₹ 5,000) | 40% (i.e. ₹ 4,000) |
| Lowest bid that stays alive | ₹ 45,000 | ₹ 6,000 |

- Reserve Price must be entered as a **minimum**.
- The **same Competent Authority** that approves the minimum RP is also empowered to approve the **% STA**.
- Any **variation in % STA** (lot remaining unsold) must be approved by **ZSC**.
- Hazardous waste: ZSC should keep a **high STA%** so the lot sells in the first attempt.

---

## 5. Chart 5 — IT equipment (PCs, laptops, printers, scanners)

```mermaid
flowchart TD
    I1(["IT asset completes 5 years<br/>from date of capitalisation<br/>(life as per MERC Regulations)"]) --> I2["IT Department initiates the disposal proposal"]
    I2 --> I3{"Still suitable for use?"}
    I3 -->|Yes| I4["Donate FREE OF COST to Government<br/>educational institutes / schools under CSR<br/>— institutes identified by CIRO<br/>— approval of Competent Authority"]
    I4 --> I9(["Asset leaves MSETCL — no auction"])
    I3 -->|"No / still surplus"| I5["Proposal placed before <b>SCIT</b><br/>Scrapping Committee for IT"]
    I5 --> I6["SCIT composition:<br/>CGM (IT) — Chairman<br/>EE (Admin), Zone office — Member<br/>AGM (HR), Zone office — Member<br/>IT Analyst — Conveyor"]
    I6 --> I7["SCIT scrutinises &amp; forwards to the<br/>Competent Authority as per GO 1 (F&amp;A)"]
    I7 -->|Approved| I8["EE (Store) disposes through MSTC<br/>e-auction — same as general lot"]
    I7 -->|Rejected| I5
    I8 --> I10(["Finance de-capitalises the item<br/>from the Asset Register"])

    style I4 fill:#e8f5e9,stroke:#2e7d32
    style I8 fill:#f3e5f5,stroke:#6a1b9a
```

---

## 6. Chart 6 — Used lead acid batteries (hazardous waste)

```mermaid
flowchart TD
    B1(["Used lead acid battery"]) --> B2["Make a SEPARATE lot under<br/>HAZARDOUS WASTE"]
    B2 --> B3["Route: dealer / manufacturer / importer /<br/>assembler / registered recycler / re-conditioner<br/>or designated collection centre"]
    B3 --> B4["E-auction through MSTC — ONLY recyclers<br/>registered with the Pollution Control Board may bid"]
    B4 --> B5["Field offices ensure safety &amp; environmental<br/>compliance during handling"]
    B5 --> B6["ZSC keeps a HIGH STA% so the lot sells<br/>in the first attempt itself"]
    B6 --> B7(["Disposal complete — rest of the procedure<br/>is the same as the general lot"])

    style B2 fill:#ffebee,stroke:#c62828
    style B4 fill:#f3e5f5,stroke:#6a1b9a
```

---

## 7. Who does what — at a glance

| Body | Full name | Composition | Main job |
|---|---|---|---|
| **Asset Owner** | Concerned division | — | Identify, categorise, prepare Proforma-A/B, arrange joint inspection, hand over asset |
| **CLARC** | Circle Level Asset Retirement Committee | SE (O&M) Circle – Chairman; EE (O&M) – Conveyor; EE (Testing) – Member; Manager (F&A) – Member | Concurrence for A(a); declare retirement for A(b), B, C, D; issue Retirement Report |
| **ZSC** | Zonal Scrapping Committee | CE, EHV PC O&M Zone – Chairman; SE (Testing) – Member; AGM (F&A) – Member; EE (Store) – Conveyor | Consolidate CLARC reports → CO R&D; in-principle approval; recommend MRP + STA%; re-analysis of unsold lots |
| **CO R&D** | Corporate Office Research & Development Committee | Director (Operations) – Chairman; CE (O&M) – Conveyor; CE (Design); CGM (Finance); SE (CPA) | Corrective action on retirement trends |
| **SCIT** | Scrapping Committee for IT | CGM (IT) – Chairman; EE (Admin); AGM (HR); IT Analyst – Conveyor | Scrutinise IT disposal proposals |
| **Competent Authority** | As per GO No. 1 (F&A), MSETCL | Delegated financial powers | Final approval of RP, % STA, lot details |
| **MSTC** | Metal Scrap Trade Corporation | E-auction platform | Catalogue, bidding, sale/delivery orders, payment collection |

---

## 8. The clock — every deadline in the policy

| When | What | Owner |
|---|---|---|
| **Half-yearly** | Proforma-A for Category A(a) | Asset Owner → CLARC |
| **Quarterly** | Proforma-B for Category A(b), B, C, D | Asset Owner → CLARC |
| **Quarterly** | ZSC consolidated report to CO R&D | ZSC |
| **Quarterly (4× a year)** | Auction of approved scrap by each Major Store | EE (Store) |
| **Immediately** | Replaced material (LE scheme / failure) credited to Major Store or location identified by EE (Store) — *except ICT / Power Transformer* | Work-executing agency / Asset Owner |
| **Within 7 days** | Fix Reserve Price from last auctioned rate / latest MSTC scrap rate | EE (Store) |
| **2–3 days** | MSTC prepares the auction catalogue | MSTC |
| **4 hours + 8 min × 3** | E-bidding duration and auto-extensions | MSTC |
| **Within 7 days** | H-1 bidder deposits 10% EMD / security deposit | Buyer |
| **≤ 7 working days** | MSETCL communicates acceptance/rejection of STA bids | Competent Authority → MSTC |
| **Within 2 days** | CGM/AGM (F&A) confirms receipt of RTGS payment in writing | Finance |

---

## 9. Housekeeping rules (General Guidelines)

1. **Small misc. scrap below ₹ 5,000** (newspapers, magazines, broken furniture, misc. items) is disposed of **regularly by the Office In-charge** — no MSTC auction. It must be done frequently to keep premises clean.
2. Every **work order** issued to a work-executing agency must state that removed material will be moved from site to the Major Store / space identified by EE (Store).
3. **Additional security guard / CCTV** at every Major Store or identified scrap space, if required.
4. If the Major Store has no space, EE (Store) identifies space at a **nearby substation**.
5. Once the material and retirement certificate reach **EE (Store)**, *all* further approvals up to disposal are handled by EE (Store) — the division is not chased again.
6. After the auction, EE (Store) intimates the auctioned amount to the division so the equipment can be **written off** in the asset book.
7. All bids are on **"as is where is basis"**, subject to prior inspection; **no photography** of lots by outsiders/bidders (security).
8. Amendments to the policy are carried out whenever required for smooth implementation.

## 10. Why the policy exists (stated advantages)

- Scrap accumulates **at one place** instead of being scattered across the zone → **theft risk drops**.
- **One single stock register** of scrap for the whole zone, kept by the Major Store.
- Scrapping becomes **smooth, fast and simple**; administrative approvals become **directional and fast**.
- **Timely revenue** to MSETCL and **no unnecessary inventory build-up**.
- Sub-station premises stay **aesthetic** — no scrap lying around.
