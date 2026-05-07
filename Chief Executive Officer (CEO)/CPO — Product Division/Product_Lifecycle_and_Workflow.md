# SECTION 3: Product Lifecycle & Workflow

## 3.1 Stage 1: Ideation & Validation

### Inputs to the Ideation Process

| Source | Method | Owner |
| :--- | :--- | :--- |
| **Market demand signals** | Keyword research (search volume, trends) | SEO Manager + Market Research Analyst |
| **Competitive gap analysis** | Competitor product teardowns, review mining (G2, Amazon, App Store) | Market Research Analyst + PMM |
| **Customer feedback** | Support tickets, NPS verbatims, CSM insights | CSM + Product Manager |
| **Internal expertise** | SME interviews, executive vision | Content Lead + CPO |
| **AI-assisted discovery** | Trend analysis via AI tools (Exploding Topics, Google Trends) | Market Research Analyst |
| **Revenue signals** | Products with adjacent high-demand but no supply | CRO + Product Manager |

### Validation Framework (The 5-Gate Test)
Before any product concept moves to development, it must pass all five gates:

| Gate | Criteria | Responsible |
| :--- | :--- | :--- |
| **Gate 1: Market Size** | TAM ≥ $500M; identifiable SAM ≥ $50M | Market Research Analyst |
| **Gate 2: Demand Signal** | ≥ 10,000 monthly searches for core keyword; or validated B2B demand (≥5 qualified prospect confirmations) | SEO Manager + Sales |
| **Gate 3: Competitive Feasibility** | We can achieve differentiated quality or positioning vs. existing products | PMM + PM |
| **Gate 4: Production Feasibility** | Can be produced within budget and timeline constraints using existing team + AI capabilities | Content Production Manager + Engineering Manager |
| **Gate 5: Revenue Model** | Clear pricing model with LTV:CAC ≥ 3:1 projection | CFO + PMM |

### Prioritization Framework
The Portfolio Council uses a weighted scoring model:

| Criterion | Weight |
| :--- | :--- |
| Revenue potential (12-month) | 30% |
| Strategic alignment | 20% |
| Production feasibility | 20% |
| Time to market | 15% |
| Differentiation potential | 15% |

*Products scoring ≥70/100 advance to the design phase. Products scoring 50–70 enter a "parking lot" for future quarters. Below 50 are rejected with documentation.*

---

## 3.2 Stage 2: Design & Prototyping

### Design Process (8-Week Standard for Software Products)

**Week 1–2: Discovery Sprint**
*   UX Designer conducts user interviews (minimum 8 sessions)
*   PM and UX Designer co-create user journey maps and problem statement
*   Content Designer defines voice and tone brief
*   **Output:** Design Brief document (approved by PM and Head of Design)

**Week 3–4: Information Architecture & Wireframing**
*   UX Designer produces low-fidelity wireframes for all core user flows
*   PM reviews wireframes against PRD acceptance criteria
*   Engineering Manager reviews for technical feasibility
*   **Output:** Approved wireframe package in Penpot

**Week 5–6: High-Fidelity Prototyping**
*   UI Designer applies visual design to wireframes using design system components
*   Content Designer writes all UI copy (no lorem ipsum in any prototype)
*   Interactive prototype built in Penpot for usability testing
*   **Output:** Clickable high-fidelity prototype

**Week 7: Usability Testing**
*   Minimum 5 moderated usability tests with target users (via UserTesting.com or direct recruitment)
*   Minimum 50-participant unmoderated test for quantitative validation
*   Accessibility review against WCAG 2.1 AA checklist
*   **Output:** Usability test report with prioritized findings

**Week 8: Design Finalization & Handoff**
*   Design revisions based on usability test findings
*   Full Penpot handoff package prepared (annotated specs, component documentation, assets exported)
*   Engineering walkthrough of design specs
*   QA review of design for testability
*   **Output:** Approved design package; green light for development

### Design Process for Content Products (E-Books, Courses, Podcasts)

