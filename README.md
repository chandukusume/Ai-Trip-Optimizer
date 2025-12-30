# AI Trip Optimizer 🌍✈️

An intelligent AI-powered assistant that plans personalized trips based on your destination, budget, and preferences. Using advanced AI technology, this tool creates comprehensive trip plans and optimized day-by-day itineraries tailored to your specific needs.

## Features

- **Personalized Trip Planning**: Get customized trip plans based on your destination, budget, and preferences
- **Budget-Aware Recommendations**: All suggestions stay within your specified budget
- **Preference-Based Itineraries**: Activities and recommendations match your interests (adventure, cultural, relaxation, food, etc.)
- **Two Planning Modes**:
  - Comprehensive trip plan with overview, accommodation, activities, and tips
  - Day-by-day optimized itinerary with detailed schedules and cost breakdowns
- **AI-Powered**: Leverages OpenAI's GPT models for intelligent, context-aware recommendations

## Requirements

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chandukusume/Ai-Trip-Optimizer.git
cd Ai-Trip-Optimizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root (copy from `.env.example`)
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Command Line Interface

Run the main application:
```bash
python main.py
```

Follow the interactive prompts to:
1. Enter your destination
2. Specify your budget (in USD)
3. List your preferences (comma-separated)
4. Choose between comprehensive trip plan or day-by-day itinerary
5. (For itinerary) Specify the number of days

### Example Session

```
======================================================================
       AI TRIP OPTIMIZER
  Plan Your Perfect Trip with AI Assistance
======================================================================

Enter your destination: Paris, France
Enter your budget (in USD): $2000
Enter your preferences (comma-separated): cultural, food, history, art
What would you like to do?
1. Generate a comprehensive trip plan
2. Generate an optimized day-by-day itinerary

Enter your choice (1 or 2): 2
Enter number of days for the trip: 5

Generating your 5-day optimized itinerary... This may take a moment.
```

### Using as a Python Module

```python
from trip_optimizer import TripOptimizer

# Initialize the optimizer
optimizer = TripOptimizer()

# Generate a comprehensive trip plan
result = optimizer.plan_trip(
    destination="Tokyo, Japan",
    budget=3000.0,
    preferences=["cultural", "food", "technology"]
)

if result["success"]:
    print(result["trip_plan"])

# Generate an optimized itinerary
itinerary = optimizer.optimize_itinerary(
    destination="Barcelona, Spain",
    budget=1500.0,
    preferences=["beach", "architecture", "nightlife"],
    days=4
)

if itinerary["success"]:
    print(itinerary["itinerary"])
```

## Preference Options

Common preferences you can use (mix and match based on your interests):
- `adventure` - Outdoor activities, hiking, thrilling experiences
- `cultural` - Museums, cultural sites, local traditions
- `relaxation` - Spa, beaches, peaceful activities
- `food` - Culinary experiences, local cuisine, food tours
- `shopping` - Markets, shopping districts, souvenirs
- `nature` - Parks, natural scenery, wildlife
- `beach` - Coastal activities, water sports
- `history` - Historical sites, monuments, heritage
- `nightlife` - Bars, clubs, evening entertainment
- `art` - Galleries, street art, artistic venues
- `architecture` - Famous buildings, architectural tours
- `photography` - Scenic spots, photo opportunities

## Project Structure

```
Ai-Trip-Optimizer/
├── main.py              # Command-line interface
├── trip_optimizer.py    # Core trip planning logic
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## How It Works

1. **Input Collection**: The application collects your destination, budget, and preferences
2. **Input Validation**: Ensures all inputs are valid and complete
3. **AI Processing**: Sends a carefully crafted prompt to OpenAI's GPT model
4. **Plan Generation**: The AI generates a detailed trip plan or itinerary
5. **Output Formatting**: Results are formatted and displayed in a user-friendly manner

## API Methods

### `TripOptimizer.plan_trip(destination, budget, preferences)`
Generates a comprehensive trip plan including:
- Destination overview
- Recommended duration
- Accommodation suggestions
- Daily itinerary
- Food recommendations
- Transportation tips
- Budget breakdown
- Best time to visit
- Important tips

### `TripOptimizer.optimize_itinerary(destination, budget, preferences, days)`
Creates a day-by-day optimized itinerary with:
- Morning, afternoon, and evening activities for each day
- Meal recommendations
- Estimated costs
- Travel tips
- Budget-aware suggestions

## Error Handling

The application includes comprehensive error handling:
- Input validation for all user inputs
- API error handling
- Clear error messages
- Graceful failure with helpful suggestions

## Tips for Best Results

1. **Be Specific**: Provide detailed preferences for more tailored recommendations
2. **Realistic Budget**: Ensure your budget is realistic for the destination
3. **Multiple Preferences**: Include 3-5 preferences for balanced itineraries
4. **Research Costs**: Consider typical costs for your destination when setting budget

## Troubleshooting

**Issue**: "OpenAI API key is required" error
- **Solution**: Ensure your `.env` file exists and contains a valid `OPENAI_API_KEY`

**Issue**: API rate limit errors
- **Solution**: Wait a few moments and try again, or upgrade your OpenAI API plan

**Issue**: Empty or incomplete responses
- **Solution**: Check your internet connection and API key validity

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool uses AI to generate trip recommendations. Always verify information, check current travel advisories, and consult official sources before making travel decisions. The developers are not responsible for any issues arising from following the generated trip plans.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.