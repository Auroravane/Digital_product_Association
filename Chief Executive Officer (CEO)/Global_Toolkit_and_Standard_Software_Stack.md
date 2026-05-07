# Global Toolkit & Standard Software Stack

This document defines the official, company-wide software and service standards. To maintain a "Sell Forever" architecture with zero recurring overhead, we prioritize **Open-Source**, **Self-Hosted**, and **Truly Free** tools over capped "freemium" services.

## 🛠️ Global Standards

| Category | Standard Tool | Note |
| :--- | :--- | :--- |
| **Project Management** | **Obsidian** (Local) | Use Git Plugin for unlimited sync/versioning. |
| **Documentation** | **AppFlowy** / **Anytype** | Unlimited blocks and private collaboration. |
| **Design (UI/UX)** | **Penpot** | Open-source alternative to Figma; unlimited files. |
| **Vector Graphics** | **Inkscape** | Professional vector editing. |
| **Version Control** | **GitHub** / **Gitea** | Use Gitea for internal, unlimited self-hosted repos. |
| **Deployment** | **Cloudflare Pages** | Unlimited bandwidth for static/frontend assets. |
| **Hosting** | **Fly.io** / **Oracle Cloud** | Use for scalable, non-sleeping production apps. |
| **Infrastructure (IaC)** | **Terraform** / **Pulumi** | Open-source CLI management. |
| **Containerization** | **Podman** / **Docker CLI** | Avoid Docker Desktop license fees at scale. |
| **AI Inference (Senior Agents)** | **NVIDIA NIM API** | Free-tier endpoint. Confirmed models: `moonshotai/kimi-k2.6`, `meta/llama-3.3-70b-instruct`, `qwen/qwen3-next-80b-a3b-instruct`, `deepseek-ai/deepseek-v4-flash`. |
| **AI Inference (Parsing/Mini)** | **Google Gemini API** | Free-tier endpoint. Confirmed model: `gemini-2.5-flash-lite` (500 RPD). |
| **AI/ML Orchestration** | **LangChain** / **Ollama** | Run LLMs locally to avoid API usage caps. |
| **Voice Synthesis** | **Coqui TTS** | Open-source, local high-quality voice synthesis. |
| **Audio Production** | **Audacity** | Standard audio editing. |
| **Video Production** | **DaVinci Resolve** | Professional-grade free version. |
| **Page Layout (E-Books)** | **Scribus** | Professional PDF production. |
| **Analytics (Privacy)** | **Umami** | Self-hosted, lightweight, no cookie banners. |
| **Analytics (Deep)** | **PostHog** (Self-hosted) | Unlimited events and session recording. |
| **CRM / ERP** | **ERPNext** | Full-suite open-source CRM and operations. |
| **Customer Support** | **Chatwoot** | Unlimited omni-channel support and live chat. |
| **Helpdesk** | **osTicket** | Robust, unlimited ticketing. |
| **Marketing Automation** | **Listmonk** | **Unlimited** email distribution and newsletter mgmt. |
| **Payments** | **Stripe** | Pay-as-you-go; no monthly platform fees. |
| **LMS (Education)** | **Moodle** | Open-source, unlimited course and student capacity. |
| **Podcast Dist.** | **Spotify for Podcasters** | Free global distribution. |
| **Password Mgmt.** | **Vaultwarden** | Self-hosted Bitwarden API; unlimited sharing. |
| **Security Scanning** | **Trivy** | Automated vulnerability detection. |
| **Monitoring** | **Uptime Kuma** | Self-hosted, 1-second interval monitoring. |
| **Error Tracking** | **GlitchTip** | Open-source Sentry alternative. |

---

## 🚫 Deprecated & Prohibited Tools
To avoid cost-creep and data-lock-in, the following tools are deprecated in favor of the Global Standards above:

*   **NVIDIA / NVIDIA (Paid APIs):** Replaced by **NVIDIA NIM Free Tier** (Llama 3.3 70B, Llama 3.3 70B) for all reasoning tasks.
*   **Mailchimp:** Replaced by **Listmonk** (Unlimited distribution).
*   **Figma (Pro):** Replaced by **Penpot** for team-wide unlimited design.
*   **Sentry (Cloud):** Replaced by **GlitchTip**.
*   **HubSpot (Paid tiers):** Replaced by **ERPNext**.
*   **UptimeRobot:** Replaced by **Uptime Kuma**.

## 🔄 Update Protocol
1.  **Selection:** Any tool not on the "Standard" list must pass a CFO/CTO review for "Sell Forever" compliance.
2.  **Migration:** Teams should migrate existing capped accounts to the global standards during the next quarterly audit.
