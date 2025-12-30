"""
Example usage of the AI Trip Optimizer
This file demonstrates how to use the TripOptimizer class programmatically
"""

from trip_optimizer import TripOptimizer
import os


def example_comprehensive_plan():
    """Example: Generate a comprehensive trip plan."""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Comprehensive Trip Plan")
    print("=" * 60 + "\n")
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY not found in environment.")
        print("This is a demonstration of how to use the API.")
        print("To run this example, set your OPENAI_API_KEY in .env file.\n")
        return
    
    # Initialize the optimizer
    optimizer = TripOptimizer()
    
    # Define trip parameters
    destination = "Bali, Indonesia"
    budget = 1500.0
    preferences = ["beach", "cultural", "relaxation", "nature"]
    
    print(f"Destination: {destination}")
    print(f"Budget: ${budget:.2f}")
    print(f"Preferences: {', '.join(preferences)}")
    print("\nGenerating trip plan...\n")
    
    # Generate trip plan
    result = optimizer.plan_trip(destination, budget, preferences)
    
    # Display results
    if result["success"]:
        print("✓ Success!\n")
        print(result["trip_plan"])
    else:
        print("✗ Failed to generate plan")
        if "error" in result:
            print(f"Error: {result['error']}")
        if "errors" in result:
            print(f"Validation errors: {result['errors']}")


def example_optimized_itinerary():
    """Example: Generate an optimized day-by-day itinerary."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Optimized Day-by-Day Itinerary")
    print("=" * 60 + "\n")
    
    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY not found in environment.")
        print("This is a demonstration of how to use the API.")
        print("To run this example, set your OPENAI_API_KEY in .env file.\n")
        return
    
    # Initialize the optimizer
    optimizer = TripOptimizer()
    
    # Define trip parameters
    destination = "Rome, Italy"
    budget = 2000.0
    preferences = ["history", "food", "art", "architecture"]
    days = 5
    
    print(f"Destination: {destination}")
    print(f"Budget: ${budget:.2f}")
    print(f"Duration: {days} days")
    print(f"Preferences: {', '.join(preferences)}")
    print("\nGenerating optimized itinerary...\n")
    
    # Generate optimized itinerary
    result = optimizer.optimize_itinerary(destination, budget, preferences, days)
    
    # Display results
    if result["success"]:
        print("✓ Success!\n")
        print(f"Daily Budget: ${result['daily_budget']:.2f}")
        print("\n" + result["itinerary"])
    else:
        print("✗ Failed to generate itinerary")
        if "error" in result:
            print(f"Error: {result['error']}")
        if "errors" in result:
            print(f"Validation errors: {result['errors']}")


def example_validation():
    """Example: Input validation."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Input Validation")
    print("=" * 60 + "\n")
    
    # These examples don't need API key as they only test validation
    optimizer = TripOptimizer(api_key="dummy_key_for_validation")
    
    # Test invalid inputs
    print("Testing invalid inputs...")
    
    # Empty destination
    result1 = optimizer.validate_inputs("", 1000, ["beach"])
    print(f"\n1. Empty destination: {result1}")
    
    # Negative budget
    result2 = optimizer.validate_inputs("Paris", -100, ["cultural"])
    print(f"2. Negative budget: {result2}")
    
    # Empty preferences
    result3 = optimizer.validate_inputs("London", 1500, [])
    print(f"3. Empty preferences: {result3}")
    
    # Valid inputs
    result4 = optimizer.validate_inputs("Tokyo", 2500, ["food", "technology"])
    print(f"4. Valid inputs: {result4}")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("     AI TRIP OPTIMIZER - USAGE EXAMPLES")
    print("=" * 60)
    
    # Run validation example (doesn't need API key)
    example_validation()
    
    # The following examples require an OpenAI API key
    print("\n" + "=" * 60)
    print("The following examples require a valid OPENAI_API_KEY")
    print("Set it in your .env file to run these examples")
    print("=" * 60)
    
    # Uncomment to run with actual API (requires valid API key)
    # example_comprehensive_plan()
    # example_optimized_itinerary()
    
    print("\n" + "=" * 60)
    print("To run the full examples with AI generation:")
    print("1. Add your OPENAI_API_KEY to .env file")
    print("2. Uncomment the function calls in this file")
    print("3. Run: python example_usage.py")
    print("=" * 60 + "\n")
