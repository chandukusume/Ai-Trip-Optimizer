# Quick Start Guide

## Setup (5 minutes)

1. **Install Python** (3.7+)
   ```bash
   python --version  # Verify installation
   ```

2. **Clone and Setup**
   ```bash
   git clone https://github.com/chandukusume/Ai-Trip-Optimizer.git
   cd Ai-Trip-Optimizer
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Get an OpenAI API key from https://platform.openai.com/api-keys
   - Copy `.env.example` to `.env`
   - Add your key: `OPENAI_API_KEY=your_key_here`

## Run the Application

```bash
python main.py
```

## Example Input

```
Destination: Paris, France
Budget: $2000
Preferences: cultural, food, art, history
Choice: 2 (Optimized itinerary)
Days: 5
```

## What You'll Get

- ✅ Detailed day-by-day itinerary
- ✅ Activity recommendations matching your preferences
- ✅ Budget breakdown
- ✅ Dining suggestions
- ✅ Transportation tips
- ✅ Best times to visit attractions

## Troubleshooting

**No API key error?**
→ Create `.env` file with `OPENAI_API_KEY=your_key`

**Module not found?**
→ Run `pip install -r requirements.txt`

**Rate limit error?**
→ Wait a few minutes or check your OpenAI API quota

## Next Steps

- Try different destinations and preferences
- Adjust your budget to see different recommendations
- Use as a Python module (see README.md)
- Explore `example_usage.py` for programmatic usage
