"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


# upper limit in km, min speed km/h, max speed km/h
SPEEDS = [
   (200, 15, 34),
   (400, 15, 32),
   (600, 15, 30),
   (1000, 11.428, 28),
]

# Fixed closing time (hours) for the finish control
FINISH_LIMITS = {200: 13.5, 400: 27}

def total_hours(dist_km, use_max):
   total = 0
   lower = 0
   for upper, min_speed, max_speed in SPEEDS:
      km_in_range = min(dist_km, upper) - lower
      if km_in_range <= 0:
         break

      if use_max:
         speed = max_speed
      else:
         speed = min_speed
      total += km_in_range / speed
      lower = upper
   return total

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, the control distance in kilometers
      brevet_dist_km: number, the nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
   Returns:
      An ISO 8601 format date string indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """

   dist = min(control_dist_km, brevet_dist_km)
   hours = total_hours(dist, True)
   minutes = round(hours * 60)

   start = arrow.get(brevet_start_time)
   return start.shift(minutes=minutes).isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, the control distance in kilometers
         brevet_dist_km: number, the nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  An ISO 8601 format date-time string indicating
         the official start time of the brevet
   Returns:
      An ISO 8601 format date string indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """

   dist = min(control_dist_km, brevet_dist_km)

   if dist <= 60:
        hours = dist / 20 + 1
   elif dist == brevet_dist_km and brevet_dist_km in FINISH_LIMITS:
        hours = FINISH_LIMITS[brevet_dist_km]
   else:
        hours = total_hours(dist, False)

   minutes = round(hours * 60)
   start = arrow.get(brevet_start_time)
   return start.shift(minutes=minutes).isoformat()
