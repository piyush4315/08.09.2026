# MSETCL — Asset Retirement, Scrap Declaration & Disposal Policy
### The whole policy as diagrammatic flow charts

Source documents in this repo:
- `Policy.pdf` — the policy circular (signed by Director (Operations))
- `MSA wardha new scrapping policy.pdf` — the 19-slide presentation of the same policy
- `covering letter.pdf` — covering letter from the Chief Engineer (Trans O&M), dated 02.12.2024

The policy is **two halves that run back to back**:

> **Part 1 — ASSET RETIREMENT** (take the asset out of service and out of the books) →
> **Part 2 — SCRAP DECLARATION & DISPOSAL** (sell or destroy the material and recover money).

---

## 1. Flow-chart symbols used

```mermaid
flowchart LR
    L1(["TERMINATOR<br/>start / end"]) --> L2["PROCESS<br/>an action or step"]
    L2 --> L3{"DECISION<br/>yes / no question"}
    L3 --> L4[/"DOCUMENT<br/>form, certificate, report"/]
    L4 --> L5[("DATABASE<br/>register / record")]
    L5 --> L6[["SUB-PROCESS<br/>detailed in another chart"]]
    L6 --> L7((("CONNECTOR<br/>goes to next chart")))

    style L1 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style L2 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style L3 fill:#fff8e1,stroke:#f9a825,stroke-width:2px
    style L4 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style L5 fill:#eceff1,stroke:#546e7a,stroke-width:2px
    style L6 fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style L7 fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
```

**Colour = who owns the step**

| Colour | Actor |
|---|---|
| 🔵 Blue | Asset Owner / Division |
| 🟢 Green | **CLARC** — Circle Level Asset Retirement Committee |
| 🟠 Amber | **ZSC** — Zonal Scrapping Committee |
| 🔴 Red | **Competent Authority** (GO 1 F&A) / Finance |
| 🟣 Purple | **MSTC** — e-auction platform |
| ⚪ Grey | IT / stores / housekeeping |

---

## 2. Chart 0 — Master flow: the whole policy on one line

```mermaid
flowchart LR
    START(["ASSET IN<br/>SERVICE"]) --> S1["<b>1 · IDENTIFY</b><br/>Asset Owner<br/>Category A–E"]
    S1 --> S2["<b>2 · RETIRE</b><br/>CLARC<br/>Proforma-A / -B"]
    S2 --> S3["<b>3 · HAND OVER</b><br/>to EE (Store)<br/>+ certificate"]
    S3 --> S4["<b>4 · VALUE</b><br/>EE (Store)<br/>RP + STA%"]
    S4 --> S5["<b>5 · APPROVE</b><br/>ZSC → Competent<br/>Authority"]
    S5 --> S6["<b>6 · AUCTION</b><br/>MSTC e-auction"]
    S6 --> S7["<b>7 · REALISE</b><br/>EMD → RTGS<br/>→ Delivery Order"]
    S7 --> S8["<b>8 · DE-CAP</b><br/>Finance writes off"]
    S8 --> FINISH(["REVENUE IN<br/>ASSET OFF BOOKS"])

    S2 -.->|"A(a): concurrence<br/>to keep running"| START
    S1 -.->|"Category E"| KILL(["Destroy /<br/>dispose as debris"])
    S1 -.->|"IT equipment"| IT[["Chart 5<br/>SCIT route"]]
    S3 -.->|"Lead acid<br/>batteries"| HAZ[["Chart 6<br/>hazardous lot"]]
    S6 -.->|"no bid / below STA /<br/>H-1 defaults"| RE["Re-lot · re-fix MRP<br/>· raise STA%"]
    RE -.->|"re-auction"| S6
    RE -.->|"still unsold"| KILL

    START2(("Chart 1")) --> S1
    S2 --> C2(("Chart 2"))
    S4 --> C3(("Chart 3"))
    S6 --> C4(("Chart 4"))

    style S1 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style S2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style S3 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style S4 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style S5 fill:#fff8e1,stroke:#f9a825,stroke-width:2px
    style S6 fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style S7 fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style S8 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style START fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style FINISH fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px
    style KILL fill:#eceff1,stroke:#546e7a,stroke-width:2px
    style RE fill:#fff8e1,stroke:#f9a825,stroke-width:2px
    style START2 fill:#e1f5fe,stroke:#0277bd
    style C2 fill:#e1f5fe,stroke:#0277bd
    style C3 fill:#e1f5fe,stroke:#0277bd
    style C4 fill:#e1f5fe,stroke:#0277bd
```

