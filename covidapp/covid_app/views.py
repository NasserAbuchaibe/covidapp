from django.shortcuts import render
import requests
import json


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "1667516e6amshc4aaf5a5a03bdb8p1fd923jsn482cb39515e0",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# Create your views here.


def reportView(request):
    if request.method == "POST":
        noofresults = int(response['results'])
        resulist = []
        for result in range(0, noofresults):
            resulist.append(response['response'][result]['country'])

        select_country = request.POST['select_country']
        for result in range(0, noofresults):
            if select_country == response['response'][result]['country']:
                new = response['response'][result]['cases']['new']
                active = response['response'][result]['cases']['active']
                critical = response['response'][result]['cases']['critical']
                recovered = response['response'][result]['cases']['recovered']
                total = response['response'][result]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'select_country': select_country, 'resulist': resulist, 'new': new, 'active': active, 'critical': critical,
                   'recovered': recovered, 'total': total, 'deaths': deaths}
        return render(request, "report.html", context)

    noofresults = int(response['results'])
    resulist = []
    for result in range(0, noofresults):
        resulist.append(response['response'][result]['country'])
    context = {'resulist': resulist}
    return render(request, "report.html", context)