**E-Books: 2-week design sprint**
*   Structure/outline approved by PM and Content Lead
*   Visual design template finalized (cover, chapter layouts, callout boxes, typography)
*   Brand compliance review
*   **Output:** E-book design template + approved structure

**Online Courses: 3-week design sprint**
*   Learning objectives defined using Bloom's Taxonomy
*   Course curriculum map and module structure approved
*   Video thumbnail and course artwork designed
*   LMS configuration template designed
*   **Output:** Course blueprint document

---

## 3.3 Stage 3: Development & Production

### Software Product Development (Agile / Sprint Model)

**Sprint Configuration**
*   **Sprint length:** 2 weeks
*   **Sprint ceremonies:** Planning (Monday), Daily standup (daily, 15 min), Mid-sprint check (Wednesday of Week 2), Review + Retro (Friday of Week 2)
*   **Team composition per sprint:** 1 Product Owner, 4–6 Engineers, 1 QA Engineer, 1 Designer (part-time)

**Development Standards**
*   All code reviewed by minimum 2 engineers before merge
*   No code merged without passing automated test suite
*   Feature flags used for all new features (enables gradual rollouts and instant rollback)
*   ADRs (Architecture Decision Records) written for all significant technical decisions
*   API documentation updated in real-time alongside code (Swagger/OpenAPI standard)

### Content Product Production (AI-Accelerated Workflow)

**E-Book Production Workflow**
```text
Step 1: Content Brief Creation (PM + Content Lead) — 2 days
  └── Defines: target audience, core premise, key learning outcomes, 
      competitive differentiation, SEO keyword targets, word count target

Step 2: AI-Assisted Outline Generation (AI Content Engineer) — 1 day
  └── Prompt-engineered outline generation → human editorial review → approved outline

Step 3: AI First Draft Generation (AI Content Engineer) — 2–3 days
  └── Chapter-by-chapter generation using approved prompts
  └── Parallel: SME review brief sent to domain expert

Step 4: Human Editorial Pass (Senior Content Writer) — 5–7 days
  └── Fact-checking against primary sources
  └── Voice and tone alignment
  └── Structural improvements
  └── Data freshness verification

Step 5: Content QA Review (Content Quality Analyst) — 2 days
  └── Factual accuracy audit
  └── Brand voice compliance
  └── Plagiarism check (Copyscape)
  └── Reading level assessment

Step 6: Design & Layout (UI Designer) — 3 days
  └── InDesign layout using approved e-book template
  └── Cover design
  └── Internal graphics, charts, callout boxes

Step 7: Final Approval (PM sign-off) — 1 day

Step 8: Asset Preparation (Production Manager) — 1 day
  └── PDF/EPUB export
  └── Amazon KDP formatting
  └── Metadata, ISBN, distribution platform configuration

Total timeline: 4–6 weeks (vs. 16–24 weeks without AI acceleration)
```

**Online Course Production Workflow**
```text
Step 1: Curriculum Design (Course Production Specialist + SME) — 1 week
Step 2: Script Writing (AI-assisted → human edited) — 2 weeks
Step 3: Recording (video or audio, with SME) — 1 week
Step 4: Video Editing + Post-Production — 1 week
Step 5: Supplementary Materials Production — 1 week
Step 6: LMS Upload + Configuration — 3 days
Step 7: QA Review (full course walkthrough) — 3 days
Step 8: Beta cohort (20 students) — 2 weeks
Step 9: Final revisions + launch — 1 week

Total timeline: 8–12 weeks
```

**AI Podcast Production Workflow**
```text
Step 1: Episode topic selection (editorial calendar) — 1 day
Step 2: Research brief (AI-assisted research) — 2 hours
Step 3: Script generation (AI + prompt engineer) — 2 hours
Step 4: Script editorial review (Content Writer) — 2 hours
Step 5: Voice synthesis (ElevenLabs or equivalent) — 1 hour
Step 6: Audio post-production (noise reduction, normalization, music, intro/outro) — 2 hours
Step 7: Show notes + chapter markers + artwork — 1 hour
Step 8: Distribution upload — 30 minutes

Total timeline: 1–2 days per episode
```

---