| # | Step | Owner | Input → Output | Frequency / clock |
|---|---|---|---|---|
| 1 | Identify & categorise | Asset Owner | Asset → Category A(a), A(b), B, C, D or E | Continuous |
| 2 | Declare retirement | CLARC | Proforma-A / -B → **Retirement Certificate** | A(a) half-yearly · others quarterly |
| 3 | Hand over | Asset Owner → EE (Store) | Asset + certificate → **Store stock register** | Immediately on retirement |
| 4 | Value & lot | EE (Store) | Stock → **Reserve Price + STA% + lots** | RP fixed within **7 days** |
| 5 | Approve | ZSC → Competent Authority | Lot proposal → **approval per GO 1 (F&A)** | ZSC meets quarterly cycle |
| 6 | Auction | MSTC | Approved lot → **H-1 bid** | Bidding **4 h + 8 min × 3** |
| 7 | Realise | Buyer / EE (Store) | 10% EMD + balance by RTGS → **Delivery Order** | EMD **7 days** · lift after DO |
| 8 | De-capitalise | Finance | Sale proceeds → **item removed from Asset Register** | After lifting |

---

## 3. Chart 1 — Which category? (the entry gate)

```mermaid
flowchart TD
    START(["Asset under review"]) --> Q1{"Served its<br/>useful life?"}

    Q1 -->|"Yes"| Q1B{"Still in<br/>active use?"}
    Q1B -->|"Yes"| AA["<b>CATEGORY A(a)</b><br/>life over,<br/>still running"]
    Q1B -->|"No"| AB["<b>CATEGORY A(b)</b><br/>life over,<br/>out of service"]

    Q1 -->|"No"| Q2{"Damaged / unserviceable /<br/>beyond economic repair<br/>WITHIN its life?"}
    Q2 -->|"Yes"| CC["<b>CATEGORY C</b><br/>failed, burnt,<br/>burst, degraded"]

    Q2 -->|"No"| Q3{"Obsolete — retention<br/>uneconomical?"}
    Q3 -->|"Yes"| BB["<b>CATEGORY B</b><br/>obsolete"]

    Q3 -->|"No"| Q4{"Salvage value?"}
    Q4 -->|"Meagre"| DD["<b>CATEGORY D</b><br/>e-waste, packing,<br/>furniture, dead spares"]
    Q4 -->|"Nil"| EE["<b>CATEGORY E</b><br/>deteriorated wood,<br/>debris"]

    AA --> PA[/"Proforma-A<br/><b>half-yearly</b>"/]
    AB --> PB[/"Proforma-B<br/><b>quarterly</b>"/]
    BB --> PB
    CC --> PB
    DD --> PB
    EE --> BIN(["Destroy / dispose<br/>as garbage-debris"])

    PA --> OUT(("Chart 2"))
    PB --> OUT

    style AA fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style AB fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style BB fill:#fff8e1,stroke:#f9a825,stroke-width:2px
    style CC fill:#ffebee,stroke:#c62828,stroke-width:2px
    style DD fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style EE fill:#eceff1,stroke:#546e7a,stroke-width:2px
    style START fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style BIN fill:#eceff1,stroke:#546e7a,stroke-width:2px
    style OUT fill:#e1f5fe,stroke:#0277bd
```

