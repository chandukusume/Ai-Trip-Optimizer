"""
AI Trip Optimizer - Command Line Interface
Main application entry point
"""

import sys
from trip_optimizer import TripOptimizer


def print_header():
    """Print application header."""
    print("\n" + "=" * 60)
    print("       AI TRIP OPTIMIZER")
    print("  Plan Your Perfect Trip with AI Assistance")
    print("=" * 60 + "\n")


def print_separator():
    """Print a separator line."""
    print("\n" + "-" * 60 + "\n")


def get_destination() -> str:
    """Get destination from user."""
    while True:
        destination = input("Enter your destination: ").strip()
        if destination:
            return destination
        print("Destination cannot be empty. Please try again.")


def get_budget() -> float:
    """Get budget from user."""
    while True:
        try:
            budget_input = input("Enter your budget (in USD): $").strip()
            budget = float(budget_input)
            if budget > 0:
                return budget
            print("Budget must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_preferences() -> list:
    """Get preferences from user."""
    print("\nEnter your preferences (comma-separated)")
    print("Examples: adventure, cultural, relaxation, food, shopping, nature, beach, history, nightlife")
    
    while True:
        preferences_input = input("Your preferences: ").strip()
        if preferences_input:
            preferences = [p.strip() for p in preferences_input.split(",") if p.strip()]
            if preferences:
                return preferences
        print("Please enter at least one preference.")


def get_days() -> int:
    """Get number of days from user."""
    while True:
        try:
            days_input = input("Enter number of days for the trip: ").strip()
            days = int(days_input)
            if days > 0:
                return days
            print("Number of days must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_trip_plan(result: dict):
    """Display the generated trip plan."""
    if result.get("success"):
        print_separator()
        print("✓ Trip Plan Generated Successfully!")
        print_separator()
        print(f"Destination: {result['destination']}")
        print(f"Budget: ${result['budget']:.2f} USD")
        print(f"Preferences: {', '.join(result['preferences'])}")
        print_separator()
        print("TRIP PLAN:\n")
        print(result["trip_plan"])
        print_separator()
    else:
        print("\n✗ Failed to generate trip plan")
        if "errors" in result:
            print("\nValidation Errors:")
            for field, error in result["errors"].items():
                print(f"  - {field}: {error}")
        elif "error" in result:
            print(f"\nError: {result['error']}")


def display_optimized_itinerary(result: dict):
    """Display the optimized itinerary."""
    if result.get("success"):
        print_separator()
        print("✓ Optimized Itinerary Generated Successfully!")
        print_separator()
        print(f"Destination: {result['destination']}")
        print(f"Total Budget: ${result['budget']:.2f} USD")
        print(f"Duration: {result['days']} days")
        print(f"Daily Budget: ${result['daily_budget']:.2f} USD")
        print(f"Preferences: {', '.join(result['preferences'])}")
        print_separator()
        print("OPTIMIZED ITINERARY:\n")
        print(result["itinerary"])
        print_separator()
    else:
        print("\n✗ Failed to generate optimized itinerary")
        if "errors" in result:
            print("\nValidation Errors:")
            for field, error in result["errors"].items():
                print(f"  - {field}: {error}")
        elif "error" in result:
            print(f"\nError: {result['error']}")


def main():
    """Main application function."""
    print_header()
    
    try:
        # Initialize trip optimizer
        optimizer = TripOptimizer()
        
        # Get user inputs
        destination = get_destination()
        budget = get_budget()
        preferences = get_preferences()
        
        # Ask user what they want to do
        print("\nWhat would you like to do?")
        print("1. Generate a comprehensive trip plan")
        print("2. Generate an optimized day-by-day itinerary")
        
        while True:
            choice = input("\nEnter your choice (1 or 2): ").strip()
            if choice in ["1", "2"]:
                break
            print("Invalid choice. Please enter 1 or 2.")
        
        if choice == "1":
            # Generate comprehensive trip plan
            print("\nGenerating your trip plan... This may take a moment.")
            result = optimizer.plan_trip(destination, budget, preferences)
            display_trip_plan(result)
        
        else:
            # Generate optimized itinerary
            days = get_days()
            print(f"\nGenerating your {days}-day optimized itinerary... This may take a moment.")
            result = optimizer.optimize_itinerary(destination, budget, preferences, days)
            display_optimized_itinerary(result)
        
        print("\nThank you for using AI Trip Optimizer!")
        print("Have a great trip! ✈️\n")
    
    except ValueError as e:
        print(f"\n✗ Configuration Error: {e}")
        print("\nPlease ensure you have:")
        print("1. Created a .env file with your OPENAI_API_KEY")
        print("2. Or set the OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye!")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
