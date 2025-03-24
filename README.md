# Istanbul Metro Network Simulation

This project is a Python simulation representing the metro lines and stations in Istanbul. The project includes various metro lines, their connections, and algorithms to find the fastest and least transfer routes between stations.

## Technologies and Libraries Used

- **Python:** The core programming language used for the project.
- **collections:** Used for creating and manipulating data structures with `defaultdict` and `deque`.
- **heapq:** Utilized for the priority queue data structure to find the fastest route.
- **typing:** Used for type hints and improving code readability.

## Algorithm Working Principles

### BFS (Breadth-First Search) Algorithm

The BFS algorithm is used to find the shortest path in graph structures. In this project, BFS is used to find the route with the fewest transfers between two stations. The working principle of the algorithm is as follows:

1. A queue is created starting from the initial station.
2. The station at the front of the queue is taken and marked as visited.
3. The neighbors of this station are added to the queue.
4. This process is repeated until the target station is reached.
5. When the target station is reached, the route is returned.

### A* (A Star) Algorithm

The A* algorithm is a pathfinding algorithm used to find the shortest path. In this project, it is used to find the fastest route between two stations. The working principle of the algorithm is as follows:

1. A priority queue is created starting from the initial station.
2. The station at the front of the queue is taken and marked as visited.
3. The neighbors of this station are added to the queue, sorted by the total time.
4. This process is repeated until the target station is reached.
5. When the target station is reached, the route and the total time are returned.

### Why These Algorithms?

- **BFS:** Ideal for finding the route with the fewest transfers because it visits all nodes at the current level before moving to the next level.
- **A*:** Ideal for finding the fastest route because it tries to minimize the cost to reach the goal.

## Example Usage and Test Results

The project allows you to add metro lines and stations, establish connections, and find routes. Below are example usage and test results:

```python
if __name__ == "__main__":
    metro = MetroNetwork()

    # Adding stations of M1 line to the network
    for idx, station in enumerate(stations_M1, start=1):
        metro.add_station(f"M1A{idx}", station, "M1")

    # Adding connections between M1 line stations
    for i in range(len(stations_M1) - 1):
        connection_time = 2 if i % 2 == 0 else 3
        metro.add_connection(f"M1A{i+1}", f"M1A{i+2}", connection_time)

    # Adding stations of M2 line to the network
    for idx, station in enumerate(stations_M2, start=1):
        metro.add_station(f"M2A{idx}", station, "M2")

    # Adding connections between M2 line stations
    for i in range(len(stations_M2) - 1):
        connection_time = 2 if i % 2 == 0 else 3
        metro.add_connection(f"M2A{i+1}", f"M2A{i+2}", connection_time)

    # (Additional code to add stations and connections)

    # Taking user input for start and end stations
    start = input("Start station: ")
    end = input("End station: ")

    # Finding the route with the fewest transfers
    route = metro.find_fewest_transfers_route(start, end)
    if route:
        print("Route with the fewest transfers:", " -> ".join(route))
    else:
        print("Route not found.")

    # Finding the fastest route
    result = metro.find_fastest_route(start, end)
    if result:
        route, time = result
        print(f"Fastest route ({time} minutes):", " -> ".join(route))
    else:
        print("Route not found.") 
```

### Test Results

- **Route with the Fewest Transfers:**
  - Example: Yenikapı to Gebze with the fewest transfers: M1A1 -> B1A13 -> ... -> B1A43
- **Fastest Route:**
  - Example: Yenikapı to Zeytinburnu fastest route: M1A1 -> M1A2 -> ... -> B1A6 (12 minutes)
  
---

# İstanbul Metro Ağı Simülasyonu

Bu proje, İstanbul'daki metro hatlarını ve istasyonlarını temsil eden bir Python simülasyonudur. Proje, çeşitli metro hatları arasındaki bağlantıları ve en hızlı ve en az aktarmalı rotaları bulma algoritmalarını içerir.

## Kullanılan Teknolojiler ve Kütüphaneler

- **Python:** Projenin temel programlama dili.
- **collections:** `defaultdict` ve `deque` sınıflarını kullanarak veri yapıları oluşturmak ve manipüle etmek için kullanılır.
- **heapq:** Öncelikli kuyruk veri yapısını kullanarak en hızlı rotayı bulmak için kullanılır.
- **typing:** Tip ipuçları ve daha iyi kod anlaşılırlığı için kullanılır.