| Category | Meaning | Form | Reporting | Ends in |
|---|---|---|---|---|
| **A(a)** | Useful life over, **still in active use** | Proforma-A | Half-yearly | Concurrence to continue **or** retirement |
| **A(b)** | Useful life over, **removed from active use** / to be replaced by advanced equipment | Proforma-B | Quarterly | Retirement → scrap |
| **B** | Obsolete, retention uneconomical | Proforma-B | Quarterly | Retirement → scrap |
| **C** | Damaged / unserviceable / beyond economic repair **within** defined life | Proforma-B | Quarterly | Retirement → scrap |
| **D** | Misc. scrap with meagre salvage value — e-waste, packing boxes, containers, furniture, discarded stationery, dead spares | Proforma-B | Quarterly | Retirement → scrap |
| **E** | Nil worth — deteriorated wood, packing, debris | — | — | Destroy / garbage, **no auction** |

> **Gate before retiring (Policy 1.3):** the asset owner must first satisfy that **no alternate economic use exists anywhere in MSETCL**. Only then can retirement start.

---

## 4. Chart 2 — Part 1: Asset Retirement approval chain

```mermaid
flowchart TD
    START(["Asset identified<br/>+ categorised"]) --> O1

    subgraph LANE1["🔵 ASSET OWNER — concerned division"]
        O1["Inspect the asset<br/>with EE (Testing)"]
        O2[/"Prepare certificate:<br/><b>Proforma-A</b> for A(a)<br/><b>Proforma-B</b> for A(b), B, C, D"/]
        O3["Arrange JOINT INSPECTION<br/>through CLARC"]
        O1 --> O2 --> O3
    end

    subgraph LANE2["🟢 CLARC — Circle Level Asset Retirement Committee"]
        C1{"Which<br/>category?"}
        C2["Ascertain need to<br/>CONTINUE IN SERVICE"]
        C3["Certify identification →<br/>declaration → RETIREMENT"]
        C4[/"<b>Asset Retirement Report</b><br/>description · book value · reasons"/]
        C1 -->|"A(a)"| C2
        C1 -->|"A(b), B, C, D"| C3 --> C4
    end

    subgraph LANE3["🟠 ZSC — Zonal Scrapping Committee"]
        Z1["Consolidate all CLARC<br/>reports of the zone"]
        Z2[/"ZSC report + views<br/>&amp; observations"/]
        Z1 --> Z2
    end

    subgraph LANE4["🔵 CO R&amp;D Committee — Corporate Office"]
        R1["Review trends &amp; failures"]
        R2["Issue CORRECTIVE ACTION<br/>to design / O&amp;M / finance"]
        R1 --> R2
    end

    O3 --> C1
    C2 -->|"Concurrence given"| KEEP(["Asset continues<br/>in service"])
    KEEP -.->|"reviewed again<br/>next half-year"| O1
    C4 -->|"Cat. A, B, C — and anything<br/>burnt, burst or degraded<br/>within its life"| Z1
    Z2 -->|"EVERY QUARTER"| R1
    C4 -->|"Cat. D"| NEXT(("Chart 3"))
    C3 -->|"Cat. D"| NEXT
    R2 -.->|"design / spec feedback"| O1

    style C1 fill:#fff8e1,stroke:#f9a825,stroke-width:2px
    style C2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style C3 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Z2 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style C4 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style O2 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style START fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style KEEP fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style NEXT fill:#e1f5fe,stroke:#0277bd
```

| Committee | Composition | Job in this chart |
|---|---|---|
| **CLARC** | SE (O&M) Circle — **Chairman** · EE (O&M) division — **Conveyor** · EE (Testing) — Member · Manager (F&A) — Member | Concurrence for A(a); declare retirement for A(b), B, C, D; issue the Asset Retirement Report |
| **ZSC** | CE, EHV PC O&M Zone — **Chairman** · SE (Testing) — Member · AGM (F&A) — Member · EE (Store) — **Conveyor** | Consolidate every CLARC report → CO R&D each quarter |
| **CO R&D** | Director (Operations) — **Chairman** · CE (O&M) — **Conveyor** · CE (Design) · CGM (Finance) · SE (CPA) | Corrective action on retirement/failure trends |

