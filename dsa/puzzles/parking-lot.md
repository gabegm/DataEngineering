# Parking Lot

A car rental company has a cooperation with a public park house operator, which allows its customers to take the car from the park house to start their rental, but also to bring the rented car back to the park house. For using the park house, the rental company pays 1 Euro for each hour its vehicle is parked in the park house. The calculation is done on a minute-basis, I.e., the rental company pays, e.g., 25 Cent for a vehicle parking 15 minutes. For simplicity, we assume that the park house operator can perfectly track the time at which a customer rental starts/ends at the park house. This time is then considered to end/start the parking duration.

For February (I.e., for all cars parking between 01.02.2021 00:00 and 28.02.2021 24:00), the bill that was received from the park house operator appears to be quite high, namely 5,230.27€.

## Task 1:
Please use the data in the attached Excel-file to check the bill. The data shows information about the rentals of customers who made use of the park house. “Start of Trip” and “End of Trip” describe the start and the end time of the corresponding customer rental, “Vehicle Id” uniquely defines the rented vehicle (and allows identifying rentals in which the same vehicle was used), and “Trip Stated in Park House”/”Trip Ended in Park House” show a “1” if the corresponding rental started and/or ended in the park house. A "0" indicates that the rental started/ended outside of the park house.

## Task 2:
The operator suggests changing the billing approach. Instead of charging 1.00 Euro per parking hour, he would charge 1.50 Euro per hour, but parking between mid-night and 08:00am would be free of cost for the future. Please provide a suggestion whether the rental company should accept this change (you may want to do calculations on the February data here, but you do not need to).

## Solution 1

```julia
import Pkg

Pkg.activate(".")
Pkg.instantiate()

Pkg.add([
    "CSV",
    "DataFrames",
    "ShiftedArrays",
    "Missings"
])

Pkg.status()

using CSV, DataFrames
using Dates
using ShiftedArrays
using Missings

const rate = 1/60
const rate2 = 1.50/60
const startdt = Dates.DateTime("01/02/2021 00:00", Dates.DateFormat("dd/mm/yyyy H:M"))
const enddt = Dates.DateTime("28/02/2021 24:00", Dates.DateFormat("dd/mm/yyyy H:M"))
const midnightstartdt = Dates.Time("00:00", Dates.DateFormat("H:M"))
const midnightenddt = Dates.Time("08:00", Dates.DateFormat("H:M"))

df = CSV.read("data/interim/2021_05_25_Parkhouse_Data.csv", DataFrame)

# convert strings to date times
df[!, [:"Start of Trip", :"End of Trip"]] =  Dates.DateTime.(df[!, [:"Start of Trip", :"End of Trip"]], Dates.DateFormat("dd/mm/yyyy H:M"))

# sort dataframe by id, start, end
sort!(df, [:"Vehicle Id", :"Start of Trip", "End of Trip"])

# store date of next trip
df[!, :"Next Trip"] = combine(groupby(df, :"Vehicle Id"), :"Start of Trip" => Base.Fix2(lead, 1) => :"next")[!, :"next"]

# replace missing dates with end of month date
df[!, :"Next Trip"] = collect(Missings.replace(df[!, :"Next Trip"], enddt))

# number of days until next trip
df[!, "Days Till Next Trip"] = round.(df[!, :"Next Trip"] .- df[!, :"End of Trip"], Day)

# calculate time diff in minutes
df[!, :"minutes"] = Minute.(df[!, :"Next Trip"] - df[!, :"End of Trip"])

# calculates minutes without night stay
df[!, :"minutes new"] = df[!, :"minutes"] .- Minute(midnightenddt - midnightstartdt)

# calculate total cost of stay
df[!, :"cost"] = Dates.value.(df[!, :"minutes"]) * rate
df[!, :"cost new"] = Dates.value.(df[!, :"minutes new"]) * rate2

# total cost at park house
round(sum(df[!, :"cost"]); digits=2) # 5228.93
round(sum(df[!, :"cost new"]); digits=2) # 6955.4
```

## Solution 2

