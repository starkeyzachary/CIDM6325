# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    Top5AirportsFreightByOrigin, \
                    Top5AirportsFreightByDestination, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDestination, \
                    Top5AirportsDistanceByOrigin, \
                    Top5AirportsDistanceByDestination, \
                    MostPaxByMonth, \
                    TopDistanceByMonth, \
                    MostFreightByAirline, \
                    MostPaxByAirline, \
                    MostMailByAirline, \
                    LongestFlightDistanceByAirline, \
                    AAPaxByMonth, \
                    ASPaxByMonth, \
                    DLPaxByMonth, \
                    UAPaxByMonth, \
                    WNPaxByMonth, \
                    AvgPaxIntoLAX, \
                    AvgPaxIntoSFO, \
                    AvgPaxIntoDFW, \
                    AvgPaxIntoATL, \
                    AvgPaxIntoORD, \
                    AvgVolOriginMIA, \
                    AvgVolOriginMEM, \
                    AvgVolOriginJFK, \
                    AvgVolOriginANC, \
                    AvgVolOriginSDF, \
                    MostFreightCityPairOrderByDistance, \
                    MostMailCityPairOrderByDistance           

urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('top5freightorigin/', 
        Top5AirportsFreightByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Total Freight by Origin Airport"}
        ), 
        name="top5freightorigin"),  
    path('top5freightdestination/', 
        Top5AirportsFreightByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Total Freight by Destination Airport"}
        ), 
        name="top5freightdestination"),
    path('top5mailorigin/', 
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Total Mail by Origin Airport"}
        ), 
        name="top5mailorigin"),  
    path('top5maildestination/', 
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Total Mail by Destination Airport"}
        ), 
        name="top5maildestination"),  
    path('top5distanceorigin/', 
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Total Distance by Origin Airport"}
        ), 
        name="top5distanceorigin"),  
    path('top5distancedestination/', 
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Total Distance by Destination Airport"}
        ), 
        name="top5distancedestination"), 
    path('mostpax_month/',  
        MostPaxByMonth.as_view(
            extra_context={'title': "Most Passengers by Month"}
        ), 
        name="mostpax_month"),  
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('mostfreight_airline/',  
        MostFreightByAirline.as_view(
            extra_context={'title': "Most Freight by Airline"}
        ), 
        name="mostfreight_airline"),
    path('mostpax_airline/',  
        MostPaxByAirline.as_view(
            extra_context={'title': "Most Passengers by Airline"}
        ), 
        name="mostpax_airline"),
    path('mostmail_airline/',  
        MostMailByAirline.as_view(
            extra_context={'title': "Most Mail by Airline"}
        ), 
        name="mostmail_airline"),
    path('longestdistance_airline/',  
        LongestFlightDistanceByAirline.as_view(
            extra_context={'title': "Longest Flight Distance by Airline"}
        ), 
        name="longestdistance_airline"),
    path('aapax_month/',  
        AAPaxByMonth.as_view(
            extra_context={'title': "Rank Order by Month of Passengers for American Airlines"}
        ), 
        name="aapax_month"),
    path('aspax_month/',  
        ASPaxByMonth.as_view(
            extra_context={'title': "Rank Order by Month of Passengers for Alaska Airlines"}
        ), 
        name="aspax_month"),
    path('dlpax_month/',  
        DLPaxByMonth.as_view(
            extra_context={'title': "Rank Order by Month of Passengers for Delta Airlines"}
        ), 
        name="dlpax_month"),
    path('uapax_month/',  
        UAPaxByMonth.as_view(
            extra_context={'title': "Rank Order by Month of Passengers for United Airlines"}
        ), 
        name="uapax_month"),
    path('wnpax_month/',  
        WNPaxByMonth.as_view(
            extra_context={'title': "Rank Order by Month of Passengers for Southwest Airlines"}
        ), 
        name="wnpax_month"),
    path('avgpax_lax/',  
        AvgPaxIntoLAX.as_view(
            extra_context={'title': "Average Passengers into LAX"}
        ), 
        name="avgpax_lax"),
    path('avgpax_sfo/',  
        AvgPaxIntoSFO.as_view(
            extra_context={'title': "Average Passengers into SFO"}
        ), 
        name="avgpax_sfo"),
    path('avgpax_dfw/',  
        AvgPaxIntoDFW.as_view(
            extra_context={'title': "Average Passengers into DFW"}
        ), 
        name="avgpax_dfw"),
    path('avgpax_atl/',  
        AvgPaxIntoATL.as_view(
            extra_context={'title': "Average Passengers into ATL"}
        ), 
        name="avgpax_atl"),
    path('avgpax_ord/',  
        AvgPaxIntoORD.as_view(
            extra_context={'title': "Average Passengers into ORD"}
        ), 
        name="avgpax_ord"),
    path('avgvol_mia/',  
        AvgVolOriginMIA.as_view(
            extra_context={'title': "Average Volume of Freight Departing MIA"}
        ), 
        name="avgvol_mia"),
    path('avgvol_mem/',  
        AvgVolOriginMEM.as_view(
            extra_context={'title': "Average Volume of Freight Departing MEM"}
        ), 
        name="avgvol_mem"),
    path('avgvol_jfk/',  
        AvgVolOriginJFK.as_view(
            extra_context={'title': "Average Volume of Freight Departing JFK"}
        ), 
        name="avgvol_jfk"),
    path('avgvol_anc/',  
        AvgVolOriginANC.as_view(
            extra_context={'title': "Average Volume of Freight Departing ANC"}
        ), 
        name="avgvol_anc"),
    path('avgvol_sdf/',  
        AvgVolOriginSDF.as_view(
            extra_context={'title': "Average Volume of Freight Departing SDF"}
        ), 
        name="avgvol_sdf"),
    path('freightcity_distance/',  
        MostFreightCityPairOrderByDistance.as_view(
            extra_context={'title': "City Pairs with Most Freight By Distance"}
        ), 
        name="freightcity_distance"),
    path('mailcity_distance/',  
        MostMailCityPairOrderByDistance.as_view(
            extra_context={'title': "City Pairs with Most Mail By Shortest Distance"}
        ), 
        name="mailcity_distance"),
]