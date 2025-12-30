"""
AI Trip Optimizer - Core Module
Handles trip planning logic with AI integration
"""

import os
from typing import Dict, List, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class TripOptimizer:
    """AI-powered trip optimizer that plans trips based on destination, budget, and preferences."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Trip Optimizer.
        
        Args:
            api_key: OpenAI API key. If not provided, will look for OPENAI_API_KEY in environment.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        
        self.client = OpenAI(api_key=self.api_key)
    
    def validate_inputs(self, destination: str, budget: float, preferences: List[str]) -> Dict[str, str]:
        """
        Validate user inputs.
        
        Args:
            destination: Travel destination
            budget: Budget in USD
            preferences: List of user preferences
            
        Returns:
            Dictionary with validation results
        """
        errors = {}
        
        if not destination or not destination.strip():
            errors["destination"] = "Destination cannot be empty"
        
        if budget <= 0:
            errors["budget"] = "Budget must be a positive number"
        
        if not preferences or len(preferences) == 0:
            errors["preferences"] = "At least one preference is required"
        
        return errors
    
    def plan_trip(self, destination: str, budget: float, preferences: List[str]) -> Dict[str, any]:
        """
        Plan a trip using AI based on destination, budget, and preferences.
        
        Args:
            destination: Travel destination
            budget: Budget in USD
            preferences: List of user preferences (e.g., ['adventure', 'cultural', 'relaxation'])
            
        Returns:
            Dictionary containing the trip plan
        """
        # Validate inputs
        validation_errors = self.validate_inputs(destination, budget, preferences)
        if validation_errors:
            return {
                "success": False,
                "errors": validation_errors
            }
        
        # Create prompt for AI
        preferences_str = ", ".join(preferences)
        prompt = f"""Create a detailed trip plan for a traveler with the following requirements:

Destination: {destination}
Budget: ${budget:.2f} USD
Preferences: {preferences_str}

Please provide a comprehensive trip plan that includes:
1. Overview of the destination
2. Recommended duration of stay
3. Accommodation suggestions within budget
4. Daily itinerary with activities matching the preferences
5. Food and dining recommendations
6. Transportation tips
7. Budget breakdown
8. Best time to visit
9. Important tips and considerations

Format the response in a clear, organized manner."""

        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful travel planning assistant that creates detailed, personalized trip itineraries based on user preferences and budget constraints."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            trip_plan = response.choices[0].message.content
            
            return {
                "success": True,
                "destination": destination,
                "budget": budget,
                "preferences": preferences,
                "trip_plan": trip_plan
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to generate trip plan: {str(e)}"
            }
    
    def optimize_itinerary(self, destination: str, budget: float, preferences: List[str], days: int) -> Dict[str, any]:
        """
        Optimize a trip itinerary for a specific number of days.
        
        Args:
            destination: Travel destination
            budget: Budget in USD
            preferences: List of user preferences
            days: Number of days for the trip
            
        Returns:
            Dictionary containing optimized itinerary
        """
        # Validate inputs
        validation_errors = self.validate_inputs(destination, budget, preferences)
        if validation_errors:
            return {
                "success": False,
                "errors": validation_errors
            }
        
        if days <= 0:
            return {
                "success": False,
                "error": "Number of days must be positive"
            }
        
        # Create prompt for AI
        preferences_str = ", ".join(preferences)
        daily_budget = budget / days
        
        prompt = f"""Create an optimized {days}-day itinerary for {destination} with the following constraints:

Total Budget: ${budget:.2f} USD
Daily Budget: ${daily_budget:.2f} USD
Preferences: {preferences_str}

For each day, provide:
- Morning activities
- Afternoon activities
- Evening activities
- Meal recommendations
- Estimated costs
- Travel tips

Ensure all activities match the user's preferences and stay within the budget."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert travel planner who creates optimized day-by-day itineraries that maximize value while respecting budget constraints."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            optimized_itinerary = response.choices[0].message.content
            
            return {
                "success": True,
                "destination": destination,
                "budget": budget,
                "days": days,
                "daily_budget": daily_budget,
                "preferences": preferences,
                "itinerary": optimized_itinerary
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to optimize itinerary: {str(e)}"
            }
