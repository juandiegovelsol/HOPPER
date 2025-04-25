from collections import defaultdict, deque

def read_input():
    import sys
    data = sys.stdin.read().strip().split('\n')
    return data

def parse_input(data):
    topology = defaultdict(list)
    votes = defaultdict(lambda: {'A': 0, 'B': 0})
    
    for line in data:
        if line.startswith("#"):
            continue
        parts = line.split(')')
        province_info = parts[0].split(',')
        province_name = province_info[0].strip()
        connections = [x.strip() for x in province_info[1:] if x.strip()]
        topology[province_name] = connections

    return topology, votes

def simulate_votes(topology, votes):
    # Assuming each province has its own votes already counted
    # We need to determine the winning party for each province
    results = {}
    for province in votes:
        if votes[province]['A'] > votes[province]['B']:
            results[province] = 'A'
        elif votes[province]['B'] > votes[province]['A']:
            results[province] = 'B'
        else:
            results[province] = 'Draw'  # Assuming draw is possible
    
    return results

def main():
    data = read_input()
    topology, votes = parse_input(data)
    results = simulate_votes(topology, votes)
    
    for province in topology:
        print(f"{province}: {results[province]}")

if __name__ == "__main__":
    main()