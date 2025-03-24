from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Station:
    def __init__(self, idx: str, name: str, line: str):
        self.idx = idx  # Station ID
        self.name = name  # Station name
        self.line = line  # Line name
        self.neighbors: List[Tuple['Station', int]] = []  # List of (station, time) tuples

    # Add a neighboring station
    def add_neighbor(self, station: 'Station', time: int):
        self.neighbors.append((station, time))

class MetroNetwork:
    def __init__(self):
        self.stations: Dict[str, Station] = {}  # Dictionary of stations by ID
        self.lines: Dict[str, List[Station]] = defaultdict(list)  # Dictionary of lines with list of stations

    # Add a new station to the network
    def add_station(self, idx: str, name: str, line: str) -> None:
        if idx not in self.stations:
            station = Station(idx, name, line)
            self.stations[idx] = station
            self.lines[line].append(station)

    # Add a connection between two stations
    def add_connection(self, station1_id: str, station2_id: str, time: int) -> None:
        if station1_id in self.stations and station2_id in self.stations:
            station1 = self.stations[station1_id]
            station2 = self.stations[station2_id]
            station1.add_neighbor(station2, time)
            station2.add_neighbor(station1, time)
    
    # Find the route with the fewest transfers
    def find_fewest_transfers_route(self, start_id: str, end_id: str) -> Optional[List[str]]:
        if start_id not in self.stations or end_id not in self.stations:
            return None
        
        queue = deque([(self.stations[start_id], [start_id])])
        visited = set()
        
        while queue:
            current_station, path = queue.popleft()
            
            if current_station.idx == end_id:
                return path
            
            visited.add(current_station.idx)
            
            for neighbor, _ in current_station.neighbors:
                if neighbor.idx not in visited:
                    queue.append((neighbor, path + [neighbor.idx]))
        
        return None
    
    # Find the fastest route
    def find_fastest_route(self, start_id: str, end_id: str) -> Optional[Tuple[List[str], int]]:
        if start_id not in self.stations or end_id not in self.stations:
            return None
        
        pq = [(0, id(self.stations[start_id]), self.stations[start_id], [start_id])]
        visited = {}
        
        while pq:
            total_time, _, current_station, path = heapq.heappop(pq)
            
            if current_station.idx == end_id:
                return path, total_time
            
            if current_station.idx in visited and visited[current_station.idx] <= total_time:
                continue
            
            visited[current_station.idx] = total_time
            
            for neighbor, time in current_station.neighbors:
                heapq.heappush(pq, (total_time + time, id(neighbor), neighbor, path + [neighbor.idx]))
        
        return None

