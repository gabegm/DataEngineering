# Questions

| Step | Section             |
| ---- | ------------------- |
| 1    | Clarify Questions   |
| 2    | Assess Requirements |
| 3    | Solution            |
| 4    | Validation          |
| 5    | Additional Concerns |

## Social Media App

You’re tasked with building a notification system for a simple Reddit-style app.

What would the backend and data model look like?

### Hypothesis

Notifications have two general types:

* trigger based notifications (event trigger)
  * notification of reply to comment
* scheduled notifications (user trigger)
  * targeted content for engagement

### Architecture & Data Model

Database for notifications with two tables:

* notifications (notification type details)
  * name: notification name
  * type: user/event

* notification metrics (notification metrics)
  * time sent
  * events: reads/clicks/delivers/etc.

A task manager would be implemented with the sole purpose of collecting triggered notifications asynchronously from the actual application.

This is done as not to bring down the application in case of an influx of notifications which would happen if we were to log notifications within the app.

Logged notifications will be inserted into the notification_metrics table to record a value.

### Design Implications

Should we want to also track reads and opens, as well as follow-through rates, we might consider updating the notification_metrics table in real-time.

A webhook can be set up to run an update or insert command, however due to performance reasons we will mainly perform an insert.

Depending on the refresh cadence for the ETL to pipe-out notification analytics, care will also needed to be taken to ensure data integrity is kept in check.

If notifications are delayed...(backfill)

## Dating App

Design a database to represent a Tinder-style dating app

What does the schema look like and what are some optimizations that you think we might need?
### Hypothesis

Key capabilities of dating app:

* onboarding (user)
  * app preferences
  * pictures
  * swiping
* matching
  * notification of match
* messaging
  * messaging other matched users

Potential specific swiping feature goals:

* matching algorithm (similarity vs. dumb matching)
* user preferences (hard vs. soft)
  * distance and gender filters (hard)
  * race and age (soft)

### Architect and Data Model

| Users           |
| --------------- |
| id              |
| name            |
| location_fk     |
| gender          |
| ethnicity       |
| bio             |
| profile_picture |

| Swipes      |
| ----------- |
| id          |
| user_a      |
| user_b      |
| created_at  |
| swipe_state |

| Messages   |
| ---------- |
| id         |
| created_at |
| body       |
| sender_id  |
| receiver_id   |

| Locations     |
| ------------- |
| id            |
| city          |
| state         |
| country       |
| zipcode       |
| centroid_long |
| centroid_lat  |

### Design Implications

Potential states represented numerically to save space and kept simple:

* user_a swipes right; user_b swipes left
* user_a swipes left; user_b swipes right
* user_a swipes right; user_b swipes right
* user_a swipes left; user_b swipes left

One extra state could be used to track when the user hasn't yet swiped on another user who has swiped right on them.

## Trade-Offs and Optimisations

Although indexing the locations table could improve query performance, it is not possible to do with the swipes table due to the nature of its size. One alternative would be to implement a sharded database design which would drastically improve performance.

Another performance improvement could be to completely remove the swipes table and treat swipe events as a log event. This design cold be scaled out using a streaming service.

## Retail Store

You’re tasked with building a data pipeline for POS data from a store like Walmart

This data will be used by data scientists. How would you do it?

## Music Database

Let’s say you work at Spotify.

We want to design a relational database for storing metadata about songs.

We want to include metadata like song title, song length, the date the song was added to the platform, artist, album, track number (on the album), the song’s release year, and its genre.

How would you go about designing this database?

### Hypothesis

Assuming songs can have multiple genres...
Assuming artists can have multiple songs...
Assuming artists can have multiple albums...

### Architect and Data Model


| Genres        |
| ------------- |
| id            |
| name          |

| Artists     |
| ------------- |
| id            |
| name          |

| Albums        |
| ------------- |
| id            |
| name          |
| artist_fk     |

| Songs          |
| -------------- |
| id             |
| title          |
| release_year   |
| published_date |
| track_no       |
| length         |
| album_fk       |
| genre_fk       |
| artist_fk      |

## Click Data Stream

How would you create a schema to represent client click data on the web?

### Hypothesis

Assuming sessions can have multiple clients...
Assuming sessions can have multiple events...

### Architect and Data Model

| Clients       |
| ------------- |
| id            |
| name          |

| Events        |
| ------------- |
| id            |
| name          |

| Sessions      |
| ------------- |
| id            |
| date_time     |
| event_fk      |
| user_fk       |

## Crossing Bridges

Let’s say we want to run some data collection on the Golden Gate Bridge.

What would the table schema look like if we wanted to track how long each car took coming into San Francisco to enter and exit the bridge? Let’s say we want to track additional descriptives like the car model and license plate.

### Hypothesis

Two rows per crossing.

### Architect and Data Model

| Drivers       |
| ------------- |
| id            |
| license_plate |
| car_fk        |

| Cars          |
| ------------- |
| id            |
| make          |
| model         |

| Events        |
| ------------- |
| id            |
| name          |

| Crossings      |
| ------------- |
| id            |
| date_time     |
| event_fk      |
| driver_fk     |

## Data Debugging

Suppose you are analysing auto insurance data. You find that in the demographic information for all insurance clients that the marriage attribute column is marked TRUE for all customers.

How would you debug what happened? What data would you look into and how would you find out who is actually married and who is not?

## Shopping Cart

You’re tasked with building a shopping cart for a simple Ebay-style app.

What would the backend and data model look like?

## Booking System

You’re tasked with building a booking system for a simple Booking-style app.

What would the backend and data model look like?

## Streaming App

You’re tasked with building a streaming app for a simple Netflix-style app.

What would the backend and data model look like?

## Ride Hailing

You’re tasked with building a ride hailing app for a simple Reddit-style app.

What would the backend and data model look like?

## Search Engine

You’re tasked with building a search engine for a simple Google-style app.

What would the backend and data model look like?

## Social Feed

You’re tasked with building a social feed system for a simple Twitter-style app.

What would the backend and data model look like?

## Cloud Storage

You’re tasked with building a cloud storage for a simple Dropbox-style app.

What would the backend and data model look like?

## Parking Lot

You’re tasked with building the data warehouse infrastructure for a collection of parking lots.

What would the backend and data model look like?

### Architect and Data Model

| Drivers       |
| ------------- |
| id            |
| license_plate |
| car_fk        |

| Cars          |
| ------------- |
| id            |
| make          |
| model         |

| Lots          |
| ------------- |
| id            |
| name          |
| street        |
| city          |
| country       |
| post_code     |
| size          |

| Events        |
| ------------- |
| id            |
| name          |

| Parking       |
| ------------- |
| id            |
| date_time     |
| fee           |
| event_fk      |
| driver_fk     |
| lot_fk        |
