import pandas as pd

def get_world_df(cities: pd.DataFrame, cap_size: int = 400) -> pd.DataFrame:
    cities = cities.copy()
    
    #Compute average location per country
    country_avg = cities.groupby("country")[["lat", "lon"]].mean().reset_index()

    #Compute average location per region (with country for lookup)
    region_avg = cities.groupby(["country", "region"])[["lat", "lon"]].mean().reset_index()

    #Count regions per country and sort descending
    region_counts = region_avg.groupby("country").size().reset_index(name="region_count")
    sorted_countries = region_counts.sort_values(by="region_count", ascending=False)["country"].tolist()

    #Select one random region per country (without repetition), until cap_size is reached
    cap_size -= len(country_avg)
    selected_regions = []
    used_regions = set()

    while len(selected_regions) < cap_size:
        added_in_round = False
        for country in sorted_countries:
            if len(selected_regions) >= cap_size:
                break

            # Filter unselected regions for this country
            available = region_avg[(region_avg["country"] == country) &
                                   (~region_avg[["country", "region"]]
                                     .apply(tuple, axis=1).isin(used_regions))]
            if not available.empty:
                chosen = available.sample(n=1)
                used_regions.add((chosen.iloc[0]["country"], chosen.iloc[0]["region"]))
                selected_regions.append(chosen[["country", "lat", "lon"]])
                added_in_round = True

        if not added_in_round:
            break  # No more unique regions left

    #Combine results
    if selected_regions:
        regions_df = pd.concat(selected_regions, ignore_index=True)
        result_df = pd.concat([country_avg, regions_df], ignore_index=True)
    else:
        result_df = country_avg.copy()

    return result_df

def get_continent_df(cities: pd.DataFrame, continent: str, cap_size: int = 400) -> pd.DataFrame:
    cities = cities.copy()
    
    #Filter countries for the given continent
    cities = cities[cities['continent']==continent].copy()
    
    #Compute average location per country
    country_avg = cities.groupby("country")[["lat", "lon"]].mean().reset_index()

    #Compute average location per region (with country for lookup)
    region_avg = cities.groupby(["country", "region"])[["lat", "lon"]].mean().reset_index()

    #Count regions per country and sort descending
    region_counts = region_avg.groupby("country").size().reset_index(name="region_count")
    sorted_countries = region_counts.sort_values(by="region_count", ascending=False)["country"].tolist()

    #Select one random region per country (without repetition), until cap_size is reached
    cap_size -= len(country_avg)
    selected_regions = []
    used_regions = set()

    while len(selected_regions) < cap_size:
        added_in_round = False
        for country in sorted_countries:
            if len(selected_regions) >= cap_size:
                break

            # Filter unselected regions for this country
            available = region_avg[(region_avg["country"] == country) &
                                   (~region_avg[["country", "region"]]
                                     .apply(tuple, axis=1).isin(used_regions))]
            if not available.empty:
                chosen = available.sample(n=1)
                used_regions.add((chosen.iloc[0]["country"], chosen.iloc[0]["region"]))
                selected_regions.append(chosen[["country", "lat", "lon"]])
                added_in_round = True

        if not added_in_round:
            break  # No more unique regions left

    #Combine results
    if selected_regions:
        regions_df = pd.concat(selected_regions, ignore_index=True)
        result_df = pd.concat([country_avg, regions_df], ignore_index=True)
    else:
        result_df = country_avg.copy()

    return result_df

def get_country_df(cities: pd.DataFrame, country: str, cap_size: int = 400) -> pd.DataFrame:
    cities = cities.copy()
    
    # Filter cities for the given country
    country_df = cities[cities["country"] == country].copy()

    if country_df.empty:
        return pd.DataFrame(columns=["city", "region", "country", "lat", "lon"])  # Return empty if no data

    # Count cities per region
    region_counts = country_df.groupby("region").size().reset_index(name="city_count")
    sorted_regions = region_counts.sort_values(by="city_count", ascending=False)["region"].tolist()

    # Track selected cities to avoid duplicates
    selected_cities = []
    used_indices = set()

    # Loop until cap_size is reached or no more cities
    while len(selected_cities) < cap_size:
        added_this_round = False
        for region in sorted_regions:
            if len(selected_cities) >= cap_size:
                break

            region_cities = country_df[(country_df["region"] == region) &
                                       (~country_df.index.isin(used_indices))]

            if not region_cities.empty:
                chosen = region_cities.sample(n=1)
                used_indices.add(chosen.index[0])
                selected_cities.append(chosen)

                added_this_round = True

        if not added_this_round:
            break  # All regions exhausted

    # Step 5: Combine results
    if selected_cities:
        result_df = pd.concat(selected_cities, ignore_index=True)
    else:
        result_df = pd.DataFrame(columns=["city", "region", "country", "lat", "lon"])

    return result_df

def get_region_df(cities: pd.DataFrame, country_name: str, region: str, cap_size: int) -> pd.DataFrame:
    cities = cities.copy()
    
    # Filter to the specific country and region
    region_df = cities[(cities["country"] == country_name) & (cities["region"] == region)].copy()

    # If no data is available, return empty DataFrame with correct structure
    if region_df.empty:
        return pd.DataFrame(columns=["city", "region", "country", "lat", "lon"])

    # Cap sample size to what's available
    sample_size = min(cap_size, len(region_df))
    return region_df.sample(n=sample_size).reset_index(drop=True)

def get_city_row(cities: pd.DataFrame, country_name: str, region: str, city_name: str) -> pd.DataFrame:
    cities = cities.copy()
    
    # Filter to match all three conditions
    city_row = cities[
        (cities["country"] == country_name) &
        (cities["region"] == region) &
        (cities["city"] == city_name)
    ]

    # Return the row (or empty DataFrame if not found)
    return city_row.reset_index(drop=True)