---

## 5. Chart 3 — Part 2: Scrapping & disposal procedure

```mermaid
flowchart TD
    START(["CLARC declares<br/>asset RETIRED"]) --> D1[/"<b>Retirement Certificate</b><br/>+ physical asset"/]
    D1 --> P1["EE (Store) takes over the file"]
    P1 --> P2["Scrutinise the proposal<br/>+ reason for scrap"]
    P2 --> P3["Verify BOOK VALUE<br/>item by item"]
    REG[("Asset<br/>Register")] -.-> P3
    P3 --> DEC{"Value available<br/>in the Asset<br/>Register?"}
    DEC -->|"No"| ALT["Estimate rough value:<br/>purchase price − depreciation<br/>(Finance fixes value at PPE<br/>verification · O&amp;M fixes weight)"]
    DEC -->|"Yes"| P4
    ALT --> P4[/"<b>Consolidated Scrapping List</b><br/>book / depreciated value"/]

    P4 --> Z1{"ZSC grants<br/>IN-PRINCIPLE<br/>approval?"}
    Z1 -->|"No — back for<br/>correction"| P2
    Z1 -->|"Yes"| P5["EE (Store) conducts<br/>PHYSICAL SURVEY"]
    P5 --> P6["Fix RESERVE PRICE within<br/><b>7 days</b> — last auctioned rate<br/>or latest MSTC metal rate"]
    P6 --> P7["MAKE LOTS — realistic lotting<br/>is the key to a sale"]
    P7 --> Z2[/"<b>ZSC recommendation</b><br/>MRP + STA% + lot details"/]
    Z2 --> CA{"COMPETENT AUTHORITY<br/>approval as per<br/><b>GO 1 (F&amp;A)</b>?"}
    CA -->|"Query / revise"| P7
    CA -->|"Approved"| AUC[["Chart 4 ·<br/>MSTC e-auction"]]
    CA -->|"Rejected"| P2

    style START fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style D1 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style P4 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style Z2 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style REG fill:#eceff1,stroke:#546e7a,stroke-width:2px
    style Z1 fill:#fff8e1,stroke:#f9a825,stroke-width:2px
    style CA fill:#ffebee,stroke:#c62828,stroke-width:3px
    style AUC fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
```

| Block | What actually happens |
|---|---|
| Book-value check | Manager (F&A) is the key player. If an item is **not in the Asset Register**, ZSC estimates a rough value from likely purchase price less depreciation; Finance fixes the value during **PPE physical verification**; O&M issues the **weight** guidelines |
| High-value assets | A **separate committee with Technical + Finance members** finalises the standardised valuation method |
| Reserve Price | Minimum RP, fixed within 7 days from the last auctioned rate or the latest scrap rates on the MSTC site |
| After hand-over | General Guideline 6: once the material + certificate reach EE (Store), **all** further approvals till disposal are done by EE (Store) |

---

## 6. Chart 4 — The MSTC e-auction: fate of each lot