```julia
"""
return date: 05/02/2021 22:00
handover: 10/02/2021 10:00

if car started in park house
    calculate minutes between beginning of month and handover date
    multiply hours by rate
end

if car in park house
    calculate hours between return and handover date
    multiply hours by rate
end

if time between return date and handover date spans over midnight to 8AM
    subtract time between midnight and 8AM
end
"""

using Base: Float64
using Dates
using CSV, DataFrames
using ShiftedArrays

const csvpath = "data/interim/2021_05_25_Parkhouse_Data.csv"
const dateformat = "dd/mm/yyyy H:M"
const types = [DateTime, DateTime, Int, Bool, Bool]
const startdt = DateTime("01/02/2021 00:00", DateFormat("dd/mm/yyyy H:M"))
const enddt = DateTime("28/02/2021 24:00", DateFormat("dd/mm/yyyy H:M"))
const midnightstart = Time("00:00", DateFormat("H:M"))
const midnightend = Time("08:00", DateFormat("H:M"))

"""
vehid = 132823555
tripstart = DateTime.(["19/02/2021 11:41", "19/02/2021 20:07", "19/02/2021 21:26", "20/02/2021 11:04"], DateFormat("dd/mm/yyyy H:M"))
tripend = DateTime.(["19/02/2021 11:53", "19/02/2021 20:43", "19/02/2021 21:32", "20/02/2021 14:32"], DateFormat("dd/mm/yyyy H:M"))
parkinglotstart = [0, 1, 1, 1]
parkinglotend = [1, 1, 1, 1]

v = Vehicle(vehid, tripstart, tripend, parkinglotstart, parkinglotend)
"""
struct Vehicle
    id::Int64
    tripstart::Vector{DateTime}
    tripend::Vector{DateTime}
    parkinglotstart::Vector{Bool}
    parlkinglotend::Vector{Bool}
end

"""
calculates the length of the trip in minutes
"""
function triplength(v::Vehicle)
    return round.(v.tripend .- v.tripstart, Minute)
end

"""
calculate the cost for the time which the vehicle spends in a parking lot
"""
function calcost(v::Vehicle, rate::Float64; nightrate=false)
    cost = 0.0
    nexttrip = lead(v.tripstart, 1; default=enddt)

    if v.parkinglotstart[1] == 1
        cost += Dates.value(round(v.tripstart[1] - startdt, Minute)) * rate/60
    end

    if v.parlkinglotend[end] == 0
        cost += sum(Dates.value.(round.(nexttrip[1:end-1] - v.tripend[1:end-1], Minute)) * rate/60)
    else
        cost += sum(Dates.value.(round.(nexttrip - v.tripend, Minute)) * rate/60)
    end

    if nightrate
        dr = [collect(x:Hour(1):y) for (x, y) in zip(v.tripend, nexttrip)]
        for i in dr
            cost -= sum((midnightstart .<= Time.(i) .<= midnightend) .& ([!(x in (6,7)) for x in Dates.dayofweek.(i)])) * rate
        end
    end

    return cost
end

"""
source = "data/interim/2021_05_25_Parkhouse_Data.csv"
dateformat = "dd/mm/yyyy H:M"
types = [DateTime, DateTime, Int, Bool, Bool]
f = CSV.File(source; dateformat, types)


0.000799 seconds (3.19 k allocations: 218.656 KiB)

356.206 μs (3185 allocations: 218.66 KiB)
"""
function main(df::DataFrame)
    vs = Vehicle[]
    for g in groupby(df, :"Vehicle Id")
        push!(
            vs,
            Vehicle(
                g[!, :"Vehicle Id"][1],
                g[!, :"Start of Trip"][:],
                g[!, :"End of Trip"][:],
                g[!, :"Trip Started in Park House"][:],
                g[!, :"Trip Ended in Park House"][:]
            )
        )
    end

    return vs
end

function main(m::Matrix{Any})
    vs = Vehicle[]
    for vehicleid in unique(m[:,3])
        v = m[m[:,3] .== vehicleid, :]
        push!(vs, Vehicle(vehicleid, v[:, 1], v[:, 2], v[:, 4], v[:, 5]))
    end

    return vs
end

df = CSV.File(source; dateformat, types) |> DataFrame
m = CSV.File(source; dateformat, types) |> Tables.matrix

vs = main(m)

round(sum(calcost.(vs, 1.0)); digits=2) # 5228.93
round(sum(calcost.(vs, 1.5; nightrate=true)); digits=2) # 6530.9
```