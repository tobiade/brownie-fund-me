from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    price_feed_address = MockV3Aggregator[-1].address
    print("Mocks deployed!")
