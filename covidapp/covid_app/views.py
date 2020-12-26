from django.shortcuts import render
import requests
import json

# Endpoint to request statistical information on covid19
url = "https://covid-193.p.rapidapi.com/statistics"

# Configuration of the key in the header to access the API
headers = {
    'x-rapidapi-key': "1667516e6amshc4aaf5a5a03bdb8p1fd923jsn482cb39515e0",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

# Get request to the endpoint to obtain statistics,
# and we convert them with the .json () method
response = requests.request("GET", url, headers=headers).json()


def reportView(request):
    """ View that renders report.html, filters and organizes
        the information according to the request received """

    # Total number of countries in the report
    noofresults = int(response['results'])

    # Generation of a list with the name of all the countries in the report
    resulist = []
    for result in range(0, noofresults):
        resulist.append(response['response'][result]['country'])

    # POST
    if request.method == "POST":
        select_country = request.POST['select_country']

        # JSON is traversed to locate the selected
        # country and obtain the respective data
        for result in range(0, noofresults):
            if select_country == response['response'][result]['country']:
                new = response['response'][result]['cases']['new']
                active = response['response'][result]['cases']['active']
                critical = response['response'][result]['cases']['critical']
                recovered = response['response'][result]['cases']['recovered']
                total = response['response'][result]['cases']['total']

                # Calculate number of deaths
                deaths = int(total) - int(active) - int(recovered)

        # Processed information is saved in the dictionary for rendering
        context = {'select_country': select_country, 'resulist': resulist,
                   'new': new, 'active': active, 'critical': critical,
                   'recovered': recovered, 'total': total, 'deaths': deaths}
        return render(request, "report.html", context)

    # GET
    context = {'resulist': resulist}
    return render(request, "report.html", context)
