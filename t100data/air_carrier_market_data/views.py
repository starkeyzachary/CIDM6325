# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum, Avg, Q


from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFreightByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_freight=Sum('freight')) \
                        .order_by('-total_freight')[0:5]
    template_name="rankorder_list_origin_freight.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFreightByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_freight=Sum('freight')) \
                        .order_by('-total_freight')[0:5]
    template_name="rankorder_list_destination_freight.html"

# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_origin_mail.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_destination_mail.html"

# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:5]
    template_name="rankorder_list_origin_distance.html"

# What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDistanceByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:5]
    template_name="rankorder_list_destination_distance.html"

# Which airport reported the most passengers by month?
class MostPaxByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airline reported the most freight carried?
class MostFreightByAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_freight=Sum('freight')) \
                        .order_by('-total_freight')[0:1]
    template_name="most_freight_by_airline.html"

# Which airline reported the most passengers carried?
class MostPaxByAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_passengers=Sum('passengers')) \
                        .order_by('-total_passengers')[0:1]
    template_name="most_passengers_by_airline.html"

# Which airline reported the most mail carried?
class MostMailByAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:1]
    template_name="most_mail_by_airline.html"
    
# Which airline reported the longest flight distance?
class LongestFlightDistanceByAirline(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:1]
    template_name="longest_distance_by_airline.html"
    
# Rank order passengers carried, by month for AA (American Airlines)
class AAPaxByMonth(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .filter(carrier_id='AA') \
                        .values('month') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:6]
    template_name="most_pax_by_month.html"

# Rank order passengers carried, by month for AS (Alaska Airlines)
class ASPaxByMonth(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .filter(carrier_id='AS') \
                        .values('month') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:6]
    template_name="most_pax_by_month.html"

# Rank order passengers carried, by month for DL (Delta Airlines)
class DLPaxByMonth(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .filter(carrier_id='DL') \
                        .values('month') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:6]
    template_name="most_pax_by_month.html"

# Rank order passengers carried, by month for UA (United Airlines)
class UAPaxByMonth(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .filter(carrier_id='UA') \
                        .values('month') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:6]
    template_name="most_pax_by_month.html"

# Rank order passengers carried, by month for WN (Southwest Airlines)
class WNPaxByMonth(ListView):
    context_object_name = "airline_list"
    queryset = MarketData.objects \
                        .filter(carrier_id='WN') \
                        .values('month') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:6]
    template_name="most_pax_by_month.html"

# Find the average number of passengers for flights into: LAX (Los Angeles)
class AvgPaxIntoLAX(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(dest_iata_code='LAX') \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(avg_pax=Avg('passengers'))
    template_name="avg_pax_into_airport.html"

# Find the average number of passengers for flights into: SFO (San Francisco)
class AvgPaxIntoSFO(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(dest_iata_code='SFO') \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(avg_pax=Avg('passengers'))
    template_name="avg_pax_into_airport.html"

# Find the average number of passengers for flights into: DFW (Dallas-Fort Worth)
class AvgPaxIntoDFW(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(dest_iata_code='DFW') \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(avg_pax=Avg('passengers'))
    template_name="avg_pax_into_airport.html"

# Find the average number of passengers for flights into: ATL (Atlanta)
class AvgPaxIntoATL(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(dest_iata_code='ATL') \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(avg_pax=Avg('passengers'))
    template_name="avg_pax_into_airport.html"
    
# Find the average number of passengers for flights into: ORD (Chicago)
class AvgPaxIntoORD(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(dest_iata_code='ORD') \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(avg_pax=Avg('passengers'))
    template_name="avg_pax_into_airport.html"
# Find the average volume of freight for flights departing: MIA (Miami)
class AvgVolOriginMIA(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(orig_iata_code='MIA') \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(avg_vol=Avg('freight'))
    template_name="avg_vol_origin.html"

# Find the average volume of freight for flights departing: MEM (Memphis)
class AvgVolOriginMEM(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(orig_iata_code='MEM') \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(avg_vol=Avg('freight'))
    template_name="avg_vol_origin.html"

# Find the average volume of freight for flights departing: JFK (New York JFK)
class AvgVolOriginJFK(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(orig_iata_code='JFK') \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(avg_vol=Avg('freight'))
    template_name="avg_vol_origin.html"

# Find the average volume of freight for flights departing: ANC (Anchorage)
class AvgVolOriginANC(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(orig_iata_code='ANC') \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(avg_vol=Avg('freight'))
    template_name="avg_vol_origin.html"

# Find the average volume of freight for flights departing: SDF (Louisville)
class AvgVolOriginSDF(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(orig_iata_code='SDF') \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(avg_vol=Avg('freight'))
    template_name="avg_vol_origin.html"

# What city pairs represent the most freight carried for the longest distance?
class MostFreightCityPairOrderByDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name','dest_iata_code','dest_city_name') \
                        .annotate(total_distance=Sum('distance'),total_freight=Sum('freight')) \
                        .order_by('-total_distance','-total_freight') [0:1] 
    template_name="most_freight_by_distance.html"

# What city pairs represent the most mail carried for the shortest distance?
class MostMailCityPairOrderByDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .filter(Q(distance__gt=0) & Q(mail__gt=0)) \
                        .values('orig_iata_code','orig_city_name','dest_iata_code','dest_city_name') \
                        .annotate(total_distance=Sum('distance'),total_mail=Sum('mail')) \
                        .order_by('total_distance','-total_mail') [0:1] 
    template_name="most_mail_by_distance.html"