## Algoritmaların Çalışma Mantığı

### BFS (Genişlik Öncelikli Arama) Algoritması

BFS algoritması, graf yapılarında en kısa yolu bulmak için kullanılır. Bu projede, iki istasyon arasındaki en az aktarmalı rotayı bulmak için BFS kullanılmıştır. Algoritmanın çalışma mantığı şu şekildedir:

1. Başlangıç istasyonundan itibaren bir kuyruk oluşturulur.
2. Kuyruğun başındaki istasyon alınır ve bu istasyon ziyaret edilmiş olarak işaretlenir.
3. Bu istasyonun komşuları kuyruğa eklenir.
4. Hedef istasyona ulaşılana kadar bu işlem tekrarlanır.
5. Hedef istasyona ulaşıldığında, rota geri döndürülür.

### A* (A Star) Algoritması

A* algoritması, en kısa yolu bulmak için kullanılan bir yol bulma algoritmasıdır. Bu projede, iki istasyon arasındaki en hızlı rotayı bulmak için kullanılmıştır. Algoritmanın çalışma mantığı şu şekildedir:

1. Başlangıç istasyonundan itibaren bir öncelikli kuyruk oluşturulur.
2. Kuyruğun başındaki istasyon alınır ve bu istasyon ziyaret edilmiş olarak işaretlenir.
3. Bu istasyonun komşuları, toplam süreye göre kuyrukta sıralanarak eklenir.
4. Hedef istasyona ulaşılana kadar bu işlem tekrarlanır.
5. Hedef istasyona ulaşıldığında, rota ve toplam süre geri döndürülür.

### Neden Bu Algoritmaları Kullandık?

- **BFS:** En az aktarmalı rotayı bulmak için idealdir çünkü her adımda bir sonraki seviyedeki tüm düğümleri ziyaret eder.
- **A*:** En hızlı rotayı bulmak için idealdir çünkü hedefe ulaşma maliyetini minimize etmeye çalışır.

## Örnek Kullanım ve Test Sonuçları

Proje, İstanbul'daki metro hatlarını ve istasyonlarını ekleyerek, bağlantılar kurarak ve rotaları bulma işlemlerini gerçekleştirebilir. Aşağıda örnek kullanım ve test sonuçları bulunmaktadır:

```python
if __name__ == "__main__":
    metro = MetroNetwork()

    # Adding stations of M1 line to the network
    for idx, station in enumerate(stations_M1, start=1):
        metro.add_station(f"M1A{idx}", station, "M1")

    # Adding connections between M1 line stations
    for i in range(len(stations_M1) - 1):
        connection_time = 2 if i % 2 == 0 else 3
        metro.add_connection(f"M1A{i+1}", f"M1A{i+2}", connection_time)

    # Adding stations of M2 line to the network
    for idx, station in enumerate(stations_M2, start=1):
        metro.add_station(f"M2A{idx}", station, "M2")

    # Adding connections between M2 line stations
    for i in range(len(stations_M2) - 1):
        connection_time = 2 if i % 2 == 0 else 3
        metro.add_connection(f"M2A{i+1}", f"M2A{i+2}", connection_time)

    # (Additional code to add stations and connections)

    # Taking user input for start and end stations
    start = input("Start station: ")
    end = input("End station: ")

    # Finding the route with the fewest transfers
    route = metro.find_fewest_transfers_route(start, end)
    if route:
        print("Route with the fewest transfers:", " -> ".join(route))
    else:
        print("Route not found.")

    # Finding the fastest route
    result = metro.find_fastest_route(start, end)
    if result:
        route, time = result
        print(f"Fastest route ({time} minutes):", " -> ".join(route))
    else:
        print("Route not found.") 
```

### Test Sonuçları

- **En Az Aktarmalı Rota:**
  - Örnek: Yenikapı'dan Gebze'ye en az aktarmalı rota: M1A1 -> B1A13 -> ... -> B1A43
- **En Hızlı Rota:**
  - Örnek: Yenikapı'dan Zeytinburnu'na en hızlı rota: M1A1 -> M1A2 -> ... -> B1A6 (12 dakika)
