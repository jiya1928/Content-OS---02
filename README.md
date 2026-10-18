# ◐ Content OS — AI-Powered Content Creation & Automation

**Content OS** is an AI-powered content creation platform designed to streamline the process of researching topics, generating social media posts, refining content, and preparing posts for LinkedIn publishing.

The application uses a multi-agent workflow to help creators produce engaging, structured, and brand-aligned content from a single topic.

## ✨ Features

- **AI Content Generation** — Generate social media post variations from a topic or idea.
- **Multi-Agent Workflow** — Coordinate specialized agents for research, writing, critique, design, and content optimization.
- **Multiple Writing Styles** — Create content in Contrarian, Story, Value Bomb, and Vulnerable styles.
- **Customizable Content Length** — Generate short, medium, or long-form posts.
- **Content Critique** — Review generated variations and select a preferred draft.
- **Trend Research** — Gather topic-related insights to inform content creation.
- **Brand Personalization** — Customize content using your profile and brand information.
- **Hashtag Suggestions** — Generate relevant hashtags for social media posts.
- **Visual Content Prompts** — Prepare prompts for content-related visual assets.
- **LinkedIn Integration** — Preview and publish posts through the LinkedIn API.
- **Interactive Dashboard** — Manage content generation and review drafts through a Streamlit interface.

## 🛠️ Tech Stack

- **Python** — Core application and automation logic
- **Streamlit** — Interactive web interface
- **Groq API** — AI-powered content generation
- **LinkedIn API** — Social media publishing
- **Requests** — HTTP requests and API communication
- **Pillow** — Image processing
- **python-dotenv** — Environment variable management

## 📁 Project Structure

```text
Content-OS---02/
├── app.py                # Main Streamlit application
├── app_backup.py         # Backup application
├── automation.py         # Coordinates the agent workflow
├── bot.py                # Bot-related functionality
├── brain.py              # Core content intelligence
├── brand_setup.py        # Brand and profile setup utilities
├── critic.py             # Content critique and evaluation
├── design_agent.py       # Visual content assistance
├── hunter.py             # Research and discovery functionality
├── publisher.py          # Publishing-related functionality
├── reply_agent.py        # Reply generation
├── tag_agent.py          # Hashtag and tagging assistance
├── post.js               # JavaScript posting utility
├── requirements.txt      # Python dependencies
├── linkedin_drafts.txt   # LinkedIn draft storage
└── twitter_drafts.txt    # Twitter draft storage
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- A Groq API key
- LinkedIn API credentials if you want to publish posts directly

### 1. Clone the repository

```bash
git clone https://github.com/jiya1928/Content-OS---02.git
cd Content-OS---02
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
LINKEDIN_TOKEN=your_linkedin_access_token
LINKEDIN_URN=auto
LINKEDIN_NAME=Your Name
LINKEDIN_HEADLINE=Your Professional Headline
```

Replace the placeholder values with your own credentials and profile information.

- `GROQ_API_KEY` is used for AI-powered content generation.
- `LINKEDIN_TOKEN` is used for LinkedIn API requests.
- `LINKEDIN_URN` identifies the LinkedIn profile used for publishing. The application attempts to resolve the profile identifier when configured as `auto`.
- `LINKEDIN_NAME` and `LINKEDIN_HEADLINE` customize the profile preview.

**Security:** Never commit your `.env` file, API keys, or access tokens to GitHub. Store credentials securely and use the required API permissions.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, typically `http://localhost:8501`.

## 📖 How to Use

1. Launch the Streamlit application.
2. Enter a topic or idea for your next social media post.
3. Select a writing style and preferred content length.
4. Optionally provide a hook or angle to guide content generation.
5. Generate content using the multi-agent workflow.
6. Review the suggested post variations and their critiques.
7. Select a variation and edit the draft in the composer.
8. Check the live preview and supporting insights, including trends, strategy, hashtags, and visual prompts.
9. Publish to LinkedIn when your credentials, permissions, and profile configuration are correct.

Review the final content before publishing.

## 🔐 API Configuration

Content generation and publishing depend on external services.

- **Groq:** Requires a valid API key and access to a supported model.
- **LinkedIn:** Requires an appropriate access token, valid profile identifier, and the API permissions needed for publishing.
- **Environment variables:** Keep credentials private and configure them locally or through your deployment platform's secret-management system.

API availability and permissions may change. Consult the relevant provider documentation if requests fail.

## 🎯 Use Cases

- Personal branding and professional networking
- LinkedIn content creation
- AI-assisted research and ideation
- Social media content planning
- Brand-aligned writing
- Content refinement and hashtag generation
- Streamlining repetitive content workflows

## 🗺️ Future Improvements

Potential enhancements include:

- Scheduled publishing and content calendars
- Analytics and engagement tracking
- Additional social media integrations
- Persistent content history
- Improved error handling and API diagnostics
- Automated testing and workflow monitoring

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork this repository.
2. Create a feature branch.
3. Make your changes.
4. Test the changes locally.
5. Submit a pull request with a clear description.

## 📄 License

No license has been specified in this README. Check the repository for a license file before reusing or distributing the project.

## 👩‍💻 Author

**Jiya Bhardwaj**

GitHub: [@jiya1928](https://github.com/jiya1928)

---

*Content OS — Research smarter. Create better content. Streamline publishing.*
