class RankedListUseCase(object):
    def __init__(self, matches):
        self.matches = matches

    # Gets freight or cargo id
    def recommend(self, id):
        match_list = []
        for match in self.matches:
            if match['freight_id'] or match['cargo_id'] == id:
                match_list.append(match)
        return sorted(match_list, key=lambda k: k['distance'], reverse=True)