## 3.4 Stage 4: Quality Assurance

### Multi-Layer QA Framework

**Layer 1: Automated QA (Continuous)**
*   Automated test suites run on every code commit (unit tests, integration tests, E2E tests)
*   Performance monitoring via Datadog — alerts on latency, error rate, and throughput degradation
*   AI content quality scoring — automated rubric applied to all AI-generated drafts before human review

**Layer 2: Peer Review (Built into Workflow)**
*   Code: 2-engineer code review before merge
*   Content: Senior Writer peer review before QA submission
*   Design: UX + UI cross-review before handoff

**Layer 3: Structured QA Review (Dedicated QA Team)**
*   **For software products:**
    *   Functional testing (all acceptance criteria validated)
    *   Regression testing (all existing features confirmed unbroken)
    *   Cross-browser/cross-device testing
    *   Performance testing (load test at 10x expected concurrent users)
    *   Security scan (OWASP Top 10 checklist)
    *   Accessibility audit (axe DevTools automated + manual review)
*   **For content products:**
    *   Factual accuracy audit (source verification for all data points, statistics, named claims)
    *   Brand voice compliance review
    *   Plagiarism check
    *   Reading level analysis
    *   SEO optimization check (meta descriptions, headers, keyword density)
    *   Legal compliance review (copyright clearance, disclaimer requirements)

**Layer 4: Stakeholder Review Gate**
*   PM sign-off: Confirms product meets PRD acceptance criteria
*   Legal review: IP, compliance, disclaimers confirmed
*   PMM review: Confirms positioning alignment and launch readiness
*   Executive sponsor sign-off for major product launches (CPO or CTO)

**Layer 5: Beta Testing**
*   Software: Closed beta with 50–200 users; 2-week testing period
*   Content products: 20-person beta reader/learner cohort; structured feedback survey
*   Minimum beta NPS of 40 required to proceed to full launch

### QA Stage Gates

| Gate | Trigger | Pass Criteria | Decision Maker |
| :--- | :--- | :--- | :--- |
| **Alpha Gate** | Development complete | All P0/P1 bugs resolved; 80% test coverage | QA Lead |
| **Beta Gate** | Alpha passed; beta launched | Beta NPS ≥40; no new P0/P1 bugs in final 5 days | PM + QA Lead |
| **Launch Gate** | Beta complete | 100% P0 bugs resolved; Legal sign-off; Marketing assets ready | PM + CPO |
| **Content Release Gate** | Content QA complete | Factual accuracy ≥99%; brand compliance 100%; Legal cleared | Content QA Lead + PM |

---

## 3.5 Stage 5: Launch & Distribution

### Launch Playbook (Standard Product Launch)

**T-8 Weeks: Pre-Launch Setup**
*   Product page/landing page live (in "coming soon" mode)
*   Email waitlist capture activated
*   SEO metadata published (to begin indexing)
*   Affiliate program configured (if applicable)

**T-4 Weeks: Launch Campaign Build**
*   Email sequence written and loaded (10-email launch sequence minimum)
*   Paid media creatives produced and reviewed
*   Social media content calendar built (30 days post-launch)
*   Press release drafted and media list built
*   Influencer/partnership outreach initiated

**T-2 Weeks: Beta Momentum**
*   Beta cohort reviews solicited for social proof
*   Early-bird pricing activated
*   Webinar/live event scheduled (for SaaS and course products)

**T-1 Week: Final Checks**
*   Full launch readiness checklist completed (100-point checklist — see Section 5)
*   All team members briefed on launch plan
*   Support team briefed and FAQ document prepared
*   Rollback plan documented and communicated to engineering

**Launch Day**
*   Phased rollout (10% of traffic → 25% → 50% → 100% over 48 hours for software products)
*   All-hands monitoring rotation (engineering, QA, customer support)
*   Real-time metrics dashboard live and shared

### Distribution Channels by Product Type

