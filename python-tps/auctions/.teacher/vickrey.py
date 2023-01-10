from utils import Cli
from auction import Auction


class VickreyAuction(Auction):

    def collect_bids(self):
        # Collect bids
        standing_bid = self.opening_bid
        bids = []
        for bidder in self.bidders:
            bid = self.cli.prompt(
                f"Opening bid is {self.opening_bid}. {bidder} bids:"
            )
            bids.append( (bidder, int(bid)))
        bids.sort(key=lambda t: t[1], reverse=True)
        (winner, _), (_, final_bid), *_ = bids
        return winner, final_bid


if __name__ == "__main__":
    auction = VickreyAuction()
    auction.play()