```mermaid
flowchart TD
    START(["Lot approved by<br/>Competent Authority"]) --> A1[/"<b>Lot list + HSN + terms</b><br/>sent to MSTC"/]
    A1 --> A2[["MSTC builds the<br/><b>Auction Catalogue</b><br/>(2–3 days)"]]
    A2 --> A3["E-bidding opens<br/><b>4 hours</b> · auto-extension<br/><b>8 min × 3</b>"]
    A3 --> A4(["Auction closes —<br/>result online at once"])
    A4 --> Q1{"Where did the<br/><b>H-1 bid</b> land?"}

    Q1 -->|"H-1 ≥ Reserve Price"| SOLD["<b>CONFIRMED</b><br/>Sale Intimation Letter<br/>auto-issued"]
    Q1 -->|"Between STA floor<br/>and RP"| STA["<b>STA</b> — Subject To Approval<br/>Provisional Sale Intimation Letter"]
    Q1 -->|"Below STA floor"| REJ["<b>REJECTED</b>"]
    Q1 -->|"No bid received"| NOBID["<b>NO BID</b>"]

    STA --> Q2{"Competent Authority<br/>accepts the STA bid?<br/><b>≤ 7 working days</b>"}
    Q2 -->|"Yes"| SOLD
    Q2 -->|"No"| REJ

    SOLD --> EMD["H-1 deposits<br/><b>10% EMD</b> within 7 days"]
    EMD --> Q3{"EMD received?"}
    Q3 -->|"Yes"| PAY["Balance by RTGS ·<br/>CGM/AGM (F&amp;A) confirms<br/>receipt in writing in <b>2 days</b>"]
    Q3 -->|"No — default"| REJ

    PAY --> DO[/"<b>Delivery Order</b>"/]
    DO --> LIFT["EE (Store) facilitates security<br/>clearance, trucks, entry passes"]
    LIFT --> DONE(["<b>DISPOSED</b><br/>→ Chart 3 de-capitalisation"])

    REJ --> RE1["ZSC re-analysis: condition, location,<br/>loading &amp; transport issues"]
    NOBID --> RE1
    RE1 --> RE2["Raise STA% (0–50% band)<br/>and/or re-fix MRP"]
    RE2 --> Q4{"Sold on<br/>re-auction?"}
    Q4 -->|"Yes"| PAY
    Q4 -->|"No"| SHIFT["Shift the lot from<br/>Category A–D → <b>Category E</b><br/>destroy / dispose as debris"]
    SHIFT --> DONE

    style START fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style A4 fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style DONE fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px
    style SOLD fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style STA fill:#fff8e1,stroke:#f9a825,stroke-width:2px
    style REJ fill:#ffebee,stroke:#c62828,stroke-width:2px
    style NOBID fill:#ffebee,stroke:#c62828,stroke-width:2px
    style SHIFT fill:#eceff1,stroke:#546e7a,stroke-width:2px
    style DO fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
```

**STA in one picture**

```
        Reserve Price (RP)  ───────────────────────────────  H-1 ≥ RP  →  CONFIRMED
                            │                              │
        STA floor           │  RP − (STA% × RP)            │  bid in this band  →  STA (needs approval)
                            │                              │
                            ▼                              ▼
                    below STA floor  →  REJECTED  →  ZSC raises STA% / re-fixes MRP  →  re-auction
```

| Entered by MSETCL | Example 1 | Example 2 |
|---|---|---|
| Reserve Price | ₹ 50,000 | ₹ 10,000 |
| % STA below RP | 10% → ₹ 5,000 | 40% → ₹ 4,000 |
| Lowest bid that survives | ₹ 45,000 | ₹ 6,000 |

- The **same Competent Authority** that approves the minimum RP also approves the **% STA**.
- Any **change in % STA** because a lot stayed unsold must be approved by **ZSC**.
- **Hazardous waste:** keep a high STA% so it sells first time.

---

## 7. Chart 5 — IT equipment (PC, laptop, printer, scanner)

```mermaid
flowchart TD
    START(["IT asset completes<br/><b>5 years</b> from capitalisation<br/>(MERC life)"]) --> I1["IT Department raises<br/>the disposal proposal"]
    I1 --> Q1{"Still fit<br/>for use?"}
    Q1 -->|"Yes"| GIFT["Donate FREE OF COST to Government<br/>schools / institutes under CSR<br/>— identified by CIRO"]
    GIFT --> Q2{"Competent Authority<br/>approves?"}
    Q2 -->|"No"| I2
    Q2 -->|"Yes"| GIFTED(["Asset leaves MSETCL<br/>— no auction"])
    Q1 -->|"No / surplus"| I2[/"Proposal to <b>SCIT</b><br/>Scrapping Committee – IT"/]

    subgraph SCIT["⚪ SCIT composition"]
        S1["CGM (IT) — Chairman<br/>EE (Admin), Zone — Member<br/>AGM (HR), Zone — Member<br/>IT Analyst — Conveyor"]
    end

    I2 --> S1
    S1 --> I3["SCIT scrutinises &amp; forwards<br/>for approval"]
    I3 --> Q3{"Competent Authority<br/>as per <b>GO 1 (F&amp;A)</b>?"}
    Q3 -->|"No"| I2
    Q3 -->|"Yes"| I4[["EE (Store) disposes<br/>through MSTC<br/>— same as a general lot"]]
    I4 --> I5(["Finance de-capitalises<br/>the item"])

    style START fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style GIFTED fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style I5 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style I2 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style I4 fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style GIFT fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
```

