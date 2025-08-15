def add_time(start, duration, starting_day=None):
    # Days of the week for indexing
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert start time to 24-hour format
    if period.upper() == "PM":
        start_hour = (start_hour % 12) + 12
    elif period.upper() == "AM" and start_hour == 12:
        start_hour = 0

    # Parse the duration
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Add time
    end_minute = start_minute + dur_minute
    extra_hour = end_minute // 60
    end_minute %= 60

    end_hour = start_hour + dur_hour + extra_hour
    days_later = end_hour // 24
    end_hour %= 24

    # Determine new period and hour in 12-hour format
    if end_hour == 0:
        display_hour = 12
        period = "AM"
    elif end_hour < 12:
        display_hour = end_hour
        period = "AM"
    elif end_hour == 12:
        display_hour = 12
        period = "PM"
    else:
        display_hour = end_hour - 12
        period = "PM"

    # Build result string
    result = f"{display_hour}:{end_minute:02d} {period}"

    # Calculate new day of week if given
    if starting_day:
        day_index = days_of_week.index(starting_day.capitalize())
        new_day = days_of_week[(day_index + days_later) % 7]
        result += f", {new_day}"

    # Append number of days later
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result
