#!/usr/bin/python3
from brownie import ArtBottest, accounts, network, config

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"



def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    simple_collectible = ArtBottest[len(ArtBottest) - 1]
    token_id = simple_collectible.totalSupply()
    transaction = simple_collectible.buyArt(5,{"from":dev})
    transaction.wait(1)
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(simple_collectible.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