| Product Type | Primary Channels | Secondary Channels |
| :--- | :--- | :--- |
| **E-Books** | Amazon KDP, Company website, Gumroad | Apple Books, Google Play Books, Kobo |
| **Online Courses** | Company LMS (owned), Udemy, Teachable marketplace | LinkedIn Learning (select courses) |
| **AI Podcasts** | Spotify, Apple Podcasts, Company website | Google Podcasts, Amazon Music, YouTube (audiogram) |
| **Google Sheets Tools** | Google Workspace Marketplace, Company website, Gumroad | AppSumo (lifetime deals), Product Hunt |
| **SaaS Platforms** | Company website (direct), App marketplaces (Salesforce, HubSpot AppConnect) | G2, Capterra (review-driven organic) |
| **Mobile Apps** | Apple App Store, Google Play Store | Company website (deep link) |
| **Web Applications** | Company website, SEO-driven direct | Product Hunt, Hacker News (on launch) |

---

## 3.6 Stage 6: Post-Launch & Iteration

### Feedback Collection Infrastructure

**Quantitative Signals**
*   Product analytics (Amplitude/Mixpanel): Daily active users, feature adoption, funnel drop-off, retention curves
*   Revenue analytics (Stripe/Recurly): MRR, churn rate, expansion revenue, refund rate
*   Support analytics (Zendesk/Intercom): Ticket volume, category breakdown, resolution time, sentiment

**Qualitative Signals**
*   In-app NPS surveys (Delighted or Pendo): Triggered at Day 7, Day 30, and Day 90
*   User interviews: 4 per month per product (CS team sources candidates)
*   Review monitoring: Amazon, App Store, Google Play, G2, Trustpilot (weekly monitoring via Brand24 or Mention)

### Iteration Cycle
*   **Monthly:** Minor updates (bug fixes, copy improvements, UX micro-improvements)
*   **Quarterly:** Minor feature releases (based on aggregated feedback and data)
*   **Semi-Annual:** Major version updates (significant feature additions or content refreshes)
*   **Annual:** Full content audit for content products (fact refresh, data updates, new chapters/modules)

### Product Health Dashboard (Weekly Review)

| Metric | Healthy | At Risk | Critical |
| :--- | :--- | :--- | :--- |
| **MoM Revenue Growth** | ≥5% | 0–5% | Negative |
| **NPS** | ≥50 | 30–50 | <30 |
| **Churn Rate (SaaS)** | <5% monthly | 5–10% | >10% |
| **Support Ticket Rate** | <2% of MAU | 2–5% | >5% |
| **Feature Adoption (core)** | ≥50% MAU | 30–50% | <30% |
| **Review Rating** | ≥4.3 stars | 3.5–4.3 | <3.5 |

---

## 3.7 Stage 7: Product Retirement

### Retirement Triggers
A product is flagged for retirement review when three or more of the following conditions are met for 3 consecutive months:

| Trigger | Threshold |
| :--- | :--- |
| **Revenue decline** | ≥30% YoY revenue decline |
| **NPS score** | <25 and declining |
| **Support ticket rate** | >10% of users contacting support monthly |
| **Update cost vs. revenue** | Cost to maintain exceeds 40% of revenue generated |
| **Market obsolescence** | Core use case replaced by market shift (e.g., AI made the tool obsolete) |
| **Compliance risk** | Cannot be updated to meet new regulatory requirements cost-effectively |

### Retirement Process

**Step 1: Retirement Review (Product Portfolio Council)**
*   Full product health analysis presented by PM
*   Alternatives evaluated: retirement vs. significant pivot vs. sale/licensing
*   Decision documented

**Step 2: Customer Communication (CSM + Marketing, minimum 90 days notice)**
*   Email announcement with migration path (if applicable)
*   FAQ published
*   Prorated refunds or migration credits issued

**Step 3: Revenue Maximization (6 months before sunset)**
*   Stop new customer acquisition
*   Maximize renewal revenue from existing base
*   Consider selling IP, codebase, or content to a strategic buyer

**Step 4: Technical Sunset**
*   Data export tools provided to customers
*   Infrastructure decommissioned in phases
*   Codebase archived (not deleted) for 5 years minimum
*   Post-mortem document written and shared with leadership
