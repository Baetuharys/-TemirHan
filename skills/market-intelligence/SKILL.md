---
id: mai-skill-market-intelligence
title: Market Intelligence & Potential Customer Research
type: skill
status: active
version: 1.1.0
summary: Research companies, competitors, projects, publicly evidenced customer relationships, tenders and market signals in Türkiye and neighboring markets for mechanical/sheet-metal business development.
tags: [market-intelligence, market-research, business-development, competitors, customers, projects, tenders, mechanical]
depends_on: [mai-module-context-audit, mai-module-source-validation, mai-module-uncertainty-management, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: market-intelligence
description: Research companies, competitors, projects, publicly evidenced customer relationships, tenders and market signals in Türkiye and neighboring markets for mechanical/sheet-metal business development.
---

# Market Intelligence & Potential Customer Research

## Purpose
Turn public evidence into a structured market map for sheet-metal, enclosure, fabrication, laser cutting, bending, welding, assembly, CAD/engineering and related mechanical businesses.

## Core capabilities
- Map companies by country, city, sector, capability and company type.
- Identify competitors and comparable suppliers.
- Research publicly evidenced projects, contracts, tenders, investments and facility expansions.
- Identify publicly evidenced customers/partners/suppliers without guessing hidden relationships.
- Discover potential customer accounts from fit signals rather than unsupported claims.
- Build company dossiers and account lists that can be refreshed over time.
- Compare companies using factual attributes without assigning unsupported scores or rankings.

## Geographic scope
Default priority:
1. Türkiye
2. Türkiye's neighboring countries and nearby industrial markets when requested
3. Wider Europe/MENA only when the user expands the scope

"Neighboring" must be interpreted geographically and stated explicitly; do not silently broaden the country set.

## Evidence rules
Every material company/project/customer claim must carry:
- source URL/reference
- source date or publication date when available
- evidence type
- confidence/evidence grade
- claim wording that does not exceed the source

### Evidence grades
- A: primary source — company announcement, official tender/procurement record, stock-exchange filing, government/public authority record, official project page, signed contract announcement.
- B: reputable secondary source — established trade press, major news outlet, industry association, recognized database.
- C: directory/aggregator/user-generated source — useful for discovery, insufficient alone for important relationship or contract claims.
- D: inference — derived from multiple signals; must be labeled as inference and never presented as fact.

## Critical distinction
Do not convert any of these into facts without evidence:
- "works with X"
- "won the project"
- "supplies X"
- "is a customer of Y"
- "will buy from us"
- "has this production capacity"
- "is the biggest/best/leader"

Use wording such as "publicly identified as...", "source states...", "appears to be a potential fit based on..." and "relationship not independently confirmed" when appropriate.

## Research workflow
### 1. Define market question
Capture:
- geography
- sector/subsector
- company type
- capabilities of interest
- target company size, if any
- project/time window
- desired output

### 2. Build candidate universe
Search multiple source classes. Start broad, then narrow by capability, geography and project relevance.

### 3. Verify company identity
Resolve legal/company-name variants, subsidiaries, brands, locations and duplicate listings before combining evidence.

### 4. Build company dossier
For each material company capture:
- company name
- country/city
- sector
- capabilities
- facilities/locations when publicly documented
- certifications/standards when documented
- projects/contracts/investments with dates
- publicly evidenced customers/partners
- procurement/contact channels
- source list
- evidence gaps

### 5. Analyze market relationships
Separate:
- confirmed public relationship
- source-reported relationship
- probable/inferred relationship
- unknown

### 6. Identify potential customers
Use fit signals such as:
- recurring need for sheet-metal parts/enclosures
- production expansion
- new plant/equipment investment
- new product/program launch
- supplier qualification activity
- public tender/procurement activity
- outsourced fabrication/assembly requirement
- industry/technology fit

Do not infer purchasing intent merely from sector membership.

### 7. Produce actionable output
Possible outputs:
- market map
- competitor map
- target-account list
- company dossiers
- project pipeline
- customer/partner relationship map
- tender/project watchlist
- outreach preparation brief

## Output contract
For a company table, prefer:
| Company | Country/City | Sector | Relevant Capability | Public Project/Signal | Public Customer/Partner Evidence | Evidence Grade | Source Date | Source |

For each target account, add:
- why it may fit
- evidence supporting the fit
- what remains unknown
- suggested verification/research next step

## Failure modes
- Treating a directory listing as proof of a contract or customer relationship.
- Confusing a contractor, project owner, end customer and supplier.
- Combining subsidiaries or companies with similar names.
- Reporting old projects as current pipeline.
- Presenting an inference as a confirmed customer relationship.
- Ranking companies without a documented, user-approved factual criterion.
- Claiming a company "needs" a supplier without evidence.
- Using a single weak source for a commercially important claim.
- Ignoring publication date and project status.

## Refresh logic
Market information is time-sensitive. When the user asks for "current", "latest", "active", "recent" or a date-bounded market picture, research fresh sources and record the search date. Do not present an undated historical result as current.
