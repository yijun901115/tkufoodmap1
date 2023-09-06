from django.shortcuts import render
import folium
from testingMaptemplate.models import FoodmapStore
# Create your views here.


def MapPage(request):
    foodstores = list(FoodmapStore.objects.values('district', 'restaurantname', 'address', 'contactinfo', 'googlelink', 'openingtime','latitude', 'longitude', 'ratingintotaloffive', 'ratingcategories')[:80])
    foodstoreslistdisplay = list(FoodmapStore.objects.values('restaurantname', 'address', 'ratingintotaloffive')[:80])

    foodstoresinfo = FoodmapStore.objects.all();
    #stores = FoodmapStore.objects.all()
    # m = folium.Map(location=[25.1691008, 121.454592], zoom_start=9)
    # for store in stores:
    #    coordinates = (store.latitude, store.longitude)
    #    folium.Marker(coordinates, popup=store.restaurantname).add_to(m)
    #context = {'map': m._repr_html_()}
    context = {'foodstores': foodstores,
               'foodstoreslistdisplay': foodstoreslistdisplay,
               'foodstoresinfo': foodstoresinfo,}
    return render(request, 'mappage.html', context)

#    if request.method == 'POST':
#        search_query = request.POST.get('search_query')
#        filtered_locations = FoodmapStore.objects.filter(name__icontains=search_query)
#    else:
#        filtered_locations = FoodmapStore.objects.all()

#    m = folium.Map(location=[filtered_locations[0].latitude, filtered_locations[0].longitude], zoom_start=10)

#    for location in filtered_locations:
#        folium.Marker([location.latitude, location.longitude], popup=location.restaurantname).add_to(m)

#    context = {'map': m.get_root().render()}
#    return render(request, 'map_template.html', context)

#    stores = FoodmapStore.objects.all()

#    m = folium.Map(location=[25.1691008, 121.454592], zoom_start=9)

#    for store in stores:
#        coordinates = (store.latitude, store.longitude)
#        folium.Marker(coordinates, popup=store.restaurantname).add_to(m)

#    context = {'map': m._repr_html_()}
#    return render(request, 'mappage.html', context)