---

## 8. Chart 6 — Used lead acid batteries (hazardous waste)

```mermaid
flowchart TD
    START(["Used lead acid<br/>battery"]) --> B1["Make a SEPARATE lot<br/>tagged <b>HAZARDOUS WASTE</b>"]
    B1 --> B2{"Route"}
    B2 -->|"Channel 1"| B3["Deposit with dealer / manufacturer /<br/>importer / assembler / registered<br/>recycler / re-conditioner"]
    B2 -->|"Channel 2"| B4["Deposit at a designated<br/>collection centre"]
    B2 -->|"Channel 3"| B5[["MSTC e-auction — ONLY recyclers<br/>registered with the Pollution<br/>Control Board may bid"]]
    B3 --> B6["Field offices ensure safety &amp;<br/>environmental compliance"]
    B4 --> B6
    B5 --> B6
    B6 --> B7["ZSC keeps a <b>HIGH STA%</b><br/>so it sells first time"]
    B7 --> DONE(["DISPOSED — rest of the<br/>procedure same as a general lot"])

    style START fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style DONE fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style B1 fill:#ffebee,stroke:#c62828,stroke-width:2px
    style B5 fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    style B7 fill:#fff8e1,stroke:#f9a825,stroke-width:2px
```

---

## 9. Chart 7 — The paper trail (every document the policy creates)

```mermaid
flowchart LR
    D1[/"<b>Proforma-A</b><br/>half-yearly<br/><i>Asset Owner</i>"/] --> D2[/"<b>Proforma-B</b><br/>quarterly<br/><i>Asset Owner</i>"/]
    D2 --> D3[/"<b>Asset Retirement Report</b><br/><i>CLARC</i>"/]
    D3 --> D4[/"<b>ZSC consolidated report</b><br/>quarterly<br/><i>ZSC</i>"/]
    D4 --> D5[/"<b>Retirement Certificate</b><br/><i>CLARC</i>"/]
    D5 --> D6[/"<b>Consolidated Scrapping List</b><br/><i>EE (Store)</i>"/]
    D6 --> D7[/"<b>Lot proposal: MRP + STA%</b><br/><i>ZSC → Competent Authority</i>"/]
    D7 --> D8[/"<b>Auction Catalogue</b><br/><i>MSTC</i>"/]
    D8 --> D9[/"<b>Sale / Provisional Sale<br/>Intimation Letter</b><br/><i>MSTC</i>"/]
    D9 --> D10[/"<b>Delivery Order</b><br/><i>MSTC</i>"/]
    D10 --> D11[/"<b>De-capitalisation advice</b><br/><i>EE (Store) → Finance</i>"/]
    D11 --> D12[("Asset<br/>Register<br/>updated")]

    style D1 fill:#fff3e0,stroke:#ef6c00
    style D2 fill:#fff3e0,stroke:#ef6c00
    style D3 fill:#fff3e0,stroke:#ef6c00
    style D4 fill:#fff3e0,stroke:#ef6c00
    style D5 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style D6 fill:#fff3e0,stroke:#ef6c00
    style D7 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style D8 fill:#f3e5f5,stroke:#6a1b9a
    style D9 fill:#f3e5f5,stroke:#6a1b9a
    style D10 fill:#f3e5f5,stroke:#6a1b9a
    style D11 fill:#ffebee,stroke:#c62828
    style D12 fill:#eceff1,stroke:#546e7a,stroke-width:2px
```

