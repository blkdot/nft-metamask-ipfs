from brownie import ArtBot, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_breed, OPENSEA_FORMAT
from pathlib import Path
import os
import json
import requests

def main():
    print("Working on " + network.show_active())
    simple_collectible = ArtBot[len(ArtBot) - 1]
    number_of_tokens = simple_collectible.tokenIdCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_tokens)
        )
    set_AllTokenURI(simple_collectible, number_of_tokens)
    print('setting base uri')



def set_AllTokenURI(nft_contract, number_of_tokens):
    dev = accounts.add(config["wallets"]["from_key"])
    for token_id in range(0,number_of_tokens):
        if os.getenv("UPLOAD_IPFS") == "true":
            image_path = "./img/1Art_Bot_no_{}.jpg".format(token_id)
            print(image_path)    
            with Path(image_path).open("rb") as fp:
                image_binary = fp.read()
                ipfs_url = (
                    os.getenv("IPFS_URL")
                    if os.getenv("IPFS_URL")
                    else "http://localhost:5001"
                )
                response = requests.post(ipfs_url + "/api/v0/add",
                                        files={"file": image_binary})
                ipfs_hash = response.json()["Hash"]
                filename = image_path.split("/")[-1:][0]
                uri = "https://ipfs.io/ipfs/{}?filename={}".format(
                    ipfs_hash, filename)
                print(uri)
                nft_contract.setBaseURI(uri, {"from": dev})
    print(
        "Awesome! Base Uri set at {}".format(
            #OPENSEA_FORMAT.format(nft_contract.address, token_id)
            uri
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')