#!/usr/bin/python3
import os
from brownie import ArtBottest, accounts, network, config
import time


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False
    ArtBottest.deploy({"from": dev}, publish_source=publish_source)
    simple_collectible = ArtBottest[len(ArtBottest) - 1]
    simple_collectible.setBaseURI("https://gateway.pinata.cloud/ipfs/QmU9a8QVcAih8zhbf1YoY5wKhLYTDMZPtVVXxiuwBW6U9Y/")
    print('setting base uri')
