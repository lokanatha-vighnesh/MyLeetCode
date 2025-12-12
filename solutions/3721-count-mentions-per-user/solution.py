class Solution(object):
    def countMentions(self, numberOfUsers, events):
        
        def get_priority(event_type):
            if event_type == "OFFLINE":
                return 0
            if event_type == "MESSAGE":
                return 1
            return 2

        sorted_events = sorted(events, key=lambda ev: (int(ev[1]), get_priority(ev[0])))

        mentions = [0] * numberOfUsers
        online = set(range(numberOfUsers))     
        offline_expiry = dict()                

        for ev in sorted_events:
            ev_type = ev[0]
            t = int(ev[1])

            to_restore = [uid for uid, exp in offline_expiry.items() if exp <= t]
            for uid in to_restore:
                offline_expiry.pop(uid, None)
                online.add(uid)

            if ev_type == "OFFLINE":
                uid = int(ev[2])
                
                if uid in online:
                    online.remove(uid)
                offline_expiry[uid] = t + 60
            else:  # MESSAGE
                mention_str = ev[2]
                if mention_str == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mention_str == "HERE":
                    for uid in online:
                        mentions[uid] += 1
                else:
                    tokens = mention_str.split()
                    for tok in tokens:
                        if tok.startswith("id"):
                            uid = int(tok[2:])
                            mentions[uid] += 1

        return mentions