---

## 10. Chart 8 — The clock: every deadline in the policy

```mermaid
flowchart LR
    T1(["Half-yearly<br/>Proforma-A"]) --> T2(["Quarterly<br/>Proforma-B"])
    T2 --> T3(["Quarterly<br/>ZSC → CO R&amp;D"])
    T3 --> T4(["Quarterly<br/>4 auctions a year"])
    T4 --> T5(["7 days<br/>fix Reserve Price"])
    T5 --> T6(["2–3 days<br/>MSTC catalogue"])
    T6 --> T7(["4 h + 8 min × 3<br/>e-bidding"])
    T7 --> T8(["7 days<br/>buyer deposits EMD"])
    T8 --> T9(["≤ 7 working days<br/>STA decision"])
    T9 --> T10(["2 days<br/>payment confirmation"])

    style T1 fill:#e3f2fd,stroke:#1565c0
    style T2 fill:#e3f2fd,stroke:#1565c0
    style T3 fill:#fff8e1,stroke:#f9a825
    style T4 fill:#f3e5f5,stroke:#6a1b9a
    style T5 fill:#fff3e0,stroke:#ef6c00
    style T6 fill:#f3e5f5,stroke:#6a1b9a
    style T7 fill:#f3e5f5,stroke:#6a1b9a
    style T8 fill:#ffebee,stroke:#c62828
    style T9 fill:#ffebee,stroke:#c62828
    style T10 fill:#ffebee,stroke:#c62828
```

| When | What | Owner |
|---|---|---|
| **Half-yearly** | Proforma-A for Category A(a) | Asset Owner → CLARC |
| **Quarterly** | Proforma-B for Category A(b), B, C, D | Asset Owner → CLARC |
| **Quarterly** | Consolidated report to CO R&D | ZSC |
| **4× a year** | Auction of approved scrap by each Major Store | EE (Store) |
| **Immediately** | Material replaced under LE scheme / on failure credited to the Major Store or a location identified by EE (Store) — *except ICT / Power Transformer* | Work-executing agency |
| **7 days** | Fix Reserve Price from last auctioned rate / latest MSTC rate | EE (Store) |
| **2–3 days** | MSTC prepares the auction catalogue | MSTC |
| **4 h + 8 min × 3** | E-bidding duration and auto-extensions | MSTC |
| **7 days** | H-1 deposits 10% EMD / security deposit | Buyer |
| **≤ 7 working days** | MSETCL posts acceptance / rejection of STA bids online | Competent Authority → MSTC |
| **2 days** | CGM/AGM (F&A) confirms RTGS receipt in writing | Finance |

---

## 11. Housekeeping rules (General Guidelines)

1. **Misc. scrap below ₹ 5,000** (newspapers, magazines, broken furniture, odd items) is disposed of **regularly by the Office In-charge** — no MSTC auction; do it often to keep premises clean.
2. Every **work order** to a work-executing agency must state that removed material goes to the Major Store or the space identified by EE (Store).
3. **Extra security guard / CCTV** at every Major Store or identified scrap space, if required.
4. If the Major Store is full, EE (Store) identifies space at a **nearby substation**.
5. Once material + retirement certificate reach **EE (Store)**, all further approvals till disposal are handled by EE (Store).
6. After auction, EE (Store) intimates the amount to the division so the equipment can be **written off** in the asset book.
7. All bids are **"as is where is"**, subject to prior inspection; **no photography** of lots by outsiders (security).
8. Amendments are issued whenever needed for smooth implementation.

## 12. Why the policy exists (stated advantages)

- Scrap collects **at one place** instead of being scattered across the zone → **theft risk falls**.
- **One stock register** for all scrap in the zone, kept by the Major Store.
- Scrapping becomes **smooth, fast and simple**; administrative approvals become **directional and fast**.
- **Timely revenue** and **no unnecessary inventory build-up**.
- Sub-station premises stay **aesthetic** — no scrap lying around.