if __name__ == "__main__":
    metro = MetroNetwork()

    # List of stations on M1 line
    stations_M1 = [
        "Yenikapı", "Aksaray", "Emniyet-Fatih", "Topkapı-Ulubatlı", "Bayrampaşa-Maltepe", "Sağmalcılar",
        "Kocatepe", "Otogar", "Terazidere", "Davutpaşa–YTÜ", "Merter", "Zeytinburnu", "Bakırköy-İncirli", 
        "Bahçelievler", "Ataköy-Şirinevler", "Yenibosna", "DTM–İstanbul", "Atatürk Havalimanı", 
        "Esenler", "Menderes", "Üçyüzlü", "Bağcılar Meydan", "Kirazlı"
    ]

    # List of stations on M2 line
    stations_M2 = [
        "Yenikapı", "Vezneciler-İstanbul Ü.", "Haliç", "Şişhane", "Taksim", "Osmanbey", 
        "Şişli-Mecidiyeköy", "Gayrettepe", "Levent", "4.Levent", "Sanayi Mahalles", "Seyrantepe", 
        "İTÜ-Ayazağa", "Atatürk Oto Sanayi", "Darüşşafaka", "Hacıosman"
    ]

    # List of stations on M3 line
    stations_M3 = [
        "Bakırköy Sahil", "Özgürlük Meydanı", "İncirli", "Haznedar", "İlkyuva", "Molla Gürani", 
        "Kirazlı-Bağcılar", "Yenimahalle", "Mahmutbey", "İSTOÇ", "İkitelli Sanayi", "Turgut Özal", 
        "Siteler", "Başak Konutları", "Başakşehir-Metrokent", "Onurkent", "Şehir Hastanesi", 
        "Toplu Konutlar", "Kayaşehir Merkez"
    ]
    
    # List of stations on M4 line
    stations_M4 = [
        "Kadıköy", "Ayrılık Çeşmesi", "Acıbadem", "Ünalan", "Göztepe", "Yenisahra", 
        "Pegasus-Kozyatağı", "Bostancı", "Küçükyalı", "Maltepe", "Huzurevi", "Gülsuyu", 
        "Esenkent", "Hastane-Adliye", "Soğanlık", "Kartal", "Yakacık-Adnan Kahveci", 
        "Pendik", "Tavşantepe", "Fevzi Çakmak-Hastane", "Yayalar-Şeyhli", "Kurtköy", 
        "Sabiha Gökçen Havalimanı"
    ]
        
    # List of stations on M5 line
    stations_M5 = [
        "Üsküdar", "Fıstıkağacı", "Bağlarbaşı", "Altunizade", "Kısıklı", "Bulgurlu", 
        "Ümraniye", "Çarşı", "Yamanevler", "Çakmak", "Ihlamurkuyu", "Altınşehir", 
        "İmam Hatip Lisesi", "Dudullu", "Necip Fazıl", "Çekmeköy", "Meclis", "Sarıgazi", 
        "Sancaktepe", "Samandıra Merkez"
    ]
       
    # List of stations on M7 line
    stations_M7 = [
        "Yıldız", "Fulya", "Mecidiyeköy", "Çağlayan", "Kağıthane", "Nurtepe", 
        "Alibeyköy", "Çırçır Mahallesi", "Veysel Karani-Akşemsettin", "Yeşilpınar", 
        "Kazım Karabekir", "Yenimahalle", "Karadeniz Mahallesi", "Tekstilkent-Giyimkent", 
        "Oruç Reis", "Göztepe Mahallesi", "Mahmutbey"
    ]
        
    # List of stations on M8 line
    stations_M8 = [
        "Bostancı", "Emin Ali Paşa", "Ayşekadın", "Kozyatağı", "Küçükbakkalköy", "İçerenköy",
        "Kayışdağı", "Mevlana", "İMES", "MODOKO-KEYAP", "Dudullu", "Huzur", "Parseller"
    ]
        
    # List of stations on M9 line
    stations_M9 = [
        "Ataköy", "Yenibosna", "Çobançeşme", "29 Ekim Cumhuriyet", "Doğu Sanayi", "Mimar Sinan",
        "15 Temmuz", "Halkalı Caddesi", "Atatürk Mahallesi", "Bahariye", "MASKO", "İkitelli Sanayi",
        "Ziya Gökalp Mahallesi", "Olimpiyat"
    ]
        
    # List of stations on Marmaray line
    stations_Marmaray = [
    "Halkalı", "Mustafa Kemal", "Küçükçekmece", "Florya", "Florya Akvaryum", "Yeşilköy", 
    "Yeşilyurt", "Ataköy", "Bakırköy", "Yenimahalle", "Zeytinburnu", "Kazlıçeşme", "Yenikapı", 
    "Sirkeci", "Üsküdar", "Ayrılık Çeşmesi", "Söğütlüçeşme", "Feneryolu", "Göztepe", 
    "Erenköy", "Suadiye", "Bostancı", "Küçükyalı", "İdealtepe", "Süreyya Plajı", "Maltepe", 
    "Cevizli", "Atalar", "Başak", "Kartal", "Yunus", "Pendik", "Kaynarca", "Tersane", "Güzelyalı", 
    "Aydıntepe", "İçmeler", "Tuzla", "Çayırova", "Fatih", "Osmangazi", "Darıca", "Gebze"
    ]
        
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
        
    # Adding stations of M3 line to the network
    for idx, station in enumerate(stations_M3, start=1):
        metro.add_station(f"M3A{idx}", station, "M3")

    # Adding connections between M3 line stations
    for i in range(len(stations_M3) - 1):
        connection_time = 2 if i % 2 == 0 else 3
        metro.add_connection(f"M3A{i+1}", f"M3A{i+2}", connection_time)

    # Adding stations of M4 line to the network
    for idx, station in enumerate(stations_M4, start=1):
        metro.add_station(f"M4A{idx}", station, "M4")

    # Adding connections between M4 line stations
    for i in range(len(stations_M4) - 1):
        metro.add_connection(f"M4A{i+1}", f"M4A{i+2}", 2 if i % 2 == 0 else 3)

    # Adding stations of M5 line to the network
    for idx, station in enumerate(stations_M5, start=1):
        metro.add_station(f"M5A{idx}", station, "M5")

    # Adding connections between M5 line stations
    for i in range(len(stations_M5) - 1):
        connection_time = 2 if i % 2 == 0 else 3
        metro.add_connection(f"M5A{i+1}", f"M5A{i+2}", connection_time)

    # Adding stations of M7 line to the network
    for idx, station in enumerate(stations_M7, start=1):
        metro.add_station(f"M7A{idx}", station, "M7")

    # Adding connections between M7 line stations
    for i in range(len(stations_M7) - 1):
        metro.add_connection(f"M7A{i+1}", f"M7A{i+2}", 2 if i % 2 == 0 else 3)

    # Adding stations of M8 line to the network
    for idx, station in enumerate(stations_M8, start=1):
        metro.add_station(f"M8A{idx}", station, "M8")

    # Adding connections between M8 line stations
    for i in range(len(stations_M8) - 1):
        metro.add_connection(f"M8A{i+1}", f"M8A{i+2}", 2 if i % 2 == 0 else 3)

    # Adding stations of M9 line to the network
    for idx, station in enumerate(stations_M9, start=1):
        metro.add_station(f"M9A{idx}", station, "M9")

    # Adding connections between M9 line stations
    for i in range(len(stations_M9) - 1):
        metro.add_connection(f"M9A{i+1}", f"M9A{i+2}", 2 if i % 2 == 0 else 3)

    # Adding stations of Marmaray line to the network
    for idx, station in enumerate(stations_Marmaray, start=1):
        metro.add_station(f"B1A{idx}", station, "B1")

    # Adding connections between Marmaray line stations
    for i in range(len(stations_Marmaray) - 1):
        metro.add_connection(f"B1A{i+1}", f"B1A{i+2}", 2)

    # Adding interchanges between lines
    metro.add_connection("M1A1", "B1A13", 2)  # Yenikapı (M1 - MR)
    metro.add_connection("M2A1", "B1A13", 2)  # Yenikapı (M2 - MR)
    metro.add_connection("M1A1", "M2A1", 2)  # Yenikapı (M1 - M2)
    metro.add_connection("M1A23", "M3A1", 1)  # Kirazlı (M1 - M3)
    metro.add_connection("M2A7", "M7A3", 1)  # Şişli-Mecidiyeköy (M2 - M7)
    metro.add_connection("M3A9", "M7A17", 1)  # Mahmutbey (M3 - M7)
    metro.add_connection("M1A13", "M3A3", 1)  # Bakırköy-İncirli (M1) -> İncirli (M3)
    metro.add_connection("M3A2", "B1A9", 1)  # Özgürlük Meydanı (M3) -> Bakırköy (MR)
    metro.add_connection("M4A2", "B1A16", 1)  # Ayrılık Çeşmesi (M4 - MR)
    metro.add_connection("M5A1", "B1A15", 1)  # Üsküdar (M5 - MR)
    metro.add_connection("M5A14", "M8A11", 1)  # Dudullu (M5 - M8)
    metro.add_connection("M4A7", "M8A4", 1)  # Kozyatağı (M4 - M8)
    metro.add_connection("M9A12", "M3A11", 1)  # İkitelli Sanayi (M9 - M3)
    metro.add_connection("M1A16", "M9A2", 1)  # Yenibosna (M1 - M9)
    metro.add_connection("M9A1", "B1A8", 1)  # Ataköy (M9 - MR)

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