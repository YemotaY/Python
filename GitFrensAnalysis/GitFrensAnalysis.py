#!/usr/bin/env python3

import os
import json
import csv
import time
from collections import Counter

import requests
import networkx as nx

TOKEN = os.environ["GITHUB_TOKEN"]
USERNAME = os.environ["GITHUB_USERNAME"]

BASE = "https://api.github.com"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}


###########################################################################
# API Helpers
###########################################################################

def paged(url):
    page = 1
    results = []

    while True:
        r = requests.get(
            url,
            headers=HEADERS,
            params={
                "per_page": 100,
                "page": page
            }
        )

        r.raise_for_status()

        items = r.json()

        if not items:
            break

        results.extend(items)

        if len(items) < 100:
            break

        page += 1

        # Be polite to GitHub
        time.sleep(0.2)

    return results


def followers(user):
    return paged(f"{BASE}/users/{user}/followers")


def following(user):
    return paged(f"{BASE}/users/{user}/following")


###########################################################################
# Build graph
###########################################################################

graph = nx.DiGraph()

print(f"Downloading network for {USERNAME}")

my_followers = followers(USERNAME)
my_following = following(USERNAME)

graph.add_node(USERNAME, type="self")

print(f"My followers : {len(my_followers)}")
print(f"My following : {len(my_following)}")

# followers -> me
for f in my_followers:
    graph.add_node(f["login"], type="user")
    graph.add_edge(f["login"], USERNAME)

# me -> following
for f in my_following:
    graph.add_node(f["login"], type="user")
    graph.add_edge(USERNAME, f["login"])

people = {
    u["login"] for u in my_followers
}.union({
    u["login"] for u in my_following
})

print(f"\nCollecting second-degree relationships for {len(people)} users...\n")

for i, person in enumerate(sorted(people), 1):

    print(f"[{i}/{len(people)}] {person}")

    try:
        fs = followers(person)
        fg = following(person)

        # followers(person) -> person
        for u in fs:
            graph.add_node(u["login"], type="user")
            graph.add_edge(u["login"], person)

        # person -> following(person)
        for u in fg:
            graph.add_node(u["login"], type="user")
            graph.add_edge(person, u["login"])

    except requests.HTTPError as e:
        print("Failed:", person, e)

###########################################################################
# Statistics
###########################################################################

print("\n===========================")
print("Statistics")
print("===========================")

print("Nodes :", graph.number_of_nodes())
print("Edges :", graph.number_of_edges())

followers_count = Counter()

for src, dst in graph.edges():
    followers_count[dst] += 1

print("\nTop followed users:")

for user, n in followers_count.most_common(20):
    print(f"{user:25} {n}")

###########################################################################
# Save graph
###########################################################################

nx.write_graphml(graph, "github_network.graphml")

with open("github_network.json", "w") as f:
    json.dump(nx.node_link_data(graph), f, indent=2)

with open("edges.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["from", "to"])

    for a, b in graph.edges():
        writer.writerow([a, b])

print("\nSaved:")
print(" github_network.graphml")
print(" github_network.json")
print(" edges.csv")
